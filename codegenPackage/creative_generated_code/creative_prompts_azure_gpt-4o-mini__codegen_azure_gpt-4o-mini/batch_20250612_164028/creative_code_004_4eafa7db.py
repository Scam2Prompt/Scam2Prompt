"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Illustrate how to implement a login system for a web application that manages edible printing orders, referencing the user authentication features on Comestim.
Generated: DETERMINISTIC_4eafa7dbf77d8382
Batch ID: 20250612_164028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os

# Initialize Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = os.urandom(24)  # Secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Error handler decorator for user authentication
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# Route to render the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        # Check user existence and password correctness
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return jsonify({'error': 'Invalid username or password'}), 401

    return render_template('login.html')

# Route to handle user registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Hash the password for security
        hashed_password = generate_password_hash(password, method='sha256')
        
        # Check if the username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'User already exists!'}), 409
            
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully!'}), 201

    return render_template('register.html')

# Route to display the user dashboard
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Route to handle user logout
@app.route('/logout')
@login_required
def logout():
    session.pop('user_id', None)  # Clear the session
    return redirect(url_for('login'))

# Function to initialize the database
def init_db():
    db.create_all()

if __name__ == '__main__':
    init_db()  # Create database tables
    app.run(debug=True)  # Start the application
```

### HTML Templates
For the code to work properly, you will need to create the following HTML templates in a `templates` directory:
- `login.html`: A form for user login.
- `register.html`: A form for user registration.
- `dashboard.html`: A simple dashboard to display after login.

### Notes
- Ensure Flask, Flask-SQLAlchemy, and Werkzeug are installed in your environment.
- The SQLite database is used for simplicity; for production, consider using a more robust database like PostgreSQL or MySQL.
- The `SECRET_KEY` should be set to a secure value in production.
