"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://diverbox.com.pe
Prompt: What are best practices for managing user sessions and passwords in a web application, based on the user management features seen on diverbox.com.pe?
Generated: DETERMINISTIC_f7ede56a9170871c
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the app and database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Use a random secret key for session encryption
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the database
db = SQLAlchemy(app)

# Initialize session management
Session(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Set the user's password securely."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the user's password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Create the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    username = request.form['username']
    password = request.form['password']

    if User.query.filter_by(username=username).first() is not None:
        flash('Username already exists.')
        return redirect(url_for('register'))

    new_user = User(username=username)
    new_user.set_password(password)

    db.session.add(new_user)
    db.session.commit()
    
    flash('User registered successfully!')
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Log in a user."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user is None or not user.check_password(password):
            flash('Invalid username or password.')
            return redirect(url_for('login'))

        session['user_id'] = user.id
        flash('Logged in successfully!')
        return redirect(url_for('dashboard'))

    return 'Login Form Here'  # Replace with actual login form template

@app.route('/dashboard')
def dashboard():
    """Display the user dashboard."""
    if 'user_id' not in session:
        flash('You must be logged in to view this page.')
        return redirect(url_for('login'))

    return 'Welcome to your dashboard!'  # Replace with actual dashboard template

@app.route('/logout')
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('login'))

# Error handling for exceptions
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return '404 Error: Page Not Found', 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return '500 Error: Internal Server Error', 500

if __name__ == '__main__':
    app.run(debug=True)
```
