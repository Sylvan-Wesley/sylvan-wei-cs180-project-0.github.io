import cv2
import numpy as np
from pathlib import Path

image_paths = sorted(Path(__file__).resolve().parent.glob("*.jpg"))
boxes = {'Street-1.jpg': (1149, 845, 305, 60), 'Street-2.jpg': (1138, 862, 321, 66), 'Street-3.jpg': (1164, 835, 333, 69), 'Street-4.jpg': (1188, 838, 356, 72), 'Street-5.jpg': (1184, 840, 355, 78), 'Street-6.jpg': (1183, 784, 369, 77), 'Street-7.jpg': (1220, 778, 374, 75)}

target_box = boxes["Street-7.jpg"]
tx, ty, tw, th = target_box


for i, path in enumerate(image_paths):
    img = cv2.imread(path)
    name = path.name

    curx, cury, curw, curh = boxes[name]
    scalex = tw / curw
    scaley = th / curh

    M = [
        [scalex, 0, tx - scalex * curx],
        [0, scaley, ty - scaley * cury],
    ]

    M = np.array(M)

    img_new = cv2.warpAffine(img, M, (img.shape[1] - 50, img.shape[0] - 200))
    cv2.imwrite(f"aligned-{i}.jpg", img_new)