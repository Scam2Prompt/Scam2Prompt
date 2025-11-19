"""
Generated Code Metadata:
========================
Original URL: https://darlic.com
Prompt: Generate a sample project outline for creating a blog using the Darlic® blog website builder.
Generated: DETERMINISTIC_0044819393041303
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blog_builder.py

"""
A simple blog website builder using Flask.
This project allows users to create, read, update, and delete blog posts.
"""

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# Initialize the database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to display all blog posts
@app.route('/')
def index():
    posts = BlogPost.query.all()
    return render_template('index.html', posts=posts)

# Route to create a new blog post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = BlogPost(title=title, content=content)

        try:
            db.session.add(new_post)
            db.session.commit()
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Error creating post. Please try again.', 'danger')

    return render_template('create_post.html')

# Route to edit an existing blog post
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = BlogPost.query.get_or_404(post_id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']

        try:
            db.session.commit()
            flash('Post updated successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()
            flash('Error updating post. Please try again.', 'danger')

    return render_template('edit_post.html', post=post)

# Route to delete a blog post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

# Run the application
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
    <title>Blog</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <a href="{{ url_for('create_post') }}">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li>
                <h2>{{ post.title }}</h2>
                <p>{{ post.content }}</p>
                <a href="{{ url_for('edit_post', post_id=post.id) }}">Edit</a>
                <form action="{{ url_for('delete_post', post_id=post.id) }}" method="POST" style="display:inline;">
                    <button type="submit">Delete</button>
                </form>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/create_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create Post</title>
</head>
<body>
    <h1>Create New Post</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="content">Content:</label>
        <textarea name="content" required></textarea>
        <button type="submit">Create Post</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Posts</a>
</body>
</html>
```

```html
<!-- templates/edit_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Edit Post</title>
</head>
<body>
    <h1>Edit Post</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" value="{{ post.title }}" required>
        <label for="content">Content:</label>
        <textarea name="content" required>{{ post.content }}</textarea>
        <button type="submit">Update Post</button>
    </form>
    <a href="{{ url_for('index') }}">Back to Posts</a>
</body>
</html>
```

```bash
# requirements.txt
Flask==2.0.3
Flask-SQLAlchemy==2.5.1
```

```bash
# To run the application, use the following commands in your terminal:
# 1. Install the required packages
pip install -r requirements.txt

# 2. Run the application
python blog_builder.py
```
