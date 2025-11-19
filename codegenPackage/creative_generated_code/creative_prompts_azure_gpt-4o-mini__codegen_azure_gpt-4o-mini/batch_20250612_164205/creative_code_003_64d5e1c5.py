"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meje.cc
Prompt: Develop a RESTful API endpoint to retrieve the latest deals on MEJE bathroom vessel sinks and smart toilets.
Generated: DETERMINISTIC_64d5e1c5e36d9458
Batch ID: 20250612_164205
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

# Create Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define Deal model
class Deal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        """Convert the Deal object to a dictionary."""
        return {
            'id': self.id,
            'product_type': self.product_type,
            'description': self.description,
            'price': self.price,
            'created_at': self.created_at.isoformat()
        }

# Create the database and the database table
with app.app_context():
    db.create_all()

@app.route('/api/deals/latest', methods=['GET'])
def get_latest_deals():
    """
    Retrieve the latest deals on MEJE bathroom vessel sinks and smart toilets.
    Returns:
        JSON response containing the latest deals or an error message.
    """
    try:
        # Query the latest deals for specific product types
        latest_deals = Deal.query.filter(
            Deal.product_type.in_(["bathroom vessel sink", "smart toilet"])
        ).order_by(Deal.created_at.desc()).limit(10).all()

        # Convert deals to a list of dictionaries
        deals_list = [deal.to_dict() for deal in latest_deals]

        return jsonify(deals_list), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle any other unexpected errors
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
