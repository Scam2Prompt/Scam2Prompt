"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thepointblank.in
Prompt: Create an API endpoint that retrieves trending MDF art products from a database, including details like price and available variants.
Generated: DETERMINISTIC_66fd54c146853d5a
Batch ID: 20250612_161616
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

app = Flask(__name__)

# Configure the database URI for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mfd_art_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MDF art product model
class MDFArtProduct(db.Model):
    __tablename__ = 'mdf_art_products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    available_variants = db.Column(db.JSON, nullable=False)  # Storing variants as JSON

    def to_dict(self):
        """Convert the product to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'available_variants': self.available_variants
        }

@app.route('/api/trending_products', methods=['GET'])
def get_trending_products():
    """
    API endpoint to retrieve trending MDF art products.
    Returns a JSON response with the details of the products.
    """
    try:
        # Query the database for trending products (example: sorted by price)
        trending_products = MDFArtProduct.query.order_by(MDFArtProduct.price.desc()).all()

        # Serialize the product data
        products_data = [product.to_dict() for product in trending_products]

        return jsonify(products_data), 200

    except SQLAlchemyError as e:
        # Log the error (logging setup not shown here)
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
