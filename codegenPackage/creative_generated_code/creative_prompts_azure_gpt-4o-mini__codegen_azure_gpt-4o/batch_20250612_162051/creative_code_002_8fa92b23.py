"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.jobone.careers
Prompt: Create a code snippet that demonstrates how to build a user registration and login system for a job placement platform, inspired by the features on jobONE.
Generated: DETERMINISTIC_8fa92b23ea54b3ac
Batch ID: 20250612_162051
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
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key for production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Helper function to hash passwords
def hash_password(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')

# Helper function to check passwords
def check_password(password, password_hash):
    return bcrypt.check_password_hash(password_hash, password)

# User registration route
@app.route('/register', methods=['POST'])
def register():
    try:
        # Parse request data
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        
        # Validate input
        if not username or not email or not password:
            return jsonify({'error': 'All fields are required'}), 400
        
        # Hash the password
        hashed_password = hash_password(password)
        
        # Create new user
        new_user = User(username=username, email=email, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'}), 201
    
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username or email already exists'}), 409
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# User login route
@app.route('/login', methods=['POST'])
def login():
    try:
        # Parse request data
        data = request.get_json()
        username = data['username']
        password = data['password']
        
        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400
        
        # Find user by username
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Verify password
        if not check_password(password, user.password_hash):
            return jsonify({'error': 'Invalid username or password'}), 401
        
        # Login successful, store user in session
        session['user_id'] = user.id
        return jsonify({'message': 'Login successful'}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to check if user is logged in
@app.route('/is_logged_in', methods=['GET'])
def is_logged_in():
    if 'user_id' in session:
        return jsonify({'logged_in': True}), 200
    return jsonify({'logged_in': False}), 200

# User logout route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logout successful'}), 200

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Run Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
