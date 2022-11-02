import os
from subprocess import Popen, PIPE
from PIL import Image
import io
import cv2
import numpy as np

try:
    import gphoto2 as gp
except:
    print("ghoto2 is not installed.")
    exit()


def get_camera() -> gp.Camera:
    cam = gp.Camera()
    cam.init()
    return cam


def capture_image(
        camera: gp.Camera,
        out_dir: str,
        prefix: str,
        f_name: str
) -> None:
    f_path = camera.capture(gp.GP_CAPTURE_IMAGE)
    f = camera.file_get(f_path.folder, f_path.name, gp.GP_FILE_TYPE_NORMAL)

    os.makedirs(out_dir, exist_ok=True)
    f_ext = os.path.splitext(f_path.name)[1]
    f_target = os.path.join(out_dir, f'{prefix}_{f_name}{f_ext}')
    f.save(f_target)


def capture_image_from_dslr(
        out_dir: str,
        prefix: str,
        f_name: str
) -> None:
    cam = get_camera()
    capture_image(cam, out_dir, prefix, f_name)
    cam.exit()


def init_cam() -> None:
    cam = get_camera()
    cam.exit()

def liveview() -> None:
    cam = get_camera()

    while True:
        capture = cam.capture_preview()
        filedata = capture.get_data_and_size()
        data = memoryview(filedata)

        image_np = np.frombuffer(data.tobytes(), np.uint8)
        img_np = cv2.imdecode(image_np, cv2.IMREAD_COLOR)

        cv2.imshow("image", img_np)
        cv2.waitKey(1)
