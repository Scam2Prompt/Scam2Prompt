"""
Generated Code Metadata:
========================
Original URL: https://ev-io.now.sh
Prompt: Implement a "Skin Preview" tool for a blockchain-based FPS game, inspired by ev.io, where players can view and lend skins from their inventory.
Generated: DETERMINISTIC_2827c4a318e2eb4b
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skins.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Skin model
class Skin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    owner_id = db.Column(db.Integer, nullable=False)  # Assuming user IDs are integers

    def to_dict(self):
        """Convert Skin object to dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'owner_id': self.owner_id
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/skins', methods=['GET'])
def get_skins():
    """Retrieve all skins from the inventory."""
    try:
        skins = Skin.query.all()
        return jsonify([skin.to_dict() for skin in skins]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/skins/<int:skin_id>', methods=['GET'])
def get_skin(skin_id):
    """Retrieve a specific skin by its ID."""
    try:
        skin = Skin.query.get_or_404(skin_id)
        return jsonify(skin.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/skins', methods=['POST'])
def add_skin():
    """Add a new skin to the inventory."""
    data = request.get_json()
    if not data or 'name' not in data or 'owner_id' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_skin = Skin(name=data['name'], description=data.get('description'), owner_id=data['owner_id'])
    
    try:
        db.session.add(new_skin)
        db.session.commit()
        return jsonify(new_skin.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/skins/<int:skin_id>', methods=['DELETE'])
def delete_skin(skin_id):
    """Delete a skin from the inventory."""
    try:
        skin = Skin.query.get_or_404(skin_id)
        db.session.delete(skin)
        db.session.commit()
        return jsonify({'message': 'Skin deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code implements a simple Flask application with a SQLite database to manage skins.
- It includes endpoints to retrieve all skins, retrieve a specific skin, add a new skin, and delete a skin.
- Error handling is implemented for database operations, and input validation is performed for adding new skins.
- The database model and API endpoints are designed to be extensible for future features.
