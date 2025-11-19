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

**Face Recognition Attendance Tracking**
======================================

**face_recognition_attendance.py**
```python
import face_recognition
import cv2
import numpy as np
import pandas as pd
from datetime import datetime

# Define constants
KNOWN_FACES_FILE = 'known_faces.csv'
ATTENDANCE_LOG_FILE = 'attendance_log.csv'

def load_known_faces(file_path):
    """
    Load known faces from CSV file.

    Returns:
        dict: Known faces with names as keys and face encodings as values.
    """
    try:
        known_faces = pd.read_csv(file_path)
        face_encodings = known_faces['face_encoding'].tolist()
        names = known_faces['name'].tolist()
        return dict(zip(names, face_encodings))
    except FileNotFoundError:
        return {}

def save_known_face(name, face_encoding):
    """
    Save a new known face to CSV file.

    Args:
        name (str): Name of the person.
        face_encoding (list): Face encoding.
    """
    known_faces = load_known_faces(KNOWN_FACES_FILE)
    known_faces[name] = face_encoding
    pd.DataFrame({'name': list(known_faces.keys()), 'face_encoding': list(known_faces.values())}).to_csv(KNOWN_FACES_FILE, index=False)

def mark_attendance(name):
    """
    Mark attendance for a person.

    Args:
        name (str): Name of the person.
    """
    try:
        attendance_log = pd.read_csv(ATTENDANCE_LOG_FILE)
        if name not in attendance_log['name'].values:
            attendance_log = pd.concat([attendance_log, pd.DataFrame({'name': [name], 'timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]})], ignore_index=True)
            attendance_log.to_csv(ATTENDANCE_LOG_FILE, index=False)
    except FileNotFoundError:
        pd.DataFrame({'name': [name], 'timestamp': [datetime.now().strftime('%Y-%m-%d %H:%M:%S')]}).to_csv(ATTENDANCE_LOG_FILE, index=False)

def recognize_face(face_encoding, known_faces):
    """
    Recognize a face and return the name.

    Args:
        face_encoding (list): Face encoding.
        known_faces (dict): Known faces.

    Returns:
        str: Name of the person or None if unknown.
    """
    face_distances = [face_recognition.face_distance(list(known_faces.values()), face_encoding)]
    best_match_index = np.argmin(face_distances)
    if face_distances[0][best_match_index] < 0.6:
        return list(known_faces.keys())[best_match_index]
    return None

def main():
    # Initialize camera
    cap = cv2.VideoCapture(0)

    # Load known faces
    known_faces = load_known_faces(KNOWN_FACES_FILE)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to RGB
        rgb_frame = frame[:, :, ::-1]

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Recognize face
            name = recognize_face(face_encoding, known_faces)

            if name:
                # Mark attendance
                mark_attendance(name)
                print(f"Attendance marked for {name}")

            # Draw rectangle around face
            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw name above face
            if name:
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display frame
        cv2.imshow('Face Recognition Attendance', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release camera and close window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
```
**known_faces.csv**
```csv
name,face_encoding
John,[-0.123, 0.456, -0.789]
Jane,[0.234, -0.567, 0.890]
```
**attendance_log.csv**
```csv
name,timestamp
John,2023-03-01 12:00:00
Jane,2023-03-01 12:05:00
```
