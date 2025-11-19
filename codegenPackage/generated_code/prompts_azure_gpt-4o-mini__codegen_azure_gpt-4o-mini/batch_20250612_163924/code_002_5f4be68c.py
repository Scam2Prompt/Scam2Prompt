"""
Generated Code Metadata:
========================
Original URL: https://passandbrazzz.blogspot.com
Prompt: Create an API endpoint that retrieves listings for businesses for sale, including details like location and price, similar to the lighting store listing in São Paulo.
Generated: DETERMINISTIC_5f4be68c7e8fd79e
Batch ID: 20250612_163924
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

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Business model
class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Business object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'price': self.price
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/businesses', methods=['GET'])
def get_businesses():
    """API endpoint to retrieve all businesses for sale."""
    try:
        # Retrieve all business listings from the database
        businesses = Business.query.all()
        return jsonify([business.to_dict() for business in businesses]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

@app.route('/api/businesses/<int:business_id>', methods=['GET'])
def get_business(business_id):
    """API endpoint to retrieve a specific business by ID."""
    try:
        # Retrieve the business by ID
        business = Business.query.get_or_404(business_id)
        return jsonify(business.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
