"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.se
Prompt: Generate code for a backend system that handles user registrations and connects them to investment education companies, ensuring compliance with data privacy policies like those mentioned on Trade GPT.
Generated: DETERMINISTIC_0c5299a20a7a0ec2
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI and other settings
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database instance
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for the database
class User(db.Model):
    """Model for storing user information."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def set_password(self, password):
        """Hash password before storing."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check hashed password against provided password."""
        return check_password_hash(self.password_hash, password)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register_user():
    """Endpoint to register a new user."""
    data = request.get_json()

    # Validate input data
    if not data or 'username' not in data or 'password' not in data or 'email' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    username = data['username']
    password = data['password']
    email = data['email']

    # Check for existing user
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 400

    try:
        # Create a new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201

    except Exception as e:
        logging.error(f"Error registering user: {e}")
        db.session.rollback()
        return jsonify({'error': 'An error occurred during registration'}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Endpoint to retrieve all registered users."""
    try:
        users = User.query.all()
        return jsonify([{'id': user.id, 'username': user.username, 'email': user.email} for user in users]), 200
    except Exception as e:
        logging.error(f"Error retrieving users: {e}")
        return jsonify({'error': 'An error occurred while retrieving users'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'false').lower() == 'true')
```

### Notes:
- Ensure to set the `DATABASE_URI` environment variable before running the application for it to connect to a real database.
- The application uses SQLite for simplicity; replace it with a production-ready database in real-world applications.
- Always handle sensitive user information securely, in compliance with data privacy laws.
