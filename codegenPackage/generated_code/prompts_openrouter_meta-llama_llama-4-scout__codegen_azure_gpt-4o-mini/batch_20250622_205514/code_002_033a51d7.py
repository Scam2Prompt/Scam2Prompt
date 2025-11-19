"""
Generated Code Metadata:
========================
Original URL: https://cartenoir.org
Prompt: "Generate a code snippet for a custom server solution that meets the requirements of a secure on-premise infrastructure, as described in the Carte Noir Consulting project for BFR Gaming."
Generated: DETERMINISTIC_033a51d72e7a0d43
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Configure database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration support
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# User model for database
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

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Error registering user: {e}")
        return jsonify({'error': 'Registration failed.'}), 500

@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid credentials.'}), 401

if __name__ == '__main__':
    # Run the application with secure settings
    app.run(host='0.0.0.0', port=5000, ssl_context=('path/to/cert.pem', 'path/to/key.pem'))
```

**Note:** Ensure to replace `'path/to/cert.pem'` and `'path/to/key.pem'` with the actual paths to your SSL certificate and key files. Additionally, create a `.env` file with the `DATABASE_URI` variable set to your database connection string.
