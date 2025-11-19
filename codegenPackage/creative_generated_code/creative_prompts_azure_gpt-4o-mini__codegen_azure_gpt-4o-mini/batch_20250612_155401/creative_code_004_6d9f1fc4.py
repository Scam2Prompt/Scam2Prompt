"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guiweb.worldliberryfinancial.com
Prompt: Provide an example of a REST API endpoint for managing user data in a financial application, inspired by the principles outlined on worldliberryfinancial.com.
Generated: DETERMINISTIC_6d9f1fc464b41d55
Batch ID: 20250612_155401
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
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    def to_dict(self):
        """Convert User model to dictionary format."""
        return {'id': self.id, 'name': self.name, 'email': self.email}

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data:
        raise BadRequest("Name and email are required fields.")
    
    # Create a new user instance
    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(new_user.to_dict()), 201

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by ID."""
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")
    
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user."""
    data = request.get_json()
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")
    
    # Update user fields if provided
    if 'name' in data:
        user.name = data['name']
    if 'email' in data:
        user.email = data['email']
    
    db.session.commit()
    
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by ID."""
    user = User.query.get(user_id)
    if user is None:
        raise NotFound(f"User with id {user_id} not found.")
    
    db.session.delete(user)
    db.session.commit()
    
    return jsonify({'message': 'User deleted successfully'}), 204

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
