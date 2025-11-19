"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Generate a code snippet for a web application that allows users to upload and print custom designs for large format printing, similar to the services offered by Ram Digi.
Generated: DETERMINISTIC_26b92b2e30e41e63
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Set the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

# Configure the application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
app.secret_key = 'your_secret_key'  # Change this to a secure key in production

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload and save it to the server."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    # If the user does not select a file, the browser may submit an empty part without a filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)  # Secure the file name
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))  # Save the file
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    else:
        flash('File type not allowed')
        return redirect(request.url)

@app.route('/print/<filename>')
def print_file(filename):
    """Route for printing the uploaded file. This is a placeholder for actual print functionality."""
    # Here you could add code to integrate with a printing service or manage printing jobs
    # For now, just confirm the print request
    return f'Print request received for {filename}'

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```

**Note:** You'll also need an `index.html` file in a `templates` directory to make this web application functional. Make sure to handle all necessary front-end aspects and integrate with a printing service in a real application.
