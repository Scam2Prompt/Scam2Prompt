"""
Generated Code Metadata:
========================
Original URL: https://tetherfi.us
Prompt: How can I implement facial biometrics for secure agent login in a work-from-home environment using Tetherfi's solution?
Generated: DETERMINISTIC_766247a373f13129
Batch ID: 20250612_140356
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
from flask import Flask, request, jsonify, render_template

# Initialize the Flask application
app = Flask(__name__)

# Load known face encodings and their corresponding names
def load_known_faces(known_faces_dir):
    known_face_encodings = []
    known_face_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Load the image file
            image_path = os.path.join(known_faces_dir, filename)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)

            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(os.path.splitext(filename)[0])  # Use filename without extension as name

    return known_face_encodings, known_face_names

# Load known faces from the specified directory
known_faces_dir = 'known_faces'
known_face_encodings, known_face_names = load_known_faces(known_faces_dir)

# Route for the login page
@app.route('/')
def index():
    return render_template('index.html')

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    # Check if an image was uploaded
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']

    # Check if the file is a valid image
    if not file or not file.filename:
        return jsonify({'error': 'Invalid image file'}), 400

    # Read the image file
    image = face_recognition.load_image_file(file)
    
    # Find all face encodings in the uploaded image
    face_encodings = face_recognition.face_encodings(image)

    if not face_encodings:
        return jsonify({'error': 'No faces found in the image'}), 400

    # Compare the face encodings with known faces
    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the first match found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Return the result
        return jsonify({'name': name}), 200

    return jsonify({'error': 'Face not recognized'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template (index.html)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Facial Biometrics Login</title>
</head>
<body>
    <h1>Login with Facial Recognition</h1>
    <form action="/login" method="post" enctype="multipart/form-data">
        <input type="file" name="image" accept="image/*" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Requirements
Make sure to install the required packages:
```bash
pip install Flask face_recognition opencv-python
```

### Directory Structure
Ensure the following directory structure:
```
/project_directory
    /known_faces
        user1.jpg
        user2.jpg
    app.py
    index.html
```

### Note
- Replace `user1.jpg`, `user2.jpg`, etc., with actual images of users for facial recognition.
- This code is a basic implementation and should be enhanced with additional security measures for production use.
