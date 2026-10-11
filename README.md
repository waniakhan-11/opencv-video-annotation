
# OpenCV Video Annotation

## Overview
A Python project that reads a video, adds text and
rectangular boxes to every frame, and saves the
processed video as an output file.

## Technologies Used
- Python
- OpenCV

## Features
- Reads video frame by frame
- Draws green rectangular boxes
- Displays the frame number
- Saves the annotated video

## Requirements
- Python 3
- OpenCV

## Installation

Create and activate a virtual environment, then run:

```bash
python -m pip install opencv-python
```

## Usage

1. Place your video in the project folder.
2. Rename it to `input.mp4`.
3. Run the script:

```bash
python main.py
```

4. Open `output.mp4` to view the result.

## Output
The output video contains a green rectangle and
a frame number on every processed frame.
