"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: How can I implement a facial recognition feature in a home security camera system to differentiate between family members and intruders?
Generated: DETERMINISTIC_6d3733d8bad5cbdd
Batch ID: 20250612_155849
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
import pickle

class FacialRecognitionSystem:
    def __init__(self, known_faces_dir='known_faces', model='cnn'):
        """
        Initializes the facial recognition system.
        
        :param known_faces_dir: Directory containing known face images.
        :param model: The model to use for face detection ('cnn' or 'hog').
        """
        self.known_faces = []
        self.known_names = []
        self.load_known_faces(known_faces_dir)
        self.model = model

    def load_known_faces(self, directory):
        """
        Loads known face encodings and names from the specified directory.
        
        :param directory: Directory containing the known face images.
        """
        for filename in os.listdir(directory):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(directory, filename)
                # Load the image file
                image = face_recognition.load_image_file(image_path)
                # Encode the face
                encoding = face_recognition.face_encodings(image)

                if encoding:
                    self.known_faces.append(encoding[0])
                    self.known_names.append(os.path.splitext(filename)[0])

    def recognize_faces(self, video_source=0):
        """
        Captures video from the specified source and recognizes faces in real-time.

        :param video_source: Video source ID (0 for built-in camera).
        """
        # Capture video from the camera
        video_capture = cv2.VideoCapture(video_source)

        if not video_capture.isOpened():
            print("Error: Could not open video source.")
            return

        try:
            while True:
                # Capture a single frame
                ret, frame = video_capture.read()
                if not ret:
                    print("Error: Could not read frame.")
                    break

                # Convert the frame to RGB
                rgb_frame = frame[:, :, ::-1]

                # Find all face locations and encodings in the current frame
                face_locations = face_recognition.face_locations(rgb_frame, model=self.model)
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                # Process each face found in the frame
                for face_encoding, face_location in zip(face_encodings, face_locations):
                    # Check if the face matches any known faces
                    matches = face_recognition.compare_faces(self.known_faces, face_encoding)
                    name = "Unknown"

                    # If a match is found, get the name of the matched face
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_names[first_match_index]

                    # Draw a rectangle around the face
                    top, right, bottom, left = face_location
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    # Draw a label with the name
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

                # Display the resulting frame
                cv2.imshow('Video', frame)

                # Break the loop with 'q' key
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Release the video capture and close all OpenCV windows
            video_capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of the FacialRecognitionSystem
    recognition_system = FacialRecognitionSystem()

    # Start recognizing faces from the default camera
    recognition_system.recognize_faces()
```

**Note:** Ensure that you have the required libraries installed (`opencv-python`, `face_recognition`, and their dependencies). You can install them via pip:

```bash
pip install opencv-python face_recognition
``` 

Additionally, place images of known family members in a directory named `known_faces` in the same location as the script, using the format `name.jpg` or `name.png`.
