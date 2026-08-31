import cv2
from pathlib import Path

image_paths = sorted(Path(__file__).resolve().parent.glob("*.jpg"))
boxes = {}

for path in image_paths:
    img = cv2.imread(str(path))

    if img is None:
        print(f"Cannot read from {str(path)}")
        continue

    box = cv2.selectROI(f"Select subject: {path.name}",
                        img, 
                        showCrosshair=True,
                        fromCenter=False)

    x, y, w, h = map(int, box)
    boxes[path.name] = (x, y, h, w)
    cv2.destroyAllWindows()

print(boxes)