# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'negative_toolkit.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setFixedSize(850, 400)
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        self.mainWidget = QWidget(MainWindow)
        self.mainWidget.setObjectName(u"mainWidget")
        self.horizontalLayout = QHBoxLayout(self.mainWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.liveViewContainer = QWidget(self.mainWidget)
        self.liveViewContainer.setObjectName(u"liveViewContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.liveViewContainer)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.liveViewWidget = QWidget(self.liveViewContainer)
        self.liveViewWidget.setObjectName(u"liveViewWidget")
        self.horizontalLayout_5 = QHBoxLayout(self.liveViewWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.liveViewLabel = QLabel(self.liveViewWidget)
        self.liveViewLabel.setObjectName(u"liveViewLabel")
        self.liveViewLabel.setMinimumSize(QSize(600, 400))
        #self.liveViewLabel.setMaximumSize(QSize(600, 400))
        self.liveViewLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.liveViewLabel)


        self.horizontalLayout_4.addWidget(self.liveViewWidget)


        self.horizontalLayout.addWidget(self.liveViewContainer)

        self.controlPanelWidget = QWidget(self.mainWidget)
        self.controlPanelWidget.setObjectName(u"controlPanelWidget")
        #self.controlPanelWidget.setMinimumSize(QSize(250, 0))
        self.controlPanelWidget.setContentsMargins(0, 10, 10, 0)
        self.verticalLayout = QVBoxLayout(self.controlPanelWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.scanGroupBox = QGroupBox(self.controlPanelWidget)
        self.scanGroupBox.setObjectName(u"scanGroupBox")
        self.verticalLayout_4 = QVBoxLayout(self.scanGroupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scanButton = QPushButton(self.scanGroupBox)
        self.scanButton.setObjectName(u"scanButton")

        self.verticalLayout_4.addWidget(self.scanButton)


        self.verticalLayout.addWidget(self.scanGroupBox)

        self.lightGroupBox = QGroupBox(self.controlPanelWidget)
        self.lightGroupBox.setObjectName(u"lightGroupBox")
        self.verticalLayout_3 = QVBoxLayout(self.lightGroupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.sourceButton1 = QRadioButton(self.lightGroupBox)
        self.sourceButtonGroup = QButtonGroup(MainWindow)
        self.sourceButtonGroup.setObjectName(u"sourceButtonGroup")
        self.sourceButtonGroup.addButton(self.sourceButton1)
        self.sourceButton1.setObjectName(u"sourceButton1")
        self.sourceButton1.setChecked(True)

        self.verticalLayout_3.addWidget(self.sourceButton1)

        self.sourceButton2 = QRadioButton(self.lightGroupBox)
        self.sourceButtonGroup.addButton(self.sourceButton2)
        self.sourceButton2.setObjectName(u"sourceButton2")

        self.verticalLayout_3.addWidget(self.sourceButton2)

        self.ipGroupBox = QGroupBox(self.lightGroupBox)
        self.ipGroupBox.setObjectName(u"ipGroupBox")
        self.horizontalLayout_6 = QHBoxLayout(self.ipGroupBox)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.ipEdit1 = QLineEdit(self.ipGroupBox)
        self.ipEdit1.setAlignment(Qt.AlignCenter)
        self.ipEdit1.setMaxLength(3)
        self.ipEdit1.setObjectName(u"ipEdit1")

        self.horizontalLayout_6.addWidget(self.ipEdit1)

        self.ipDotLabel1 = QLabel(self.ipGroupBox)
        self.ipDotLabel1.setObjectName(u"ipDotLabel1")

        self.horizontalLayout_6.addWidget(self.ipDotLabel1)

        self.ipEdit2 = QLineEdit(self.ipGroupBox)
        self.ipEdit2.setAlignment(Qt.AlignCenter)
        self.ipEdit2.setMaxLength(3)
        self.ipEdit2.setObjectName(u"ipEdit2")

        self.horizontalLayout_6.addWidget(self.ipEdit2)

        self.ipDotLabel2 = QLabel(self.ipGroupBox)
        self.ipDotLabel2.setObjectName(u"ipDotLabel2")

        self.horizontalLayout_6.addWidget(self.ipDotLabel2)

        self.ipEdit3 = QLineEdit(self.ipGroupBox)
        self.ipEdit3.setAlignment(Qt.AlignCenter)
        self.ipEdit3.setMaxLength(3)
        self.ipEdit3.setObjectName(u"ipEdit3")

        self.horizontalLayout_6.addWidget(self.ipEdit3)

        self.horizontalLayout_6.setSpacing(3)


        self.verticalLayout_3.addWidget(self.ipGroupBox)


        self.verticalLayout.addWidget(self.lightGroupBox)

        self.outputGroupBox = QGroupBox(self.controlPanelWidget)
        self.outputGroupBox.setObjectName(u"outputGroupBox")
        self.horizontalLayout_2 = QHBoxLayout(self.outputGroupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dirEdit = QLineEdit(self.outputGroupBox)
        self.dirEdit.setObjectName(u"dirEdit")

        self.horizontalLayout_2.addWidget(self.dirEdit)

        self.dirButton = QPushButton(self.outputGroupBox)
        self.dirButton.setObjectName(u"dirButton")

        self.horizontalLayout_2.addWidget(self.dirButton)


        self.verticalLayout.addWidget(self.outputGroupBox)


        self.horizontalLayout.addWidget(self.controlPanelWidget, 0, Qt.AlignTop)

        MainWindow.setCentralWidget(self.mainWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Negative Toolkit", None))
        self.liveViewLabel.setText(QCoreApplication.translate("MainWindow", u"Camera disconnected.", None))
        self.scanGroupBox.setTitle("")
        self.scanButton.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.scanGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.lightGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Light source", None))
        self.sourceButton1.setText(QCoreApplication.translate("MainWindow", u"Dedicated source", None))
        self.sourceButton2.setText(QCoreApplication.translate("MainWindow", u"Light Table app", None))
        self.ipGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"IP", None))
        self.ipDotLabel1.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.ipDotLabel2.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.outputGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Output", None))
        self.dirButton.setText(QCoreApplication.translate("MainWindow", u"@", None))
    # retranslateUi

