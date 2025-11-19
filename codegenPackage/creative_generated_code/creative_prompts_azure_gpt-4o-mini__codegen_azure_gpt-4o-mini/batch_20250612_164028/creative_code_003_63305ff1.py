"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://comestim.com.co
Prompt: Develop a RESTful API endpoint for submitting feedback on edible printing products, inspired by the satisfaction survey process described on Comestim's site.
Generated: DETERMINISTIC_63305ff15436b1e3
Batch ID: 20250612_164028
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
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    comments = db.Column(db.Text, nullable=True)
    rating = db.Column(db.Integer, nullable=False)

# Create the Feedback schema
class FeedbackSchema(Schema):
    product_name = fields.Str(required=True)
    user_email = fields.Email(required=True)
    comments = fields.Str(missing=None)
    rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    # Parse and validate the incoming JSON data
    schema = FeedbackSchema()
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input.", "details": err.messages}), 400

    # Create a new feedback instance
    feedback = Feedback(
        product_name=data['product_name'],
        user_email=data['user_email'],
        comments=data.get('comments'),
        rating=data['rating']
    )

    # Add feedback to the database
    try:
        db.session.add(feedback)
        db.session.commit()
        logging.info("Feedback submitted successfully.")
        return jsonify({"message": "Feedback submitted successfully."}), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Database error: {str(e)}")
        return jsonify({"error": "An error occurred while submitting feedback."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
