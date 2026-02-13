import os
import random

import cv2
from ultralytics import YOLO

CUR_WD = os.getcwd()
print(CUR_WD)
CKPT_ROOT = "/nobackup/nhaldert/ckpt"
DATA_ROOT = "/nfs/gigantamax/home/data/datasets"

CKPT_DIR = os.path.join(CKPT_ROOT, "yolo-obj-detector")
DATASET_DIR = os.path.join(DATA_ROOT, "nuScenes/nuscenes_data")

OUTPUT_DIR = os.path.join(CUR_WD, "outputs", "yolo-obj-detector")


def main():
    model = YOLO(os.path.join(CKPT_DIR, "yolo26n.pt"))

    sample = random.choice(os.listdir(os.path.join(DATASET_DIR, "samples/CAM_FRONT")))
    # img = cv2.imread(os.path.join(DATASET_DIR, "samples/CAM_FRONT", sample))
    vid = "/nobackup/nhaldert/data/fh5.mp4"
    # results = model.predict(
    #     source=img, save=True, save_txt=True, project=OUTPUT_DIR, name="nuscenes_sample"
    # )
    results = model.predict(
        source=vid, save=True, save_txt=True, project=OUTPUT_DIR, name="fh5"
    )
    # results = model(img, stream=True)
    # for result in results:
    #     boxes = result.boxes  # Boxes object for bounding box outputs
    #     masks = result.masks  # Masks object for segmentation masks outputs
    #     keypoints = result.keypoints  # Keypoints object for pose outputs
    #     probs = result.probs  # Probs object for classification outputs
    #     obb = result.obb  # Oriented boxes object for OBB outputs
    #     result.save(filename=os.path.join(OUTPUT_DIR, "result.jpg"))


if __name__ == "__main__":
    main()
