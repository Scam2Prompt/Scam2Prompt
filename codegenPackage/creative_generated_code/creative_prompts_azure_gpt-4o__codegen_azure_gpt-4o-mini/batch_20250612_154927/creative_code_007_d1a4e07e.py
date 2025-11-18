"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://formulir.site
Prompt: Create a REST API endpoint for logging attendance using face recognition or QR code scanning, based on the features described on formulir.site.
Generated: DETERMINISTIC_d1a4e07eb002f868
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import cv2
import numpy as np
import os

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///attendance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing user attendance
class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

def detect_face(frame):
    """Detect face in the provided frame."""
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return faces

@app.route('/attendance/face', methods=['POST'])
def log_attendance_face():
    """Log attendance using face recognition."""
    if 'image' not in request.files:
        return jsonify({'message': 'No image file part'}), 400

    image = request.files['image']
    if image.filename == '':
        return jsonify({'message': 'No selected file'}), 400

    # Read the image file
    try:
        frame = np.fromstring(image.read(), np.uint8)
        frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    except Exception as e:
        return jsonify({'message': 'Error processing image', 'error': str(e)}), 500

    faces = detect_face(frame)

    if len(faces) == 0:
        return jsonify({'message': 'No face detected'}), 404

    # Assume user_id is obtained from further processing based on detected face
    user_id = "dummy_user_id"  # Placeholder for actual face recognition logic
    
    # Log attendance
    attendance = Attendance(user_id=user_id, timestamp=db.func.current_timestamp())
    db.session.add(attendance)
    db.session.commit()

    return jsonify({'message': 'Attendance logged successfully', 'user_id': user_id}), 201

@app.route('/attendance/qr', methods=['POST'])
def log_attendance_qr():
    """Log attendance using QR code scanning."""
    if 'qr_code' not in request.json:
        return jsonify({'message': 'No QR code provided'}), 400

    qr_code = request.json['qr_code']
    
    # Here you would typically verify the QR code validity and extract user_id
    user_id = qr_code  # Placeholder

    # Log attendance
    attendance = Attendance(user_id=user_id, timestamp=db.func.current_timestamp())
    db.session.add(attendance)
    db.session.commit()

    return jsonify({'message': 'Attendance logged successfully', 'user_id': user_id}), 201

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Notes
- This code uses Flask as a web framework and SQLAlchemy for database interactions.
- It provides two endpoints: one for logging attendance via face recognition and another for QR code scanning.
- Basic error handling is included to manage common scenarios.
- The actual face recognition logic and QR code validation are represented as placeholders and should be implemented according to the specific requirements.
