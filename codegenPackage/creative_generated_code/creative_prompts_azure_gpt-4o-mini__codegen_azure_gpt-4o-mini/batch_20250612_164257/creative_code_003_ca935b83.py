"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://malkeenz.com
Prompt: Develop a RESTful API endpoint for managing customer reviews on jewelry products, inspired by the customer feedback section on Malkeenz's website.
Generated: DETERMINISTIC_ca935b833cab2504
Batch ID: 20250612_164257
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for Customer Reviews
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, nullable=False)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)

# Schema for serializing review data
class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    customer_name = fields.Str(required=True)
    rating = fields.Int(required=True, validate=lambda x: 1 <= x <= 5)
    comment = fields.Str()

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Initialize schema
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

# Create a new review
@app.route('/reviews', methods=['POST'])
def add_review():
    try:
        # Validate incoming data
        data = request.get_json()
        review = review_schema.load(data)

        # Create a new Review instance
        new_review = Review(**review)
        db.session.add(new_review)
        db.session.commit()

        return review_schema.jsonify(new_review), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Get all reviews for a specific product
@app.route('/reviews/<int:product_id>', methods=['GET'])
def get_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).all()
    return reviews_schema.jsonify(reviews)

# Update an existing review
@app.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        abort(404, description="Review not found")

    try:
        data = request.get_json()
        updated_review = review_schema.load(data)

        # Update the review fields
        for key, value in updated_review.items():
            setattr(review, key, value)
        
        db.session.commit()
        return review_schema.jsonify(review)
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete a review
@app.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    if not review:
        abort(404, description="Review not found")

    try:
        db.session.delete(review)
        db.session.commit()
        return jsonify({"message": "Review deleted"}), 204
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
