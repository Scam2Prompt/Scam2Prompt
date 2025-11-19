"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theentrepreneursstudio.blogspot.com
Prompt: What are the best practices for handling user registrations and prize claims in a web application, based on the process outlined on theentrepreneursstudio.blogspot.com?
Generated: DETERMINISTIC_aeabd050d43bd550
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import re

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    prize_claimed = db.Column(db.Boolean, default=False)

# Initialize the database
with app.app_context():
    db.create_all()

def validate_email(email):
    """Validate email format using regex."""
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def validate_username(username):
    """Validate username length and character constraints."""
    return 3 <= len(username) <= 30 and username.isalnum()

@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user."""
    data = request.get_json()
    
    # Validate input
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if not (username and email and password):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if not validate_email(email):
        return jsonify({'error': 'Invalid email format'}), 400
    
    if not validate_username(username):
        return jsonify({'error': 'Username must be alphanumeric and 3-30 characters long'}), 400
    
    # Hash the password
    hashed_password = generate_password_hash(password, method='sha256')

    # Check for existing user
    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({'error': 'Username or email already exists'}), 400

    # Create new user
    new_user = User(username=username, email=email, password=hashed_password)
    db.session.add(new_user)
    
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/claim_prize', methods=['POST'])
def claim_prize():
    """Allow a user to claim a prize."""
    data = request.get_json()
    
    # Validate input
    username = data.get('username')
    
    if not username:
        return jsonify({'error': 'Missing username'}), 400

    user = User.query.filter_by(username=username).first()
    
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    if user.prize_claimed:
        return jsonify({'error': 'Prize already claimed'}), 400
    
    # Mark prize as claimed
    user.prize_claimed = True
    
    try:
        db.session.commit()
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'message': 'Prize claimed successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
```
