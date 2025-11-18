"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Suggest an API for integrating multilingual reviews and ratings into a hotel website, similar to the review section on Hostal Koltin Suchitoto's page.
Generated: DETERMINISTIC_f872c07e1130c0ae
Batch ID: 20250612_152620
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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database model for hotel reviews
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hotel_id = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    comment = db.Column(db.String(500), nullable=False)
    language = db.Column(db.String(5), nullable=False)  # ISO language code

    def to_dict(self):
        """Convert review instance to dictionary."""
        return {
            'id': self.id,
            'hotel_id': self.hotel_id,
            'rating': self.rating,
            'comment': self.comment,
            'language': self.language
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def add_review():
    """API endpoint to add a new review."""
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('hotel_id', 'rating', 'comment', 'language')):
        return jsonify({'error': 'Missing fields'}), 400

    new_review = Review(
        hotel_id=data['hotel_id'],
        rating=data['rating'],
        comment=data['comment'],
        language=data['language']
    )

    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/reviews/<int:hotel_id>', methods=['GET'])
def get_reviews(hotel_id):
    """API endpoint to get reviews by hotel ID."""
    reviews = Review.query.filter_by(hotel_id=hotel_id).all()
    return jsonify([review.to_dict() for review in reviews]), 200

@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """API endpoint to delete a review by ID."""
    review = Review.query.get(review_id)
    if review is None:
        return jsonify({'error': 'Review not found'}), 404

    try:
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted'}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
