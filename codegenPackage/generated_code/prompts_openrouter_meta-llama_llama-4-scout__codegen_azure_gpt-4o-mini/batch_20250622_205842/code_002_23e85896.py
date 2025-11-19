"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Recommend APIs or libraries that can be used for building a personal portfolio website with a blogging feature, similar to EMFresh2o Digital Resume.
Generated: DETERMINISTIC_23e8589627d40fb3
Batch ID: 20250622_205842
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # For session management

# Initialize the database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Post {self.title}>'

# Route for the homepage
@app.route('/')
def home():
    posts = BlogPost.query.all()  # Fetch all blog posts
    return render_template('home.html', posts=posts)

# Route for creating a new blog post
@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        
        # Error handling for empty fields
        if not title or not content:
            flash('Title and content cannot be empty!', 'danger')
            return redirect(url_for('new_post'))

        new_post = BlogPost(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('home'))

    return render_template('new_post.html')

# Route for viewing a single blog post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)  # Fetch post or return 404
    return render_template('post.html', post=post)

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (for completeness)

**home.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Portfolio</title>
</head>
<body>
    <h1>My Blog</h1>
    <a href="{{ url_for('new_post') }}">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li><a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**new_post.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Post</title>
</head>
<body>
    <h1>Create New Post</h1>
    <form method="POST">
        <input type="text" name="title" placeholder="Post Title" required>
        <textarea name="content" placeholder="Post Content" required></textarea>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

**post.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>{{ post.content }}</p>
    <a href="{{ url_for('home') }}">Back to Home</a>
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
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Instructions
1. Ensure you have Flask and Flask-SQLAlchemy installed in your Python environment.
2. Create a folder structure for your templates and place the HTML files accordingly.
3. Run the application, and it will create a SQLite database for your blog posts.
