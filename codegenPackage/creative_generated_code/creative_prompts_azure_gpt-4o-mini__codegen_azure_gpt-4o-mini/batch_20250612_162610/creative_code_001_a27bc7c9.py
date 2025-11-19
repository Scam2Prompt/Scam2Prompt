"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://survey-uniwaps.org
Prompt: How can I implement user authentication in a survey tool with UniWaps?
Generated: DETERMINISTIC_a27bc7c9c7cf045b
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# survey_auth.py

from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a more secure key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)
CORS(app)  # Enable CORS for all routes

# User model representing the user table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        # Validate input
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Invalid input'}), 400
        
        username = data['username']
        password = data['password']
        
        # Check if username already exists
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'User already exists'}), 409

        # Hash the password and create a new user
        new_user = User(username=username, password=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        # Validate input
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({'message': 'Invalid input'}), 400
        
        user = User.query.filter_by(username=data['username']).first()
        
        # Check if user exists and password is correct
        if user and check_password_hash(user.password, data['password']):
            session['user_id'] = user.id  # Store user ID in session
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'message': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route for user logout
@app.route('/logout', methods=['POST'])
def logout():
    try:
        session.pop('user_id', None)  # Remove user_id from session
        return jsonify({'message': 'Logout successful'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

# Route to check if user is authenticated
@app.route('/status', methods=['GET'])
def status():
    if 'user_id' in session:
        return jsonify({'message': 'User is logged in', 'user_id': session['user_id']}), 200
    else:
        return jsonify({'message': 'User is not logged in'}), 401

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True only in development
```
