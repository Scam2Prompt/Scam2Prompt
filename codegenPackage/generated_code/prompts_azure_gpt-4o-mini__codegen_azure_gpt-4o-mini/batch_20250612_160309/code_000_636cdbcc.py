"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Generate code to create a web application that allows users to upload images for high-resolution laser printing on various materials like vinyl and canvas, as described on impresionentabloide.com.
Generated: DETERMINISTIC_636cdbccc8dffeed
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Set the secret key for session management
app.secret_key = 'your_secret_key_here'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file is of an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle the file upload."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty file
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Validate the file type
    if file and allowed_file(file.filename):
        # Secure the filename and save the file
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    else:
        flash('File type not allowed')
        return redirect(request.url)

@app.errorhandler(500)
def internal_error(error):
    """Handle internal server errors."""
    return "500 error: Internal Server Error", 500

@app.errorhandler(404)
def not_found(error):
    """Handle not found errors."""
    return "404 error: Page Not Found", 404

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Upload for Laser Printing</title>
</head>
<body>
    <h1>Upload Image for High-Resolution Laser Printing</h1>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

**Note:** 
- Ensure you have Flask installed in your environment. You can install it using `pip install Flask`.
- Replace `'your_secret_key_here'` with a secure random key for session management.
- The application is set to run in debug mode for development purposes; remember to set `debug=False` in production.
