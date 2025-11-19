"""
Generated Code Metadata:
========================
Original URL: https://starke-orte.land
Prompt: "Create a simple web application using a framework like Flask or Django to facilitate knowledge sharing and collaboration among municipalities, inspired by the Starke Orte Netzwerk's community platform."
Generated: DETERMINISTIC_29f9082b91e0cfb4
Batch ID: 20250622_205523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A simple web application using Flask to facilitate knowledge sharing and collaboration among municipalities.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)

# Set up secret key for session management and flash messages
app.secret_key = os.environ.get('SECRET_KEY', 'default_secret_key')

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///municipalities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the database model for posts
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Post {self.title}>"

# Route for the home page
@app.route('/')
def index():
    posts = Post.query.all()  # Fetch all posts from the database
    return render_template('index.html', posts=posts)

# Route for creating a new post
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        author = request.form.get('author')

        # Validate form inputs
        if not title or not content or not author:
            flash('All fields are required!', 'error')
            return redirect(url_for('create'))

        # Create a new post and save it to the database
        new_post = Post(title=title, content=content, author=author)
        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating post: {str(e)}', 'error')
            return redirect(url_for('create'))

    return render_template('create.html')

# Route for viewing a single post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)  # Fetch the post or return 404
    return render_template('view_post.html', post=post)

# Route for deleting a post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    try:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting post: {str(e)}', 'error')
    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    # Start the Flask development server
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Municipalities Collaboration Platform</title>
</head>
<body>
    <h1>Municipalities Collaboration Platform</h1>
    <a href="{{ url_for('create') }}">Create New Post</a>
    <hr>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>By {{ post.author }}</p>
        <p>{{ post.content }}</p>
        <a href="{{ url_for('view_post', post_id=post.id) }}">View Details</a>
        <form action="{{ url_for('delete_post', post_id=post.id) }}" method="POST">
            <button type="submit">Delete</button>
        </form>
        <hr>
    {% endfor %}
</body>
</html>
```

```html
<!-- templates/create.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Post</title>
</head>
<body>
    <h1>Create New Post</h1>
    <form action="{{ url_for('create') }}" method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required>
        <br>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/view_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author }}</p>
    <p>{{ post.content }}</p>
    <a href="{{ url_for('index') }}">Back to Home</a>
</body>
</html>
```
