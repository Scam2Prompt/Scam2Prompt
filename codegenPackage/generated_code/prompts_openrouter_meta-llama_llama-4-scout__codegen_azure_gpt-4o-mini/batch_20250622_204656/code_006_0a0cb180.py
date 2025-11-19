"""
Generated Code Metadata:
========================
Original URL: https://labvidadourados.com.br
Prompt: Create a code example to implement a secure and user-friendly login system for patients to access their laboratory test results online, similar to LabVida's service.
Generated: DETERMINISTIC_0a0cb1807411d50e
Batch ID: 20250622_204656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os
import re

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the database and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///patients.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model for the database
class User(UserMixin, db.Model):
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
        
        # Validate user input
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400
        
        user = User.query.filter_by(username=username).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            return jsonify({"error": "Invalid username or password."}), 401

    return render_template('login.html')

# Route for the dashboard (protected)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.username)

# Route for logging out
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Route for user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate user input
        if not username or not password:
            return jsonify({"error": "Username and password are required."}), 400
        
        # Check for valid username format
        if not re.match("^[a-zA-Z0-9_]+$", username):
            return jsonify({"error": "Username must be alphanumeric."}), 400
        
        # Hash the password and create a new user
        hashed_password = generate_password_hash(password, method='sha256')
        new_user = User(username=username, password=hashed_password)
        
        # Add user to the database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"message": "User registered successfully."}), 201

    return render_template('register.html')

# Error handling for 404
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(e):
    return jsonify({"error": "Internal server error."}), 500

# Main entry point to create the database
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=False)  # Set debug to False for production
```

### Note:
- Ensure you have the required packages installed: `Flask`, `Flask-SQLAlchemy`, `Flask-Login`, and `Werkzeug`.
- Create the corresponding HTML templates (`login.html`, `dashboard.html`, `register.html`) for the application to function correctly.
- This code is designed for educational purposes and should be reviewed and tested before deploying in a production environment.
