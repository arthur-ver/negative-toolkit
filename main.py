from PySide6 import QtCore, QtWidgets, QtGui, QtSvgWidgets
import os
from utils.camera import init_cam, liveview, get_camera
from utils.light_table import sendViaUDP
from utils.scan import scan_rgb
import shutil
from pathlib import Path
import socket
from PySide6.QtCore import QSettings, QThread, Signal as pyqtSignal, Slot as pyqtSlot, Qt
from PySide6.QtGui import QPixmap
import subprocess
import numpy as np
import cv2
import sys
import psutil

from MainWindow import Ui_MainWindow


class LiveViewThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True
        self.cam = None

    def run(self):
        while self._run_flag:
            if self.cam is not None:
                try:
                    frame = self.cam.capture_preview()
                    frame_data = frame.get_data_and_size()
                    frame_data_mem = memoryview(frame_data)
                    frame_np = np.frombuffer(frame_data_mem.tobytes(), np.uint8)
                    self.change_pixmap_signal.emit(cv2.imdecode(frame_np, cv2.IMREAD_COLOR))
                except:
                    self.cam = None
                    self.change_pixmap_signal.emit(None)

        if self.cam is not None:
            self.cam.exit()

    def init_cam(self):
        try:
            self.kill_cam_process()
            self.cam = get_camera()
        except:
            print("Camera not connected.")

    def kill_cam_process(self):
        for proc in psutil.process_iter():
            if proc.name() == "ptpcamerad":
                proc.kill()

    def stop(self):
        if self.cam is not None:
            self.kill_cam_process()
            self.cam.exit()
        self._run_flag = False
        self.wait()


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Init UI
        super(MainWindow, self).__init__()
        self.setting_variables = None
        self.setupUi(self)

        # Create temp working dir
        root_dir = os.path.dirname(__file__)
        temp_dir = os.path.join(root_dir, ".temp")
        shutil.rmtree(temp_dir, ignore_errors=True)
        os.makedirs(temp_dir, exist_ok=True)

        # Check deps
        try:
            subprocess.run([
                "gphoto2",
                "--version"
            ],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT
            )
        except FileNotFoundError:
            QtWidgets.QMessageBox.critical(self, "Error", "ghoto2 is not installed.")
            exit()

        # Load settings
        self.get_settings()
        ip_part1 = "192" if not self.setting_variables.value("ip_part1") else self.setting_variables.value("ip_part1")
        ip_part2 = "168" if not self.setting_variables.value("ip_part2") else self.setting_variables.value("ip_part2")
        ip_part3 = "" if not self.setting_variables.value("ip_part3") else self.setting_variables.value("ip_part3")
        out_dir = str(
            Path.home() / "Pictures" if not self.setting_variables.value("out_dir") else self.setting_variables.value(
                "out_dir"))
        dedicated_source_checked = self.setting_variables.value("dedicated_source_checked")

        # Apply settings
        self.ipEdit1.setText(ip_part1)
        self.ipEdit2.setText(ip_part2)
        self.ipEdit3.setText(ip_part3)
        self.dirEdit.setText(out_dir)
        if dedicated_source_checked:
            self.sourceButton1.setChecked(True)
            self.ipGroupBox.setEnabled(False)
        else:
            self.sourceButton2.setChecked(True)

        # Connect buttons
        self.sourceButton1.toggled.connect(self.toggle_light_source)
        self.dirButton.clicked.connect(self.select_dir)

        # LiveView thread
        self.thread = LiveViewThread()
        self.thread.change_pixmap_signal.connect(self.update_image)
        self.thread.start()
        self.thread.init_cam()

    def get_settings(self):
        self.setting_variables = QSettings("NegativeToolkit_", "Variables")

    def closeEvent(self, event):
        self.setting_variables.setValue("ip_part1", self.ipEdit1.text())
        self.setting_variables.setValue("ip_part2", self.ipEdit2.text())
        self.setting_variables.setValue("ip_part3", self.ipEdit3.text())
        self.setting_variables.setValue("dedicated_source_checked", self.sourceButton1.isChecked())
        self.setting_variables.setValue("out_dir", self.dirEdit.text())
        self.thread.stop()
        event.accept()

    @QtCore.Slot()
    def toggle_light_source(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.ipGroupBox.setEnabled(False)
        else:
            self.ipGroupBox.setEnabled(True)

    @QtCore.Slot()
    def select_dir(self):
        out_dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        if out_dir == "":
            out_dir = self.dirEdit.text()
        self.dirEdit.setText(out_dir)

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        if cv_img is not None:
            def convert_cv_qt(cv_img):
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                convert_to_qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
                p = convert_to_qt_format.scaled(600, 400, Qt.KeepAspectRatio)
                return QPixmap.fromImage(p)

            qt_img = convert_cv_qt(cv_img)
            self.liveViewLabel.setPixmap(qt_img)
        else:
            self.liveViewLabel.clear()
            self.liveViewLabel.setText("Camera disconnected.")


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
