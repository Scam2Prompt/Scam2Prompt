"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Write a Python script to create a photography portfolio website with sections for wedding, fashion, and event photography, inspired by Officine dell'Immagine's services.
Generated: DETERMINISTIC_2b6310c681585984
Batch ID: 20250622_212148
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
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

# Create a Flask application instance
app = Flask(__name__)

# Define configuration for the application
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB

# Initialize the upload folder if it doesn't exist
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Define a function to handle image uploads
def allowed_file(filename):
    """Check if a file is an allowed image file."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ['jpg', 'jpeg', 'png', 'gif']

# Define routes for the application
@app.route('/')
def index():
    """Render the index template."""
    return render_template('index.html')

@app.route('/wedding')
def wedding():
    """Render the wedding template."""
    images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], 'wedding'))
    return render_template('wedding.html', images=images)

@app.route('/fashion')
def fashion():
    """Render the fashion template."""
    images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], 'fashion'))
    return render_template('fashion.html', images=images)

@app.route('/event')
def event():
    """Render the event template."""
    images = os.listdir(os.path.join(app.config['UPLOAD_FOLDER'], 'event'))
    return render_template('event.html', images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Handle image uploads."""
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
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
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
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
    <title>Photography Portfolio</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('wedding') }}">Wedding</a></li>
            <li><a href="{{ url_for('fashion') }}">Fashion</a></li>
            <li><a href="{{ url_for('event') }}">Event</a></li>
        </ul>
    </nav>
    <h1>Welcome to our photography portfolio!</h1>
</body>
</html>
```

```html
<!-- templates/wedding.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wedding Photography</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('wedding') }}">Wedding</a></li>
            <li><a href="{{ url_for('fashion') }}">Fashion</a></li>
            <li><a href="{{ url_for('event') }}">Event</a></li>
        </ul>
    </nav>
    <h1>Wedding Photography</h1>
    <div class="gallery">
        {% for image in images %}
        <img src="{{ url_for('static', filename='images/wedding/' + image) }}" alt="Wedding Photo">
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- templates/fashion.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fashion Photography</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('wedding') }}">Wedding</a></li>
            <li><a href="{{ url_for('fashion') }}">Fashion</a></li>
            <li><a href="{{ url_for('event') }}">Event</a></li>
        </ul>
    </nav>
    <h1>Fashion Photography</h1>
    <div class="gallery">
        {% for image in images %}
        <img src="{{ url_for('static', filename='images/fashion/' + image) }}" alt="Fashion Photo">
        {% endfor %}
    </div>
</body>
</html>
```

```html
<!-- templates/event.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Event Photography</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('wedding') }}">Wedding</a></li>
            <li><a href="{{ url_for('fashion') }}">Fashion</a></li>
            <li><a href="{{ url_for('event') }}">Event</a></li>
        </ul>
    </nav>
    <h1>Event Photography</h1>
    <div class="gallery">
        {% for image in images %}
        <img src="{{ url_for('static', filename='images/event/' + image) }}" alt="Event Photo">
        {% endfor %}
    </div>
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
    <title>Upload Image</title>
</head>
<body>
    <h1>Upload Image</h1>
    <form action="" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
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
    <h1>404 Error: Page Not Found</h1>
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
    <h1>500 Error: Internal Server Error</h1>
</body>
</html>
```
