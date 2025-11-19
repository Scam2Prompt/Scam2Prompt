"""
Generated Code Metadata:
========================
Original URL: https://medicidsas.com
Prompt: Create a web application for downloading medical concepts related to occupational health, similar to the platform described on Medicid IPS's website, with user authentication and secure data access.
Generated: DETERMINISTIC_e619e5de604ae488
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the application
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Initialize extensions
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# User model for database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')  # Render the home page

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        # Create a new user
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))  # Redirect to login after registration
    return render_template('register.html')  # Render registration page

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()  # Fetch user by username
        if user and bcrypt.check_password_hash(user.password, password):  # Verify password
            login_user(user)  # Log in the user
            return redirect(url_for('dashboard'))  # Redirect to dashboard
        else:
            return 'Login Failed. Check your username and password.'  # Error message
    return render_template('login.html')  # Render login page

# Route for user dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)  # Render dashboard

# Route for downloading medical concepts
@app.route('/download', methods=['GET'])
@login_required
def download():
    # Placeholder for downloading medical concepts
    # In a real application, this would fetch data from a database or an API
    medical_concepts = {
        "concepts": [
            {"id": 1, "name": "Occupational Asthma"},
            {"id": 2, "name": "Carpal Tunnel Syndrome"},
            {"id": 3, "name": "Noise-Induced Hearing Loss"}
        ]
    }
    return jsonify(medical_concepts)  # Return medical concepts as JSON

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()  # Log out the user
    return redirect(url_for('home'))  # Redirect to home page

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404  # Render 404 error page

# Main entry point for the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Occupational Health Platform</h1>
    <a href="/register">Register</a>
    <a href="/login">Login</a>
</body>
</html>
```

**register.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register</title>
</head>
<body>
    <h1>Register</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>
</body>
</html>
```

**login.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
</head>
<body>
    <h1>Login</h1>
    <form method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

**dashboard.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard</title>
</head>
<body>
    <h1>Welcome, {{ username }}</h1>
    <a href="/download">Download Medical Concepts</a>
    <a href="/logout">Logout</a>
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
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="/">Go to Home</a>
</body>
</html>
```

### Note
Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Bcrypt Flask-Login
```

This code provides a basic structure for a web application with user authentication and secure data access for downloading medical concepts related to occupational health.
