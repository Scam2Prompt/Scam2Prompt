"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create an API endpoint that retrieves listings for businesses for sale, including details like location and price, similar to the lighting store listing in São Paulo.
Generated: DETERMINISTIC_5f4be68c7e8fd79e
Batch ID: 20250612_163924
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

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Business Listings
class BusinessListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the BusinessListing object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'price': self.price
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/listings', methods=['GET'])
def get_listings():
    """API endpoint to retrieve business listings."""
    try:
        # Retrieve optional query parameters for filtering
        location_filter = request.args.get('location')
        price_filter = request.args.get('price', type=float)

        # Query the database for listings
        query = BusinessListing.query

        if location_filter:
            query = query.filter(BusinessListing.location.ilike(f'%{location_filter}%'))
        if price_filter:
            query = query.filter(BusinessListing.price <= price_filter)

        listings = query.all()
        return jsonify([listing.to_dict() for listing in listings]), 200

    except SQLAlchemyError as e:
        # Handle SQLAlchemy-specific errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
