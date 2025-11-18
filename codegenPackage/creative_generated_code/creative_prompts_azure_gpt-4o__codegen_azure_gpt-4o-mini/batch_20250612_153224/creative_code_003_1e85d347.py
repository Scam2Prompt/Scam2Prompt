"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoinayadv.com
Prompt: Provide Python code to integrate a feature into a website that allows customers to upload their designs for metallic stickers, including Nickel and Stainless Steel options, as described on jttlogos.com.
Generated: DETERMINISTIC_1e85d3476643bcf5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, render_template, redirect, url_for, flash
import os

app = Flask(__name__)

# Set secret key for session management
app.secret_key = 'your_secret_key_here'

# Configure upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Check if the uploaded file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Render the main upload page."""
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle the file upload from the user."""
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Secure the filename to prevent directory traversal attacks
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        
        try:
            file.save(file_path)
            flash('File successfully uploaded')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'An error occurred while saving the file: {str(e)}')
            return redirect(request.url)
    else:
        flash('Invalid file type. Allowed types are: png, jpg, jpeg, gif.')
        return redirect(request.url)

if __name__ == "__main__":
    # Run the app in debug mode for development
    app.run(debug=True)
```

```html
<!-- templates/upload.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Your Design</title>
</head>
<body>
    <h1>Upload Your Sticker Design</h1>
    <form action="{{ url_for('upload_file') }}" method="post" enctype="multipart/form-data">
        <label for="file">Choose your design file:</label>
        <input type="file" name="file" id="file" required>
        <button type="submit">Upload</button>
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

**Note**: Ensure you have Flask installed (`pip install Flask`) and create the `uploads/` directory in your working directory before running the app. Adjust the `secret_key` for production use.
