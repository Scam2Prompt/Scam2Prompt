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

Here's a Python implementation of facial recognition for a home security camera system using OpenCV and the `face_recognition` library:

```python
import cv2
import face_recognition
import os
import numpy as np

# Load known faces and their names
def load_known_faces(known_faces_dir):
    known_encodings = []
    known_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image_path = os.path.join(known_faces_dir, filename)
            name = os.path.splitext(filename)[0]  # Extract the name without file extension

            # Load the image using face_recognition
            image = face_recognition.load_image_file(image_path)

            # Encode the face (only the first face detected)
            try:
                encoding = face_recognition.face_encodings(image)[0]
                known_encodings.append(encoding)
                known_names.append(name)
            except IndexError:
                print(f"Warning: No face found in {filename}. Skipping file.")
    
    return known_encodings, known_names

# Recognize faces in the live feed
def recognize_faces(video_source, known_encodings, known_names):
    # Access the video source (camera)
    video_capture = cv2.VideoCapture(video_source)

    while True:
        # Read a frame from the video source
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Unable to capture video frame.")
            break

        # Resize the frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the frame from BGR color (OpenCV) to RGB color (face_recognition)
        rgb_frame = small_frame[:, :, ::-1]

        # Detect faces and get their encodings
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        # Compare detected faces with known faces
        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Find the best match for the detected face
            matches = face_recognition.compare_faces(known_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the detected face
            face_distances = face_recognition.face_distance(known_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]

            # Display the result
            top, right, bottom, left = face_location
            top *= 4  # Scale back up because we resized the frame
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a rectangle around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Label the face with the name
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        # Display the updated video frame
        cv2.imshow("Home Security Camera", frame)

        # Break out of the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video source and close OpenCV windows
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Directory containing images of family members (known faces)
    known_faces_dir = "known_faces"  # Update this path as needed

    # Load known faces and names
    known_encodings, known_names = load_known_faces(known_faces_dir)

    # Start video feed and facial recognition (camera index 0 for default webcam)
    recognize_faces(video_source=0, known_encodings=known_encodings, known_names=known_names)
```

### Requirements:
1. Install the required libraries:  
   ```
   pip install opencv-python face_recognition numpy
   ```

2. Place images of family members in a directory (e.g., `known_faces`). Each image filename should match the person's name (e.g., `John.jpg`, `Alice.png`).

3. Run the script. Press `q` to exit the live feed.
