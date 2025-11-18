"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Suggest libraries or frameworks for developing a blog feature for an educational institution, referencing the "Blog" section mentioned on the IEBCA website.
Generated: DETERMINISTIC_149b777eda4d497f
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# blog_feature.py
"""
This script provides a basic implementation of a blog feature for an educational institution. 
It includes example usage of libraries and frameworks suitable for developing a blog system. 
"""

# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blogs.db'  # Database configuration
app.config['SECRET_KEY'] = 'your_secret_key'  # Secret key for session management
db = SQLAlchemy(app)  # Initialize SQLAlchemy

# Set up logging for error handling
logging.basicConfig(level=logging.INFO)

# Define the Blog model
class Blog(db.Model):
    """Model to represent a blog post."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Blog {self.title}>'

# Home route to display blog posts
@app.route('/')
def index():
    """Render the index page with all blog posts."""
    try:
        posts = Blog.query.all()  # Fetch all blog posts
        return render_template('index.html', posts=posts)  # Render template with posts
    except Exception as e:
        logging.error(f"Error fetching blog posts: {e}")
        flash('Error fetching blog posts. Please try again later.', 'error')
        return render_template('index.html', posts=[])

# Route to create a new blog post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    """Handle the creation of a new blog post."""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        try:
            # Create a new blog post and add it to the database
            new_blog = Blog(title=title, content=content)
            db.session.add(new_blog)
            db.session.commit()
            flash('Blog post created successfully!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            logging.error(f"Error creating blog post: {e}")
            flash('Error creating blog post. Please try again.', 'error')
    return render_template('new_post.html')  # Render the new post form

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors by rendering a custom error page."""
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Create the database if it doesn't exist
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)  # Run the application in debug mode
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Posts</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <a href="{{ url_for('new_post') }}">Create New Post</a>
    {% with messages = get_flashed_messages() %}
      {% if messages %}
        <ul>
        {% for message in messages %}
          <li>{{ message }}</li>
        {% endfor %}
        </ul>
      {% endif %}
    {% endwith %}
    <ul>
        {% for post in posts %}
            <li>
                <h2>{{ post.title }}</h2>
                <p>{{ post.content }}</p>
                <small>{{ post.date_posted.strftime('%Y-%m-%d') }}</small>
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- templates/new_post.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Post</title>
</head>
<body>
    <h1>Create a New Blog Post</h1>
    <form method="POST">
        <label for="title">Title:</label><br>
        <input type="text" id="title" name="title" required><br>
        <label for="content">Content:</label><br>
        <textarea id="content" name="content" required></textarea><br>
        <input type="submit" value="Submit">
    </form>
    <a href="{{ url_for('index') }}">Back to Blog Posts</a>
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
    <p>The page you are looking for does not exist.</p>
    <a href="{{ url_for('index') }}">Back to Blog Posts</a>
</body>
</html>
```
