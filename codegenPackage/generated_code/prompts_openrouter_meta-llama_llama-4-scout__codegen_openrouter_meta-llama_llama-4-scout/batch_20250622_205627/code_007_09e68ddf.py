"""
Generated Code Metadata:
========================
Original URL: https://luwukpost.id
Prompt: "Propose a content management system (CMS) for a regional news website, incorporating features that could enhance user engagement and news dissemination, similar to luwukpost.id."
Generated: DETERMINISTIC_09e68ddfd6c373b3
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Create a Flask application instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///regional_news.db'
db = SQLAlchemy(app)

# Define the User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Define the NewsArticle model
class NewsArticle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    author = db.relationship('User', backref=db.backref('articles', lazy=True))

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('news_article.id'), nullable=False)
    article = db.relationship('NewsArticle', backref=db.backref('comments', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

# Initialize the LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Define routes
@app.route('/')
def index():
    articles = NewsArticle.query.all()
    return render_template('index.html', articles=articles)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/article/<int:article_id>')
def article(article_id):
    article = NewsArticle.query.get(article_id)
    if article is None:
        return 'Article not found', 404
    return render_template('article.html', article=article)

@app.route('/article/new', methods=['GET', 'POST'])
@login_required
def new_article():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        article = NewsArticle(title=title, content=content, author=current_user)
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_article.html')

@app.route('/comment/new', methods=['POST'])
@login_required
def new_comment():
    article_id = request.form['article_id']
    content = request.form['content']
    article = NewsArticle.query.get(article_id)
    if article is None:
        return 'Article not found', 404
    comment = Comment(content=content, article=article, user=current_user)
    db.session.add(comment)
    db.session.commit()
    return redirect(url_for('article', article_id=article_id))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Regional News</title>
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Home</a></li>
            <li><a href="{{ url_for('login') }}">Login</a></li>
            <li><a href="{{ url_for('register') }}">Register</a></li>
        </ul>
    </nav>
    <div class="content">
        {% block content %}{% endblock %}
    </div>
</body>
</html>
```

```html
<!-- templates/index.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Regional News</h1>
    <ul>
    {% for article in articles %}
        <li><a href="{{ url_for('article', article_id=article.id) }}">{{ article.title }}</a></li>
    {% endfor %}
    </ul>
    <p><a href="{{ url_for('new_article') }}">New Article</a></p>
{% endblock %}
```

```html
<!-- templates/login.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Login</h1>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
{% endblock %}
```

```html
<!-- templates/register.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>Register</h1>
    <form method="post">
        <label>Username:</label>
        <input type="text" name="username"><br><br>
        <label>Email:</label>
        <input type="email" name="email"><br><br>
        <label>Password:</label>
        <input type="password" name="password"><br><br>
        <input type="submit" value="Register">
    </form>
{% endblock %}
```

```html
<!-- templates/article.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>{{ article.title }}</h1>
    <p>{{ article.content }}</p>
    <h2>Comments:</h2>
    <ul>
    {% for comment in article.comments %}
        <li>{{ comment.content }} ({{ comment.user.username }})</li>
    {% endfor %}
    </ul>
    <form method="post">
        <input type="hidden" name="article_id" value="{{ article.id }}">
        <label>Comment:</label>
        <textarea name="content"></textarea><br><br>
        <input type="submit" value="Post Comment">
    </form>
{% endblock %}
```

```html
<!-- templates/new_article.html -->
{% extends 'base.html' %}

{% block content %}
    <h1>New Article</h1>
    <form method="post">
        <label>Title:</label>
        <input type="text" name="title"><br><br>
        <label>Content:</label>
        <textarea name="content"></textarea><br><br>
        <input type="submit" value="Post Article">
    </form>
{% endblock %}
```
