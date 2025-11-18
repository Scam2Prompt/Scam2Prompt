"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://apexcapitalflow.com
Prompt: Develop a secure login system for a cryptocurrency investment platform, referencing Apex Capital Flow's user dashboard features like mobile-friendly design and encryption.
Generated: DETERMINISTIC_5507de0e0ed75b65
Batch ID: 20250612_150246
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
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app
app = Flask(__name__)

# Configuration for the app
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Replace with a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Using SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        """Hashes the password and stores it."""
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Validates the password."""
        return bcrypt.check_password_hash(self.password_hash, password)

# Initialize the database
with app.app_context():
    db.create_all()

# Helper function to validate inputs
def validate_input(data, required_fields):
    """Validates the input data to ensure all required fields are present."""
    for field in required_fields:
        if field not in data or not data[field].strip():
            raise BadRequest(f"Missing or empty field: {field}")

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.json
    validate_input(data, ['username', 'email', 'password'])

    if User.query.filter((User.username == data['username']) | (User.email == data['email'])).first():
        raise BadRequest("Username or email already exists.")

    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully!"}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    """Handles user login."""
    data = request.json
    validate_input(data, ['username', 'password'])

    user = User.query.filter_by(username=data['username']).first()
    if not user or not user.check_password(data['password']):
        raise Unauthorized("Invalid username or password.")

    # Create user session (for demonstration, avoid storing sensitive data in session)
    session['user_id'] = user.id
    session['username'] = user.username

    return jsonify({"message": "Login successful!"}), 200

# User logout endpoint
@app.route('/logout', methods=['POST'])
def logout():
    """Handles user logout by clearing the session."""
    session.clear()
    return jsonify({"message": "Logged out successfully!"}), 200

# Secured endpoint for dashboard access
@app.route('/dashboard', methods=['GET'])
def dashboard():
    """A sample secured endpoint to demonstrate login sessions."""
    if 'user_id' not in session:
        raise Unauthorized("Access denied. Please log in.")

    return jsonify({"message": f"Welcome to your dashboard, {session['username']}!"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
