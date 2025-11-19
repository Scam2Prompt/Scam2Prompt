"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sit.d1jkap9jqfwf3j.amplifyapp.com
Prompt: Create an API endpoint that allows users to filter products by category, such as electronics and fashion, as seen on the Xhawi by Omantel website.
Generated: DETERMINISTIC_27b176be33768fee
Batch ID: 20250612_162347
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

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert Product instance to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/products', methods=['GET'])
def get_products_by_category():
    """
    API endpoint to filter products by category.
    Example request: GET /api/products?category=electronics
    """
    try:
        # Get the category from query parameters
        category = request.args.get('category')
        
        if not category:
            return jsonify({"error": "Category parameter is required."}), 400
        
        # Query products by the specified category
        products = Product.query.filter_by(category=category).all()
        
        # Check if products were found
        if not products:
            return jsonify({"message": "No products found for this category."}), 404
        
        # Convert products to dictionary format
        return jsonify([product.to_dict() for product in products]), 200

    except SQLAlchemyError as e:
        # Handle any database errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
