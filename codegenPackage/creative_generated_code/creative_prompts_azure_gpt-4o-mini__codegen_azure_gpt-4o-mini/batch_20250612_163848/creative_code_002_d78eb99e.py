"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meta-mask-co-wallet.blogspot.com
Prompt: Create an API endpoint for a pizza restaurant that allows users to submit reviews about unique pizza experiences, like those at A Pizza da Mooca.
Generated: DETERMINISTIC_d78eb99e5f963119
Batch ID: 20250612_163848
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
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy ORM
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    pizza_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Review {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/reviews', methods=['POST'])
def submit_review():
    """
    Endpoint to submit a pizza review.
    Expects JSON payload with username, pizza_name, review_text, and rating.
    Returns success message or error message in JSON format.
    """
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not all(key in data for key in ('username', 'pizza_name', 'review_text', 'rating')):
            return jsonify({'error': 'Missing data'}), 400
        
        username = data['username']
        pizza_name = data['pizza_name']
        review_text = data['review_text']
        rating = data['rating']

        # Validate rating
        if not isinstance(rating, int) or rating < 1 or rating > 5:
            return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

        # Create a new review instance
        new_review = Review(username=username, pizza_name=pizza_name, review_text=review_text, rating=rating)
        
        # Add the review to the database
        db.session.add(new_review)
        db.session.commit()

        return jsonify({'message': 'Review submitted successfully!'}), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit review, please try again.'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the app on the specified port
    app.run(debug=True, port=5000)
```
