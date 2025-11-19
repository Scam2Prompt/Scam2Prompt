"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://niftin.info
Prompt: How can I implement user authentication in a web application similar to Niftin's login and signup features?
Generated: DETERMINISTIC_c03e817a7dde30d6
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_cors import CORS
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the application
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key')  # Make sure to use a secure key in production
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Enable CORS for all routes
CORS(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for the user."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verify the password against the stored hash."""
        return check_password_hash(self.password_hash, password)

# Route for user registration
@app.route('/signup', methods=['POST'])
def signup():
    """Create a new user."""
    data = request.json

    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400

    # Check if user already exists
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'User already exists!'}), 400

    new_user = User(username=data['username'])
    new_user.set_password(data['password'])

    # Save the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and start a session."""
    data = request.json

    # Validate input data
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400

    user = User.query.filter_by(username=data['username']).first()
    
    # Check if user exists and password matches
    if user is None or not user.check_password(data['password']):
        return jsonify({'message': 'Invalid username or password!'}), 401

    session['user_id'] = user.id  # Store user_id in session
    return jsonify({'message': 'Login successful!'}), 200

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    """End user session."""
    session.pop('user_id', None)  # Remove user_id from session
    return jsonify({'message': 'Logout successful!'}), 200

# Main entry point
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)  # Set debug=False in production
```
