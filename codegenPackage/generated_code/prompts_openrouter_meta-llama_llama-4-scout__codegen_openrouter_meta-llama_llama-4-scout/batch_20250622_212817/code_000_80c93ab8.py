"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Write a Python script to create a portfolio website for a freelance artist with sections for music and horror projects, inspired by PhantomsLens.
Generated: DETERMINISTIC_80c93ab8935095d4
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

# Create a Flask application instance
app = Flask(__name__)

# Define configuration for the application
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Ensure the upload folder exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define a function to allowed file types
def allowed_file(filename):
    # Allow image files
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['png', 'jpg', 'jpeg', 'gif']

# Define routes for the application
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/horror')
def horror():
    return render_template('horror.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
        # If user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            return 'No file selected', 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully', 200
    return render_template('upload.html')

# Define error handlers
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Freelance Artist Portfolio</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Welcome to my portfolio website!</h1>
    </main>
</body>
</html>
```

```html
<!-- templates/music.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Music Projects</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Music Projects</h1>
        <!-- Add music project content here -->
    </main>
</body>
</html>
```

```html
<!-- templates/horror.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Horror Projects</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Horror Projects</h1>
        <!-- Add horror project content here -->
    </main>
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
    <title>Upload File</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>Upload File</h1>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    </main>
</body>
</html>
```

```css
/* static/styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

h1 {
    color: #333;
}
```

```html
<!-- templates/404.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Error</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>404 Error: Page Not Found</h1>
        <p>The page you are looking for does not exist.</p>
    </main>
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
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                <li><a href="{{ url_for('music') }}">Music</a></li>
                <li><a href="{{ url_for('horror') }}">Horror</a></li>
                <li><a href="{{ url_for('upload_file') }}">Upload</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <h1>500 Error: Internal Server Error</h1>
        <p>An internal server error occurred.</p>
    </main>
</body>
</html>
```
