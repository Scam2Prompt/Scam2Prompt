"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mirrorcommunity.com
Prompt: What libraries can I use to create a secure password entry system for an e-commerce website?
Generated: DETERMINISTIC_83ccdeed71d1db48
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# Create the database tables
with app.app_context():
    db.create_all()

def hash_password(password):
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(stored_password, provided_password):
    """Check a hashed password against a provided password."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password)

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input data
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully.'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Username already exists.'}), 400

@app.route('/login', methods=['POST'])
def login():
    """Log in an existing user by checking their username and password."""
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Validate input data
    if not username or not password:
        return jsonify({'error': 'Username and password are required.'}), 400

    user = User.query.filter_by(username=username).first()

    if user and check_password(user.password_hash, password):
        return jsonify({'message': 'Login successful.'}), 200
    else:
        return jsonify({'error': 'Invalid username or password.'}), 401

if __name__ == '__main__':
    app.run(debug=True)
```

**Required Libraries:**
- Flask
- Flask-SQLAlchemy
- bcrypt

**Installation Command:**
```bash
pip install Flask Flask-SQLAlchemy bcrypt
```
