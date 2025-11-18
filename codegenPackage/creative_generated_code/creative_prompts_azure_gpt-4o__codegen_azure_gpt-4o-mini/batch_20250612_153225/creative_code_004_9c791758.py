"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rayzentreprise.com
Prompt: Write code to integrate cloud security features into a video surveillance system, ensuring secure storage and remote access, as described by Ray-Z Entreprise.
Generated: DETERMINISTIC_9c79175830d3a064
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
import json
from cryptography.fernet import Fernet
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveillance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Encryption key for secure storage
# In production, use a secure method to store keys
encryption_key = Fernet.generate_key()
cipher = Fernet(encryption_key)

# Database model for storing video metadata
class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(100), nullable=False)
    encrypted_data = db.Column(db.LargeBinary, nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

@app.route('/upload', methods=['POST'])
def upload_video():
    """Endpoint to upload a new video and store it securely."""
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        # Read and encrypt the video file
        file_data = file.read()
        encrypted_data = cipher.encrypt(file_data)

        # Store video metadata in the database
        new_video = Video(filename=file.filename, encrypted_data=encrypted_data)
        db.session.add(new_video)
        db.session.commit()

        return jsonify({"message": "Video uploaded successfully", "id": new_video.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Database error: {e}")
        return jsonify({"error": "Failed to upload video"}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/videos/<int:video_id>', methods=['GET'])
def get_video(video_id):
    """Endpoint to retrieve a video by its ID."""
    try:
        video = Video.query.get(video_id)
        if not video:
            return jsonify({"error": "Video not found"}), 404
        
        # Decrypt the video data
        decrypted_data = cipher.decrypt(video.encrypted_data)

        return jsonify({
            "filename": video.filename,
            "data": decrypted_data.decode('latin-1')  # Decode to display or stream
        }), 200
    except Exception as e:
        logging.error(f"Error retrieving video: {e}")
        return jsonify({"error": "Failed to retrieve video"}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```

**Note:** Before deploying this code in a production environment, ensure that you store your encryption key securely and handle video data appropriately per your requirements. The encrypted video data should not be exposed directly in a production API response. The provided code is for demonstration purposes and may require further adjustments based on specific security needs and compliance requirements.
