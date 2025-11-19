"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Recommend APIs or libraries for creating a photo gallery website that can showcase different types of photography, such as portrait, boudoir, and still life, similar to Officine dell'Immagine's work.
Generated: DETERMINISTIC_d31a423613cffedc
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///gallery.db'
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16 MB
db = SQLAlchemy(app)

# Define the Photo model
class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    filename = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Photo {self.title}>'

# Create the database
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def index():
    """Render the home page with all photos."""
    photos = Photo.query.all()
    return render_template('index.html', photos=photos)

# Route for uploading a new photo
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    """Handle photo upload and save to the database."""
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        file = request.files['file']

        # Validate file upload
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Create a new Photo instance and save to the database
            new_photo = Photo(title=title, category=category, filename=filename)
            db.session.add(new_photo)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return "Invalid file type. Please upload a valid image.", 400

    return render_template('upload.html')

# Function to check allowed file types
def allowed_file(filename):
    """Check if the uploaded file is an allowed image type."""
    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Render a custom 404 error page."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Photo Gallery</title>
</head>
<body>
    <h1>Photo Gallery</h1>
    <a href="{{ url_for('upload') }}">Upload New Photo</a>
    <div>
        {% for photo in photos %}
            <div>
                <h2>{{ photo.title }}</h2>
                <p>Category: {{ photo.category }}</p>
                <img src="{{ url_for('static', filename='uploads/' + photo.filename) }}" alt="{{ photo.title }}">
            </div>
        {% endfor %}
    </div>
</body>
</html>
```

**upload.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Upload Photo</title>
</head>
<body>
    <h1>Upload New Photo</h1>
    <form action="{{ url_for('upload') }}" method="post" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="category">Category:</label>
        <input type="text" name="category" required>
        <label for="file">File:</label>
        <input type="file" name="file" accept="image/*" required>
        <button type="submit">Upload</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Gallery</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Gallery</a>
</body>
</html>
```

### Note
Make sure to create a folder named `static/uploads` in your project directory to store uploaded images.
