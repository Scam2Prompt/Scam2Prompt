"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status-ehaat.life
Prompt: Develop a REST API for managing lottery app user accounts, inspired by the "welcome盈彩购彩大厅广东" section of the website.
Generated: DETERMINISTIC_ebf47abe3717491e
Batch ID: 20250612_145832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize Flask application
app = Flask(__name__)

# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lottery_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """
        Convert User object to dictionary for JSON representation.
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

# Error handler for resource not found
@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e)), 404

# Route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user account.
    Expects 'username', 'email', and 'password' in the request JSON body.
    """
    data = request.get_json()  # Parse JSON request body
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Invalid input. Username, email, and password are required.'}), 400

    # Hash the user's password
    hashed_password = generate_password_hash(data['password'], method='sha256')

    try:
        # Create and save the user
        new_user = User(username=data['username'], email=data['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully!', 'user': new_user.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to create user. ' + str(e)}), 500

# Route to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    """
    Retrieve all user accounts.
    """
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

# Route to fetch a user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Retrieve a user by ID.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404
    return jsonify(user.to_dict()), 200

# Route to update a user's email or password
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a user's email or password.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input.'}), 400

    if 'email' in data:
        user.email = data['email']
    if 'password' in data:
        user.password = generate_password_hash(data['password'], method='sha256')

    try:
        db.session.commit()
        return jsonify({'message': 'User updated successfully!', 'user': user.to_dict()}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to update user. ' + str(e)}), 500

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a user account.
    """
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found.'}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'Failed to delete user. ' + str(e)}), 500

# Main entry point
if __name__ == '__main__':
    # Create database tables before starting the server
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
