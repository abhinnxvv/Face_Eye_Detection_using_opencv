# Face & Eye Detection

This Python script utilizes OpenCV to perform real-time face and eye detection in a video feed from a webcam.

## Requirements

- Python 3.x
- OpenCV
- haarcascade_frontalface_default.xml (included in OpenCV)
- haarcascade_eye.xml (included in OpenCV)

## Installation

1. Make sure you have Python installed. If not, download and install it from [python.org](https://www.python.org/).

2. Install OpenCV library using pip:

    ```
    pip install opencv-python
    ```

3. Clone this repository or download the `Face&EyeDetection.py` file.

4. Run the script:

    ```
    python Face&EyeDetection.py
    ```

## How to Use

- When the script is running, it will open a window displaying the video feed from your webcam.
- Faces and eyes will be detected in real-time and highlighted with rectangles.
- Press the 'q' key to quit the program.

## Acknowledgements

- The face and eye detection is performed using Haar cascades provided by OpenCV.
- Inspiration and guidance for this project came from various online tutorials and resources.
