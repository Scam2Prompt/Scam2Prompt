"""
Generated Code Metadata:
========================
Original URL: https://jualessandraensina.com
Prompt: Generate a code snippet for a web application that allows users to access exclusive makeup tutorials and live sessions, similar to the membership features of Ju Ensina.
Generated: DETERMINISTIC_2e4f9054939c8412
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask-based web application for exclusive makeup tutorials and live sessions

from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Secret key for session management

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///membership.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    is_member = db.Column(db.Boolean, default=False)

class Tutorial(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class LiveSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    scheduled_at = db.Column(db.DateTime, nullable=False)

# Routes
@app.route('/')
def home():
    """Home page displaying public content."""
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        hashed_password = generate_password_hash(password, method='sha256')

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered.', 'error')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_member'] = user.is_member
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.', 'error')

    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout route."""
    session.clear()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    """Dashboard for members."""
    if 'user_id' not in session:
        flash('Please log in to access the dashboard.', 'error')
        return redirect(url_for('login'))

    tutorials = Tutorial.query.all()
    live_sessions = LiveSession.query.all()
    return render_template('dashboard.html', tutorials=tutorials, live_sessions=live_sessions)

@app.route('/membership')
def membership():
    """Membership upgrade route."""
    if 'user_id' not in session:
        flash('Please log in to upgrade membership.', 'error')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    user.is_member = True
    db.session.commit()
    session['is_member'] = True
    flash('Membership upgraded successfully!', 'success')
    return redirect(url_for('dashboard'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """Handle 500 errors."""
    return render_template('500.html'), 500

# Run the app
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
```

### Notes:
- This code assumes the existence of HTML templates (`home.html`, `register.html`, `login.html`, `dashboard.html`, `404.html`, `500.html`) in a `templates` directory.
- The database file (`membership.db`) will be created in the root directory of the project.
- Replace `debug=True` with `debug=False` in production.
