"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panicinpolkadots.com
Prompt: Generate a code snippet for a web application that allows users to upload their old t-shirts for creating custom quilts, similar to the services offered by Panic in Polkadots.
Generated: DETERMINISTIC_98ba0cc4eab1d99e
Batch ID: 20250612_155327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Set the upload folder in the app's configuration
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the upload form."""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and return success or error message."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']

    # If user does not select a file, the browser may submit an empty part without filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Check if the file is allowed
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Here you could add logic to queue or process the images for quilt creation
        
        return jsonify({'message': 'File successfully uploaded', 'filename': filename}), 201
    
    return jsonify({'error': 'File type not allowed'}), 400

if __name__ == '__main__':
    # Run the app in debug mode for development purposes
    app.run(debug=True)
```

**HTML Template (upload.html)**:
```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>T-Shirt Quilt Upload</title>
</head>
<body>
    <h1>Upload Your T-Shirts for Custom Quilts</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept=".png, .jpg, .jpeg, .gif" required>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

This code provides a basic web application using Flask for uploading images of t-shirts, ready for further expansion into custom quilt creation functionality.
