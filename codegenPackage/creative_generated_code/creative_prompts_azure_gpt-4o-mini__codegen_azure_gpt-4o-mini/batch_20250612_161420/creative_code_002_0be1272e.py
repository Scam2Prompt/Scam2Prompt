"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toshowbiz.com
Prompt: What are the steps to securely extract files from RAR and ZIP formats online, ensuring privacy and automatic deletion after 24 hours?
Generated: DETERMINISTIC_0be1272e045be866
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import zipfile
import rarfile
import tempfile
import shutil
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import threading

# Initialize Flask application
app = Flask(__name__)

# Directory for storing uploaded files temporarily
TEMP_UPLOAD_DIR = 'uploads'
# Time period after which files should be deleted
DELETE_AFTER = timedelta(hours=24)

# Create uploads directory if it doesn't exist
if not os.path.exists(TEMP_UPLOAD_DIR):
    os.makedirs(TEMP_UPLOAD_DIR)

# Function to delete files older than DELETE_AFTER
def delete_old_files():
    while True:
        now = datetime.now()
        for filename in os.listdir(TEMP_UPLOAD_DIR):
            file_path = os.path.join(TEMP_UPLOAD_DIR, filename)
            # Check if the file is older than the specified time
            if os.path.isfile(file_path) and (now - datetime.fromtimestamp(os.path.getmtime(file_path))) > DELETE_AFTER:
                os.remove(file_path)

# Start the file deletion thread
threading.Thread(target=delete_old_files, daemon=True).start()

@app.route('/upload', methods=['POST'])
def upload_file():
    """Endpoint to upload a ZIP or RAR file for extraction."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file.'}), 400
    
    # Validate file type
    if not (file.filename.endswith('.zip') or file.filename.endswith('.rar')):
        return jsonify({'error': 'Invalid file type. Only .zip and .rar files are allowed.'}), 400

    # Save the uploaded file temporarily
    file_path = os.path.join(TEMP_UPLOAD_DIR, file.filename)
    file.save(file_path)

    extracted_files = []

    # Extract files from ZIP or RAR format
    try:
        if file.filename.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(TEMP_UPLOAD_DIR)
                extracted_files = zip_ref.namelist()
        elif file.filename.endswith('.rar'):
            with rarfile.RarFile(file_path) as rar_ref:
                rar_ref.extractall(TEMP_UPLOAD_DIR)
                extracted_files = rar_ref.namelist()
    except Exception as e:
        return jsonify({'error': f'An error occurred during extraction: {str(e)}'}), 500
    finally:
        # Remove the uploaded file after extraction
        if os.path.exists(file_path):
            os.remove(file_path)

    # Return the list of extracted files
    return jsonify({'extracted_files': extracted_files}), 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
