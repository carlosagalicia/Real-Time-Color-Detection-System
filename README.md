# Real-Time-Color-Detection-System

This project implements a real-time color detection system using computer vision techniques. It captures video from a webcam, processes the frames to detect specific colors, and provides visual feedback about the detected objects including their area and position.

## Overview
- **Functionality:** The program processes live video feed from a webcam, detects objects of specific colors (red, green, orange, blue, yellow, and white), and provides real-time visualization of the detected objects with their properties.
- **Objective:** Identify and track colored objects in real-time, providing information about their size and position.

## Key Learning Areas

### 1. Color Detection in HSV Space
- **HSV Color Ranges:** Precisely defined color ranges in HSV color space for better color recognition
- **Multi-Color Detection:** Simultaneous detection of multiple colors (red, green, orange, blue, yellow)
- **Color Validation:** Center pixel analysis for accurate color identification

### 2. Image Processing Pipeline
- **Gaussian Blur:** Noise reduction using configurable blur parameters
- **Edge Detection:** Implementation of Canny edge detection with adjustable thresholds
- **Contour Processing:** Object detection and analysis using contour detection

### 3. Real-Time Parameter Adjustment
- **Interactive Controls:** Dynamic adjustment of HSV parameters, thresholds, and area limits
- **Visual Feedback:** Real-time update of detection results based on parameter changes
- **Area Filtering:** Configurable minimum area threshold to filter out noise

### 4. Object Analysis and Visualization
- **Centroid Calculation:** Computation of object centers
- **Area Measurement:** Real-time calculation of object areas
- **Visual Markers:** Cross-hair indicators and bounding boxes for detected objects

## Languages and Tools Used
### Python
- **OpenCV:** For video capture, image processing, and real-time object detection.
- **NumPy:** For numerical operations and array handling.

## Installation and Usage

### Requirements
- **Python 3.x** to run the script.
- **OpenCV and NumPy libraries.** Install using:
```bash
pip install opencv-python numpy
```

## Instructions
1. Clone the repository
  ```bash
  git clone https://github.com/carlosagalicia/Real-Time-Color-Detection-System.git
  ```

2. Run the script
  ```bash
  python color_detection.py
  ```
3. Make sure your webcam is connected and functional.

## Operation
The program provides two main windows:

### HSV Control Window:
- Adjust HUE, SATURATION, and VALUE ranges
- Set edge detection thresholds
- Configure minimum area threshold

### Detection Windows:
- "Canny": Shows the edge detection result
- "Contour": Displays the original image with detected objects

### Available Controls

**Color Parameters:**
- HUE min/max (0-179)
- SATURATION min/max (0-255)
- VALUE min/max (0-255)

**Edge Detection:**
- Threshold1 (0-255)
- Threshold2 (0-255)

**Object Detection:**
- Area threshold (0-30000)

## Usage
- Launch the program
- Adjust the HSV parameters using the trackbars to optimize detection for your lighting conditions
- Use the area threshold to filter out noise and small objects
- Press 'q' to quit the program

## Additional Notes
- The white color detection is commented out but can be enabled by uncommenting the relevant code
- The system uses a 480x480 resolution by default
- The Gaussian blur uses a 9x9 kernel size
- The dilation process uses a 7x7 kernel

## Visual Representation
<table>
<tr>
  <td width="50%">
    <h3 align="center">Color recognition</h3>
    <div align="center">
      <img src="https://github.com/user-attachments/assets/03561c9a-65d7-4f99-97dd-e36a847d4d85" >
    </div>
  </td>
</tr>
</table>
</table>
