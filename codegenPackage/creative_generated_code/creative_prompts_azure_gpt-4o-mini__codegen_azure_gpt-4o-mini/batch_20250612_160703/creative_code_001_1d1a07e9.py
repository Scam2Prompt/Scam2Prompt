"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trezor.vozp.cz
Prompt: What are best practices for managing user authentication and password security in a system like Trezor VoZP?
Generated: DETERMINISTIC_1d1a07e97959a85c
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import bcrypt
from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# User schema for serialization
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

# Create the database and the user table
with app.app_context():
    db.create_all()

# Helper function to hash passwords
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Helper function to verify passwords
def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

# API endpoint to register a new user
@app.route('/register', methods=['POST'])
def register_user():
    """Register a new user, storing hashed password."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        abort(400, 'Username and password are required.')

    hashed_password = hash_password(password)

    new_user = User(username=username, password_hash=hashed_password)

    try:
        db.session.add(new_user)
        db.session.commit()
        return UserSchema().dump(new_user), 201
    except IntegrityError:
        db.session.rollback()
        abort(400, 'User already exists.')

# API endpoint to authenticate a user
@app.route('/login', methods=['POST'])
def login_user():
    """Authenticate a user and return success status."""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        abort(400, 'Username and password are required.')

    user = User.query.filter_by(username=username).first()

    if user and verify_password(user.password_hash, password):
        return jsonify(message='Login successful.'), 200
    else:
        abort(401, 'Invalid username or password.')

# API endpoint to change password
@app.route('/change-password', methods=['POST'])
def change_password():
    """Change a user's password."""
    username = request.json.get('username')
    old_password = request.json.get('old_password')
    new_password = request.json.get('new_password')

    if not username or not old_password or not new_password:
        abort(400, 'Username, old password, and new password are required.')

    user = User.query.filter_by(username=username).first()

    if user and verify_password(user.password_hash, old_password):
        user.password_hash = hash_password(new_password)
        db.session.commit()
        return jsonify(message='Password changed successfully.'), 200
    else:
        abort(401, 'Invalid username or password.')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
