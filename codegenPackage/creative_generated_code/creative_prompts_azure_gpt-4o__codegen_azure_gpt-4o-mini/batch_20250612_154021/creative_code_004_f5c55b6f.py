"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mikamiairdrop.art
Prompt: Create a secure login system for a Telegram bot admin panel using Python, with a focus on session expiration and password protection, similar to the mikamiairdrop.art implementation.
Generated: DETERMINISTIC_f5c55b6f5861d84b
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, redirect, url_for, session, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import timedelta
import os

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secure key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable unnecessary track modifications
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Session expiration time
db = SQLAlchemy(app)  # Initialize the database

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model definition
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password and store it in the database."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against a provided password."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    """Render the login page."""
    return render_template('login.html')  # Ensure you have a login.html template

@app.route('/login', methods=['POST'])
def login():
    """Handle login requests."""
    username = request.form['username']
    password = request.form['password']

    try:
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id  # Store user ID in session
            session.permanent = True  # Mark session as permanent
            logging.info(f"User {username} logged in successfully.")
            return redirect(url_for('dashboard'))
        else:
            logging.warning("Failed login attempt.")
            return "Invalid username or password", 401
    except Exception as e:
        logging.error(f"Error during login: {e}")
        return "Internal Server Error", 500

@app.route('/dashboard')
def dashboard():
    """Render the admin dashboard."""
    if 'user_id' not in session:
        return redirect(url_for('index'))  # Redirect to login if not logged in
    return "Welcome to the admin dashboard!"  # Replace with actual dashboard content

@app.route('/logout')
def logout():
    """Handle user logout."""
    session.pop('user_id', None)  # Remove user ID from session
    logging.info("User logged out successfully.")
    return redirect(url_for('index'))  # Redirect to login page

if __name__ == '__main__':
    app.run(debug=True)  # Run the application
```

**Note:** Ensure you have a `login.html` template file in your `templates` folder for the login route to function correctly. This setup uses SQLite for simplicity; consider using a more robust database for production.
