"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis.com.tw
Prompt: Suggest tools or frameworks for developing a web application that allows users to upload packaging designs and preview features like "window cutouts" and "foil stamping" in real-time, inspired by Metis's services.
Generated: DETERMINISTIC_ad15c28acfbc4ee3
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
import os
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Set the upload folder and allowed file extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Configure the application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and return a preview URL."""
    # Check if the post request has the file
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    
    # If the user does not select a file, the browser submits an empty file
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file is allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        preview_url = f"/uploads/{filename}"
        return jsonify({'message': 'File uploaded successfully', 'url': preview_url}), 200

    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """Serve the uploaded file."""
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
```

### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packaging Design Upload</title>
</head>
<body>
    <h1>Upload Packaging Design</h1>
    <form id="uploadForm" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
    <div id="preview"></div>

    <script>
        document.getElementById('uploadForm').onsubmit = async function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();
            if (response.ok) {
                document.getElementById('preview').innerHTML = `<img src="${result.url}" alt="Preview" style="max-width: 300px;">`;
            } else {
                alert(result.error);
            }
        };
    </script>
</body>
</html>
```

### Requirements
If you need to run this code, make sure to install Flask by executing:
```bash
pip install Flask
```

### Directory Structure
Ensure your directory structure looks like this:
```
/your_project_directory
    app.py          # Python code
    /uploads        # Folder for uploaded files
    /templates      # Folder for HTML files
        index.html  # HTML file
```

This code provides a basic Flask web application to upload packaging designs, with error handling and a simple frontend for previewing the uploaded images.
