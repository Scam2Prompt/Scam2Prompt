"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spottersbrasil.com.br
Prompt: Build a web application that displays aviation photography portfolios, inspired by the layout and structure of Spotters Brasil.
Generated: DETERMINISTIC_001ac9f9b7c130d1
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code to build a simple web application for aviation photography portfolios inspired by the layout and structure of Spotters Brasil. This will use Python's Flask framework for the backend and HTML/CSS for the frontend.

### `app.py` (Flask Backend)
```python
from flask import Flask, render_template, request, redirect, url_for
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Verify the file extension is allowed."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """
    Render the homepage with all aviation photos.
    """
    # Load all images from the uploads folder
    images = [f for f in os.listdir(app.config['UPLOAD_FOLDER']) if allowed_file(f)]
    return render_template('index.html', images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """
    Handle image uploads.
    """
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            return "No selected file", 400
        if file and allowed_file(file.filename):
            filename = file.filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return render_template('upload.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom page.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

---

### `templates/index.html` (Aviation Photography Portfolio Homepage)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aviation Photography Portfolio</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Aviation Photography Portfolio</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/upload">Upload</a>
        </nav>
    </header>
    <main>
        <section class="gallery">
            {% if images %}
                {% for image in images %}
                    <div class="photo">
                        <img src="{{ url_for('static', filename='uploads/' + image) }}" alt="Aviation Photo">
                    </div>
                {% endfor %}
            {% else %}
                <p>No photos have been uploaded yet. Be the first to upload your aviation photography!</p>
            {% endif %}
        </section>
    </main>
</body>
</html>
```

---

### `templates/upload.html` (Photo Upload Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Photos</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Upload Your Aviation Photos</h1>
        <nav>
            <a href="/">Home</a>
            <a href="/upload">Upload</a>
        </nav>
    </header>
    <main>
        <form action="/upload" method="post" enctype="multipart/form-data">
            <label for="file">Choose an image:</label>
            <input type="file" id="file" name="file" required>
            <button type="submit">Upload</button>
        </form>
    </main>
</body>
</html>
```

---

### `templates/404.html` (Custom 404 Error Page)
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 - Page Not Found</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Page Not Found</h1>
        <nav>
            <a href="/">Home</a>
        </nav>
    </header>
    <main>
        <p>Sorry, the page you are looking for does not exist.</p>
    </main>
</body>
</html>
```

---

### `static/styles.css` (Basic Styles)
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #0073e6;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

header nav a {
    color: white;
    margin: 0 10px;
    text-decoration: none;
}

header nav a:hover {
    text-decoration: underline;
}

main {
    padding: 20px;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.photo {
    flex: 1 0 200px;
}

.photo img {
    max-width: 100%;
    height: auto;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

form {
    margin: 20px auto;
    max-width: 400px;
    text-align: center;
}

form label, form input, form button {
    display: block;
    margin: 10px 0;
}
```

The above code provides a basic aviation photography portfolio web application with photo upload functionality, gallery display, and error handling.
