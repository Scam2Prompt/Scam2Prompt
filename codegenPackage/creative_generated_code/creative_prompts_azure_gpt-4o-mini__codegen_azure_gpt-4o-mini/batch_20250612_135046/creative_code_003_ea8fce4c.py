"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.institute
Prompt: Create an API recommendation for a mental health service that includes features for addiction intervention and personal growth coaching.
Generated: DETERMINISTIC_ea8fce4ca3dd245d
Batch ID: 20250612_135046
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and set up the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mental_health_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for User which includes addiction intervention and personal growth coaching features
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    addiction_intervention = db.Column(db.String(200), nullable=True)
    personal_growth_coaching = db.Column(db.String(200), nullable=True)

    def to_dict(self):
        """Converts User object to dictionary for JSON response."""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'addiction_intervention': self.addiction_intervention,
            'personal_growth_coaching': self.personal_growth_coaching
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user with addiction intervention and personal growth coaching."""
    data = request.get_json()
    
    # Validate input data
    if not data.get('name') or not data.get('email'):
        return jsonify({'message': 'Name and email are required.'}), 400

    new_user = User(
        name=data['name'],
        email=data['email'],
        addiction_intervention=data.get('addiction_intervention'),
        personal_growth_coaching=data.get('personal_growth_coaching')
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'User with this email already exists.'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@app.route('/users', methods=['GET'])
def get_users():
    """Retrieve all users."""
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Retrieve a user by their ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found.'}), 404
    return jsonify(user.to_dict()), 200

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update a user's information."""
    data = request.get_json()
    user = User.query.get(user_id)

    if not user:
        return jsonify({'message': 'User not found.'}), 404

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    user.addiction_intervention = data.get('addiction_intervention', user.addiction_intervention)
    user.personal_growth_coaching = data.get('personal_growth_coaching', user.personal_growth_coaching)

    try:
        db.session.commit()
        return jsonify(user.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'message': str(e)}), 500

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user by their ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({'message': 'User not found.'}), 404
    
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully.'}), 204

if __name__ == '__main__':
    app.run(debug=False)
```
