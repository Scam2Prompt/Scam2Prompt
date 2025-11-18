"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Suggest an API for managing categorized listings (e.g., "Ξενοδοχεία," "Ταπετσαρίες Επίπλων") and provide example code for adding, updating, and deleting entries.
Generated: DETERMINISTIC_54615154c05359bf
Batch ID: 20250612_151044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and configure the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listings.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Listing model
class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'category': self.category,
            'title': self.title
        }

# Create the database (only needed first time)
with app.app_context():
    db.create_all()

# Route to add a new listing
@app.route('/listings', methods=['POST'])
def add_listing():
    data = request.json
    if 'category' not in data or 'title' not in data:
        abort(400, description="Missing 'category' or 'title' field")
    
    new_listing = Listing(category=data['category'], title=data['title'])
    db.session.add(new_listing)
    db.session.commit()
    return jsonify(new_listing.to_dict()), 201

# Route to update an existing listing
@app.route('/listings/<int:listing_id>', methods=['PUT'])
def update_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing is None:
        abort(404, description="Listing not found")

    data = request.json
    if 'category' in data:
        listing.category = data['category']
    if 'title' in data:
        listing.title = data['title']

    db.session.commit()
    return jsonify(listing.to_dict())

# Route to delete a listing
@app.route('/listings/<int:listing_id>', methods=['DELETE'])
def delete_listing(listing_id):
    listing = Listing.query.get(listing_id)
    if listing is None:
        abort(404, description="Listing not found")

    db.session.delete(listing)
    db.session.commit()
    return jsonify({'message': 'Listing deleted successfully'}), 204

# Route to get all listings
@app.route('/listings', methods=['GET'])
def get_listings():
    listings = Listing.query.all()
    return jsonify([listing.to_dict() for listing in listings])

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

# Error handling for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
