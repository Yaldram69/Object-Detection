# Object Detection

Real-time object detection from a webcam using the pretrained YOLOv8 nano model. Each frame is annotated with bounding boxes and class labels and shown in a window. The model uses the standard COCO classes.

## Features

- YOLOv8n detection (80 COCO classes) on a live webcam feed
- Boxes and labels drawn with `results[0].plot()`
- Press `q` to quit

## Project structure

- `main.py`: the program. Loads `yolov8n.pt`, reads from webcam index 0, and shows the annotated frames.
- `yolov8n.pt`: pretrained YOLOv8 nano weights, included in the repository.
- `DEMO.mp4`: demo video of the output.
- `ReadMe.txt`: original install notes. It lists `opencv-pyhon`, which should read `opencv-python`.

## Requirements

Imports used: `cv2`, `ultralytics`.

```
pip install opencv-python ultralytics
```

## Installation

```
git clone https://github.com/Yaldram69/Object-Detection.git
cd Object-Detection
pip install opencv-python ultralytics
```

## Usage

Run from the repository folder so that `yolov8n.pt` is found:

```
python main.py
```

The script takes no arguments and reads from the default webcam (index 0). If the webcam cannot be opened, it prints an error and exits. Press `q` in the window to quit.

## Notes

- `yolov8n.pt` is included. If the file is missing from the working directory, Ultralytics downloads it on first use, which needs internet access.
- The model detects only the COCO classes. Custom objects need a model trained on your own dataset.
- The window title is "YOLOv8 Real-time Object Detection".
- No training code is included.
