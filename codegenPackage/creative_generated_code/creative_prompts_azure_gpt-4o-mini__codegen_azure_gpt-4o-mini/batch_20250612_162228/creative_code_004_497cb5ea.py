"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mjpa.co.in
Prompt: Illustrate how to implement a RESTful API to manage inventory for various additives and pigments, referencing the product categories from M J Pigment & Additives.
Generated: DETERMINISTIC_497cb5eaab3548c1
Batch ID: 20250612_162228
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
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Additive and Pigment model
class Additive(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

# Database schema for validation using Marshmallow
class AdditiveSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    quantity = fields.Int(required=True)

additive_schema = AdditiveSchema()
additives_schema = AdditiveSchema(many=True)

# Error handling for invalid data
@app.errorhandler(ValidationError)
def handle_validation_error(err):
    return jsonify(err.messages), 400

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Create a new additive
@app.route('/additives', methods=['POST'])
def add_additive():
    try:
        # Validate and deserialize input
        additive_data = additive_schema.load(request.json)
        new_additive = Additive(**additive_data)
        db.session.add(new_additive)
        db.session.commit()
        return additive_schema.jsonify(new_additive), 201
    except Exception as e:
        abort(400, str(e))

# Retrieve all additives
@app.route('/additives', methods=['GET'])
def get_additives():
    all_additives = Additive.query.all()
    return additives_schema.jsonify(all_additives), 200

# Retrieve a specific additive by ID
@app.route('/additives/<int:additive_id>', methods=['GET'])
def get_additive(additive_id):
    additive = Additive.query.get_or_404(additive_id)
    return additive_schema.jsonify(additive), 200

# Update an existing additive
@app.route('/additives/<int:additive_id>', methods=['PUT'])
def update_additive(additive_id):
    additive = Additive.query.get_or_404(additive_id)
    try:
        # Validate and update input
        updated_data = additive_schema.load(request.json)
        for key, value in updated_data.items():
            setattr(additive, key, value)
        db.session.commit()
        return additive_schema.jsonify(additive), 200
    except Exception as e:
        abort(400, str(e))

# Delete an additive
@app.route('/additives/<int:additive_id>', methods=['DELETE'])
def delete_additive(additive_id):
    additive = Additive.query.get_or_404(additive_id)
    db.session.delete(additive)
    db.session.commit()
    return jsonify({'message': 'Additive deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
