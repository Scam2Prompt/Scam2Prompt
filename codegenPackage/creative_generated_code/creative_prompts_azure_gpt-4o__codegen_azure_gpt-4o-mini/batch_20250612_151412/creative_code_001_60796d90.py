"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Recommend an API for managing product discounts on a website selling replica championship belts, such as AEW Women’s World Championship Replica Title Belt and MLB Title Belts.
Generated: DETERMINISTIC_60796d9039d7fa84
Batch ID: 20250612_151412
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///discounts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Discount(db.Model):
    """Model for storing discount information."""
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

    def serialize(self):
        """Convert the model instance to a JSON serializable dict."""
        return {
            'id': self.id,
            'product_name': self.product_name,
            'discount_percentage': self.discount_percentage
        }

@app.route('/discounts', methods=['POST'])
def create_discount():
    """Create a new discount entry."""
    data = request.json
    product_name = data.get('product_name')
    discount_percentage = data.get('discount_percentage')

    if not product_name or not isinstance(discount_percentage, (int, float)):
        return jsonify({'error': 'Invalid input'}), 400

    try:
        new_discount = Discount(product_name=product_name, discount_percentage=discount_percentage)
        db.session.add(new_discount)
        db.session.commit()
        return jsonify(new_discount.serialize()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/discounts/<int:discount_id>', methods=['GET'])
def get_discount(discount_id):
    """Retrieve a discount by its ID."""
    discount = Discount.query.get(discount_id)
    if discount is None:
        return jsonify({'error': 'Discount not found'}), 404
    return jsonify(discount.serialize()), 200

@app.route('/discounts/<int:discount_id>', methods=['PUT'])
def update_discount(discount_id):
    """Update an existing discount entry."""
    discount = Discount.query.get(discount_id)
    if discount is None:
        return jsonify({'error': 'Discount not found'}), 404
    
    data = request.json
    discount_percentage = data.get('discount_percentage')

    if discount_percentage is not None and isinstance(discount_percentage, (int, float)):
        try:
            discount.discount_percentage = discount_percentage
            db.session.commit()
            return jsonify(discount.serialize()), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/discounts/<int:discount_id>', methods=['DELETE'])
def delete_discount(discount_id):
    """Delete a discount entry."""
    discount = Discount.query.get(discount_id)
    if discount is None:
        return jsonify({'error': 'Discount not found'}), 404

    try:
        db.session.delete(discount)
        db.session.commit()
        return jsonify({'message': 'Discount deleted successfully'}), 204
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```
