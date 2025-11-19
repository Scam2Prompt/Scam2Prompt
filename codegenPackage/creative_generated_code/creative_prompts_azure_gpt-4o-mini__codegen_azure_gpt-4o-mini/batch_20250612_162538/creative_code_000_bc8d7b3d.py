"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://districtchronicles.com
Prompt: Write a code snippet to implement a secure login system for an online gaming platform similar to Pixxie928, ensuring data encryption and user privacy.
Generated: DETERMINISTIC_bc8d7b3d7b26da37
Batch ID: 20250612_162538
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

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this in production
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Use a more secure database in production
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def check_password(provided_password, stored_password_hash):
    """Verifies a provided password against a stored hash."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password_hash.encode('utf-8'))

@app.route('/register', methods=['POST'])
def register():
    """Endpoint for user registration."""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        raise BadRequest("Username and password are required.")
    
    if User.query.filter_by(username=username).first():
        raise BadRequest("Username already exists.")
    
    hashed_password = hash_password(password)
    new_user = User(username=username, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify({"message": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        raise BadRequest("Username and password are required.")
    
    user = User.query.filter_by(username=username).first()
    
    if user is None or not check_password(password, user.password_hash):
        raise Unauthorized("Invalid username or password.")
    
    session['user_id'] = user.id
    return jsonify({"message": "Login successful."}), 200

@app.route('/logout', methods=['POST'])
def logout():
    """Endpoint for user logout."""
    session.pop('user_id', None)
    return jsonify({"message": "Logout successful."}), 200

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False in production
```

**Note**: Remember to change the `secret_key` and database URI to more secure options in a production environment. Use HTTPS for all communications.
