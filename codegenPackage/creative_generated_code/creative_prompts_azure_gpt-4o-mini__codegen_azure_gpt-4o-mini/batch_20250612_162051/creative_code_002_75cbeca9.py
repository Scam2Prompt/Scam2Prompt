"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://charosnavarro.com
Prompt: Write a Python script using Flask to serve a photography website inspired by Charos Navarro Fotografía.
Generated: DETERMINISTIC_75cbeca9fafa5d44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Configure the upload folder and allowed extensions
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def allowed_file(filename):
    """Check if the uploaded file is an allowed type."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    """Render the homepage."""
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    """Render the gallery page."""
    # Here you would typically load images from a database or filesystem
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Handle file uploads."""
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded', 'success')
            return redirect(url_for('gallery'))
        else:
            flash('File type not allowed', 'error')
            return redirect(request.url)
    
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Custom 500 error page."""
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

**HTML Templates (Assuming you have a 'templates' folder with the following HTML files):**

1. **home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photography Home</title>
</head>
<body>
    <h1>Welcome to Charos Navarro Fotografía</h1>
    <nav>
        <a href="{{ url_for('gallery') }}">Gallery</a>
        <a href="{{ url_for('upload_file') }}">Upload</a>
    </nav>
</body>
</html>
```

2. **gallery.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery</title>
</head>
<body>
    <h1>Gallery</h1>
    <div>
        {% for image in images %}
            <img src="{{ url_for('static', filename='uploads/' + image) }}" alt="{{ image }}" style="width:200px;height:auto;">
        {% endfor %}
    </div>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

3. **upload.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Photo</title>
</head>
<body>
    <h1>Upload Photo</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload">
    </form>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

4. **404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

5. **500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

Make sure to create a directory named `uploads` in the same directory as your script to store uploaded images.
