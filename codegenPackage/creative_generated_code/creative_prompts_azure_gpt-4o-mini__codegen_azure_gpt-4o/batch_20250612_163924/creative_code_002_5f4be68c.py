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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite used for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database object
db = SQLAlchemy(app)

# Define the BusinessListing model
class BusinessListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary key
    name = db.Column(db.String(100), nullable=False)  # Business name
    location = db.Column(db.String(100), nullable=False)  # Business location
    price = db.Column(db.Float, nullable=False)  # Price of the business
    description = db.Column(db.String(500), nullable=True)  # Optional description

    def to_dict(self):
        """
        Convert the model instance to a dictionary for JSON serialization.
        """
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'price': self.price,
            'description': self.description
        }


@app.route('/api/listings', methods=['GET'])
def get_listings():
    """
    API endpoint to retrieve all business listings.
    Filters can be applied via query parameters.
    """
    try:
        location_filter = request.args.get('location')  # Optional filter by location
        max_price = request.args.get('max_price')  # Optional filter by maximum price

        # Base query
        query = BusinessListing.query

        # Apply filters if provided
        if location_filter:
            query = query.filter(BusinessListing.location.ilike(f'%{location_filter}%'))
        if max_price:
            try:
                max_price = float(max_price)
                query = query.filter(BusinessListing.price <= max_price)
            except ValueError:
                return jsonify({'error': 'Invalid max_price value'}), 400

        # Execute the query
        listings = query.all()

        # Convert the results to a list of dictionaries
        results = [listing.to_dict() for listing in listings]

        return jsonify({'listings': results}), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': 'An error occurred', 'details': str(e)}), 500


# Initialize the database (create tables if they don't exist)
with app.app_context():
    db.create_all()

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
