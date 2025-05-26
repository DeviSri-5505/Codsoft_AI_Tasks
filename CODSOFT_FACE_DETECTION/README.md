#codsoft task-5

# CodSoft AI Internship - Task 5: Face Detection and Recognition

## Project Overview

This project implements a basic real-time face detection system using OpenCV and Haar Cascade classifiers. As part of the CodSoft Artificial Intelligence Internship, this task focuses on using pre-trained models to identify and locate faces within an image or a live video stream (webcam).

## Features

- **Real-time Face Detection:** Detects faces in a live video feed from a webcam.
- **Bounding Box Visualization:** Draws rectangles around detected faces.
- **Simple Setup:** Utilizes pre-trained Haar Cascades for ease of use.

## How to Run

1.  **Prerequisites:**

    - Python 3.x installed (Download from: [https://www.python.org/downloads/](https://www.python.org/downloads/))
    - OpenCV Python package installed:
      ```bash
      pip install opencv-python
      ```

2.  **Download Haar Cascade XML:**

    - Download the `haarcascade_frontalface_default.xml` file from the official OpenCV GitHub repository:
      [https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)
    - Save this file directly into the `CODSOFT_FACE_DETECTION` directory, alongside `face_detector.py`.

3.  **Clone the Repository (or ensure local files are set up):**

    - (This project should be located as a sub-folder within your main `Codsoft_AI_Tasks` GitHub repository.)
    - If cloning: `git clone https://github.com/YourGitHubUsername/Codsoft_AI_Tasks.git`
    - Then, navigate to the `CODSOFT_FACE_DETECTION` sub-folder.

4.  **Navigate to the project directory:**

    ```bash
    cd Codsoft_AI_Tasks/CODSOFT_FACE_DETECTION
    ```

5.  **Run the face detection script:**
    ```bash
    python face_detector.py
    ```
    - A window will open displaying your webcam feed. Faces detected will be marked with blue rectangles.
    - Press the `q` key on your keyboard to quit the application.

## Code Structure

- `face_detector.py`: Contains the main logic for initializing the webcam, loading the Haar Cascade classifier, detecting faces in real-time frames, and displaying the results.
- `haarcascade_frontalface_default.xml`: The pre-trained XML file used by OpenCV for frontal face detection.
- `README.md`: This file, providing project information and instructions.

## Potential Enhancements

- **Face Recognition:** Integrate a face recognition model to identify detected faces.
- **Performance Optimization:** Explore more advanced and faster deep learning-based face detectors (e.g., MTCNN, RetinaFace).
- **Additional Detections:** Implement detection for eyes, smiles, or other facial features.
- **Error Handling:** Add more robust error handling for webcam access or file loading.

## Author

KOMMURI VENKATA DEVISRI
www.linkedin.com/in/kommuri-venkata-devisri-965043296
https://github.com/DeviSri-5505

## CodSoft Internship Information

This project was completed as part of the Artificial Intelligence Internship at CodSoft. This is Task 5.
#codsoft #internship #artificialintelligence #facedetection #computer vision #opencv
