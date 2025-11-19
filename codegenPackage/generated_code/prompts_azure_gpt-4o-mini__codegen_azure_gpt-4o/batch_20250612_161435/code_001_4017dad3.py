"""
Generated Code Metadata:
========================
Original URL: https://formulir.site
Prompt: Write a code snippet for integrating face recognition for attendance tracking as described on Formulir.
Generated: DETERMINISTIC_4017dad3f5276520
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import face_recognition
import cv2
import os
import numpy as np
from datetime import datetime

# Path to the directory containing known face images
KNOWN_FACES_DIR = "known_faces"
# Path to the attendance log file
ATTENDANCE_LOG = "attendance_log.csv"

# Load known faces and their names
def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    # Iterate through each file in the known faces directory
    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Load the image and encode the face
            image_path = os.path.join(KNOWN_FACES_DIR, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]

            # Append the encoding and name (filename without extension)
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])

    return known_face_encodings, known_face_names

# Mark attendance in the log file
def mark_attendance(name):
    try:
        # Open the log file in append mode
        with open(ATTENDANCE_LOG, "a") as file:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{name},{timestamp}\n")
    except Exception as e:
        print(f"Error writing to attendance log: {e}")

# Main function to run face recognition for attendance
def run_attendance_system():
    # Load known faces
    known_face_encodings, known_face_names = load_known_faces()

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    # Set to keep track of already marked attendees
    attendees = set()

    try:
        while True:
            # Capture a single frame from the webcam
            ret, frame = video_capture.read()
            if not ret:
                print("Failed to capture frame from webcam. Exiting...")
                break

            # Resize frame for faster processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            # Loop through each face found in the frame
            for face_encoding, face_location in zip(face_encodings, face_locations):
                # Compare the face with known faces
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                    # Mark attendance if not already marked
                    if name not in attendees:
                        attendees.add(name)
                        mark_attendance(name)
                        print(f"Attendance marked for {name}")

                    # Draw a rectangle around the face and display the name
                    top, right, bottom, left = [v * 4 for v in face_location]
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            # Display the video feed
            cv2.imshow("Attendance System", frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Release the webcam and close all OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    run_attendance_system()
```
