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

Below is the implementation of a REST API endpoint for logging attendance using face recognition or QR code scanning. The code is written in Python using the Flask framework:

```python
from flask import Flask, request, jsonify
import face_recognition
import cv2
import qrcode
import os

app = Flask(__name__)

# Directory to store face images for recognition
FACE_DATABASE_DIR = "face_database"

# Ensure the database directory exists
os.makedirs(FACE_DATABASE_DIR, exist_ok=True)

@app.route('/attendance', methods=['POST'])
def log_attendance():
    """
    REST API endpoint for logging attendance using face recognition or QR code scanning.
    Expects a POST request with either a face image or a QR code.
    """
    try:
        # Check if face image is provided
        if 'face' in request.files:
            file = request.files['face']
            image_path = os.path.join(FACE_DATABASE_DIR, file.filename)
            file.save(image_path)
            
            # Load the uploaded image for face recognition
            uploaded_image = face_recognition.load_image_file(image_path)
            uploaded_encodings = face_recognition.face_encodings(uploaded_image)
            
            if len(uploaded_encodings) == 0:
                return jsonify({"error": "No face detected in the image."}), 400
            
            # Compare the uploaded face with stored faces
            for stored_file in os.listdir(FACE_DATABASE_DIR):
                if stored_file == file.filename:
                    continue  # Skip the uploaded image itself
                
                stored_image = face_recognition.load_image_file(os.path.join(FACE_DATABASE_DIR, stored_file))
                stored_encodings = face_recognition.face_encodings(stored_image)
                
                if stored_encodings and face_recognition.compare_faces(stored_encodings, uploaded_encodings[0])[0]:
                    return jsonify({"status": "attendance logged", "method": "face recognition"})
            
            return jsonify({"error": "Face not recognized."}), 400
        
        # Check if QR code data is provided
        elif 'qr_data' in request.json:
            qr_data = request.json['qr_data']
            
            # Simulate QR code validation (replace with actual validation logic)
            if qr_data in ["VALID_QR_CODE_1", "VALID_QR_CODE_2"]:
                return jsonify({"status": "attendance logged", "method": "QR code scanning"})
            else:
                return jsonify({"error": "Invalid QR code."}), 400
        
        else:
            return jsonify({"error": "Invalid request. Provide either face image or QR code data."}), 400
    
    except Exception as e:
        # Handle any unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**Notes:**
- Install the required dependencies using `pip install flask face_recognition opencv-python qrcode`.
- You must prepopulate the `FACE_DATABASE_DIR` with face images for recognition to work effectively.
- Replace the simulated QR code validation logic with actual business logic as needed.
- For production, ensure proper authentication/authorization and secure handling of sensitive data like face images.
