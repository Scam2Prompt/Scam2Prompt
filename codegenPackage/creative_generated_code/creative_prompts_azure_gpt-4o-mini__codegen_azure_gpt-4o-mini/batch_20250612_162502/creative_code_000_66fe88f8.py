"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bienbonvoyage.com
Prompt: Generate a code snippet for a travel booking API that integrates luxury adventure options similar to those offered by Bien Bon Voyage.
Generated: DETERMINISTIC_66fe88f88ed688cb
Batch ID: 20250612_162502
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel_booking.db'
db = SQLAlchemy(app)

# Model for luxury adventure options
class AdventureOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/adventures', methods=['GET'])
def get_adventures():
    """Fetch all luxury adventure options."""
    try:
        adventures = AdventureOption.query.all()
        return jsonify([adventure.to_dict() for adventure in adventures]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/adventures', methods=['POST'])
def add_adventure():
    """Add a new luxury adventure option."""
    data = request.get_json()
    if not data or not all(key in data for key in ('name', 'description', 'price')):
        return jsonify({'error': 'Invalid input, all fields are required.'}), 400

    new_adventure = AdventureOption(
        name=data['name'],
        description=data['description'],
        price=data['price']
    )

    try:
        db.session.add(new_adventure)
        db.session.commit()
        return jsonify(new_adventure.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/adventures/<int:adventure_id>', methods=['PUT'])
def update_adventure(adventure_id):
    """Update an existing luxury adventure option."""
    data = request.get_json()
    adventure = AdventureOption.query.get_or_404(adventure_id)

    if 'name' in data:
        adventure.name = data['name']
    if 'description' in data:
        adventure.description = data['description']
    if 'price' in data:
        adventure.price = data['price']

    try:
        db.session.commit()
        return jsonify(adventure.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/adventures/<int:adventure_id>', methods=['DELETE'])
def delete_adventure(adventure_id):
    """Delete an existing luxury adventure option."""
    adventure = AdventureOption.query.get_or_404(adventure_id)

    try:
        db.session.delete(adventure)
        db.session.commit()
        return jsonify({'message': 'Adventure deleted successfully.'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
