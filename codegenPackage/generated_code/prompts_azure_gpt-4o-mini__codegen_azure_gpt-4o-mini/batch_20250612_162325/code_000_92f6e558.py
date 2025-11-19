"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a code snippet for a web application that allows users to create their own cosmetic brand using the full-service project model described by Fabricare Cosméticos.
Generated: DETERMINISTIC_92f6e558e446265f
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cosmetic_brands.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the CosmeticBrand model
class CosmeticBrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    owner_name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<CosmeticBrand {self.name}>'

# Create a schema for validation
class CosmeticBrandSchema(Schema):
    name = fields.Str(required=True)
    description = fields.Str(required=False)
    owner_name = fields.Str(required=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Route to create a new cosmetic brand
@app.route('/api/brands', methods=['POST'])
def create_brand():
    # Validate and deserialize input
    schema = CosmeticBrandSchema()
    try:
        brand_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new brand instance
    new_brand = CosmeticBrand(
        name=brand_data['name'],
        description=brand_data.get('description'),
        owner_name=brand_data['owner_name']
    )

    # Add the new brand to the database
    try:
        db.session.add(new_brand)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Brand created successfully", "brand": brand_data}), 201

# Route to get all cosmetic brands
@app.route('/api/brands', methods=['GET'])
def get_brands():
    brands = CosmeticBrand.query.all()
    brand_schema = CosmeticBrandSchema(many=True)
    return jsonify(brand_schema.dump(brands)), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
