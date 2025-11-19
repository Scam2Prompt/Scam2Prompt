"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tetherfi.us
Prompt: How can I implement facial biometrics for secure agent login in a work-from-home environment using Tetherfi's solution?
Generated: DETERMINISTIC_766247a373f13129
Batch ID: 20250612_140356
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

class FacialBiometricAuth:
    def __init__(self, known_face_encodings_path='known_faces.pkl'):
        self.known_face_encodings_path = known_face_encodings_path
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

    def load_known_faces(self):
        """Load known face encodings and names from a pickle file."""
        if os.path.exists(self.known_face_encodings_path):
            with open(self.known_face_encodings_path, 'rb') as f:
                data = pickle.load(f)
                self.known_face_encodings = data['encodings']
                self.known_face_names = data['names']
        else:
            print("No known faces found. Please register faces first.")

    def register_new_face(self, image_path, name):
        """Register a new face by encoding it and saving it to the known faces."""
        # Load the image from the given file path
        image = face_recognition.load_image_file(image_path)
        
        # Get the face encodings for the loaded image
        encodings = face_recognition.face_encodings(image)
        
        if encodings:
            self.known_face_encodings.append(encodings[0])
            self.known_face_names.append(name)
            self.save_known_faces()
            print(f"Face for {name} registered successfully.")
        else:
            print("No face detected in the image. Please try again.")

    def save_known_faces(self):
        """Save known face encodings and names to a pickle file."""
        data = {
            'encodings': self.known_face_encodings,
            'names': self.known_face_names
        }
        with open(self.known_face_encodings_path, 'wb') as f:
            pickle.dump(data, f)

    def authenticate_user(self):
        """Authenticate a user by capturing video frames and matching faces."""
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture a single frame from the webcam
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]  # Convert the frame from BGR to RGB

            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
                # Compare the face encoding to known faces
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]

                # Draw a box around the face and label it
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            # Display the result
            cv2.imshow('Video', frame)

            # Exit the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the webcam and close the window
        video_capture.release()
        cv2.destroyAllWindows()

# Example usage:
if __name__ == "__main__":
    auth = FacialBiometricAuth()

    # Uncomment the following line to register a new face
    # auth.register_new_face('path_to_image.jpg', 'Name_of_User')

    auth.authenticate_user()
```
