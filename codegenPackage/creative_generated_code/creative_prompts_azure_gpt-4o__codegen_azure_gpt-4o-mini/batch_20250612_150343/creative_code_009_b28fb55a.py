"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet.in
Prompt: Write code to integrate door access control using biometric solutions like face recognition, as outlined by Starknet IT Solutions.
Generated: DETERMINISTIC_b28fb55a471fa513
Batch ID: 20250612_150343
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
import json
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BiometricAccessControl:
    def __init__(self, known_faces_dir):
        """
        Initializes the Biometric Access Control system.

        :param known_faces_dir: Directory containing images of known faces with their names as the filename
        """
        self.known_faces = []
        self.known_face_names = []
        self.load_known_faces(known_faces_dir)

    def load_known_faces(self, directory):
        """
        Load known faces from the specified directory.

        :param directory: Directory containing known face images
        """
        try:
            for filename in os.listdir(directory):
                if filename.endswith(('.jpg', '.jpeg', '.png')):
                    # Load image and get encodings
                    image_path = os.path.join(directory, filename)
                    image = face_recognition.load_image_file(image_path)
                    encoding = face_recognition.face_encodings(image)

                    if encoding:
                        self.known_faces.append(encoding[0])
                        self.known_face_names.append(os.path.splitext(filename)[0])
                        logging.info(f"Loaded face for {filename}")
                    else:
                        logging.warning(f"No face found in image {filename}")
        except Exception as e:
            logging.error(f"Error loading known faces: {e}")

    def recognize_face(self, frame):
        """
        Recognize faces in the provided frame.

        :param frame: The image frame captured from the video
        :return: List of names of recognized faces
        """
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        recognized_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_faces, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_faces, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            recognized_names.append(name)

        return recognized_names

    def log_access(self, name):
        """
        Log access attempts with timestamp.

        :param name: Name of the person who attempted access
        """
        log_entry = {
            'name': name,
            'timestamp': datetime.now().isoformat()
        }
        logging.info(f"Access attempt by: {name}")

        # Write log entry to a JSON file for persistence
        try:
            with open('access_log.json', 'a') as log_file:
                json.dump(log_entry, log_file)
                log_file.write("\n")
        except Exception as e:
            logging.error(f"Error logging access: {e}")

    def start_camera(self):
        """
        Start the camera and process video stream for face recognition.
        """
        video_capture = cv2.VideoCapture(0)  # Open default camera

        if not video_capture.isOpened():
            logging.error("Unable to access the camera.")
            return

        while True:
            ret, frame = video_capture.read()
            if not ret:
                logging.error("Failed to capture image.")
                break

            # Convert frame from BGR (OpenCV) to RGB (face_recognition)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Recognize faces in the current frame
            recognized_names = self.recognize_face(rgb_frame)

            # Display results
            for name in recognized_names:
                self.log_access(name)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Break on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Instantiate the access control system with the directory of known faces
    access_control = BiometricAccessControl(known_faces_dir='known_faces')
    access_control.start_camera()
```

**Note**: This code requires the `face_recognition` and `opencv-python` packages. Install them using pip before running the code:
```bash
pip install face_recognition opencv-python
```
