"""
Generated Code Metadata:
========================
Original URL: https://web.procat-saas.online
Prompt: "Create a template for launching a SaaS product with modern technologies and essential integrations."
Generated: DETERMINISTIC_433df755b499703d
Batch ID: 20250622_211753
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define a User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400

    # Check if user already exists
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'User already exists'}), 409

    # Create a new user
    new_user = User(email=data['email'], password=data['password'])  # Password should be hashed in production
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    if not data or not 'email' in data or not 'password' in data:
        return jsonify({'error': 'Invalid input'}), 400

    user = User.query.filter_by(email=data['email'], password=data['password']).first()  # Password should be hashed in production
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Main entry point
if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate Flask-Cors
```

### Database Setup
Make sure to set the `DATABASE_URL` environment variable for your production database or it will default to a local SQLite database.
