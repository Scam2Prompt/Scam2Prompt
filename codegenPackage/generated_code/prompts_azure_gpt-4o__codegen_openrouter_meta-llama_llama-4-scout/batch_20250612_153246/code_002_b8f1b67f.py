"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: Generate code for a feature that allows users to upload photos of their vehicle for trade-in purposes, inspired by the Cid Autos "Recibimos tu Vehículo" functionality.
Generated: DETERMINISTIC_b8f1b67f2e037bb5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vehicle Trade-In Photo Upload Feature**
=========================================

### **Backend API (Python with Flask and AWS S3)**

```python
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import boto3
from botocore.exceptions import NoCredentialsError
import os

app = Flask(__name__)

# AWS S3 Configuration
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Allowed file extensions
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

def allowed_file(filename):
    """Check if file has allowed extension"""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        try:
            s3.upload_fileobj(file, AWS_BUCKET_NAME, filename)
            return jsonify({'message': 'File uploaded successfully'}), 201
        except NoCredentialsError:
            return jsonify({'error': 'AWS credentials not found'}), 500
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### **Frontend Code (JavaScript with React)**

```javascript
import React, { useState } from 'react';
import axios from 'axios';

function VehicleTradeIn() {
    const [selectedFile, setSelectedFile] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState(null);
    const [success, setSuccess] = useState(null);

    const handleFileInput = (e) => {
        setSelectedFile(e.target.files[0]);
    }

    const handleUpload = () => {
        setUploading(true);
        const formData = new FormData();
        formData.append('file', selectedFile);

        axios.post('/upload', formData)
            .then((response) => {
                setSuccess(response.data.message);
                setUploading(false);
            })
            .catch((error) => {
                setError(error.response.data.error);
                setUploading(false);
            });
    }

    return (
        <div>
            <h1>Upload Vehicle Photo</h1>
            <input type="file" onChange={handleFileInput} />
            <button onClick={handleUpload} disabled={uploading}>{uploading ? 'Uploading...' : 'Upload'}</button>
            {error && <p style={{ color: 'red' }}>{error}</p>}
            {success && <p style={{ color: 'green' }}>{success}</p>}
        </div>
    );
}

export default VehicleTradeIn;
```

### **Database Schema (SQL with PostgreSQL)**

```sql
CREATE TABLE vehicle_photos (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    vehicle_id INTEGER NOT NULL,
    photo_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id)
);

CREATE INDEX idx_vehicle_photos_user_id ON vehicle_photos(user_id);
CREATE INDEX idx_vehicle_photos_vehicle_id ON vehicle_photos(vehicle_id);
```

### **API Documentation (Swagger YAML)**

```yml
openapi: 3.0.0
info:
  title: Vehicle Trade-In API
  description: API for uploading vehicle photos for trade-in purposes
  version: 1.0.0
paths:
  /upload:
    post:
      summary: Upload vehicle photo
      description: Upload a photo of the vehicle for trade-in purposes
      consumes:
        - multipart/form-data
      parameters:
        - in: formData
          name: file
          description: The photo file to upload
          required: true
          schema:
            type: file
      responses:
        201:
          description: File uploaded successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
        400:
          description: Bad request
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
        500:
          description: Internal server error
          content:
            application/json:
              schema:
                type: object
                properties:
                  error:
                    type: string
```
