"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://churchproweb.com
Prompt: Write code to create a "Sermon Manager" feature for a church website, including functionality for uploading sermons, categorizing them by date and topic, and enabling users to stream or download them. Use ChurchProWeb's design principles for user-friendly navigation.
Generated: DETERMINISTIC_629b04e13608f1c3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# sermon_manager.py

from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
import os
from datetime import datetime

app = Flask(__name__)

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'mp3', 'mp4', 'wav'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_sermon():
    """
    Endpoint to upload a sermon file.
    Expects a file, date, and topic in the form data.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        sermon_date = request.form.get('date')
        topic = request.form.get('topic')
        
        # Optionally validate date and topic here
        if not sermon_date or not topic:
            return jsonify({'error': 'Date and topic are required'}), 400
        
        # Create a unique filename using date and topic
        unique_filename = f"{sermon_date}_{topic}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        
        return jsonify({'message': 'File uploaded successfully', 'filename': unique_filename}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/sermons', methods=['GET'])
def list_sermons():
    """
    Endpoint to list all uploaded sermons.
    """
    sermons = []
    
    try:
        for filename in os.listdir(app.config['UPLOAD_FOLDER']):
            sermons.append({
                'filename': filename,
                'url': f"/stream/{filename}",
                'download_url': f"/download/{filename}"
            })
        
        return jsonify(sermons), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/stream/<filename>', methods=['GET'])
def stream_sermon(filename):
    """
    Endpoint to stream a sermon by filename.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/download/<filename>', methods=['GET'])
def download_sermon(filename):
    """
    Endpoint to download a sermon by filename.
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**Note**: This code assumes you have Flask installed in your Python environment. Use `pip install Flask` to install it. Adjust the configuration as needed for production environments, such as turning off debug mode and implementing a more robust file validation system.
