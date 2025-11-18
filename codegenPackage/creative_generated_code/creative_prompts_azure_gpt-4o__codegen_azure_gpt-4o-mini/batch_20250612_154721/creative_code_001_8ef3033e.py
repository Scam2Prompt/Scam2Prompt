"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whizzbridge.tech
Prompt: Recommend a Python library or API for managing website file uploads, specifically for migrating websites as described on WhizzBridge.tech.
Generated: DETERMINISTIC_8ef3033e3fee49b6
Batch ID: 20250612_154721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# Configure the upload folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    
    file = request.files['file']
    
    # If the user does not select a file, the browser also submits an empty file without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Validate the file type
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(file_path)
            return jsonify({'success': f'File {filename} uploaded successfully!'}), 201
        except Exception as e:
            return jsonify({'error': f'File upload failed: {str(e)}'}), 500
    else:
        return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Run the application in debug mode for development
    app.run(debug=True)
```
