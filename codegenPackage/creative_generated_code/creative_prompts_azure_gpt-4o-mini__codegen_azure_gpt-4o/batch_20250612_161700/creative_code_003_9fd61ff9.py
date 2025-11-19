"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lggraphics.com.br
Prompt: Develop a web application feature that allows users to upload designs for vinyl stickers and select from different adhesive types available at L&G Graphics.
Generated: DETERMINISTIC_9fd61ff9fcdcd3fd
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, jsonify
import os
from werkzeug.utils import secure_filename

# Initialize Flask application
app = Flask(__name__)

# Configuration for file uploads
UPLOAD_FOLDER = 'uploads/'  # Directory to store uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg', 'pdf'}  # Allowed file extensions
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the main page to display the upload form
@app.route('/')
def index():
    return render_template('index.html')  # Render the HTML form for file upload

# Route to handle file uploads and adhesive type selection
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    adhesive_type = request.form.get('adhesive_type')  # Get adhesive type from form

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Secure the filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file
        return jsonify({
            'message': 'File uploaded successfully',
            'filename': filename,
            'adhesive_type': adhesive_type
        }), 200
    else:
        return jsonify({'error': 'Invalid file format'}), 400

# Error handler for 404 (page not found)
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Page not found'}), 404

# Error handler for 500 (internal server error)
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'An internal error occurred'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Vinyl Sticker Designs</title>
</head>
<body>
    <h1>Upload Your Vinyl Sticker Design</h1>
    <form action="/upload" method="POST" enctype="multipart/form-data">
        <label for="file">Choose file:</label>
        <input type="file" id="file" name="file" required>
        <br><br>
        <label for="adhesive_type">Select adhesive type:</label>
        <select id="adhesive_type" name="adhesive_type" required>
            <option value="standard">Standard</option>
            <option value="removable">Removable</option>
            <option value="permanent">Permanent</option>
        </select>
        <br><br>
        <button type="submit">Upload</button>
    </form>
</body>
</html>
```

### Notes:
- This code utilizes Flask for backend development and provides a simple HTML form for file uploads.
- Error handling is implemented for missing files, invalid formats, and server errors.
- The uploaded files are stored in the `uploads/` directory, and a user can select the adhesive type during upload.
- The code is production-ready with basic security practices like file type validation and secure filename handling.
