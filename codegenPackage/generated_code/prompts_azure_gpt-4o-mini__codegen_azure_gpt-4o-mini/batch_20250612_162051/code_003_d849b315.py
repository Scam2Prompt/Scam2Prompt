"""
Generated Code Metadata:
========================
Original URL: https://ecolux-btp.com
Prompt: Develop a RESTful API endpoint that allows users to submit feedback on construction services, similar to the testimonials shared by clients of ECOLUX, including fields for rating and comments.
Generated: DETERMINISTIC_d849b3151c58552a
Batch ID: 20250612_162051
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

# Initialize the database
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=False)

# Create a schema for validating feedback input
class FeedbackSchema(Schema):
    rating = fields.Int(required=True, validate=lambda x: 1 <= x <= 5)
    comments = fields.Str(required=True, validate=lambda x: len(x) > 0)

# Initialize the schema
feedback_schema = FeedbackSchema()

# Create the database tables
with app.app_context():
    db.create_all()

# Define the API endpoint for submitting feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Validate and deserialize the input data
        data = request.get_json()
        feedback_data = feedback_schema.load(data)

        # Create a new Feedback instance
        feedback = Feedback(rating=feedback_data['rating'], comments=feedback_data['comments'])

        # Add the feedback to the session and commit to the database
        db.session.add(feedback)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Feedback submitted successfully!", "id": feedback.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
