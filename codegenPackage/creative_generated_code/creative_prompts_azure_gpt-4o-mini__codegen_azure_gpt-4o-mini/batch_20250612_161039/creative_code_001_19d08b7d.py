"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.solcialapp.com
Prompt: What are the best practices for creating a password-protected area in a web app like Solcial?
Generated: DETERMINISTIC_19d08b7d757c7272
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

# Initialize Flask app, Bcrypt, and SQLAlchemy
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Decorator for protecting routes
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash('You need to log in first.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route for home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('Login successful!')
            return redirect(url_for('protected'))
        else:
            flash('Login failed. Check your username and password.')
    return render_template('login.html')

# Route for registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! You can now log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Protected route
@app.route('/protected')
@login_required
def protected():
    return render_template('protected.html')

# Route for logout
@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

# Error handling for database issues
@app.errorhandler(500)
def internal_error(error):
    return "An internal error occurred. Please try again later.", 500

# Create the database and tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```

### Note:
1. Ensure to replace `'your_secret_key'` with a secure random key before deploying to production.
2. This code uses Flask, Flask-Bcrypt for password hashing, and Flask-SQLAlchemy for ORM with SQLite as the database. Install the required packages using `pip install Flask Flask-Bcrypt Flask-SQLAlchemy`.
3. The templates (`home.html`, `login.html`, `register.html`, `protected.html`) need to be created in a `templates` directory as per Flask's conventions.
