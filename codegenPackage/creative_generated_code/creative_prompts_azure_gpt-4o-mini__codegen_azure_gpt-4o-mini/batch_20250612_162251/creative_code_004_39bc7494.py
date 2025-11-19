"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phanytom.com
Prompt: Provide an example of a web application that utilizes Techmaestropus's cloud management solutions for secure user authentication.
Generated: DETERMINISTIC_39bc74946ec54b82
Batch ID: 20250612_162251
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
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

# Initialize Flask application
app = Flask(__name__)

# Enable CORS for handling cross-origin requests
CORS(app)

# Configure secret key and database URI
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your_secret_key_here')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and password hashing
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define User model for database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(username=data['username'], password=hashed_password)

    # Check if username already exists
    if User.query.filter_by(username=new_user.username).first():
        return jsonify({'error': 'Username already exists.'}), 400

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and create session."""
    data = request.get_json()

    if not data or not data.get('username') or not data.get('password'):
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        session['user_id'] = user.id
        return jsonify({'message': 'Logged in successfully.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the current user."""
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully.'}), 200

@app.route('/protected', methods=['GET'])
def protected():
    """A protected route that requires authentication."""
    if 'user_id' not in session:
        return jsonify({'error': 'Unauthorized access.'}), 403
    return jsonify({'message': 'Welcome to the protected route!'}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
