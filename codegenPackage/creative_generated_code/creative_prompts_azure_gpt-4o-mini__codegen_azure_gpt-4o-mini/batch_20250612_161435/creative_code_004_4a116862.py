"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Provide an example of how to use face recognition technology for employee attendance based on the methods outlined on Formulir.
Generated: DETERMINISTIC_4a11686245d7c0c4
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
from datetime import datetime

class FaceRecognitionAttendance:
    def __init__(self, attendance_file='attendance.csv'):
        """Initialize the FaceRecognitionAttendance object."""
        self.attendance_file = attendance_file
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()

    def load_known_faces(self):
        """Load known face encodings and names from the 'employees' directory."""
        employees_dir = 'employees'
        
        # Check if the directory exists
        if not os.path.exists(employees_dir):
            raise FileNotFoundError(f"The directory '{employees_dir}' does not exist.")

        for image_name in os.listdir(employees_dir):
            image_path = os.path.join(employees_dir, image_name)
            try:
                # Load the image
                image = face_recognition.load_image_file(image_path)
                # Get the face encoding
                face_encoding = face_recognition.face_encodings(image)[0]
                self.known_face_encodings.append(face_encoding)
                self.known_face_names.append(os.path.splitext(image_name)[0])  # Use filename as name
            except IndexError:
                print(f"No face found in the image {image_name}. Skipping.")
            except Exception as e:
                print(f"Error loading image {image_name}: {e}")

    def mark_attendance(self, name):
        """Mark the attendance of the recognized employee."""
        now = datetime.now()
        date_string = now.strftime('%Y-%m-%d')
        time_string = now.strftime('%H:%M:%S')
        
        # Check if the attendance file exists; create if not
        if not os.path.isfile(self.attendance_file):
            with open(self.attendance_file, 'w') as f:
                f.write('Name,Date,Time\n')  # Write header
        # Append attendance record
        with open(self.attendance_file, 'a') as f:
            f.write(f'{name},{date_string},{time_string}\n')

    def capture_attendance(self):
        """Capture attendance through webcam using face recognition."""
        # Start video capture
        video_capture = cv2.VideoCapture(0)

        while True:
            # Capture frame-by-frame
            ret, frame = video_capture.read()
            rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

            # Find all face locations and encodings in the current frame
            face_locations = face_recognition.face_locations(rgb_frame)
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

            for face_encoding, face_location in zip(face_encodings, face_locations):
                # Check if the face is recognized
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"

                # Use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                    self.mark_attendance(name)  # Mark attendance for recognized face

                # Draw rectangle around the face
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

            # Display the resulting frame
            cv2.imshow('Video', frame)

            # Exit loop when 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release video capture and close windows
        video_capture.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an instance of the FaceRecognitionAttendance class
    attendance_system = FaceRecognitionAttendance()
    # Start capturing attendance
    attendance_system.capture_attendance()
```
