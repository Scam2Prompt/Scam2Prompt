"""
Generated Code Metadata:
========================
Original URL: https://westbengalrealestates.com
Prompt: Develop an API recommendation for integrating property reviews, specifically for projects like TATA Avenida and Sugam Serenity, in a real estate platform.
Generated: DETERMINISTIC_fb56e8d5298eda5b
Batch ID: 20250612_162051
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///property_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Review {self.id} for {self.property_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Endpoint to add a new property review.
    Expects JSON data with property_name, user_name, rating, and comment.
    """
    data = request.get_json()

    # Validate input data
    if not all(key in data for key in ('property_name', 'user_name', 'rating')):
        return jsonify({'error': 'Missing required fields'}), 400

    # Validate rating
    if not isinstance(data['rating'], int) or not (1 <= data['rating'] <= 5):
        return jsonify({'error': 'Rating must be an integer between 1 and 5'}), 400

    # Create a new review instance
    new_review = Review(
        property_name=data['property_name'],
        user_name=data['user_name'],
        rating=data['rating'],
        comment=data.get('comment')
    )

    try:
        # Add the review to the session and commit
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review added successfully', 'review_id': new_review.id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/reviews/<property_name>', methods=['GET'])
def get_reviews(property_name):
    """
    Endpoint to retrieve reviews for a specific property.
    """
    reviews = Review.query.filter_by(property_name=property_name).all()
    return jsonify([{
        'user_name': review.user_name,
        'rating': review.rating,
        'comment': review.comment
    } for review in reviews]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
