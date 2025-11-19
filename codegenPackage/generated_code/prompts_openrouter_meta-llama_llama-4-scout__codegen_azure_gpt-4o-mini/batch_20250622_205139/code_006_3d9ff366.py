"""
Generated Code Metadata:
========================
Original URL: https://metamark.lt
Prompt: Implement a content management system (CMS) for a business website, allowing clients to easily update content, images, and other elements, using a platform like WordPress or a custom solution.
Generated: DETERMINISTIC_3d9ff366340b3bdf
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit upload size to 16MB
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initialize the database
db = SQLAlchemy(app)

# Define the Content model
class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)
    image_filename = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Content {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the homepage
@app.route('/')
def index():
    contents = Content.query.all()
    return render_template('index.html', contents=contents)

# Route to add new content
@app.route('/add', methods=['GET', 'POST'])
def add_content():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        image = request.files.get('image')

        # Validate title and body
        if not title or not body:
            flash('Title and body are required!', 'error')
            return redirect(url_for('add_content'))

        # Handle image upload
        image_filename = None
        if image:
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))

        # Create new content entry
        new_content = Content(title=title, body=body, image_filename=image_filename)
        db.session.add(new_content)
        db.session.commit()
        flash('Content added successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('add_content.html')

# Route to edit existing content
@app.route('/edit/<int:content_id>', methods=['GET', 'POST'])
def edit_content(content_id):
    content = Content.query.get_or_404(content_id)

    if request.method == 'POST':
        content.title = request.form['title']
        content.body = request.form['body']
        image = request.files.get('image')

        # Handle image upload
        if image:
            image_filename = secure_filename(image.filename)
            image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_filename))
            content.image_filename = image_filename

        db.session.commit()
        flash('Content updated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('edit_content.html', content=content)

# Route to delete content
@app.route('/delete/<int:content_id>', methods=['POST'])
def delete_content(content_id):
    content = Content.query.get_or_404(content_id)
    db.session.delete(content)
    db.session.commit()
    flash('Content deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Ensure the upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)  # Set debug=False in production
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CMS Home</title>
</head>
<body>
    <h1>Content Management System</h1>
    <a href="{{ url_for('add_content') }}">Add New Content</a>
    <ul>
        {% for content in contents %}
            <li>
                <h2>{{ content.title }}</h2>
                <p>{{ content.body }}</p>
                {% if content.image_filename %}
                    <img src="{{ url_for('static', filename='uploads/' + content.image_filename) }}" alt="{{ content.title }}">
                {% endif %}
                <form action="{{ url_for('delete_content', content_id=content.id) }}" method="POST">
                    <button type="submit">Delete</button>
                </form>
                <a href="{{ url_for('edit_content', content_id=content.id) }}">Edit</a>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

**add_content.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Content</title>
</head>
<body>
    <h1>Add New Content</h1>
    <form action="{{ url_for('add_content') }}" method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="body">Body:</label>
        <textarea name="body" required></textarea>
        <label for="image">Image:</label>
        <input type="file" name="image">
        <button type="submit">Add Content</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

**edit_content.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Content</title>
</head>
<body>
    <h1>Edit Content</h1>
    <form action="{{ url_for('edit_content', content_id=content.id) }}" method="POST" enctype="multipart/form-data">
        <label for="title">Title:</label>
        <input type="text" name="title" value="{{ content.title }}" required>
        <label for="body">Body:</label>
        <textarea name="body" required>{{ content.body }}</textarea>
        <label for="image">Image:</label>
        <input type="file" name="image">
        <button type="submit">Update Content</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
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
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

### Note
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Adjust the `UPLOAD_FOLDER` path as needed.
- Replace `your_secret_key` with a secure random key for production use.
