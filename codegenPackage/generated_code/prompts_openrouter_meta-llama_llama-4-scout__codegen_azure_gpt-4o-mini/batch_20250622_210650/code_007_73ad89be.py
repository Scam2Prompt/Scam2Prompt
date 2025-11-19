"""
Generated Code Metadata:
========================
Original URL: https://vaarabella.com
Prompt: "Develop a RESTful API endpoint to handle customer reviews for Vaarabella, allowing users to submit and view reviews for various products."
Generated: DETERMINISTIC_73ad89becbf73832
Batch ID: 20250622_210650
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vaarabella_reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convert the Review object to a dictionary."""
        return {
            'id': self.id,
            'product_id': self.product_id,
            'customer_name': self.customer_name,
            'rating': self.rating,
            'comment': self.comment
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def submit_review():
    """Endpoint to submit a new customer review."""
    data = request.get_json()

    # Validate input data
    if not data or 'product_id' not in data or 'customer_name' not in data or 'rating' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    # Create a new review
    new_review = Review(
        product_id=data['product_id'],
        customer_name=data['customer_name'],
        rating=data['rating'],
        comment=data.get('comment')
    )

    try:
        db.session.add(new_review)
        db.session.commit()
        return jsonify(new_review.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit review, please try again.'}), 500

@app.route('/reviews/<string:product_id>', methods=['GET'])
def get_reviews(product_id):
    """Endpoint to retrieve reviews for a specific product."""
    reviews = Review.query.filter_by(product_id=product_id).all()
    return jsonify([review.to_dict() for review in reviews]), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
