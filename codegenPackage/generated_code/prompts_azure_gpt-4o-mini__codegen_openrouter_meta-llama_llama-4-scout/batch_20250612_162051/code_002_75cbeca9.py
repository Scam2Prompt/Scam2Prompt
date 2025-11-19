"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Write a Python script using Flask to serve a photography website inspired by Charos Navarro Fotografía.
Generated: DETERMINISTIC_75cbeca9fafa5d44
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

# Create a Flask application instance
app = Flask(__name__)

# Configuration for the application
app.config['UPLOAD_FOLDER'] = './static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Create the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define a route for the home page
@app.route('/')
def home():
    """Renders the home page."""
    return render_template('home.html')

# Define a route for the gallery page
@app.route('/gallery')
def gallery():
    """Renders the gallery page."""
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

# Define a route for the about page
@app.route('/about')
def about():
    """Renders the about page."""
    return render_template('about.html')

# Define a route for uploading images
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Handles image uploads."""
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'No image part', 400
        image = request.files['image']
        if image.filename == '':
            return 'No image selected', 400
        if image:
            filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))
    return render_template('upload.html')

# Define a route for handling errors
@app.errorhandler(404)
def not_found(error):
    """Handles 404 errors."""
    return render_template('404.html'), 404

# Define a route for handling internal server errors
@app.errorhandler(500)
def internal_server_error(error):
    """Handles 500 errors."""
    return render_template('500.html'), 500

# Run the application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Charos Navarro Fotografía</title>
</head>
<body>
    <h1>Welcome to Charos Navarro Fotografía</h1>
    <p>Home page content</p>
</body>
</html>
```

```html
<!-- templates/gallery.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery</title>
</head>
<body>
    <h1>Gallery</h1>
    <ul>
    {% for image in images %}
        <li><img src="{{ url_for('static', filename='images/' + image) }}" alt="{{ image }}"></li>
    {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/about.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>About</title>
</head>
<body>
    <h1>About</h1>
    <p>About page content</p>
</body>
</html>
```

```html
<!-- templates/upload.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload</title>
</head>
<body>
    <h1>Upload Image</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="image">
        <input type="submit" value="Upload">
    </form>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>Page not found</p>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Error</title>
</head>
<body>
    <h1>500 Error</h1>
    <p>Internal server error</p>
</body>
</html>
```
