"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sin88.makeup
Prompt: Generate code for a secure user login system for an online betting platform like SIN88.
Generated: DETERMINISTIC_efc1eb9a8c784a8d
Batch ID: 20250612_164217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import BadRequest, Unauthorized

# Initialize Flask app and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a secure random key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a secure database in production
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        """Hash the password for storage."""
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, password):
        """Check the hashed password against the provided password."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    """Register a new user with a username and password."""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Missing username or password")

    username = data['username']
    password = data['password']
    
    if User.query.filter_by(username=username).first():
        raise BadRequest("Username already exists")

    # Create and store new user
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
    """Log in a user with their username and password."""
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        raise BadRequest("Missing username or password")

    user = User.query.filter_by(username=data['username']).first()
    
    if user is None or not user.check_password(data['password']):
        raise Unauthorized("Invalid username or password")

    # Store user id in session
    session['user_id'] = user.id
    return jsonify({"message": "Logged in successfully"}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Log out the currently logged-in user."""
    session.pop('user_id', None)
    return jsonify({"message": "Logged out successfully"}), 200

@app.route('/status', methods=['GET'])
def status():
    """Check if the user is logged in."""
    if 'user_id' in session:
        return jsonify({"message": "User is logged in", "user_id": session['user_id']}), 200
    else:
        return jsonify({"message": "No user is logged in"}), 401

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

In this code:
- A Flask web application is set up to handle user registration, login, and logout.
- Passwords are securely hashed using bcrypt.
- Error handling is implemented to ensure proper responses are sent for missing information or invalid credentials.
- The code includes routes to check the user's login status. 
- The database is created using SQLAlchemy and utilizes SQLite for simplicity; you should replace it with a secure production-ready database.
