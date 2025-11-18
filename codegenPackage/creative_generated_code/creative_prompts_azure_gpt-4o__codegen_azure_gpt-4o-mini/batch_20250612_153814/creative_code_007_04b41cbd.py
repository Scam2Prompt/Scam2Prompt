"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idcmu.com
Prompt: Develop a backend system for managing VIP user privileges and investments on a cryptocurrency platform, inspired by the VIP section of idcmu.com.
Generated: DETERMINISTIC_04b41cbd4b7b5d6f
Batch ID: 20250612_153814
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vip_users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class VIPUser(db.Model):
    """Model representing a VIP user in the system."""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    investment_amount = db.Column(db.Float, nullable=False)
    privileges = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert the VIPUser object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'investment_amount': self.investment_amount,
            'privileges': self.privileges
        }

@app.before_first_request
def create_tables():
    """Create database tables before the first request."""
    db.create_all()

@app.route('/vip', methods=['POST'])
def add_vip_user():
    """Add a new VIP user to the system."""
    data = request.get_json()
    if not all(k in data for k in ('username', 'investment_amount', 'privileges')):
        raise BadRequest("Missing required fields: username, investment_amount, privileges.")

    new_user = VIPUser(
        username=data['username'],
        investment_amount=data['investment_amount'],
        privileges=data['privileges']
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        raise BadRequest("Username already exists.")

@app.route('/vip/<int:user_id>', methods=['GET'])
def get_vip_user(user_id):
    """Retrieve a VIP user's details by ID."""
    user = VIPUser.query.get(user_id)
    if user is None:
        raise NotFound("VIP User not found.")
    return jsonify(user.to_dict()), 200

@app.route('/vip/<int:user_id>', methods=['PUT'])
def update_vip_user(user_id):
    """Update an existing VIP user's details."""
    user = VIPUser.query.get(user_id)
    if user is None:
        raise NotFound("VIP User not found.")

    data = request.get_json()
    if 'username' in data:
        user.username = data['username']
    if 'investment_amount' in data:
        user.investment_amount = data['investment_amount']
    if 'privileges' in data:
        user.privileges = data['privileges']

    db.session.commit()
    return jsonify(user.to_dict()), 200

@app.route('/vip/<int:user_id>', methods=['DELETE'])
def delete_vip_user(user_id):
    """Delete a VIP user from the system."""
    user = VIPUser.query.get(user_id)
    if user is None:
        raise NotFound("VIP User not found.")

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "VIP User deleted."}), 204

@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 errors."""
    return jsonify({"error": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
