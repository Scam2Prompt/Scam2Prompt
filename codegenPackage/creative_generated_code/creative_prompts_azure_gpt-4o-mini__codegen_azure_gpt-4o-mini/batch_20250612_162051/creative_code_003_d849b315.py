"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecolux-btp.com
Prompt: Develop a RESTful API endpoint that allows users to submit feedback on construction services, similar to the testimonials shared by clients of ECOLUX, including fields for rating and comments.
Generated: DETERMINISTIC_d849b3151c58552a
Batch ID: 20250612_162051
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
from flask_marshmallow import Marshmallow
from marshmallow import fields, validate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///feedback.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500), nullable=False)

    def __init__(self, rating, comment):
        self.rating = rating
        self.comment = comment

# Feedback schema for serialization
class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

    # Validate fields
    rating = fields.Int(required=True, validate=validate.Range(min=1, max=5))
    comment = fields.Str(required=True, validate=validate.Length(min=1, max=500))

# Initialize the schema
feedback_schema = FeedbackSchema()
feedbacks_schema = FeedbackSchema(many=True)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit feedback
@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get JSON data from request
        json_data = request.get_json()

        # Validate and deserialize data
        feedback_data = feedback_schema.load(json_data)

        # Create a new Feedback instance
        new_feedback = Feedback(**feedback_data)

        # Add and commit to the database
        db.session.add(new_feedback)
        db.session.commit()

        # Return success response
        return feedback_schema.jsonify(new_feedback), 201
    except Exception as e:
        # Rollback in case of error
        db.session.rollback()
        # Return an error response
        return jsonify({"error": str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('DEBUG', 'False').lower() in ('true', '1'))
```
