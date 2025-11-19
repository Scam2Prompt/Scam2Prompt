"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Design a secure and user-friendly login system for a counseling service website, ensuring confidentiality and data protection for clients.
Generated: DETERMINISTIC_4a601f6c227f5c95
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SECRET_KEY'] = os.urandom(24)  # Generate a random secret key for session management
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Redirect to login page if not logged in

# User model for the database
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Load user callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Fetch user from the database
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and/or password.', 'danger')
    
    return render_template('login.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Create a new user and add to the database
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for the user dashboard (protected)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

### Note:
- Ensure you have the necessary HTML templates (`login.html`, `register.html`, `dashboard.html`, `404.html`, `500.html`) in a `templates` directory for this code to function correctly.
- Install the required packages using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Login Werkzeug
  ```
