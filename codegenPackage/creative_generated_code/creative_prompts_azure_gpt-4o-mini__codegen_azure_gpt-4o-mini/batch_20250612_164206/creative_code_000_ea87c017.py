"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://you-trip.ru
Prompt: Generate a code snippet for a travel booking API that allows users to search for affordable tours to popular destinations like Egypt and Turkey, incorporating filters for ratings and reviews.
Generated: DETERMINISTIC_ea87c017fb64c120
Batch ID: 20250612_164206
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tours.db'  # Example SQLite database
db = SQLAlchemy(app)

# Define the Tour model
class Tour(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    destination = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    reviews_count = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Tour object to dictionary for JSON response."""
        return {
            'id': self.id,
            'destination': self.destination,
            'price': self.price,
            'rating': self.rating,
            'reviews_count': self.reviews_count
        }

# Route to search for affordable tours
@app.route('/api/tours/search', methods=['GET'])
def search_tours():
    """Search for affordable tours with optional filters for destination, rating, and reviews count."""
    try:
        destination = request.args.get('destination', '').strip()
        max_price = request.args.get('max_price', type=float)
        min_rating = request.args.get('min_rating', type=float)
        min_reviews_count = request.args.get('min_reviews_count', type=int)

        # Build the query dynamically based on provided filters
        query = Tour.query

        if destination:
            query = query.filter(Tour.destination.ilike(f'%{destination}%'))  # Case-insensitive match

        if max_price is not None:
            query = query.filter(Tour.price <= max_price)

        if min_rating is not None:
            query = query.filter(Tour.rating >= min_rating)

        if min_reviews_count is not None:
            query = query.filter(Tour.reviews_count >= min_reviews_count)

        # Execute query and get results
        tours = query.all()
        return jsonify([tour.to_dict() for tour in tours]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

# Main function to run the app
if __name__ == '__main__':
    # Create database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```
