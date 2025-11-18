"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a REST API to display CMQLF's eco-friendly packaging options and their associated products, such as "coffrets en bois de peuplier."
Generated: DETERMINISTIC_59c608f2f3c9a0eb
Batch ID: 20250612_151918
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eco_friendly_packaging.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the EcoFriendlyPackaging model
class EcoFriendlyPackaging(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    products = db.relationship('Product', backref='packaging', lazy=True)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    packaging_id = db.Column(db.Integer, db.ForeignKey('eco_friendly_packaging.id'), nullable=False)

# Schema for serializing EcoFriendlyPackaging
class EcoFriendlyPackagingSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    products = fields.List(fields.Str(attribute="name"))

# Initialize schema
packaging_schema = EcoFriendlyPackagingSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to fetch eco-friendly packaging options
@app.route('/api/packaging', methods=['GET'])
def get_packaging_options():
    """Fetch all eco-friendly packaging options along with associated products."""
    try:
        packaging_options = EcoFriendlyPackaging.query.all()
        return jsonify(packaging_schema.dump(packaging_options)), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add new eco-friendly packaging option
@app.route('/api/packaging', methods=['POST'])
def add_packaging_option():
    """Add a new eco-friendly packaging option."""
    try:
        data = request.get_json()
        if not data or 'name' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        new_packaging = EcoFriendlyPackaging(name=data['name'])
        db.session.add(new_packaging)
        db.session.commit()
        return jsonify({'id': new_packaging.id, 'name': new_packaging.name}), 201
    except ValidationError as ve:
        return jsonify({'error': ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route to fetch products under a specific packaging option
@app.route('/api/packaging/<int:packaging_id>/products', methods=['GET'])
def get_products(packaging_id):
    """Fetch products associated with a specific eco-friendly packaging option."""
    try:
        packaging = EcoFriendlyPackaging.query.get_or_404(packaging_id)
        products = [product.name for product in packaging.products]
        return jsonify({'packaging': packaging.name, 'products': products}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
