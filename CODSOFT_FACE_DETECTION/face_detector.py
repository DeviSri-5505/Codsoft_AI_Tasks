# face_detector.py

import cv2

# --- Configuration ---
# Make sure this file path is correct and the XML file is in the same folder as this script
HAARCASCADE_PATH = 'haarcascade_frontalface_default.xml'

# --- 1. Load the pre-trained Haar Cascade classifier ---
try:
    face_cascade = cv2.CascadeClassifier(HAARCASCADE_PATH)
    if face_cascade.empty():
        raise IOError(f"Cannot load Haar Cascade XML file: {HAARCASCADE_PATH}")
    print("Haar Cascade classifier loaded successfully.")
except Exception as e:
    print(f"Error loading Haar Cascade: {e}")
    print("Please ensure 'haarcascade_frontalface_default.xml' is in the same directory as 'face_detector.py'")
    exit() # Exit if the cascade file cannot be loaded

# --- 2. Initialize the webcam (video capture) ---
# 0 usually refers to the default webcam. If you have multiple webcams, you might try 1, 2, etc.
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream (webcam).")
    print("Please check if your webcam is connected and not in use by another application.")
    exit() # Exit if webcam cannot be opened

print("Webcam initialized successfully. Press 'q' to quit.")

# --- 3. Main loop for real-time face detection ---
while True:
    # Read a frame from the webcam
    ret, frame = cap.read() # 'ret' is a boolean indicating if the frame was read successfully, 'frame' is the image itself

    if not ret:
        print("Error: Failed to grab frame from webcam. Exiting...")
        break # Exit loop if no frame is captured

    # Convert the frame to grayscale (face detection works best on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Perform face detection on the current frame
    # Parameters are similar to image detection:
    # - scaleFactor: How much the image size is reduced at each image scale.
    # - minNeighbors: How many neighbors each candidate rectangle should have to retain it.
    # - minSize: Minimum possible object size. Objects smaller than that are ignored.
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) # Draw a blue rectangle (BGR format) with thickness 2

    # Display the frame with detected faces
    cv2.imshow('Live Face Detection', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'): # waitKey(1) means wait 1ms for a key press
        break

# --- 4. Release webcam and destroy all OpenCV windows ---
cap.release() # Release the webcam resource
cv2.destroyAllWindows() # Close all OpenCV windows
print("Webcam stream ended. All windows closed.")