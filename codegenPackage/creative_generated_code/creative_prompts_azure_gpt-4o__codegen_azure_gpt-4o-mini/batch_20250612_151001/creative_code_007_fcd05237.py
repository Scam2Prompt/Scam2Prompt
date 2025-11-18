"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://junkintheboxatl.com
Prompt: Recommend an API for managing customer reviews and testimonials, like those featured on the Junk In The Box ATL website, and provide an example of how to integrate it into a web application.
Generated: DETERMINISTIC_fcd0523702235f4e
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Customer Reviews
class CustomerReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    review_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'review_text': self.review_text,
            'rating': self.rating
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# API route to create a new review
@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    
    if not all(k in data for k in ('customer_name', 'review_text', 'rating')):
        return jsonify({'error': 'Missing data'}), 400

    try:
        new_review = CustomerReview(
            customer_name=data['customer_name'],
            review_text=data['review_text'],
            rating=data['rating']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to add the review'}), 500

# API route to retrieve all reviews
@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = CustomerReview.query.all()
    return jsonify([review.to_dict() for review in reviews]), 200

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
