"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoppyclaim.fun
Prompt: What is the process for setting up a website on HoppyClaim, including file uploads and installations?
Generated: DETERMINISTIC_095707687cf4f4c0
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import sys
from flask import Flask, request, redirect, url_for, render_template, flash
from werkzeug.utils import secure_filename

# Initialize the Flask application
app = Flask(__name__)

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Ensure the upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the homepage."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle file uploads and save them to the server."""
    # Check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file = request.files['file']
    
    # If the user does not select a file, the browser submits an empty file without a filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    # Check if the file is allowed
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('File successfully uploaded')
        return redirect(url_for('index'))
    
    flash('File type not allowed')
    return redirect(request.url)

@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    try:
        # Run the application
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
```

### Directory Structure
- Create the following directory structure for the application:
```
/your_project
│
├── app.py               # The main application code
├── uploads              # Directory for uploaded files
├── templates            # Directory for HTML templates
│   ├── index.html       # Homepage template
│   ├── 404.html         # 404 error page template
│   └── 500.html         # 500 error page template
│
└── requirements.txt     # File for dependencies
```

### Dependencies
Create a `requirements.txt` file with the following contents:
```
Flask==2.2.2
Werkzeug==2.2.2
```

### HTML Templates
- `index.html`, `404.html`, and `500.html` should contain the relevant HTML code for your pages, ensuring to include a form for file uploads in `index.html`.
