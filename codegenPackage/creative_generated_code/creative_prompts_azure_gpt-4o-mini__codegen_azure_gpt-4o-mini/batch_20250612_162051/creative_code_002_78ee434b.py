"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.matinshop.dk
Prompt: Create an API endpoint that allows users to search for men's grooming products, specifically focusing on natural ingredients like jojoba and argan oil as highlighted on Matin Shop.
Generated: DETERMINISTIC_78ee434b398ba4dd
Batch ID: 20250612_162051
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

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///grooming_products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Product model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        """Convert Product object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'ingredients': self.ingredients
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/products/search', methods=['GET'])
def search_products():
    """
    API endpoint to search for men's grooming products
    based on natural ingredients like jojoba and argan oil.
    Query parameters:
    - ingredient: str (the ingredient to search for)
    """
    ingredient = request.args.get('ingredient', '').lower()

    if not ingredient:
        return jsonify({'error': 'No ingredient provided'}), 400

    try:
        # Query the database for products containing the specified ingredient
        products = Product.query.filter(Product.ingredients.ilike(f'%{ingredient}%')).all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # If a database error occurs, log it and return an error response
        app.logger.error(f"Database error: {str(e)}")
        return jsonify({'error': 'Database error occurred'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
