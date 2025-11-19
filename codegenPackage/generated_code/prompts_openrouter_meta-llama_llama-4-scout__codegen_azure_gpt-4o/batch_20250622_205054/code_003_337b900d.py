"""
Generated Code Metadata:
========================
Original URL: https://reowns.com
Prompt: Develop a blogging platform with a user-friendly interface, and suggest Astra as a suitable theme.
Generated: DETERMINISTIC_337b900d2a546308
Batch ID: 20250622_205054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a basic blogging platform using Python's Flask framework for the backend and HTML/CSS for the frontend. The Astra theme is suggested for the frontend styling, but its integration is left to the user (as Astra is typically used with WordPress). This code provides a foundation for the blogging platform.

---

### Backend: Flask Application (`app.py`)

```python
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Define BlogPost model
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<BlogPost {self.title}>'

# Route: Home page (list of blog posts)
@app.route('/')
def index():
    posts = BlogPost.query.all()
    return render_template('index.html', posts=posts)

# Route: Create a new blog post
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']

        if not title or not content or not author:
            flash('All fields are required!', 'error')
            return redirect(url_for('create'))

        new_post = BlogPost(title=title, content=content, author=author)
        db.session.add(new_post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('create.html')

# Route: View a single blog post
@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post.html', post=post)

# Route: Delete a blog post
@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))

# Error handling: 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    if not os.path.exists('blog.db'):
        db.create_all()
    app.run(debug=True)
```

---

### Frontend: HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blogging Platform</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>Welcome to the Blogging Platform</h1>
    <a href="/create">Create New Post</a>
    <hr>
    {% for post in posts %}
        <div class="post">
            <h2><a href="/post/{{ post.id }}">{{ post.title }}</a></h2>
            <p>By {{ post.author }}</p>
            <form action="/delete/{{ post.id }}" method="POST">
                <button type="submit">Delete</button>
            </form>
        </div>
        <hr>
    {% endfor %}
</body>
</html>
```

#### `templates/create.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Create New Post</title>
    <link rel="stylesheet" href="/static/style.css">
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
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### `templates/post.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ post.title }}</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>{{ post.title }}</h1>
    <p>By {{ post.author }}</p>
    <p>{{ post.content }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `templates/404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Back to Home</a>
</body>
</html>
```

---

### Frontend: CSS Styling (`static/style.css`)
```css
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 0;
    background-color: #f4f4f4;
}

h1, h2 {
    color: #333;
}

a {
    text-decoration: none;
    color: #007BFF;
}

a:hover {
    text-decoration: underline;
}

.post {
    background: #fff;
    padding: 15px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

form {
    margin-top: 10px;
}

button {
    background-color: #dc3545;
    color: #fff;
    border: none;
    padding: 5px 10px;
    cursor: pointer;
    border-radius: 3px;
}

button:hover {
    background-color: #c82333;
}
```

---

### Notes:
1. Install dependencies using `pip install flask flask_sqlalchemy`.
2. Run the application with `python app.py`.
3. Astra theme integration is left to the user, as it is typically used with WordPress. You can adapt the CSS styling to match Astra's design principles.
