"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yoway.com
Prompt: Develop a simple web application that allows users to register and log in to an online slot site like Gempa777, ensuring secure handling of user data.
Generated: DETERMINISTIC_970ee415e902c09f
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

# Initialize Flask application
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  # Secret key for session management

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Check if user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'User already exists!'}), 400

    # Create new user
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully!'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    # Fetch user from the database
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user id in session
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password!'}), 401

# Route for user logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user from session
    return redirect(url_for('home'))

# Error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found!'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'An internal error occurred!'}), 500

# Run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug to False in production
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Slot Site Registration/Login</title>
</head>
<body>
    <h1>Welcome to Gempa777</h1>
    
    <h2>Register</h2>
    <form action="/register" method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Register</button>
    </form>

    <h2>Login</h2>
    <form action="/login" method="POST">
        <input type="text" name="username" placeholder="Username" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    </form>
</body>
</html>
```

### Notes
- Ensure that you have Flask, Flask-SQLAlchemy, Flask-Migrate, and Werkzeug installed in your Python environment.
- Create a virtual environment and install the required packages using `pip install Flask Flask-SQLAlchemy Flask-Migrate`.
- This code uses SQLite for simplicity. In a production environment, consider using a more robust database system such as PostgreSQL or MySQL.
- Remember to set `debug=False` in the production environment for security reasons.
