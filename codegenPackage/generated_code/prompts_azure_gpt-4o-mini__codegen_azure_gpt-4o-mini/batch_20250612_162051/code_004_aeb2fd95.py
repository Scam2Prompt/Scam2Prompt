"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Illustrate how to implement a user authentication system for a web platform that provides access to multidisciplinary health services, inspired by the offerings of Centro Abakadabra.
Generated: DETERMINISTIC_aeb2fd959d70fcb8
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Initialize the database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'User already exists.'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully.'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and create a session."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful.'}), 200

    return jsonify({'error': 'Invalid username or password.'}), 401

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """Log out the user by clearing the session."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful.'}), 200

# Route to check if the user is authenticated
@app.route('/auth', methods=['GET'])
def auth():
    """Check if the user is authenticated."""
    if 'user_id' in session:
        return jsonify({'authenticated': True}), 200
    return jsonify({'authenticated': False}), 401

# Error handling for database errors
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return a JSON response."""
    return jsonify({'error': str(e)}), 500

# Main entry point to run the application
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=True)  # Run the application in debug mode
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Cors Werkzeug
```
