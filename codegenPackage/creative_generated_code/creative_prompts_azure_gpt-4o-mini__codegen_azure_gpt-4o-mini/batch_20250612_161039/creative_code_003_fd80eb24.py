"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcoins.net
Prompt: Create a simple web application that allows users to register and log in to Claimcoins, utilizing their payment proof system.
Generated: DETERMINISTIC_fd80eb24586df315
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py
from flask import Flask, request, jsonify, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Set configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SECRET_KEY'] = os.urandom(24)  # Random secret key for session management
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

# Initialize the database (Create tables)
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists."}), 400

    # Hash the password and create a new user
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User registered successfully."}), 201

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Retrieve the user by username
    user = User.query.filter_by(username=username).first()

    # Validate user credentials
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"message": "Invalid credentials."}), 401

# Endpoint to check session status
@app.route('/status', methods=['GET'])
def status():
    if 'user_id' in session:
        return jsonify({"message": "User is logged in.", "user_id": session['user_id']}), 200
    return jsonify({"message": "No user is logged in."}), 401

# Endpoint for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful."}), 200

# Main entry point to run the application
if __name__ == '__main__':
    app.run(debug=True)
```

```bash
# requirements.txt
Flask==2.2.2
Flask-SQLAlchemy==2.5.1
Werkzeug==2.2.2
```

### Instructions to Run the Application

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the application:
   ```bash
   python app.py
   ```

3. Use a tool like Postman or curl to interact with the endpoints:
   - POST to `/register` with JSON body `{"username": "your_username", "password": "your_password"}`
   - POST to `/login` with JSON body `{"username": "your_username", "password": "your_password"}`
   - GET to `/status` to check login status
   - POST to `/logout` to log out.
