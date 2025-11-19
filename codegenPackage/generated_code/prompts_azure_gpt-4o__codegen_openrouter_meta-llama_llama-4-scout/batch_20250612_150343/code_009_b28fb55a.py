"""
Generated Code Metadata:
========================
Original URL: https://starknet.in
Prompt: Write code to integrate door access control using biometric solutions like face recognition, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_b28fb55a471fa513
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# door_access_control.py

import cv2
import numpy as np
from datetime import datetime
import logging
import os

# Set up logging
logging.basicConfig(filename='door_access_control.log', level=logging.INFO)

class FaceRecognitionSystem:
    def __init__(self, known_faces_dir):
        """
        Initialize the face recognition system.

        Args:
            known_faces_dir (str): Directory containing known faces.
        """
        self.known_faces = []
        self.known_names = []

        # Load known faces
        for file in os.listdir(known_faces_dir):
            if file.endswith(".jpg") or file.endswith(".png"):
                img = cv2.imread(os.path.join(known_faces_dir, file))
                self.known_faces.append(img)
                self.known_names.append(file.split('.')[0])

        # Create a face recognizer
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Train the face recognizer
        self.face_recognizer.train(self.known_faces, np.array(range(len(self.known_faces))))

    def recognize_face(self, face):
        """
        Recognize a face.

        Args:
            face (numpy array): Face to recognize.

        Returns:
            str: Name of the recognized person or None if not recognized.
        """
        try:
            # Use the face recognizer to predict the face
            _, name = self.face_recognizer.predict(face)
            if name < len(self.known_names):
                return self.known_names[name]
            else:
                return None
        except Exception as e:
            logging.error(f"Error recognizing face: {e}")
            return None

class DoorAccessControl:
    def __init__(self, face_recognition_system):
        """
        Initialize the door access control system.

        Args:
            face_recognition_system (FaceRecognitionSystem): Face recognition system.
        """
        self.face_recognition_system = face_recognition_system
        self.allowed_faces = ["admin", "user"]

    def grant_access(self, face):
        """
        Grant access if the face is recognized and allowed.

        Args:
            face (numpy array): Face to recognize.

        Returns:
            bool: True if access is granted, False otherwise.
        """
        name = self.face_recognition_system.recognize_face(face)
        if name in self.allowed_faces:
            logging.info(f"Access granted for {name}")
            return True
        else:
            logging.info(f"Access denied for {name}")
            return False

def main():
    known_faces_dir = "known_faces"
    face_recognition_system = FaceRecognitionSystem(known_faces_dir)
    door_access_control = DoorAccessControl(face_recognition_system)

    # Initialize the camera
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        for (x, y, w, h) in faces:
            # Extract the face
            face = gray[y:y+h, x:x+w]

            # Check if access is granted
            if door_access_control.grant_access(face):
                cv2.putText(frame, "Access granted", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
            else:
                cv2.putText(frame, "Access denied", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

            # Draw a rectangle around the face
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Door Access Control', frame)

        # Exit on key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
```
