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
import face_recognition
import cv2
import os
import numpy as np
from datetime import datetime

# Function to load known face encodings and their names
def load_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []

    for file_name in os.listdir(known_faces_dir):
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            # Load image and encode face
            image = face_recognition.load_image_file(os.path.join(known_faces_dir, file_name))
            encodings = face_recognition.face_encodings(image)

            if encodings:  # Ensure face encoding is found
                known_encodings.append(encodings[0])
                known_names.append(os.path.splitext(file_name)[0])  # Use file name (without extension) as the name

    return known_encodings, known_names

# Function to mark attendance in a file
def mark_attendance(name):
    with open("attendance.csv", "a") as file:
        now = datetime.now()  # Get current date and time
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{name},{timestamp}\n")

# Main function to run the attendance tracking system
def main():
    # Directory containing known face images
    known_faces_dir = "known_faces"

    # Load known face encodings and names
    known_encodings, known_names = load_known_faces(known_faces_dir)

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Unable to access webcam.")
        return

    print("Press 'q' to exit.")

    # Set for tracking attendance to avoid duplicates
    attendance_recorded = set()

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Unable to read frame from webcam.")
            break

        # Convert the frame to RGB (OpenCV uses BGR by default)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces and encode them
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare detected face with known faces
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            if matches[best_match_index]:
                name = known_names[best_match_index]

                # Mark attendance if not already recorded
                if name not in attendance_recorded:
                    mark_attendance(name)
                    attendance_recorded.add(name)

                # Draw a rectangle around the face and label it
                top, right, bottom, left = face_location
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

        # Display the resulting frame
        cv2.imshow("Attendance Tracking", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    video_capture.release()
    cv2.destroyAllWindows()

# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Ensure you have a folder named `known_faces` in the same directory as the script. Place images of known individuals in this folder, naming each file with the individual's name (e.g., `John_Doe.jpg`).
- The script writes attendance records to a file called `attendance.csv`.
- You need to install the required libraries (`face_recognition`, `opencv-python`, `numpy`) before running the script.
- Error handling is included for webcam access and general exceptions.
