"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbiotic-gt.com
Prompt: Outline a RESTful API design for managing the inventory of produce grown using SymBiotic's vertical farming systems, emphasizing pest-free production.
Generated: DETERMINISTIC_357f034b08620e00
Batch ID: 20250612_155632
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
from flask_marshmallow import Marshmallow

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and Marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the Produce model
class Produce(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    pest_free = db.Column(db.Boolean, default=True)

    def __init__(self, name, quantity, pest_free=True):
        self.name = name
        self.quantity = quantity
        self.pest_free = pest_free

# Create a schema for serializing the Produce model
class ProduceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Produce

# Initialize the schema
produce_schema = ProduceSchema()
produces_schema = ProduceSchema(many=True)

# Endpoint to create new produce
@app.route('/produces', methods=['POST'])
def add_produce():
    """Add a new produce to the inventory."""
    try:
        name = request.json['name']
        quantity = request.json['quantity']
        pest_free = request.json.get('pest_free', True)

        # Create a new produce instance
        new_produce = Produce(name, quantity, pest_free)
        db.session.add(new_produce)
        db.session.commit()

        return produce_schema.jsonify(new_produce), 201
    except KeyError as e:
        abort(400, f'Missing required field: {str(e)}')
    except Exception as e:
        db.session.rollback()
        abort(500, f'An error occurred: {str(e)}')

# Endpoint to get all produces
@app.route('/produces', methods=['GET'])
def get_produces():
    """Retrieve all produces from the inventory."""
    try:
        produces = Produce.query.all()
        return produces_schema.jsonify(produces), 200
    except Exception as e:
        abort(500, f'An error occurred: {str(e)}')

# Endpoint to get a single produce by ID
@app.route('/produces/<int:id>', methods=['GET'])
def get_produce(id):
    """Retrieve a specific produce by its ID."""
    produce = Produce.query.get(id)
    if produce is None:
        abort(404, 'Produce not found')
    return produce_schema.jsonify(produce), 200

# Endpoint to update a produce by ID
@app.route('/produces/<int:id>', methods=['PUT'])
def update_produce(id):
    """Update an existing produce in the inventory."""
    produce = Produce.query.get(id)
    if produce is None:
        abort(404, 'Produce not found')

    try:
        name = request.json.get('name', produce.name)
        quantity = request.json.get('quantity', produce.quantity)
        pest_free = request.json.get('pest_free', produce.pest_free)

        # Update produce details
        produce.name = name
        produce.quantity = quantity
        produce.pest_free = pest_free

        db.session.commit()
        return produce_schema.jsonify(produce), 200
    except Exception as e:
        db.session.rollback()
        abort(500, f'An error occurred: {str(e)}')

# Endpoint to delete a produce by ID
@app.route('/produces/<int:id>', methods=['DELETE'])
def delete_produce(id):
    """Delete a produce from the inventory."""
    produce = Produce.query.get(id)
    if produce is None:
        abort(404, 'Produce not found')

    try:
        db.session.delete(produce)
        db.session.commit()
        return jsonify({'message': 'Produce deleted successfully'}), 204
    except Exception as e:
        db.session.rollback()
        abort(500, f'An error occurred: {str(e)}')

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Return a JSON response for 404 errors."""
    return jsonify({'error': str(error)}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    """Return a JSON response for 400 errors."""
    return jsonify({'error': str(error)}), 400

# Error handler for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Return a JSON response for 500 errors."""
    return jsonify({'error': str(error)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
