"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sala-events.co.il
Prompt: Suggest a cloud-based solution for managing large-scale events with up to 5,000 participants, inspired by DCITY Events' capacity and technological infrastructure.
Generated: DETERMINISTIC_4ce1b8a780e19082
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import boto3
from botocore.exceptions import ClientError
import json
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# AWS S3 configuration
S3_BUCKET_NAME = 'your-s3-bucket-name'

# Initialize the S3 client
s3_client = boto3.client('s3')

def upload_file_to_s3(file, bucket, object_name=None):
    """Uploads a file to an S3 bucket.

    Args:
        file (File): The file to upload.
        bucket (str): The S3 bucket name.
        object_name (str): The object name in the bucket.
    
    Returns:
        bool: True if file was uploaded, else False.
    """
    try:
        if object_name is None:
            object_name = file.filename
            
        s3_client.upload_fileobj(file, bucket, object_name)
        return True
    except ClientError as e:
        print(f"Error uploading file: {e}")
        return False

@app.route('/upload', methods=['POST'])
def upload_event_data():
    """Endpoint to upload event-related files.

    Returns:
        json: Response indicating success or failure of the upload.
    """
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Upload file to S3
    success = upload_file_to_s3(file, S3_BUCKET_NAME)
    
    if success:
        return jsonify({"message": "File uploaded successfully"}), 200
    else:
        return jsonify({"error": "File upload failed"}), 500

@app.route('/events', methods=['GET'])
def get_events():
    """Endpoint to retrieve all events.

    Returns:
        json: List of events.
    """
    # This is a placeholder for your event data access logic.
    events = [
        {"id": 1, "name": "Tech Conference", "participants": 5000},
        {"id": 2, "name": "Music Festival", "participants": 3000},
    ]
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Install Flask and Boto3 using pip:
```bash
pip install Flask boto3
```

### Notes:
- Replace `'your-s3-bucket-name'` with the actual name of your S3 bucket.
- Ensure that your AWS credentials are configured properly to allow S3 access.
