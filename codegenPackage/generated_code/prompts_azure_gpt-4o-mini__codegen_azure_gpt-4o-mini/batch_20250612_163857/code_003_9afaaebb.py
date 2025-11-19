"""
Generated Code Metadata:
========================
Original URL: https://flaviadossantos.co
Prompt: Create a RESTful API endpoint to fetch product information for the "Disney / Pixar's Soul Men's NY Jazz Night Logo Tee."
Generated: DETERMINISTIC_9afaaebbe331198e
Batch ID: 20250612_163857
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Create the database and the Product table
with app.app_context():
    db.create_all()

# Sample data insertion (for demonstration purposes)
def insert_sample_data():
    if Product.query.count() == 0:  # Only insert if the table is empty
        sample_product = Product(
            name="Disney / Pixar's Soul Men's NY Jazz Night Logo Tee",
            description="A stylish tee featuring the NY Jazz Night logo from Disney/Pixar's Soul.",
            price=24.99
        )
        db.session.add(sample_product)
        db.session.commit()

insert_sample_data()

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
    Fetch product information by product ID.

    Args:
        product_id (int): The ID of the product to fetch.

    Returns:
        JSON response containing product information or an error message.
    """
    try:
        product = Product.query.get(product_id)
        if product is None:
            return jsonify({'error': 'Product not found'}), 404
        return jsonify(product.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
