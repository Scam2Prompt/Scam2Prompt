"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rbby-wollet.teachable.com
Prompt: Suggest APIs for managing terms of use and privacy policies dynamically for an online course platform like rbby-wollet.
Generated: DETERMINISTIC_e8683fcfc88efbf0
Batch ID: 20250612_153722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///policies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Terms of Use and Privacy Policy
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Policy object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content
        }

# Initialize the database
with app.app_context():
    db.create_all()

@app.route('/policies', methods=['GET'])
def get_policies():
    """Retrieve all policies."""
    policies = Policy.query.all()
    return jsonify([policy.to_dict() for policy in policies]), 200

@app.route('/policies/<int:policy_id>', methods=['GET'])
def get_policy(policy_id):
    """Retrieve a specific policy by ID."""
    policy = Policy.query.get(policy_id)
    if policy is None:
        abort(404, description="Policy not found")
    return jsonify(policy.to_dict()), 200

@app.route('/policies', methods=['POST'])
def create_policy():
    """Create a new policy."""
    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if not title or not content:
        abort(400, description="Title and content are required")

    new_policy = Policy(title=title, content=content)

    try:
        db.session.add(new_policy)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description="Policy with this title already exists")

    return jsonify(new_policy.to_dict()), 201

@app.route('/policies/<int:policy_id>', methods=['PUT'])
def update_policy(policy_id):
    """Update an existing policy."""
    policy = Policy.query.get(policy_id)
    if policy is None:
        abort(404, description="Policy not found")

    data = request.get_json()
    title = data.get('title')
    content = data.get('content')

    if title:
        policy.title = title
    if content:
        policy.content = content

    db.session.commit()
    return jsonify(policy.to_dict()), 200

@app.route('/policies/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    """Delete a policy by ID."""
    policy = Policy.query.get(policy_id)
    if policy is None:
        abort(404, description="Policy not found")

    db.session.delete(policy)
    db.session.commit()
    return jsonify({"message": "Policy deleted successfully"}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
