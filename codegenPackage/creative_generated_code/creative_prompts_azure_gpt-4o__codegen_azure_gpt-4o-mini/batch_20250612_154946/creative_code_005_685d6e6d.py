"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Create an API endpoint for managing discounts on products, such as "-25% Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Língua Portuguesa," for an e-commerce platform.
Generated: DETERMINISTIC_685d6e6dfdaf8149
Batch ID: 20250612_154946
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
from sqlalchemy.exc import IntegrityError

# Initialize Flask app and SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db'  # Use SQLite for demonstration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a Discount model
class Discount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'product_name': self.product_name,
            'discount_percentage': self.discount_percentage
        }

# Create the database
with app.app_context():
    db.create_all()

# API endpoint to create a new discount
@app.route('/discounts', methods=['POST'])
def create_discount():
    data = request.get_json()

    # Validate input data
    if not data or 'product_name' not in data or 'discount_percentage' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    product_name = data['product_name']
    discount_percentage = data['discount_percentage']

    # Create new discount record
    new_discount = Discount(product_name=product_name, discount_percentage=discount_percentage)

    try:
        db.session.add(new_discount)
        db.session.commit()
        return jsonify(new_discount.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Discount already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve all discounts
@app.route('/discounts', methods=['GET'])
def get_discounts():
    discounts = Discount.query.all()
    return jsonify([discount.to_dict() for discount in discounts]), 200

# API endpoint to update an existing discount
@app.route('/discounts/<int:discount_id>', methods=['PUT'])
def update_discount(discount_id):
    data = request.get_json()
    discount = Discount.query.get(discount_id)

    if not discount:
        return jsonify({'error': 'Discount not found'}), 404

    if 'product_name' in data:
        discount.product_name = data['product_name']
    if 'discount_percentage' in data:
        discount.discount_percentage = data['discount_percentage']

    try:
        db.session.commit()
        return jsonify(discount.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# API endpoint to delete a discount
@app.route('/discounts/<int:discount_id>', methods=['DELETE'])
def delete_discount(discount_id):
    discount = Discount.query.get(discount_id)

    if not discount:
        return jsonify({'error': 'Discount not found'}), 404

    try:
        db.session.delete(discount)
        db.session.commit()
        return jsonify({'message': 'Discount deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
