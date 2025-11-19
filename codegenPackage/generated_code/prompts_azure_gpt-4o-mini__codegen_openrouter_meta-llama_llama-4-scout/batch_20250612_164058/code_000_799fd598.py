"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: Generate a code snippet for a custom web application that includes features for SEO optimization and user management as described by شرکت متا.
Generated: DETERMINISTIC_799fd5986e20b8c8
Batch ID: 20250612_164058
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm ready when you are. However, I need to clarify that I'll be using Python with the Flask web framework for this task, along with SQLAlchemy for database operations and Flask-SQLAlchemy for ORM. Additionally, I'll be using Flask-SEO to handle SEO optimization and Flask-Login for user management.

Please find the code below:

```python
# app.py

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_seo import Seo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

seo = Seo(app)

class User(UserMixin, db.Model):
    """User model."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        """Set user password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check user password."""
        return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(user_id):
    """Load user."""
    return User.query.get(int(user_id))

@app.route('/')
@seo.register(title='Home', description='Home page', keywords=['home', 'index'])
def home():
    """Home page."""
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
@seo.register(title='Login', description='Login page', keywords=['login', 'signin'])
def login():
    """Login page."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
@seo.register(title='Register', description='Register page', keywords=['register', 'signup'])
def register():
    """Register page."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if not user:
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/dashboard')
@login_required
@seo.register(title='Dashboard', description='Dashboard page', keywords=['dashboard', 'account'])
def dashboard():
    """Dashboard page."""
    return render_template('dashboard.html')

@app.route('/logout')
@login_required
def logout():
    """Logout."""
    logout_user()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```python
# models.py

from app import db

# Add your models here if you need more than User model.

```

```python
# templates/home.html

<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
    <meta name="description" content="Home page">
    <meta name="keywords" content="home, index">
</head>
<body>
    <h1>Welcome to our website!</h1>
</body>
</html>

```

```python
# templates/login.html

<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <meta name="description" content="Login page">
    <meta name="keywords" content="login, signin">
</head>
<body>
    <h1>Login</h1>
    <form method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>

```

```python
# templates/register.html

<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
    <meta name="description" content="Register page">
    <meta name="keywords" content="register, signup">
</head>
<body>
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
</body>
</html>

```

```python
# templates/dashboard.html

<!DOCTYPE html>
<html>
<head>
    <title>Dashboard</title>
    <meta name="description" content="Dashboard page">
    <meta name="keywords" content="dashboard, account">
</head>
<body>
    <h1>Welcome, {{ current_user.username }}!</h1>
</body>
</html>

```
