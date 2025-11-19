"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccemza.com
Prompt: How can I implement security measures in my web hosting environment to prevent vulnerabilities like those mentioned on ccemza.com?
Generated: DETERMINISTIC_ef2cc4b7d9161400
Batch ID: 20250612_161331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for secure cross-origin requests
CORS(app)

# Configure database and logging
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Initialize the database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hashes the user's password for secure storage."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Check the provided password against the stored password hash."""
        return check_password_hash(self.password_hash, password)

@app.route('/register', methods=['POST'])
def register():
    """Endpoint to register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Username already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        logging.error(f"Error during user registration: {e}")
        db.session.rollback()
        return jsonify({'error': 'Failed to register user'}), 500

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'error': 'Invalid username or password'}), 401

@app.errorhandler(404)
def page_not_found(e):
    """Custom error handler for 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

@app.errorhandler(Exception)
def handle_exception(e):
    """Global error handler for unexpected exceptions."""
    logging.error(f"Unexpected error: {e}")
    return jsonify({'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    # Run the application securely
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), ssl_context=('cert.pem', 'key.pem'))
```
