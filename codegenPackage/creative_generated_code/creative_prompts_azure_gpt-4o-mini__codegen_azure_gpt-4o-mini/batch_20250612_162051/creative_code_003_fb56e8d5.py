"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://westbengalrealestates.com
Prompt: Develop an API recommendation for integrating property reviews, specifically for projects like TATA Avenida and Sugam Serenity, in a real estate platform.
Generated: DETERMINISTIC_fb56e8d5298eda5b
Batch ID: 20250612_162051
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

# Configure the database (using SQLite for demonstration; replace with your DB of choice)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///realestate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the PropertyReview model
class PropertyReview(db.Model):
    __tablename__ = 'property_reviews'

    id = db.Column(db.Integer, primary_key=True)
    property_name = db.Column(db.String(100), nullable=False)
    user_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)  # Rating from 1 to 5
    comment = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<PropertyReview {self.property_name} - {self.rating}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a property review
@app.route('/api/reviews', methods=['POST'])
def submit_review():
    """
    Submits a review for a property.
    
    Request JSON format:
    {
        "property_name": "string",
        "user_name": "string",
        "rating": integer (1-5),
        "comment": "string"
    }
    """
    data = request.get_json()

    # Validate input data
    if not data or not all(key in data for key in ('property_name', 'user_name', 'rating')):
        return jsonify({"error": "Invalid input data"}), 400

    if data['rating'] < 1 or data['rating'] > 5:
        return jsonify({"error": "Rating must be between 1 and 5"}), 400

    new_review = PropertyReview(
        property_name=data['property_name'],
        user_name=data['user_name'],
        rating=data['rating'],
        comment=data.get('comment', '')
    )

    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify({"message": "Review submitted successfully", "review_id": new_review.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Failed to submit review, please try again."}), 500

# Endpoint to get reviews for a specific property
@app.route('/api/reviews/<property_name>', methods=['GET'])
def get_reviews(property_name):
    """
    Retrieves all reviews for a specified property.
    
    URL parameter:
    - property_name: The name of the property to get reviews for
    """
    reviews = PropertyReview.query.filter_by(property_name=property_name).all()
    reviews_data = [
        {
            "user_name": review.user_name,
            "rating": review.rating,
            "comment": review.comment
        } for review in reviews
    ]
    
    return jsonify(reviews_data), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
