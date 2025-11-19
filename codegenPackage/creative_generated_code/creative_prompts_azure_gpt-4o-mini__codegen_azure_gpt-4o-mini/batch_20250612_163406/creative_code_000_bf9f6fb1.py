"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gmvci.gmprog.com
Prompt: How can I implement user authentication using the login and registration features from the HELPGM platform?
Generated: DETERMINISTIC_bf9f6fb1f7148615
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

# Initialize Flask app and configure database
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)  # Use a secure random key for session management
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # SQLite database for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks the password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Username and password required."}), 400
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({"error": "Username already exists."}), 400
    
    new_user = User(username=data['username'])
    new_user.set_password(data['password'])
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if not data or not 'username' in data or not 'password' in data:
        return jsonify({"error": "Username and password required."}), 400
    
    user = User.query.filter_by(username=data['username']).first()
    if user is None or not user.check_password(data['password']):
        return jsonify({"error": "Invalid username or password."}), 401

    session['user_id'] = user.id  # Store user ID in session
    return jsonify({"message": "Login successful."}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({"message": "Logout successful."}), 200

# Function to run the app
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Start the Flask application
```
Ensure you have the required packages installed by running:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Werkzeug
```
Remember to run database migrations and manage the database as needed for production use.
