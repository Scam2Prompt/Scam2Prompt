"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homlukkkkkkkkh.pages.dev
Prompt: Create a REST API that allows users to search for products in categories like "Food colorings" and "Cake packaging" from Condi Shop and retrieve details such as price and availability.
Generated: DETERMINISTIC_f84527d7efb7d5f5
Batch ID: 20250612_151343
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

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///condi_shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    availability = db.Column(db.Boolean, default=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'availability': self.availability
        }

# Route to search for products by category
@app.route('/api/products', methods=['GET'])
def search_products():
    # Get the 'category' query parameter
    category = request.args.get('category')
    
    if not category:
        return jsonify({"error": "Category parameter is required"}), 400

    try:
        # Query products based on the category
        products = Product.query.filter_by(category=category).all()
        # Serialize the product details
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

# Create the database and tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Instructions for Running the Code:
1. Make sure you have Flask and SQLAlchemy installed. You can install them using:
   ```bash
   pip install Flask Flask-SQLAlchemy
   ```
2. Create a SQLite database file named `condi_shop.db` or modify the database URI as needed.
3. Populate the database with sample data for testing.
4. Run the application using:
   ```bash
   python app.py
   ```
5. Make GET requests to `/api/products?category=Food colorings` or `/api/products?category=Cake packaging` to retrieve product details.
