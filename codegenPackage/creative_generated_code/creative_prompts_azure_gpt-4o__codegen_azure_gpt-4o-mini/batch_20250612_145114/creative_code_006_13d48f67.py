"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Suggest an API for integrating customer reviews into a roofing service website, similar to the testimonials displayed on King Roofing's webpage.
Generated: DETERMINISTIC_13d48f67db2031a1
Batch ID: 20250612_145114
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=False)

# Create the Review schema for validation and serialization
class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_name = fields.Str(required=True)
    rating = fields.Int(validate=lambda n: 1 <= n <= 5, required=True)
    comment = fields.Str(required=True)

# Initialize the schema
review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/reviews', methods=['POST'])
def add_review():
    """
    Endpoint to add a new customer review.
    Expects JSON data with customer_name, rating, and comment.
    """
    try:
        # Validate and deserialize input data
        review_data = review_schema.load(request.json)
        # Create a new review instance
        new_review = Review(**review_data)
        # Add the review to the database
        db.session.add(new_review)
        db.session.commit()
        # Serialize the new review and return it
        return review_schema.jsonify(new_review), 201
    except ValidationError as err:
        # Return validation errors if the input data is invalid
        return jsonify(err.messages), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

@app.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Endpoint to retrieve all customer reviews.
    Returns a list of reviews in JSON format.
    """
    try:
        # Query all reviews from the database
        reviews = Review.query.all()
        # Serialize the reviews and return them
        return reviews_schema.jsonify(reviews), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Instructions:
1. Ensure you have Flask, Flask-SQLAlchemy, and Marshmallow installed.
2. Run the code in an environment where you can manage Python packages, and it will create a SQLite database named `reviews.db`.
3. Use tools like Postman or curl to test the API endpoints for adding and retrieving customer reviews.
