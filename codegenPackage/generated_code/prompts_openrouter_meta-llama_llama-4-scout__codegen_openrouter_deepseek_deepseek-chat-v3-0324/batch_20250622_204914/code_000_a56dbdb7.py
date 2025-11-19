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
import os
import pickle
import face_recognition
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from datetime import datetime
import time

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            face_encoding BLOB,
            last_login TIMESTAMP,
            is_active BOOLEAN DEFAULT 1
        )
    ''')
    conn.commit()
    conn.close()

# Initialize database on startup
init_db()

class FaceAuthenticator:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_usernames = []
        self.load_known_faces()

    def load_known_faces(self):
        conn = get_db_connection()
        cursor = conn.execute('SELECT username, face_encoding FROM users WHERE face_encoding IS NOT NULL')
        for row in cursor:
            self.known_face_usernames.append(row['username'])
            self.known_face_encodings.append(pickle.loads(row['face_encoding']))
        conn.close()

    def register_user(self, username, password, image_path):
        # Load the image
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        
        if len(face_locations) != 1:
            return False, "Image must contain exactly one face"

        # Generate face encoding
        face_encoding = face_recognition.face_encodings(image, face_locations)[0]
        
        # Store user in database
        password_hash = generate_password_hash(password)
        face_encoding_pickle = pickle.dumps(face_encoding)
        
        conn = get_db_connection()
        try:
            conn.execute(
                'INSERT INTO users (username, password_hash, face_encoding) VALUES (?, ?, ?)',
                (username, password_hash, face_encoding_pickle)
            )
            conn.commit()
            self.known_face_encodings.append(face_encoding)
            self.known_face_usernames.append(username)
            return True, "User registered successfully"
        except sqlite3.IntegrityError:
            return False, "Username already exists"
        finally:
            conn.close()

    def authenticate_user(self, username, password, image_path=None):
        # First verify password
        conn = get_db_connection()
        user = conn.execute(
            'SELECT password_hash, face_encoding FROM users WHERE username = ?',
            (username,)
        ).fetchone()
        conn.close()
        
        if not user or not check_password_hash(user['password_hash'], password):
            return False, "Invalid username or password"

        # If image_path is provided, verify face
        if image_path:
            if not user['face_encoding']:
                return False, "User has no registered face"
            
            # Load and process the image
            unknown_image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(unknown_image)
            
            if len(face_locations) != 1:
                return False, "Image must contain exactly one face"
            
            unknown_encoding = face_recognition.face_encodings(unknown_image, face_locations)[0]
            known_encoding = pickle.loads(user['face_encoding'])
            
            # Compare faces
            matches = face_recognition.compare_faces([known_encoding], unknown_encoding)
            if not matches[0]:
                return False, "Face verification failed"
            
            # Update last login time
            conn = get_db_connection()
            conn.execute(
                'UPDATE users SET last_login = ? WHERE username = ?',
                (datetime.now(), username)
            )
            conn.commit()
            conn.close()

        return True, "Authentication successful"

    def capture_and_verify(self, username):
        # Initialize camera
        video_capture = cv2.VideoCapture(0)
        
        if not video_capture.isOpened():
            return False, "Could not open camera"

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            video_capture.release()
            return False, "Could not capture frame"

        # Save the captured frame
        temp_image_path = f"temp_{username}.jpg"
        cv2.imwrite(temp_image_path, frame)
        video_capture.release()

        # Verify the captured image
        success, message = self.authenticate_user(username, None, temp_image_path)
        
        # Clean up
        try:
            os.remove(temp_image_path)
        except OSError:
            pass

        return success, message

# Flask routes
@app.route('/register', methods=['POST'])
def register():
    if 'username' not in request.form or 'password' not in request.form or 'image' not in request.files:
        return jsonify({"success": False, "message": "Missing required fields"}), 400
    
    username = request.form['username']
    password = request.form['password']
    image_file = request.files['image']
    
    # Save the uploaded file temporarily
    temp_image_path = f"temp_register_{username}.jpg"
    image_file.save(temp_image_path)
    
    authenticator = FaceAuthenticator()
    success, message = authenticator.register_user(username, password, temp_image_path)
    
    # Clean up
    try:
        os.remove(temp_image_path)
    except OSError:
        pass
    
    return jsonify({"success": success, "message": message})

@app.route('/login', methods=['POST'])
def login():
    if 'username' not in request.form or 'password' not in request.form:
        return jsonify({"success": False, "message": "Missing required fields"}), 400
    
    username = request.form['username']
    password = request.form['password']
    use_camera = request.form.get('use_camera', 'false').lower() == 'true'
    
    authenticator = FaceAuthenticator()
    
    if use_camera:
        success, message = authenticator.capture_and_verify(username)
    else:
        if 'image' not in request.files:
            return jsonify({"success": False, "message": "Image required for face verification"}), 400
        
        image_file = request.files['image']
        temp_image_path = f"temp_login_{username}.jpg"
        image_file.save(temp_image_path)
        
        success, message = authenticator.authenticate_user(username, password, temp_image_path)
        
        # Clean up
        try:
            os.remove(temp_image_path)
        except OSError:
            pass
    
    if not success:
        return jsonify({"success": False, "message": message}), 401
    
    return jsonify({"success": True, "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
```
