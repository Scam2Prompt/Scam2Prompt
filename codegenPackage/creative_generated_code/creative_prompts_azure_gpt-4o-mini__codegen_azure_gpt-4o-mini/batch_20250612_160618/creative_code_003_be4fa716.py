"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Suggest a REST API design for a cosmetics store that includes features for tracking eco-friendly products and DIY kits, inspired by the offerings at C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_be4fa716b1a97750
Batch ID: 20250612_160618
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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cosmetics_store.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Eco-Friendly Products
class EcoFriendlyProduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    is_eco_friendly = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_eco_friendly': self.is_eco_friendly
        }

# Model for DIY Kits
class DIYKit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients.split(',')
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all eco-friendly products
@app.route('/api/eco-friendly-products', methods=['GET'])
def get_eco_friendly_products():
    products = EcoFriendlyProduct.query.all()
    return jsonify([product.to_dict() for product in products])

# Route to add a new eco-friendly product
@app.route('/api/eco-friendly-products', methods=['POST'])
def add_eco_friendly_product():
    data = request.get_json()
    if not data or not 'name' in data or not 'description' in data:
        abort(400, description='Invalid input')

    new_product = EcoFriendlyProduct(name=data['name'], description=data['description'])
    db.session.add(new_product)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description='Product already exists')
    
    return jsonify(new_product.to_dict()), 201

# Route to get all DIY kits
@app.route('/api/diy-kits', methods=['GET'])
def get_diy_kits():
    kits = DIYKit.query.all()
    return jsonify([kit.to_dict() for kit in kits])

# Route to add a new DIY kit
@app.route('/api/diy-kits', methods=['POST'])
def add_diy_kit():
    data = request.get_json()
    if not data or not 'name' in data or not 'ingredients' in data:
        abort(400, description='Invalid input')

    new_kit = DIYKit(name=data['name'], ingredients=data['ingredients'])
    db.session.add(new_kit)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(400, description='Kit already exists')
    
    return jsonify(new_kit.to_dict()), 201

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
