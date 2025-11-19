"""
Generated Code Metadata:
========================
Original URL: https://tetherfi.us
Prompt: Write a Python code snippet to implement facial biometrics-based login for secure work-from-home applications using Edge-AI and Camera vision, similar to Tetherfi's solution.
Generated: DETERMINISTIC_a56dbdb7f0f02824
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import cv2
import numpy as np
import face_recognition
import os
import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load known face encodings and their corresponding names
def load_known_faces(known_faces_dir):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.pkl'):
            with open(os.path.join(known_faces_dir, filename), 'rb') as f:
                data = pickle.load(f)
                known_face_encodings.append(data['encoding'])
                known_face_names.append(data['name'])

    return known_face_encodings, known_face_names

# Initialize known faces
known_faces_dir = 'known_faces'
known_face_encodings, known_face_names = load_known_faces(known_faces_dir)

# Initialize video capture
video_capture = cv2.VideoCapture(0)

@app.route('/login', methods=['POST'])
def login():
    # Capture a single frame from the video feed
    ret, frame = video_capture.read()
    if not ret:
        return jsonify({'error': 'Failed to capture image'}), 500

    # Convert the image from BGR to RGB
    rgb_frame = frame[:, :, ::-1]

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Check for matches with known faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        # If a known face is found, return success
        if name != "Unknown":
            return jsonify({'status': 'success', 'user': name}), 200

    return jsonify({'status': 'failure', 'message': 'Face not recognized'}), 401

@app.route('/shutdown', methods=['POST'])
def shutdown():
    """Shutdown the video capture gracefully."""
    video_capture.release()
    cv2.destroyAllWindows()
    return jsonify({'status': 'success', 'message': 'Video capture stopped'}), 200

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(f"Error starting the server: {e}")
```

### Notes:
- Ensure you have the required libraries installed: `opencv-python`, `face_recognition`, `flask`, and `numpy`.
- The `known_faces` directory should contain `.pkl` files with face encodings and names.
- This code provides a simple API for facial recognition-based login and includes error handling for image capture and server startup.
