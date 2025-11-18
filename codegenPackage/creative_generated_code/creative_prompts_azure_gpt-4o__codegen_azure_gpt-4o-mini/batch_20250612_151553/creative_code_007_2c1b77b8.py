"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://telltak.com
Prompt: Develop a REST API that allows users to search for accessories like "کابل تایپ سی سامسونگ" or "هندزفری بلوتوث شیائومی" by category, price range, and brand, based on the website's data.
Generated: DETERMINISTIC_2c1b77b837e6723d
Batch ID: 20250612_151553
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

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accessories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Accessories model
class Accessory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Accessory object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price,
            'brand': self.brand
        }

# API endpoint to search accessories
@app.route('/api/accessories/search', methods=['GET'])
def search_accessories():
    try:
        # Get query parameters
        category = request.args.get('category')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        brand = request.args.get('brand')

        # Build query
        query = Accessory.query

        if category:
            query = query.filter(Accessory.category.ilike(f'%{category}%'))
        if min_price is not None:
            query = query.filter(Accessory.price >= min_price)
        if max_price is not None:
            query = query.filter(Accessory.price <= max_price)
        if brand:
            query = query.filter(Accessory.brand.ilike(f'%{brand}%'))

        # Execute query and get results
        accessories = query.all()

        # Return results as JSON
        return jsonify([accessory.to_dict() for accessory in accessories]), 200

    except Exception as e:
        # Handle errors and return a 500 response
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
