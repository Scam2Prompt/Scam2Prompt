"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Generate an API design for managing surgical instrument inventory, referencing specific product categories such as "Cone Knives," "Tongue Depressors," and "Needle Holders" mentioned on the Curative Surgical Industry webpage.
Generated: DETERMINISTIC_548586b6e11dff26
Batch ID: 20250612_153246
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

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surgical_instruments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Instrument model
class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'quantity': self.quantity
        }

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

# API endpoint to get all instruments
@app.route('/instruments', methods=['GET'])
def get_instruments():
    """Retrieve a list of all surgical instruments."""
    instruments = Instrument.query.all()
    return jsonify([instrument.to_dict() for instrument in instruments]), 200

# API endpoint to add a new instrument
@app.route('/instruments', methods=['POST'])
def add_instrument():
    """Add a new surgical instrument to the inventory."""
    data = request.get_json()
    try:
        new_instrument = Instrument(
            name=data['name'],
            category=data['category'],
            quantity=data.get('quantity', 0)
        )
        db.session.add(new_instrument)
        db.session.commit()
        return jsonify(new_instrument.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to update an existing instrument
@app.route('/instruments/<int:instrument_id>', methods=['PUT'])
def update_instrument(instrument_id):
    """Update a specific surgical instrument by ID."""
    instrument = Instrument.query.get_or_404(instrument_id)
    data = request.get_json()
    try:
        instrument.name = data.get('name', instrument.name)
        instrument.category = data.get('category', instrument.category)
        instrument.quantity = data.get('quantity', instrument.quantity)
        db.session.commit()
        return jsonify(instrument.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# API endpoint to delete an instrument
@app.route('/instruments/<int:instrument_id>', methods=['DELETE'])
def delete_instrument(instrument_id):
    """Delete a specific surgical instrument by ID."""
    instrument = Instrument.query.get_or_404(instrument_id)
    try:
        db.session.delete(instrument)
        db.session.commit()
        return jsonify({'message': 'Instrument deleted'}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
