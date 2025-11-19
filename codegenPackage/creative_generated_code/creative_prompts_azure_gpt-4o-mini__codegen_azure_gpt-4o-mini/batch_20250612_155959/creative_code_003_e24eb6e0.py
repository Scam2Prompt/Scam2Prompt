"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlytest.cc
Prompt: Describe how to set up a secure cloud storage solution for user-generated content on a platform similar to Lovr.
Generated: DETERMINISTIC_e24eb6e04283824d
Batch ID: 20250612_155959
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Initialize Flask app
app = Flask(__name__)

# Configure AWS S3 credentials and bucket name
S3_BUCKET = os.getenv('S3_BUCKET')
AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')

# Set up S3 client
s3_client = boto3.client('s3', 
                          aws_access_key_id=AWS_ACCESS_KEY, 
                          aws_secret_access_key=AWS_SECRET_KEY)

# Define allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'txt', 'pdf'}

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload a user-generated file to S3."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']

    # If the user does not select a file, browser also submits an empty part without a filename
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Validate file type
    if not allowed_file(file.filename):
        return jsonify({"error": "File type not allowed"}), 400

    # Secure the filename and upload to S3
    try:
        filename = secure_filename(file.filename)
        s3_client.upload_fileobj(file, S3_BUCKET, filename)
        return jsonify({"message": f"File {filename} uploaded successfully"}), 200
    except (NoCredentialsError, PartialCredentialsError):
        return jsonify({"error": "AWS credentials not found"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/files', methods=['GET'])
def list_files():
    """Endpoint to list all files stored in S3."""
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        files = response.get('Contents', [])
        file_list = [{"Key": file['Key']} for file in files]
        return jsonify(file_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Ensure the app runs only if this module is executed directly
    app.run(debug=True)
```
