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
import cv2
import numpy as np
import face_recognition
import os
import pandas as pd
from datetime import datetime

# Constants
ATTENDANCE_CSV = 'attendance.csv'
ATTENDANCE_FOLDER = 'attendance_images'

# Function to load images and create encodings
def load_and_encode_images(folder_path):
    images = []
    class_names = []
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename))
        if img is not None:
            images.append(img)
            class_names.append(os.path.splitext(filename)[0])  # Remove file extension
    # Convert images to face encodings
    encodings = [face_recognition.face_encodings(img)[0] for img in images if len(face_recognition.face_encodings(img)) > 0]
    return class_names, encodings

# Function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')
    # Check if the attendance CSV exists and create it if not
    if not os.path.isfile(ATTENDANCE_CSV):
        # Create DataFrame and save it
        df = pd.DataFrame(columns=['Name', 'Date'])
        df.to_csv(ATTENDANCE_CSV, index=False)

    # Append attendance record
    with open(ATTENDANCE_CSV, 'a') as f:
        f.write(f'{name},{dt_string}\n')
    print(f'Attendance marked for {name} at {dt_string}')

# Main function to run face recognition
def main():
    # Load known face encodings
    class_names, known_encodings = load_and_encode_images(ATTENDANCE_FOLDER)

    # Initialize the webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        # Convert the frame from BGR to RGB
        rgb_frame = frame[:, :, ::-1]

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Loop through each face found
        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Check for matches with known faces
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = class_names[best_match_index]

            # Draw a box around the face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Mark attendance if identified
            if name != "Unknown":
                mark_attendance(name)

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    main()
```
