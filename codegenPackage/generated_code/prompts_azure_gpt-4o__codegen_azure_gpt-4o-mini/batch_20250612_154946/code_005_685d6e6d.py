"""
Generated Code Metadata:
========================
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Create an API endpoint for managing discounts on products, such as "-25% Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Língua Portuguesa," for an e-commerce platform.
Generated: DETERMINISTIC_685d6e6dfdaf8149
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Discount(db.Model):
    """Model for storing discount information."""
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Discount object to a dictionary."""
        return {
            'id': self.id,
            'product_name': self.product_name,
            'discount_percentage': self.discount_percentage
        }

@app.route('/discounts', methods=['POST'])
def create_discount():
    """API endpoint to create a new discount."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'product_name' not in data or 'discount_percentage' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        new_discount = Discount(
            product_name=data['product_name'],
            discount_percentage=data['discount_percentage']
        )
        db.session.add(new_discount)
        db.session.commit()
        return jsonify(new_discount.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/discounts', methods=['GET'])
def get_discounts():
    """API endpoint to retrieve all discounts."""
    try:
        discounts = Discount.query.all()
        return jsonify([discount.to_dict() for discount in discounts]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/discounts/<int:discount_id>', methods=['PUT'])
def update_discount(discount_id):
    """API endpoint to update an existing discount."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'product_name' not in data or 'discount_percentage' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        discount = Discount.query.get_or_404(discount_id)
        discount.product_name = data['product_name']
        discount.discount_percentage = data['discount_percentage']
        db.session.commit()
        return jsonify(discount.to_dict()), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/discounts/<int:discount_id>', methods=['DELETE'])
def delete_discount(discount_id):
    """API endpoint to delete a discount."""
    try:
        discount = Discount.query.get_or_404(discount_id)
        db.session.delete(discount)
        db.session.commit()
        return jsonify({'message': 'Discount deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
