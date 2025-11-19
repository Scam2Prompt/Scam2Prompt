"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creditu.com.ar
Prompt: Generate a code snippet for an e-commerce application that integrates a financing option for purchasing products like air conditioners and smartphones as described on the Creditu website.
Generated: DETERMINISTIC_c632a5158f23aa9d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Define the FinancingOption model
class FinancingOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    monthly_payment = db.Column(db.Float, nullable=False)
    duration_months = db.Column(db.Integer, nullable=False)

    product = db.relationship('Product', backref=db.backref('financing_options', lazy=True))

# Create the database and tables
with app.app_context():
    db.create_all()

# Route to add a product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    try:
        product = Product(name=data['name'], price=data['price'])
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Product already exists'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a financing option
@app.route('/financing', methods=['POST'])
def add_financing_option():
    data = request.get_json()
    
    try:
        financing_option = FinancingOption(
            product_id=data['product_id'],
            monthly_payment=data['monthly_payment'],
            duration_months=data['duration_months']
        )
        db.session.add(financing_option)
        db.session.commit()
        return jsonify({'message': 'Financing option added successfully'}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Financing option already exists or product does not exist'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get financing options for a product
@app.route('/financing/<int:product_id>', methods=['GET'])
def get_financing_options(product_id):
    options = FinancingOption.query.filter_by(product_id=product_id).all()
    if not options:
        return jsonify({'message': 'No financing options available for this product'}), 404
    return jsonify([{
        'monthly_payment': option.monthly_payment,
        'duration_months': option.duration_months
    } for option in options]), 200

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
