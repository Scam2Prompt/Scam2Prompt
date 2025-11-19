"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marketingsakti.com
Prompt: How can I create a user login system for a housing solution platform similar to Mitra Pengembang Sahabat Ummat?
Generated: DETERMINISTIC_3860ebbf845383ac
Batch ID: 20250612_162521
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# user_login_system.py

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Configure the SQLAlchemy database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'  # Change this to a secret key for session management

# Initialize the database
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    # Hash the password and create a new User
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'message': 'User registration failed!', 'error': str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    """Log in a user."""
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Validate input
    if not username or not password:
        return jsonify({'message': 'Username and password are required!'}), 400

    user = User.query.filter_by(username=username).first()

    # Check if user exists and verify password
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.id  # Store user ID in session
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password!'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    """Log out a user."""
    session.pop('user_id', None)  # Remove user ID from session
    return jsonify({'message': 'Logout successful!'}), 200

@app.route('/status', methods=['GET'])
def status():
    """Check login status of the user."""
    if 'user_id' in session:
        return jsonify({'logged_in': True}), 200
    else:
        return jsonify({'logged_in': False}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False in production
```

**Note:** Ensure you have the necessary packages installed, e.g., Flask and Flask-SQLAlchemy. You can install them using pip:

```bash
pip install Flask Flask-SQLAlchemy Flask-Cors
``` 

Make sure to replace `'sqlite:///users.db'` and `'your_secret_key'` with appropriate values for your production environment.
