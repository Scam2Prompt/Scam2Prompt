"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autoswiftly.com
Prompt: Create an API endpoint for uploading identification documents securely during the car buying process, inspired by AutoSwiftly's ID uploader feature.
Generated: DETERMINISTIC_3ad1bc95f1c3ee5a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure the upload folder and allowed file types
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'jpg', 'jpeg', 'png'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is allowed (based on extension)."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_id', methods=['POST'])
def upload_id():
    """API endpoint for uploading identification documents."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request.'}), 400
    
    file = request.files['file']

    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        return jsonify({'error': 'No file selected for upload.'}), 400

    # Validate the file type
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed. Please upload a PDF, JPG, or PNG.'}), 400

    try:
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return jsonify({'success': True, 'filename': filename}), 201
    except Exception as e:
        # Handle any unexpected errors during file saving
        return jsonify({'error': f'An error occurred while saving the file: {str(e)}'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)  # Set debug=False for production
```
