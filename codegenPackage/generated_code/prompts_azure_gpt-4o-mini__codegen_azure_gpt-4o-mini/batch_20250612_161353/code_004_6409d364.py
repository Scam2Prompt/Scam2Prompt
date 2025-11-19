"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Design a RESTful API endpoint for submitting feedback on photography services, including fields for client name, rating, and comments, reflecting the testimonials highlighted on the Perth Real Estate Photography webpage.
Generated: DETERMINISTIC_6409d364c028480f
Batch ID: 20250612_161353
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
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

# Create a schema for validating feedback input
class FeedbackSchema(Schema):
    client_name = fields.Str(required=True, validate=lambda s: len(s) > 0)
    rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    comments = fields.Str(required=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Define the API endpoint for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    # Parse and validate the incoming JSON data
    schema = FeedbackSchema()
    try:
        feedback_data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new Feedback instance
    new_feedback = Feedback(
        client_name=feedback_data['client_name'],
        rating=feedback_data['rating'],
        comments=feedback_data.get('comments')
    )

    # Add the feedback to the database
    try:
        db.session.add(new_feedback)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Failed to save feedback", "details": str(e)}), 500

    # Return a success response
    return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_data}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
