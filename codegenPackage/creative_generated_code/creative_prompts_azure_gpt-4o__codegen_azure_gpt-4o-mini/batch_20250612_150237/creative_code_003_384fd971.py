"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinbased.beautyjibindia.com
Prompt: Create a backend system using Flask or Django to handle login requests for a platform like "Coin Base," ensuring secure password storage.
Generated: DETERMINISTIC_384fd9718453fba4
Batch ID: 20250612_150237
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here’s a backend system using Flask to handle login requests with secure password storage:

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Generates a hashed password."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Checks hashed password against the provided password."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    """Handles user registration."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    username = data['username']
    password = data['password']

    # Check if username already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists'}), 400

    new_user = User(username=username)
    new_user.set_password(password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Handles user login."""
    data = request.get_json()
    
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.check_password(data['password']):
        return jsonify({'message': 'Login successful'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

# Error handling for database errors
@app.errorhandler(500)
def internal_error(error):
    """Handles internal server errors."""
    return jsonify({'message': 'Internal Server Error'}), 500

# Main entry point
if __name__ == '__main__':
    db.create_all()  # Create database tables
    app.run(debug=False)  # Run the app
```

### Instructions to Run:
1. Ensure you have Flask and SQLAlchemy installed: `pip install Flask Flask-SQLAlchemy Flask-Migrate`
2. Save the code to a file (e.g., `app.py`).
3. Run the Flask application with `python app.py`.
4. Use a tool like Postman or curl to test the registration and login endpoints (`/register` and `/login`).

### Database Migration:
To handle database migrations, you can initialize the database and create migration files using the Flask-Migrate command line interface.
