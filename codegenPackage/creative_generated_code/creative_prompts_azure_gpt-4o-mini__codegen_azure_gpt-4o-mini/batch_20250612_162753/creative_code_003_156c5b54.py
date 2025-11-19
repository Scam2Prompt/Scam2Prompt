"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masscompras.com
Prompt: Develop an API endpoint that returns promotional offers and discounts for products in categories like "Belleza / Spa" and "Deporte," akin to the offers featured on Mass Compras.
Generated: DETERMINISTIC_156c5b54828ecb19
Batch ID: 20250612_162753
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///offers.db'  # Database URI (use appropriate URI in production)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Offer(db.Model):
    """Model representing a promotional offer."""
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    discount_percentage = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Offer object to a dictionary."""
        return {
            'id': self.id,
            'category': self.category,
            'description': self.description,
            'discount_percentage': self.discount_percentage
        }

@app.route('/api/offers', methods=['GET'])
def get_offers():
    """
    API endpoint to retrieve promotional offers for specified categories.
    
    Query parameters:
    - categories: Comma-separated list of categories (e.g., "Belleza/Spa,Deporte").
    
    Returns:
    - JSON response containing a list of offers for the specified categories.
    """
    try:
        categories = request.args.get('categories')
        if not categories:
            return jsonify({"error": "No categories provided"}), 400

        # Split categories and strip whitespace
        category_list = [category.strip() for category in categories.split(',')]
        
        # Query offers for the specified categories
        offers = Offer.query.filter(Offer.category.in_(category_list)).all()
        offers_list = [offer.to_dict() for offer in offers]

        return jsonify(offers_list), 200

    except SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 500

if __name__ == '__main__':
    # Create the database and the tables if they don't exist
    db.create_all()
    app.run(debug=True)  # Set debug to False in production
```
