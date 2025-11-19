"""
Generated Code Metadata:
========================
Original URL: https://you-trip.ru
Prompt: Generate a code snippet for a travel booking API that allows users to search for affordable tours to popular destinations like Egypt and Turkey, incorporating filters for ratings and reviews.
Generated: DETERMINISTIC_ea87c017fb64c120
Batch ID: 20250612_164206
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Tour
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviews = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'price': self.price,
            'rating': self.rating,
            'reviews': self.reviews
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to search for affordable tours
@app.route('/api/tours', methods=['GET'])
def search_tours():
    try:
        # Get query parameters
        destination = request.args.get('destination', type=str)
        max_price = request.args.get('max_price', type=float)
        min_rating = request.args.get('min_rating', type=float)

        # Build query
        query = Tour.query

        if destination:
            query = query.filter(Tour.destination.ilike(f'%{destination}%'))
        if max_price is not None:
            query = query.filter(Tour.price <= max_price)
        if min_rating is not None:
            query = query.filter(Tour.rating >= min_rating)

        # Execute query and return results
        tours = query.all()
        return jsonify([tour.to_dict() for tour in tours]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
