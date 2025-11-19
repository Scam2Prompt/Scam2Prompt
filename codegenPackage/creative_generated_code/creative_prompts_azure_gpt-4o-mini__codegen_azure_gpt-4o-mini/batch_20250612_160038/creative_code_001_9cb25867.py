"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sei.land
Prompt: What are the best practices for ensuring user data protection in a web application like sei.land?
Generated: DETERMINISTIC_9cb2586703be23c7
Batch ID: 20250612_160038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for web development and security
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv
from flask_cors import CORS

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# User model for storing user information securely
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with hashed password."""
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
        
        if not username or not password:
            return jsonify({'message': 'Username and password are required.'}), 400
        
        # Check if the user already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists.'}), 409

        user = User(username=username)
        user.set_password(password)
        
        db.session.add(user)
        db.session.commit()
        
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of an error
        return jsonify({'message': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a success message."""
    data = request.get_json()
    try:
        username = data['username']
        password = data['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            return jsonify({'message': 'Login successful.'}), 200
        else:
            return jsonify({'message': 'Invalid credentials.'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({'message': 'Not found.'}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'message': 'Internal server error.'}), 500

if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=False)
```
