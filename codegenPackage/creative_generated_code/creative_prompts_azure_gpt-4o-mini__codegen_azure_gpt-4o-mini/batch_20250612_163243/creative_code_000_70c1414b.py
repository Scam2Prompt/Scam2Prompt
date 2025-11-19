"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://acula.com.ua
Prompt: Generate a code snippet for an e-commerce website that allows users to filter diving gear by category, such as wetsuits, fins, and masks, similar to the product categorization found on acula.com.ua.
Generated: DETERMINISTIC_70c1414bdad66f4f
Batch ID: 20250612_163243
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

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    """Model representing a diving gear product."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category
        }

@app.route('/products', methods=['GET'])
def get_products():
    """Retrieve products filtered by category."""
    category = request.args.get('category')
    try:
        if category:
            products = Product.query.filter_by(category=category).all()
        else:
            products = Product.query.all()
        
        return jsonify([product.to_dict() for product in products]), 200
        
    except Exception as e:
        # Error handling for unexpected issues
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database and tables if they don't exist
    with app.app_context():
        db.create_all()
    # Start the Flask web server
    app.run(debug=True)
```

### Notes:
- This code sets up a basic Flask application with SQLite as the database.
- It defines a `Product` model with fields for `id`, `name`, and `category`.
- The `/products` endpoint allows filtering products by category using a query parameter.
- Proper error handling is included to manage unexpected exceptions.
