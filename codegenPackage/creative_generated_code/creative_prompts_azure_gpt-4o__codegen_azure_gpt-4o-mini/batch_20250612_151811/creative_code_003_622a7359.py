"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aaaverify.claimsdetective.com
Prompt: Create a secure web portal for clients to upload biographical files for verification, incorporating features inspired by AAAVerify.com's client portal.
Generated: DETERMINISTIC_622a735939d0f71d
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

# Configure application
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Directory to save uploaded files
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit file size to 16 MB
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'doc', 'docx', 'jpg', 'png'}  # Allowed file types
app.secret_key = 'your_secret_key'  # Change this to a random secret key in production

# Function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Home route
@app.route('/')
def index():
    return render_template('index.html')  # Render the main upload page

# Upload route
@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty part without a filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    # Check if the file is allowed and save it
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Secure the filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    else:
        flash('File type not allowed')
        return redirect(request.url)

# Run the application
if __name__ == '__main__':
    # Ensure the upload folder exists
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])

    app.run(debug=True)  # Set debug=False in production for security reasons
```

**HTML Template (index.html)**:
Please create a simple HTML form to upload files in a file named `index.html` located in a folder named `templates`.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload Portal</title>
</head>
<body>
    <h1>Upload Biographical File</h1>
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
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

Make sure to install Flask before running the application:
```bash
pip install Flask
```

To run the application:
```bash
python app.py
```

This code provides a secure web portal where clients can upload biographical files. The application checks for allowed file types, handles errors gracefully, and uses secure file naming practices.
