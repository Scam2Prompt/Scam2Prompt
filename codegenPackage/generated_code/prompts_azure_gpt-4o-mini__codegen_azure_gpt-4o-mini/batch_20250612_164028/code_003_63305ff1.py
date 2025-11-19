"""
Generated Code Metadata:
========================
Original URL: https://comestim.com.co
Prompt: Develop a RESTful API endpoint for submitting feedback on edible printing products, inspired by the satisfaction survey process described on Comestim's site.
Generated: DETERMINISTIC_63305ff15436b1e3
Batch ID: 20250612_164028
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
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)

# Create a schema for validating feedback input
class FeedbackSchema(Schema):
    product_name = fields.Str(required=True)
    rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    comments = fields.Str(required=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    # Parse and validate incoming JSON data
    schema = FeedbackSchema()
    try:
        feedback_data = schema.load(request.json)
    except ValidationError as err:
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400

    # Create a new Feedback instance
    feedback = Feedback(
        product_name=feedback_data['product_name'],
        rating=feedback_data['rating'],
        comments=feedback_data.get('comments')
    )

    # Save feedback to the database
    try:
        db.session.add(feedback)
        db.session.commit()
        logging.info(f"Feedback submitted: {feedback_data}")
        return jsonify({"message": "Feedback submitted successfully"}), 201
    except Exception as e:
        logging.error(f"Database error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Failed to submit feedback"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
