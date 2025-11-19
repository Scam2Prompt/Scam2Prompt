"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Write a code snippet for integrating face recognition for attendance tracking as described on Formulir.
Generated: DETERMINISTIC_4017dad3f5276520
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import face_recognition
import cv2
import os
import numpy as np
from datetime import datetime

# Path to the folder containing known face images
KNOWN_FACES_DIR = "known_faces"
# Path to save the attendance log
ATTENDANCE_LOG = "attendance.csv"

# Initialize known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces from the directory
try:
    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load image and encode face
            image_path = os.path.join(KNOWN_FACES_DIR, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])  # Use the filename (without extension) as the name
except Exception as e:
    print(f"Error loading known faces: {e}")

# Initialize video capture (0 for default webcam)
video_capture = cv2.VideoCapture(0)

# Helper function to log attendance
def log_attendance(name):
    try:
        # Open the attendance log file in append mode
        with open(ATTENDANCE_LOG, "a") as log_file:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            log_file.write(f"{name},{timestamp}\n")
    except Exception as e:
        print(f"Error logging attendance: {e}")

print("Starting face recognition for attendance tracking. Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if not ret:
        print("Failed to capture video frame. Exiting...")
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert frame from BGR to RGB (for face_recognition)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare the current face encoding with known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance if there is a match
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # Display the name of the recognized person
        print(f"Detected: {name}")

        # Log attendance for the recognized face
        if name != "Unknown":
            log_attendance(name)

    # Display the resulting frame
    cv2.imshow("Video", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
```
