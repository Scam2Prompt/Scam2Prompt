"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegladiatorshoes.com
Prompt: Develop a REST API endpoint to retrieve product details from Gladiator Shoes, including certifications like "CE Certified" and industry-specific categories like "automotive" or "building and construction."
Generated: DETERMINISTIC_89788cd3a0c56a35
Batch ID: 20250612_153246
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # example using SQLite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    certifications = db.Column(db.String(150), nullable=True)
    category = db.Column(db.String(150), nullable=True)

    def to_dict(self):
        """Convert the Product instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'certifications': self.certifications,
            'category': self.category
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Retrieve product details by product ID.
    
    Args:
        product_id (int): The ID of the product to retrieve.
    
    Returns:
        JSON response with product details or error message.
    """

    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product not found'}), 404
        
        return jsonify(product.to_dict()), 200

    except SQLAlchemyError as e:
        # Log the error (not shown here for brevity)
        return jsonify({'error': 'Database error occurred'}), 500

@app.route('/api/products', methods=['POST'])
def create_product():
    """
    Create a new product with details.
    
    Returns:
        JSON response with created product details or error message.
    """
    data = request.get_json()
    try:
        new_product = Product(
            name=data['name'],
            certifications=data.get('certifications'),
            category=data.get('category')
        )
        db.session.add(new_product)
        db.session.commit()
        return jsonify(new_product.to_dict()), 201

    except (SQLAlchemyError, KeyError) as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)  # Set to False in production
```
