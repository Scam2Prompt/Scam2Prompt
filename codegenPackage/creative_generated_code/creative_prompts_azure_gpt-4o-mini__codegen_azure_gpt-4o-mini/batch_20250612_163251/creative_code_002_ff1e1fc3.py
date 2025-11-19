"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maderaselaboradas.com.ar
Prompt: Create a RESTful API endpoint for a service that provides information about different types of wood products, including "Maderas duras del Norte Argentino," as mentioned on the Maderas Elaboradas site.
Generated: DETERMINISTIC_ff1e1fc38fd52e1d
Batch ID: 20250612_163251
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (using SQLite for demonstration)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///woods.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Database model for wood products
class WoodProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    origin = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<WoodProduct {self.name}>'

# Schema for serializing wood product data
class WoodProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    origin = fields.Str(required=True)

# Initialize schema instance
wood_product_schema = WoodProductSchema()
wood_products_schema = WoodProductSchema(many=True)

# Create the database and the WoodProduct table
with app.app_context():
    db.create_all()

# API endpoint to get all wood products
@app.route('/api/woods', methods=['GET'])
def get_woods():
    """Retrieve all wood products"""
    woods = WoodProduct.query.all()
    return wood_products_schema.jsonify(woods)

# API endpoint to get a specific wood product by ID
@app.route('/api/woods/<int:wood_id>', methods=['GET'])
def get_wood(wood_id):
    """Retrieve a wood product by its ID"""
    wood = WoodProduct.query.get(wood_id)
    if wood is None:
        abort(404, description=f"Wood product with ID {wood_id} not found.")
    return wood_product_schema.jsonify(wood)

# API endpoint to create a new wood product
@app.route('/api/woods', methods=['POST'])
def create_wood():
    """Create a new wood product"""
    try:
        wood_data = wood_product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_wood = WoodProduct(**wood_data)
    db.session.add(new_wood)
    db.session.commit()
    return wood_product_schema.jsonify(new_wood), 201

# API endpoint to update an existing wood product
@app.route('/api/woods/<int:wood_id>', methods=['PUT'])
def update_wood(wood_id):
    """Update an existing wood product"""
    wood = WoodProduct.query.get(wood_id)
    if wood is None:
        abort(404, description=f"Wood product with ID {wood_id} not found.")

    try:
        wood_data = wood_product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    for key, value in wood_data.items():
        setattr(wood, key, value)

    db.session.commit()
    return wood_product_schema.jsonify(wood)

# API endpoint to delete a wood product
@app.route('/api/woods/<int:wood_id>', methods=['DELETE'])
def delete_wood(wood_id):
    """Delete a wood product"""
    wood = WoodProduct.query.get(wood_id)
    if wood is None:
        abort(404, description=f"Wood product with ID {wood_id} not found.")

    db.session.delete(wood)
    db.session.commit()
    return jsonify({"message": "Wood product deleted successfully."}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
