"""
Generated Code Metadata:
========================
Original URL: https://formulir.site
Prompt: "Generate a Python script for a face recognition-based attendance system with login functionality."
Generated: DETERMINISTIC_97be25e3aee72143
Batch ID: 20250622_212320
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
import os
import face_recognition
import pickle
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, session

# Initialize Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Path to the directory containing known faces
KNOWN_FACES_DIR = 'known_faces'
ATTENDANCE_FILE = 'attendance.csv'

# Load known faces and their names
def load_known_faces():
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(KNOWN_FACES_DIR, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(os.path.splitext(filename)[0])  # Use filename as name

    return known_face_encodings, known_face_names

# Record attendance
def mark_attendance(name):
    with open(ATTENDANCE_FILE, 'a') as f:
        now = datetime.now()
        f.write(f"{name},{now.strftime('%Y-%m-%d %H:%M:%S')}\n")

# Home route
@app.route('/')
def home():
    return render_template('login.html')

# Login route
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Simple authentication (replace with a proper user management system)
    if username == 'admin' and password == 'password':  # Change credentials for production
        session['logged_in'] = True
        return redirect(url_for('attendance'))
    return 'Invalid credentials', 401

# Attendance route
@app.route('/attendance')
def attendance():
    if not session.get('logged_in'):
        return redirect(url_for('home'))

    # Load known faces
    known_face_encodings, known_face_names = load_known_faces()

    # Start video capture
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]  # Convert BGR to RGB

        # Find all face locations and encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding in face_encodings:
            # Check if the face matches any known faces
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                mark_attendance(name)  # Mark attendance for recognized face

            # Display the results
            print(f"Recognized: {name}")

        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture and close windows
    video_capture.release()
    cv2.destroyAllWindows()
    return 'Attendance marked!'

# Logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**Note:** Ensure you have the required libraries installed (`opencv-python`, `face_recognition`, `flask`, `numpy`) and create a directory named `known_faces` with images of known individuals for the face recognition to work. Adjust the secret key and login credentials for production use.
