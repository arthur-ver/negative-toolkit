import uuid
from PySide6 import QtWidgets
import socket
import glob
import subprocess
import os
import time

from utils.camera import capture_image_from_dslr
from utils.light_table import sendViaUDP

from PySide6 import QtWidgets


def scan_rgb(
        ip: str,
        temp_dir: str,
        port: int = 100
) -> None:
    f_name = uuid.uuid1()

    # scan 3 RGB channels
    for color in ["r", "g", "b"]:
        time.sleep(0.5)
        data = sendViaUDP(color, ip, port)

        capture_image_from_dslr(temp_dir, color, f_name)

    # save to linear TIFF
    #for color in ["r", "g", "b"]:
    #    for file in glob.glob(os.path.join(temp_dir, f"{color}_{f_name}.*")):
    #        subprocess.run([
    #            os.path.join(self.root_dir, "libs/dcraw_emu"),
    #            "-r", "1", "1", "1", "1",
    #            "-t", "0",
    #            "-o", "0",
    #            "-4",
    #            "-T",
    #            file
    #        ],
    #            stdout=subprocess.DEVNULL,
    #            stderr=subprocess.STDOUT
    #        )