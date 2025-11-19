"""
Generated Code Metadata:
========================
Original URL: https://blacksabbathmerch.com
Prompt: Create a RESTful API endpoint to retrieve a list of Black Sabbath merchandise products by category (e.g., t-shirts, hoodies, etc.) and write a sample API request and response.
Generated: DETERMINISTIC_b5b493f375ccf0ab
Batch ID: 20250622_212908
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///merchandise.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Merchandise model
class Merchandise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Merchandise object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'price': self.price
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/merchandise', methods=['GET'])
def get_merchandise_by_category():
    """Retrieve a list of merchandise products by category."""
    category = request.args.get('category')

    if not category:
        return jsonify({'error': 'Category parameter is required.'}), 400

    try:
        # Query the database for merchandise in the specified category
        products = Merchandise.query.filter_by(category=category).all()
        return jsonify([product.to_dict() for product in products]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Sample API Request
```
GET /api/merchandise?category=t-shirts
```

### Sample API Response
```json
[
    {
        "id": 1,
        "name": "Black Sabbath Logo T-Shirt",
        "category": "t-shirts",
        "price": 19.99
    },
    {
        "id": 2,
        "name": "Vintage Black Sabbath T-Shirt",
        "category": "t-shirts",
        "price": 24.99
    }
]
```
