"""
Generated Code Metadata:
========================
Original URL: https://www.izikard.com
Prompt: Create a REST API for managing NFC tag configurations, allowing users to update actions like redirecting to a webpage or collecting reviews, inspired by Izikard's web app.
Generated: DETERMINISTIC_5a3ac436201912c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nfc_tags.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the NFC Tag model
class NFCTag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    action_type = db.Column(db.String(50), nullable=False)
    action_value = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the NFCTag object to a dictionary."""
        return {
            'id': self.id,
            'action_type': self.action_type,
            'action_value': self.action_value
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/nfc_tags', methods=['POST'])
def create_nfc_tag():
    """Create a new NFC tag configuration."""
    data = request.get_json()
    if not data or 'action_type' not in data or 'action_value' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_tag = NFCTag(action_type=data['action_type'], action_value=data['action_value'])
    db.session.add(new_tag)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to create NFC tag'}), 500

    return jsonify(new_tag.to_dict()), 201

@app.route('/nfc_tags/<int:tag_id>', methods=['GET'])
def get_nfc_tag(tag_id):
    """Retrieve an NFC tag configuration by ID."""
    tag = NFCTag.query.get(tag_id)
    if tag is None:
        return jsonify({'error': 'NFC tag not found'}), 404
    return jsonify(tag.to_dict()), 200

@app.route('/nfc_tags/<int:tag_id>', methods=['PUT'])
def update_nfc_tag(tag_id):
    """Update an existing NFC tag configuration."""
    tag = NFCTag.query.get(tag_id)
    if tag is None:
        return jsonify({'error': 'NFC tag not found'}), 404

    data = request.get_json()
    if not data or 'action_type' not in data or 'action_value' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    tag.action_type = data['action_type']
    tag.action_value = data['action_value']
    db.session.commit()

    return jsonify(tag.to_dict()), 200

@app.route('/nfc_tags/<int:tag_id>', methods=['DELETE'])
def delete_nfc_tag(tag_id):
    """Delete an NFC tag configuration."""
    tag = NFCTag.query.get(tag_id)
    if tag is None:
        return jsonify({'error': 'NFC tag not found'}), 404

    db.session.delete(tag)
    db.session.commit()
    return jsonify({'message': 'NFC tag deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=False)
```
