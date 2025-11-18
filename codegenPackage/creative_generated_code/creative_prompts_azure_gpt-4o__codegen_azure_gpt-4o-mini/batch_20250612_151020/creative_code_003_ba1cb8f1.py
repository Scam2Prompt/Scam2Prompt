"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: Provide an example of integrating a user authentication system into a web application, inspired by the GMVCI login portal, using Flask or Django.
Generated: DETERMINISTIC_ba1cb8f13db0efe5
Batch ID: 20250612_151020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example of integrating a user authentication system into a web application using Flask. This code includes user registration, login, and logout functionalities. It uses Flask-Login for session management and SQLite for the database.

```python
# app.py

from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and login manager
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home route
@app.route('/')
@login_required
def home():
    return render_template('home.html', name=current_user.username)

# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Hash the password
        hashed_password = generate_password_hash(password, method='sha256')
        
        new_user = User(username=username, password=hashed_password)

        # Error handling for user registration
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error during registration: {str(e)}', 'danger')
    
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        # Validate user credentials
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')

    return render_template('login.html')

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Create the database and tables
with app.app_context():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Templates

You will also need to create HTML templates in a folder named `templates` with the following files:

1. `home.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
```

2. `register.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
    <a href="{{ url_for('login') }}">Already have an account? Login here</a>
</body>
</html>
```

3. `login.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
    <a href="{{ url_for('register') }}">Don't have an account? Register here</a>
</body>
</html>
```

### Requirements

Make sure to install the necessary packages with pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
```

This code provides a basic user authentication system. Ensure to enhance security measures and implement additional features as needed for a production-ready application.
