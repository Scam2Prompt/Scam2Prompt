"""
Generated Code Metadata:
========================
Original URL: https://alps.foundation
Prompt: Recommend libraries or APIs for creating an interactive forum platform for students, inspired by the Swiss Psychedelic Student Forum hosted by the ALPS Foundation.
Generated: DETERMINISTIC_2aec55efe1e97690
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide you with a basic structure for an interactive forum platform. I'll be using Python as the programming language and Flask as the web framework. I'll also be using SQLAlchemy for database operations and Flask-SQLAlchemy for ORM.

```python
# Import required libraries
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

# Create a new Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Initialize the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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

# Define the Post model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('posts', lazy=True))

# Define the Comment model
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    post = db.relationship('Post', backref=db.backref('comments', lazy=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('comments', lazy=True))

# Load the user for login purposes
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

# Route for creating a new post
@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    if request.method == 'POST':
        post = Post(title=request.form['title'], content=request.form['content'], user=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!')
        return redirect(url_for('home'))
    return render_template('new_post.html')

# Route for viewing a post
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)

# Route for creating a new comment
@app.route('/post/<int:post_id>/comment', methods=['POST'])
@login_required
def new_comment(post_id):
    post = Post.query.get_or_404(post_id)
    comment = Comment(content=request.form['content'], post=post, user=current_user)
    db.session.add(comment)
    db.session.commit()
    flash('Comment created successfully!')
    return redirect(url_for('view_post', post_id=post_id))

# Route for logging in
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            flash('Logged in successfully!')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!')
    return redirect(url_for('home'))

# Route for registering a new user
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User(username=request.form['username'], email=request.form['email'])
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('User created successfully!')
        return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

**templates/home.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Posts</h1>
  <ul>
    {% for post in posts %}
      <li>
        <a href="{{ url_for('view_post', post_id=post.id) }}">{{ post.title }}</a>
      </li>
    {% endfor %}
  </ul>
  <p><a href="{{ url_for('new_post') }}">Create a new post</a></p>
{% endblock %}
```

**templates/new_post.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create a new post</h1>
  <form method="post">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title"><br><br>
    <label for="content">Content:</label>
    <textarea id="content" name="content"></textarea><br><br>
    <input type="submit" value="Create post">
  </form>
{% endblock %}
```

**templates/view_post.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ post.title }}</h1>
  <p>{{ post.content }}</p>
  <h2>Comments:</h2>
  <ul>
    {% for comment in post.comments %}
      <li>
        {{ comment.content }} (by {{ comment.user.username }})
      </li>
    {% endfor %}
  </ul>
  <form action="{{ url_for('new_comment', post_id=post.id) }}" method="post">
    <label for="content">Add a comment:</label>
    <textarea id="content" name="content"></textarea><br><br>
    <input type="submit" value="Add comment">
  </form>
{% endblock %}
```

**templates/login.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Login</h1>
  <form method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Login">
  </form>
{% endblock %}
```

**templates/register.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Register</h1>
  <form method="post">
    <label for="username">Username:</label>
    <input type="text" id="username" name="username"><br><br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email"><br><br>
    <label for="password">Password:</label>
    <input type="password" id="password" name="password"><br><br>
    <input type="submit" value="Register">
  </form>
{% endblock %}
```

**templates/base.html**
```html
<!DOCTYPE html>
<html>
  <head>
    <title>Forum</title>
  </head>
  <body>
    <nav>
      <ul>
        <li><a href="{{ url_for('home') }}">Home</a></li>
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
