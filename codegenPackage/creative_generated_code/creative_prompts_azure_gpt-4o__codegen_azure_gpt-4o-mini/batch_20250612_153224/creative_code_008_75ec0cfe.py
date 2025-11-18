"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Suggest an API for managing eco-friendly cleaning supply inventory, ensuring the supplies are safe for families and meet professional cleaning standards.
Generated: DETERMINISTIC_75ec0cfe5241d404
Batch ID: 20250612_153224
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_supplies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CleaningSupply model
class CleaningSupply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    safe_for_families = db.Column(db.Boolean, default=True)
    professional_standard = db.Column(db.Boolean, default=True)

# Create the schema for validation
class CleaningSupplySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    safe_for_families = fields.Bool(required=True)
    professional_standard = fields.Bool(required=True)

# Initialize the schema
cleaning_supply_schema = CleaningSupplySchema()
cleaning_supplies_schema = CleaningSupplySchema(many=True)

# Error handler for bad requests
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify(error=str(e)), 500

# Route to create a new cleaning supply
@app.route('/supplies', methods=['POST'])
def add_cleaning_supply():
    try:
        # Validate and deserialize input
        new_supply = cleaning_supply_schema.load(request.json)
        supply = CleaningSupply(**new_supply)
        db.session.add(supply)
        db.session.commit()
        return cleaning_supply_schema.dump(supply), 201
    except ValidationError as err:
        return handle_validation_error(err)

# Route to get all cleaning supplies
@app.route('/supplies', methods=['GET'])
def get_cleaning_supplies():
    supplies = CleaningSupply.query.all()
    return cleaning_supplies_schema.dump(supplies)

# Route to get a specific cleaning supply by id
@app.route('/supplies/<int:supply_id>', methods=['GET'])
def get_cleaning_supply(supply_id):
    supply = CleaningSupply.query.get_or_404(supply_id)
    return cleaning_supply_schema.dump(supply)

# Route to update a cleaning supply
@app.route('/supplies/<int:supply_id>', methods=['PUT'])
def update_cleaning_supply(supply_id):
    supply = CleaningSupply.query.get_or_404(supply_id)
    try:
        # Validate and deserialize input
        updated_supply = cleaning_supply_schema.load(request.json)
        for key, value in updated_supply.items():
            setattr(supply, key, value)
        db.session.commit()
        return cleaning_supply_schema.dump(supply)
    except ValidationError as err:
        return handle_validation_error(err)

# Route to delete a cleaning supply
@app.route('/supplies/<int:supply_id>', methods=['DELETE'])
def delete_cleaning_supply(supply_id):
    supply = CleaningSupply.query.get_or_404(supply_id)
    db.session.delete(supply)
    db.session.commit()
    return '', 204

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
