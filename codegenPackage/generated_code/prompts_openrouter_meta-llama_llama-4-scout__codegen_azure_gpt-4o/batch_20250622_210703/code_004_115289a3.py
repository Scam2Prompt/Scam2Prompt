"""
Generated Code Metadata:
========================
Original URL: https://jkpcrnica.rs
Prompt: How would you implement a simple document management system for a public communal enterprise like "ЦРНИЦА" in Параћин using a library or framework of your choice?
Generated: DETERMINISTIC_115289a3606b7a18
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx', 'xlsx', 'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to upload a document
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        # Check if a file is included in the request
        if 'file' not in request.files:
            return jsonify({'error': 'No file part in the request'}), 400
        
        file = request.files['file']
        
        # Check if the file has a valid name
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        # Validate file extension
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'message': f'File {filename} uploaded successfully'}), 200
        else:
            return jsonify({'error': 'Invalid file type'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to list all uploaded documents
@app.route('/documents', methods=['GET'])
def list_documents():
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        return jsonify({'documents': files}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to download a specific document
@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        # Secure the filename and check if it exists
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(filepath):
            return jsonify({'message': f'File {filename} is ready for download'}), 200
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Route to delete a specific document
@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file(filename):
    try:
        # Secure the filename and check if it exists
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename))
        if os.path.exists(filepath):
            os.remove(filepath)
            return jsonify({'message': f'File {filename} deleted successfully'}), 200
        else:
            return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```
