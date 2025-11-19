"""
Generated Code Metadata:
========================
Original URL: https://ad-o.jp
Prompt: "What are the best practices for securing a website hosted on Xserver, and how can I implement them?"
Generated: DETERMINISTIC_3fb3d62cd7a1e35f
Batch ID: 20250622_205306
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

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
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
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a secure password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"error": "User already exists."}), 400

    new_user = User(username=username)
    new_user.set_password(password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully."}), 201
    except Exception as e:
        logging.error(f"Error registering user: {e}")
        db.session.rollback()
        return jsonify({"error": "Registration failed."}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate a user and return a success message."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return jsonify({"message": "Login successful."}), 200
    return jsonify({"error": "Invalid username or password."}), 401

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": "Not found."}), 404

# Error handling for 500
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=False)
```

### .env file example
```
DATABASE_URL=sqlite:///site.db
PORT=5000
```

### Requirements
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- python-dotenv
- Werkzeug

### Best Practices Implemented
- Password hashing for security
- Input validation
- Error handling
- Logging for monitoring
- Environment variables for configuration
- Use of a database for user management
