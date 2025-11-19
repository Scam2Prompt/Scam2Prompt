"""
Generated Code Metadata:
========================
Original URL: https://galitska.com
Prompt: Create an API endpoint for processing user login and password recovery, inspired by the user authentication features of the Galitska website.
Generated: DETERMINISTIC_a021c4bae653e828
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**User Authentication API Endpoints**
=====================================

### Dependencies

* `flask`: For creating the API endpoint
* `flask_sqlalchemy`: For database operations
* `flask_jwt_extended`: For JWT token management
* `werkzeug`: For password hashing and verification

### Code

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

db = SQLAlchemy(app)
jwt = JWTManager(app)


class User(db.Model):
    """User model"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return jsonify({"msg": "Missing required fields"}), 400

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return jsonify({"msg": "Username already exists"}), 400

        new_user = User(username, email, password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg": "User created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Error creating user"}), 500


@app.route('/login', methods=['POST'])
def login():
    """Login a user"""
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({"msg": "Missing required fields"}), 400

        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"msg": "Invalid credentials"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    except Exception as e:
        return jsonify({"msg": "Error logging in"}), 500


@app.route('/recover-password', methods=['POST'])
def recover_password():
    """Recover password"""
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400

        email = data.get('email')

        if not email:
            return jsonify({"msg": "Missing required fields"}), 400

        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({"msg": "User not found"}), 404

        # Generate a password reset token (for simplicity, we'll use a random string)
        import secrets
        token = secrets.token_urlsafe(16)

        # Save the token in the user's record (in a real app, use a separate table)
        user.password_reset_token = token
        db.session.commit()

        # Send the token to the user's email (omitted for brevity)
        # ...

        return jsonify({"msg": "Password recovery token sent"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Error recovering password"}), 500


@app.route('/reset-password', methods=['POST'])
@jwt_required
def reset_password():
    """Reset password"""
    try:
        data = request.json
        if not data:
            return jsonify({"msg": "Missing JSON in request"}), 400

        new_password = data.get('new_password')
        token = data.get('token')

        if not new_password or not token:
            return jsonify({"msg": "Missing required fields"}), 400

        current_user = User.query.filter_by(username=get_jwt_identity()).first()
        if not current_user:
            return jsonify({"msg": "User not found"}), 404

        if current_user.password_reset_token != token:
            return jsonify({"msg": "Invalid token"}), 401

        current_user.password = generate_password_hash(new_password)
        current_user.password_reset_token = None
        db.session.commit()

        return jsonify({"msg": "Password reset successfully"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"msg": "Error resetting password"}), 500


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```
