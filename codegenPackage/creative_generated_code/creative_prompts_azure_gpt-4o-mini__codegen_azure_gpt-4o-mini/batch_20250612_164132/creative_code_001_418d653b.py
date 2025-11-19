"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isabellanoviyaonlinetechblog.blogspot.com
Prompt: What are the key strategies for developing a bitcoin trade website similar to Paxful?
Generated: DETERMINISTIC_418d653b9c9397e1
Batch ID: 20250612_164132
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///trading_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input!'}), 400
    
    username = data['username']
    password = data['password']
    
    # Check if the user already exists
    if User.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already exists!'}), 400
    
    # Hash the password and create a new user
    hashed_password = generate_password_hash(password, method='sha256')
    new_user = User(username=username, password=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': 'Error creating user!', 'error': str(e)}), 500

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Validate input
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Invalid input!'}), 400
    
    username = data['username']
    password = data['password']

    # Find the user
    user = User.query.filter_by(username=username).first()
    
    # Check if user exists and password is correct
    if user and check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password!'}), 401

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
