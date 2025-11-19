"""
Generated Code Metadata:
========================
Original URL: https://yourpalmreading.com
Prompt: Write Python code to create a web application that allows users to upload images of their hands and stores them securely for analysis, similar to the functionality described on YourPalmReading.com.
Generated: DETERMINISTIC_64b85da6eeee4caf
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for session management
app.secret_key = 'your_secret_key_here'

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to check if the uploaded file is of an allowed type
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle file uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty file
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Validate the file and save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        try:
            file.save(file_path)
            flash('File successfully uploaded')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred while saving the file: {e}')
            return redirect(request.url)
    else:
        flash('File type not allowed')
        return redirect(request.url)

# Route to display uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Template (index.html)**

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Hand Image Upload</title>
</head>
<body>
    <h1>Upload Your Hand Image</h1>
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file" accept="image/*" required>
        <input type="submit" value="Upload">
    </form>
    {% with messages = get_flashed_messages() %}
        {% if messages %}
            <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

**Note:** Ensure you have Flask installed in your environment. You can install it using pip:

```bash
pip install Flask
```

Make sure to replace `'your_secret_key_here'` with a strong secret key for session management.
