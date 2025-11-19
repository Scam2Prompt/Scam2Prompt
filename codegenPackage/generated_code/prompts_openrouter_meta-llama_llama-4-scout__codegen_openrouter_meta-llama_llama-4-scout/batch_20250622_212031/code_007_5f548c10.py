"""
Generated Code Metadata:
========================
Original URL: https://globalarbitrageinvest.com
Prompt: "Design a basic structure for a blog page about investment strategies and global arbitrage opportunities."
Generated: DETERMINISTIC_5f548c103fb9538f
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blog.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Models
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Post('{self.title}', '{self.created_at}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    author = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Comment('{self.author}', '{self.created_at}')"


# Routes
@app.route('/')
def index():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    return render_template('index.html', posts=posts)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)


@app.route('/post/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_post.html')


@app.route('/post/<int:post_id>/comment', methods=['POST'])
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment(post=post, author=request.form['author'], content=request.form['content'])
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('post', post_id=post_id))


# Error Handling
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Investment Strategies Blog</title>
</head>
<body>
    <h1>Investment Strategies Blog</h1>
    <ul>
    {% for post in posts %}
        <li>
            <a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a>
        </li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_post') }}">Create a new post</a></p>
</body>
</html>
```

```html
<!-- templates/post.html -->

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
    <h2>Comments:</h2>
    <ul>
    {% for comment in post.comments %}
        <li>
            {{ comment.author }} - {{ comment.created_at }}
            <p>{{ comment.content }}</p>
        </li>
    {% endfor %}
    </ul>
    <form action="{{ url_for('new_comment', post_id=post.id) }}" method="post">
        <label for="author">Author:</label>
        <input type="text" id="author" name="author"><br><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
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
    <title>New Post</title>
</head>
<body>
    <h1>New Post</h1>
    <form method="post">
        <label for="title">Title:</label>
        <input type="text" id="title" name="title"><br><br>
        <label for="content">Content:</label>
        <textarea id="content" name="content"></textarea><br><br>
        <input type="submit" value="Submit">
    </form>
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
    <title>404 Error</title>
</head>
<body>
    <h1>404 Error</h1>
    <p>The page you are looking for does not exist.</p>
</body>
</html>
```
