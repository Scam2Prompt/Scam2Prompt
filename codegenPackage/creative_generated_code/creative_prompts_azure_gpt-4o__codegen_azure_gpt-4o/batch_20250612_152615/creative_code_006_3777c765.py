"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Write code to securely integrate a client portal for legal and accounting services, inspired by Carthew Chau & Co's convenience-focused solutions.
Generated: DETERMINISTIC_3777c765f1ea62e2
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python-based implementation of a secure client portal for legal and accounting services, using Flask for the web framework:

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask application
app = Flask(__name__)

# Security settings
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')  # Use environment variables for production
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///client_portal.db')  # Database URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User model for client portal
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, password):
        """Hashes the password and stores the hash."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks if the provided password matches the hash."""
        return check_password_hash(self.password_hash, password)


# Home route
@app.route('/')
def home():
    return render_template('home.html')


# Registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check for matching passwords
        if password != confirm_password:
            flash('Passwords do not match!', 'error')
            return redirect(url_for('register'))

        # Check for username/email uniqueness
        if User.query.filter_by(username=username).first() or User.query.filter_by(email=email).first():
            flash('Username or email already exists!', 'error')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Verify user credentials
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials!', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')


# Dashboard route (protected)
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login to access the dashboard.', 'error')
        return redirect(url_for('login'))
    return render_template('dashboard.html', username=session['username'])


# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))


# Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


# Run the application
if __name__ == '__main__':
    # Create database tables (if not exists)
    with app.app_context():
        db.create_all()

    # Start the server
    app.run(debug=False)  # Set debug=False for production
```

### Notes:
- The code uses Flask for the web framework, SQLAlchemy for database interaction, and Werkzeug for password hashing.
- Replace `SECRET_KEY` and `DATABASE_URL` with appropriate environment variables for production.
- Templates (`home.html`, `register.html`, `login.html`, `dashboard.html`, `404.html`, and `500.html`) should be created in the `templates` directory following Flask's conventions.
- Use HTTPS for production to secure data transmission.
