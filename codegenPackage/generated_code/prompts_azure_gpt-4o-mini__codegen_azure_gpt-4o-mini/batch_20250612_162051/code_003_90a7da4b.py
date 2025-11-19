"""
Generated Code Metadata:
========================
Original URL: https://jiyojaago.org
Prompt: Develop a mobile app feature that encourages users to participate in initiatives like "Jiyo Jaago Swasthalaya," focusing on health and wellness, inspired by the content from the Jiyo Jaago website.
Generated: DETERMINISTIC_90a7da4b444b884b
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jiyojaago.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Initiative model
class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the Initiative object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/initiatives', methods=['GET'])
def get_initiatives():
    """Fetch all initiatives."""
    try:
        initiatives = Initiative.query.all()
        return jsonify([initiative.to_dict() for initiative in initiatives]), 200
    except Exception as e:
        logging.error(f"Error fetching initiatives: {e}")
        return jsonify({"error": "Could not fetch initiatives"}), 500

@app.route('/initiatives', methods=['POST'])
def create_initiative():
    """Create a new initiative."""
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data:
        return jsonify({"error": "Title and description are required"}), 400

    new_initiative = Initiative(title=data['title'], description=data['description'])
    try:
        db.session.add(new_initiative)
        db.session.commit()
        return jsonify(new_initiative.to_dict()), 201
    except Exception as e:
        logging.error(f"Error creating initiative: {e}")
        db.session.rollback()
        return jsonify({"error": "Could not create initiative"}), 500

@app.route('/initiatives/<int:id>', methods=['GET'])
def get_initiative(id):
    """Fetch a specific initiative by ID."""
    initiative = Initiative.query.get(id)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404
    return jsonify(initiative.to_dict()), 200

@app.route('/initiatives/<int:id>', methods=['PUT'])
def update_initiative(id):
    """Update an existing initiative."""
    data = request.get_json()
    initiative = Initiative.query.get(id)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404

    if 'title' in data:
        initiative.title = data['title']
    if 'description' in data:
        initiative.description = data['description']

    try:
        db.session.commit()
        return jsonify(initiative.to_dict()), 200
    except Exception as e:
        logging.error(f"Error updating initiative: {e}")
        db.session.rollback()
        return jsonify({"error": "Could not update initiative"}), 500

@app.route('/initiatives/<int:id>', methods=['DELETE'])
def delete_initiative(id):
    """Delete an initiative."""
    initiative = Initiative.query.get(id)
    if initiative is None:
        return jsonify({"error": "Initiative not found"}), 404

    try:
        db.session.delete(initiative)
        db.session.commit()
        return jsonify({"message": "Initiative deleted successfully"}), 200
    except Exception as e:
        logging.error(f"Error deleting initiative: {e}")
        db.session.rollback()
        return jsonify({"error": "Could not delete initiative"}), 500

if __name__ == '__main__':
    app.run(debug=False)
```
