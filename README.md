# AI Facial Detection
## Description
Implements real time facial detection using the OpenCV library in Python. Capturing video from the default webcam, and detects each face frame by frame, highlighting them with colored rectangles

## Installation and usage
### Pre-requisites
- Python 3.x
- OpenCV Library
  
### Installation
Install the OpenCV dependency running `pip install opencv-python` in your project directory
To run the facial detection program, execute `python main.py` or `python3 main.py`

### Usage 
This script will open a window displaying the webcam feed. each face detected will be highlighter with green rectangles

### Key features
**Real time detection** : This program captures video from the defaut webcam and processes it in real time
**Face highlighting** : Detected faces are highlighted with green rectangles
**Easy termination** : press 'q' to close the app

### How it works
**Cascade classifier** : OpenCV's Cascade classifier uses a pre-trained Haar Cascade model to detect faces [visit the official openCV documentation for more info](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html)

### Limitations and consideration
Light conditions and visual environment might affects the app's ability to properly detect faces
The script uses the default webcam. If you wish to use another webcam, you will have to modify it yourself in your system's settings.
