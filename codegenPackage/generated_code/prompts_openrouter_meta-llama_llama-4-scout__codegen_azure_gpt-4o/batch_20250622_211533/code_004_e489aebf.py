"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Design a web application for promoting sustainable living practices, including a blog for sharing environmental tips and a resource section for community projects.
Generated: DETERMINISTIC_e489aebff4039bf0
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# app.py
# A Flask-based web application for promoting sustainable living practices.
# Includes a blog for sharing environmental tips and a resource section for community projects.

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sustainable_living.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for Blog Posts
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=db.func.current_timestamp())

# Database model for Community Resources
class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(200), nullable=False)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the blog page
@app.route('/blog')
def blog():
    posts = BlogPost.query.order_by(BlogPost.date_posted.desc()).all()
    return render_template('blog.html', posts=posts)

# Route for creating a new blog post
@app.route('/blog/new', methods=['GET', 'POST'])
def new_blog_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Title and content are required!', 'error')
            return redirect(url_for('new_blog_post'))
        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash('Blog post created successfully!', 'success')
        return redirect(url_for('blog'))
    return render_template('new_blog_post.html')

# Route for the resources page
@app.route('/resources')
def resources():
    resources = Resource.query.all()
    return render_template('resources.html', resources=resources)

# Route for adding a new resource
@app.route('/resources/new', methods=['GET', 'POST'])
def new_resource():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        link = request.form['link']
        if not name or not description or not link:
            flash('All fields are required!', 'error')
            return redirect(url_for('new_resource'))
        new_resource = Resource(name=name, description=description, link=link)
        db.session.add(new_resource)
        db.session.commit()
        flash('Resource added successfully!', 'success')
        return redirect(url_for('resources'))
    return render_template('new_resource.html')

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point
if __name__ == '__main__':
    # Ensure the database exists
    if not os.path.exists('sustainable_living.db'):
        with app.app_context():
            db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/home.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sustainable Living</title>
</head>
<body>
    <h1>Welcome to Sustainable Living</h1>
    <nav>
        <a href="{{ url_for('blog') }}">Blog</a> |
        <a href="{{ url_for('resources') }}">Resources</a>
    </nav>
</body>
</html>
```

```html
<!-- templates/blog.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog - Sustainable Living</title>
</head>
<body>
    <h1>Blog</h1>
    <a href="{{ url_for('new_blog_post') }}">Create New Post</a>
    <ul>
        {% for post in posts %}
        <li>
            <h2>{{ post.title }}</h2>
            <p>{{ post.content }}</p>
            <small>Posted on {{ post.date_posted }}</small>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/new_blog_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Blog Post</title>
</head>
<body>
    <h1>Create a New Blog Post</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title" required>
        <br>
        <label for="content">Content:</label>
        <textarea id="content" name="content" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('blog') }}">Back to Blog</a>
</body>
</html>
```

```html
<!-- templates/resources.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resources - Sustainable Living</title>
</head>
<body>
    <h1>Community Resources</h1>
    <a href="{{ url_for('new_resource') }}">Add New Resource</a>
    <ul>
        {% for resource in resources %}
        <li>
            <h2>{{ resource.name }}</h2>
            <p>{{ resource.description }}</p>
            <a href="{{ resource.link }}" target="_blank">Learn More</a>
        </li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

```html
<!-- templates/new_resource.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Resource</title>
</head>
<body>
    <h1>Add a New Resource</h1>
    <form method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" required></textarea>
        <br>
        <label for="link">Link:</label>
        <input type="url" id="link" name="link" required>
        <br>
        <button type="submit">Submit</button>
    </form>
    <a href="{{ url_for('resources') }}">Back to Resources</a>
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
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```
