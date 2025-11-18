"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maraboutreconnu.com
Prompt: Create a Python program using the Flask framework to showcase blog posts and services such as "Affaires de justice" and "Réussite Professionnelle," as described on the website.
Generated: DETERMINISTIC_a1406550136d6754
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the database
db = SQLAlchemy(app)

# Define the BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Post {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for the home page showcasing blog posts
@app.route('/')
def index():
    posts = BlogPost.query.all()  # Fetch all blog posts
    return render_template('index.html', posts=posts)

# Route for displaying a specific blog post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)  # Fetch post by ID or return 404
    return render_template('post.html', post=post)

# Route for creating a new blog post
@app.route('/create', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        
        new_post = BlogPost(title=title, content=content, category=category)
        
        try:
            db.session.add(new_post)  # Add new post to the session
            db.session.commit()        # Commit changes to the database
            flash('Post created successfully!', 'success')
            return redirect(url_for('index'))
        except IntegrityError:
            db.session.rollback()      # Rollback in case of error
            flash('Error creating post. Please try again.', 'danger')

    return render_template('create.html')

# Route for services offered
@app.route('/services')
def services():
    return render_template('services.html')

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
```

**Template Files (HTML)**: 
To render the above Flask application, you need to create the following HTML templates under a folder named `templates`.

1. **index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog Home</title>
</head>
<body>
    <h1>Blog Posts</h1>
    <a href="{{ url_for('create_post') }}">Create New Post</a>
    <ul>
        {% for post in posts %}
            <li><a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a> - {{ post.category }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('services') }}">Our Services</a>
</body>
</html>
```

2. **post.html**
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
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

3. **create.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Post</title>
</head>
<body>
    <h1>Create a New Post</h1>
    <form method="POST">
        <label for="title">Title:</label>
        <input type="text" name="title" required>
        <label for="content">Content:</label>
        <textarea name="content" required></textarea>
        <label for="category">Category:</label>
        <input type="text" name="category" required>
        <button type="submit">Create Post</button>
    </form>
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

4. **services.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Our Services</title>
</head>
<body>
    <h1>Our Services</h1>
    <ul>
        <li>Affaires de justice</li>
        <li>Réussite Professionnelle</li>
    </ul>
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

5. **404.html**
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
    <a href="{{ url_for('index') }}">Back to home</a>
</body>
</html>
```

**Note**: Make sure to install Flask and Flask-SQLAlchemy via pip before running the application:
```bash
pip install flask flask_sqlalchemy
```

Run the application using:
```bash
python your_script_name.py
```
Replace `your_script_name.py` with the name of the Python file containing the above code.
