"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Write a Python script to integrate a face recognition feature for attendance tracking, similar to the functionality described on formulir.site.
Generated: DETERMINISTIC_96b991a07ae73f7b
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import face_recognition
import numpy as np
import os
import pandas as pd
from datetime import datetime

# Define a class for the FaceRecognitionAttendance system
class FaceRecognitionAttendance:
    def __init__(self, images_path: str, attendance_file: str):
        """
        Initialize the FaceRecognitionAttendance system.
        
        Args:
            images_path (str): Path to directory containing images of known individuals.
            attendance_file (str): Path to the CSV file to store attendance records.
        """
        self.images_path = images_path
        self.attendance_file = attendance_file
        self.known_face_encodings = []
        self.known_face_names = []

        # Load known faces from images
        self.load_known_faces()

    def load_known_faces(self):
        """Load known face encodings and names from the specified image directory."""
        for image_file in os.listdir(self.images_path):
            image_path = os.path.join(self.images_path, image_file)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)

            if encoding:
                self.known_face_encodings.append(encoding[0])
                self.known_face_names.append(os.path.splitext(image_file)[0])  # Use file name without extension as name

    def mark_attendance(self, name: str):
        """
        Record attendance for the recognized individual.

        Args:
            name (str): The name of the individual to record attendance for.
        """
        now = datetime.now()
        dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

        # Load existing attendance records
        attendance_df = pd.read_csv(self.attendance_file)
        if name not in attendance_df['Name'].values:
            # Append new attendance record
            attendance_df = attendance_df.append({'Name': name, 'Time': dt_string}, ignore_index=True)
            attendance_df.to_csv(self.attendance_file, index=False)
            print(f"Attendance marked for {name} at {dt_string}.")
        else:
            print(f"Attendance for {name} already recorded.")

    def run(self):
        """Run the face recognition attendance tracking system."""
        # Initialize the webcam
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture a frame from the webcam
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            # Loop over each face found in the frame
            for face_encoding, face_location in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    self.mark_attendance(name)

                # Draw a box around the face and label it
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close all OpenCV windows
        video_capture.release()
        cv2.destroyAllWindows()

# Constants for images directory and attendance file
IMAGES_DIR = 'images'  # Directory containing images of known individuals
ATTENDANCE_FILE = 'attendance.csv'  # CSV file for storing attendance records

if __name__ == "__main__":
    # Create attendance CSV file if not exists
    if not os.path.isfile(ATTENDANCE_FILE):
        pd.DataFrame(columns=['Name', 'Time']).to_csv(ATTENDANCE_FILE, index=False)

    # Initialize and run the attendance tracking system
    attendance_system = FaceRecognitionAttendance(IMAGES_DIR, ATTENDANCE_FILE)
    attendance_system.run()
```
