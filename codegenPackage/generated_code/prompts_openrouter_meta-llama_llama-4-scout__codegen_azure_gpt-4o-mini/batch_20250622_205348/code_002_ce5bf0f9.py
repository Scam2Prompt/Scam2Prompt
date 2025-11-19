"""
Generated Code Metadata:
========================
Original URL: https://planetaria.world
Prompt: Generate a Python API to interact with a metaverse platform, inspired by Planetaria's features and architecture.
Generated: DETERMINISTIC_ce5bf0f900ab50e0
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///metaverse.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for the User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    avatar_url = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'avatar_url': self.avatar_url
        }

# Create the database tables
with app.app_context():
    db.create_all()

# API endpoint to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400

    new_user = User(username=data['username'], avatar_url=data.get('avatar_url'))
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to get a user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200

# API endpoint to update a user's avatar
@app.route('/api/users/<int:user_id>/avatar', methods=['PUT'])
def update_avatar(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data or 'avatar_url' not in data:
        return jsonify({'error': 'Avatar URL is required'}), 400

    user.avatar_url = data['avatar_url']
    try:
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to delete a user
@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False') == 'True')
```
