"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeco.pk
Prompt: Provide an API recommendation for managing agricultural machinery inventory, similar to the tractor attachments offered by JECO.
Generated: DETERMINISTIC_10986a5db2e759b0
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///machinery_inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Model for machinery inventory
class Machinery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert the Machinery object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'quantity': self.quantity
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/machinery', methods=['GET'])
def get_machinery():
    """Get the list of all machinery in the inventory."""
    try:
        machinery_list = Machinery.query.all()
        return jsonify([m.to_dict() for m in machinery_list]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/machinery', methods=['POST'])
def add_machinery():
    """Add a new machinery item to the inventory."""
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'type', 'quantity')):
        return jsonify({'error': 'Invalid input'}), 400

    new_machinery = Machinery(
        name=data['name'],
        type=data['type'],
        quantity=data['quantity']
    )

    try:
        db.session.add(new_machinery)
        db.session.commit()
        return jsonify(new_machinery.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/machinery/<int:machinery_id>', methods=['PUT'])
def update_machinery(machinery_id):
    """Update an existing machinery item."""
    machinery = Machinery.query.get(machinery_id)
    if not machinery:
        return jsonify({'error': 'Machinery not found'}), 404

    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'type', 'quantity')):
        return jsonify({'error': 'Invalid input'}), 400

    machinery.name = data['name']
    machinery.type = data['type']
    machinery.quantity = data['quantity']

    try:
        db.session.commit()
        return jsonify(machinery.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/machinery/<int:machinery_id>', methods=['DELETE'])
def delete_machinery(machinery_id):
    """Delete a machinery item from the inventory."""
    machinery = Machinery.query.get(machinery_id)
    if not machinery:
        return jsonify({'error': 'Machinery not found'}), 404

    try:
        db.session.delete(machinery)
        db.session.commit()
        return jsonify({'message': 'Machinery deleted successfully'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
