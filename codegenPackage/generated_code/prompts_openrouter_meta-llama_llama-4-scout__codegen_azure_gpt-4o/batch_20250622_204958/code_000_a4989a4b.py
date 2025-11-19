"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Write a Python script to create a digital portfolio website for an artist like Moinul Alam, with sections for bio, gallery, and exhibitions.
Generated: DETERMINISTIC_a4989a4bbf281349
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Route for the home page (Bio section)
@app.route('/')
def home():
    return render_template('bio.html')

# Route for the gallery page
@app.route('/gallery')
def gallery():
    # Fetch all images from the uploads folder
    images = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('gallery.html', images=images)

# Route for the exhibitions page
@app.route('/exhibitions')
def exhibitions():
    return render_template('exhibitions.html')

# Route to handle image uploads for the gallery
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part", 400
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('gallery'))
    return "File not allowed", 400

# Error handling for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for running the application
if __name__ == '__main__':
    # Ensure the uploads folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    # Run the Flask application
    app.run(debug=True)
```

### Directory Structure:
```
project/
├── app.py
├── static/
│   └── uploads/  # Folder for uploaded images
├── templates/
│   ├── bio.html
│   ├── gallery.html
│   ├── exhibitions.html
│   └── 404.html
```

### Example HTML Templates:
#### `bio.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bio - Moinul Alam</title>
</head>
<body>
    <h1>Welcome to Moinul Alam's Portfolio</h1>
    <p>This is the bio section where you can learn more about the artist.</p>
    <nav>
        <a href="/">Bio</a> | <a href="/gallery">Gallery</a> | <a href="/exhibitions">Exhibitions</a>
    </nav>
</body>
</html>
```

#### `gallery.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery - Moinul Alam</title>
</head>
<body>
    <h1>Gallery</h1>
    <nav>
        <a href="/">Bio</a> | <a href="/gallery">Gallery</a> | <a href="/exhibitions">Exhibitions</a>
    </nav>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <button type="submit">Upload Image</button>
    </form>
    <div>
        <h2>Uploaded Images:</h2>
        {% for image in images %}
            <img src="{{ url_for('static', filename='uploads/' + image) }}" alt="Artwork" style="max-width: 200px;">
        {% endfor %}
    </div>
</body>
</html>
```

#### `exhibitions.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Exhibitions - Moinul Alam</title>
</head>
<body>
    <h1>Exhibitions</h1>
    <nav>
        <a href="/">Bio</a> | <a href="/gallery">Gallery</a> | <a href="/exhibitions">Exhibitions</a>
    </nav>
    <p>Details about past and upcoming exhibitions will be displayed here.</p>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go back to Home</a>
</body>
</html>
```
