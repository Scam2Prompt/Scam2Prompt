"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jieyasoft.com
Prompt: Suggest a library or framework for creating a "混合制直销软件" (hybrid direct selling system) that combines features of level-based and matrix systems, as described by JieyaSoft.
Generated: DETERMINISTIC_143d95f098365408
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
hybrid_direct_selling.py

This module provides a basic structure for implementing a hybrid direct selling system.
The system combines features of level-based and matrix compensation plans.
This code serves as a foundational framework that can be extended as per specific requirements.

Dependencies:
- Flask for the web framework
- SQLAlchemy for database interactions
"""
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///direct_selling.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    """User model representing a participant in the direct selling system."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=1)
    sponsor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<User {self.name}>'

# Define a route to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user in the system."""
    data = request.get_json()
    new_user = User(name=data['name'], level=data.get('level', 1), sponsor_id=data.get('sponsor_id'))

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully', 'user_id': new_user.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'User could not be created'}), 400

# Define a route to get user details
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve details of a user by ID."""
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify({'id': user.id, 'name': user.name, 'level': user.level, 'sponsor_id': user.sponsor_id}), 200

# Initialize the database
@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

# Run the application
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the application: {e}")
```
