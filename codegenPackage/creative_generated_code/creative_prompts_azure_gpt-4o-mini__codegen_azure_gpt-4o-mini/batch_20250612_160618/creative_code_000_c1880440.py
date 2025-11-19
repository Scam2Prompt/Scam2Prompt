"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Generate a code snippet for an e-commerce website that implements a zero-waste checkout process for natural cosmetics, similar to the offerings on C'est Moi Qui L'ai Fait Pour Vous.
Generated: DETERMINISTIC_c188044063b2c538
Batch ID: 20250612_160618
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
from flask_marshmallow import Marshmallow
from marshmallow import validates, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and schema
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    eco_friendly = db.Column(db.Boolean, default=True)

# Product Schema
class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product

    @validates('price')
    def validate_price(self, price):
        if price < 0:
            raise ValidationError("Price must be a non-negative value.")

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve all eco-friendly products."""
    products = Product.query.all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products))

@app.route('/checkout', methods=['POST'])
def checkout():
    """Process the checkout for natural cosmetics."""
    try:
        items = request.json.get('items', [])
        total_cost = 0.0
        
        for item in items:
            product = Product.query.get(item['id'])
            if not product or not product.eco_friendly:
                return jsonify({"error": "Invalid product or not eco-friendly"}), 400
            total_cost += product.price * item['quantity']

        return jsonify({"total_cost": total_cost}), 200

    except Exception as e:
        # Log the error (could be to a file, monitoring system, etc.)
        app.logger.error(f"Checkout error: {str(e)}")
        return jsonify({"error": "An error occurred during checkout."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=False for production
```
