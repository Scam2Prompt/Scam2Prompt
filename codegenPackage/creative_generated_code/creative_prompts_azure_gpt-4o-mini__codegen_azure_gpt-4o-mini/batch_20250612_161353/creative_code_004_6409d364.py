"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Design a RESTful API endpoint for submitting feedback on photography services, including fields for client name, rating, and comments, reflecting the testimonials highlighted on the Perth Real Estate Photography webpage.
Generated: DETERMINISTIC_6409d364c028480f
Batch ID: 20250612_161353
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

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_name = db.Column(db.String(100), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.Text, nullable=True)

# Create a schema for validating feedback data
class FeedbackSchema(Schema):
    client_name = fields.String(required=True)
    rating = fields.Integer(required=True, validate=lambda n: 1 <= n <= 5)
    comments = fields.String(required=False)

# Create the feedback schema instance
feedback_schema = FeedbackSchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Define the POST endpoint for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    # Get the JSON data from the request
    json_data = request.get_json()

    # Validate the input data
    try:
        feedback_data = feedback_schema.load(json_data)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new Feedback instance
    new_feedback = Feedback(
        client_name=feedback_data['client_name'],
        rating=feedback_data['rating'],
        comments=feedback_data.get('comments')
    )

    # Add the feedback to the database
    db.session.add(new_feedback)
    db.session.commit()

    # Return the created feedback as a JSON response
    return jsonify({"message": "Feedback submitted successfully", "feedback": feedback_schema.dump(new_feedback)}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
