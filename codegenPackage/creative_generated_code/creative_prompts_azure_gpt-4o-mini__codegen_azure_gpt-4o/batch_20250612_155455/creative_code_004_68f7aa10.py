"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Illustrate how to implement a client portal using a web framework that allows secure communication and collaboration, inspired by the services provided by Carthew Chau & Co.
Generated: DETERMINISTIC_68f7aa106299dc97
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Filename: client_portal.py

# Import necessary libraries and modules
from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration settings
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')  # Use environment variable for production
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///client_portal.db')  # Use environment variable for production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy for database handling
db = SQLAlchemy(app)

# Setup Flask-Login for user authentication
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect to login page if not authenticated

# Database model for User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Method to set password securely
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Method to verify password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Database model for Messages (secure communication)
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipient_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Flask-Login user loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for homepage
@app.route('/')
def home():
    return render_template('home.html')

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists.')
            return redirect(url_for('register'))

        # Create new user
        new_user = User(username=username)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for user login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('portal'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        # Verify user credentials
        if user and user.check_password(password):
            login_user(user)
            flash('Login successful.')
            return redirect(url_for('portal'))
        else:
            flash('Invalid username or password.')
    
    return render_template('login.html')

# Route for user logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

# Route for client portal dashboard
@app.route('/portal')
@login_required
def portal():
    users = User.query.filter(User.id != current_user.id).all()  # List of other users
    return render_template('portal.html', users=users)

# Route to send messages
@app.route('/message', methods=['POST'])
@login_required
def message():
    recipient_id = request.form['recipient_id']
    content = request.form['content']
    
    # Validate recipient and content
    recipient = User.query.get(recipient_id)
    if not recipient:
        flash('Recipient not found.')
        return redirect(url_for('portal'))
    
    if not content.strip():
        flash('Message cannot be empty.')
        return redirect(url_for('portal'))
    
    # Save message to database
    new_message = Message(sender_id=current_user.id, recipient_id=recipient_id, content=content)
    db.session.add(new_message)
    db.session.commit()
    flash('Message sent successfully.')
    return redirect(url_for('portal'))

# Route to view messages
@app.route('/messages')
@login_required
def view_messages():
    messages = Message.query.filter_by(recipient_id=current_user.id).all()
    return render_template('messages.html', messages=messages)

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

# Entry point of the application
if __name__ == '__main__':
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    # Run application
    app.run(debug=True)  # Disable debug mode in production
```

### Notes on Files to Create:
- `home.html`, `register.html`, `login.html`, `portal.html`, `messages.html`, `404.html`, and `500.html` are templates that need to be created in the `templates` directory to render the respective pages.

### Dependency Installation:
Ensure you have Flask, Flask-SQLAlchemy, and Flask-Login installed:
```bash
pip install flask flask-sqlalchemy flask-login werkzeug
```
