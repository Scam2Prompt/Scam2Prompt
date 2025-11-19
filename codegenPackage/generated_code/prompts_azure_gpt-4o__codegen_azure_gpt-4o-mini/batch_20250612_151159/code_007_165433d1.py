"""
Generated Code Metadata:
========================
Original URL: https://freelistingaustralia.com
Prompt: Create a REST API in Flask that allows users to submit business listings to FreeListingAustralia and retrieve featured listings by category.
Generated: DETERMINISTIC_165433d19266f8df
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the BusinessListing model
class BusinessListing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def to_dict(self):
        """Convert the BusinessListing object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/listings', methods=['POST'])
def create_listing():
    """Create a new business listing."""
    data = request.get_json()
    
    # Validate input data
    if not data or 'name' not in data or 'category' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    new_listing = BusinessListing(
        name=data['name'],
        category=data['category'],
        description=data.get('description')
    )

    try:
        db.session.add(new_listing)
        db.session.commit()
        return jsonify(new_listing.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Listing already exists'}), 409
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/listings', methods=['GET'])
def get_listings():
    """Retrieve featured business listings by category."""
    category = request.args.get('category')
    
    if category:
        listings = BusinessListing.query.filter_by(category=category).all()
    else:
        listings = BusinessListing.query.all()

    return jsonify([listing.to_dict() for listing in listings]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
