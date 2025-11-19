"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mycoastalroofing.com
Prompt: Develop a RESTful API endpoint for submitting customer reviews for Coastal Roofing & Waterproofing's roofing services.
Generated: DETERMINISTIC_8b111fe2817f8c4c
Batch ID: 20250612_161700
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
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy part of the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Review model
class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=True)

# Create the Review schema for validation and serialization
class ReviewSchema(Schema):
    customer_name = fields.String(required=True)
    rating = fields.Integer(required=True, validate=lambda n: 1 <= n <= 5)
    comment = fields.String()

# Initialize the schema
review_schema = ReviewSchema()

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Define the API endpoint for submitting reviews
@app.route('/api/reviews', methods=['POST'])
def submit_review():
    # Parse the incoming JSON data
    json_data = request.get_json()
    
    # Validate the data using the schema
    try:
        data = review_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new review instance
    new_review = Review(
        customer_name=data['customer_name'],
        rating=data['rating'],
        comment=data.get('comment')
    )

    # Add the review to the session and commit
    try:
        db.session.add(new_review)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

    # Return a success response
    return jsonify({"message": "Review submitted successfully.", "review": review_schema.dump(new_review)}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```

This code sets up a Flask web application with an SQLite database to store customer reviews for Coastal Roofing & Waterproofing. It handles incoming JSON data, validates it, and provides appropriate error handling. The application includes comments for clarity and follows best practices in Python programming.
