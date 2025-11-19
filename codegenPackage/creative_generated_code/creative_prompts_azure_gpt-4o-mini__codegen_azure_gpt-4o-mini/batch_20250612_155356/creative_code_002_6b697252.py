"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://treehousesessions.co.uk
Prompt: Create an API endpoint that allows users to submit feedback on performances at Tree House Sessions, including artist names and performance ratings.
Generated: DETERMINISTIC_6b697252a1f88805
Batch ID: 20250612_155356
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

# Initialize the Flask application
app = Flask(__name__)

# Configurations for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(100), nullable=False)
    performance_rating = db.Column(db.Integer, nullable=False)

# Create a schema for validation using Marshmallow
class FeedbackSchema(Schema):
    artist_name = fields.String(required=True)
    performance_rating = fields.Integer(required=True, validate=lambda x: 1 <= x <= 5)

# Initialize the schema
feedback_schema = FeedbackSchema()

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/feedback', methods=['POST'])
def submit_feedback():
    """
    API endpoint to submit feedback on performances.

    Expects JSON payload with:
    - artist_name: str
    - performance_rating: int (1-5)
    """
    try:
        # Validate input data
        data = request.get_json()
        validated_data = feedback_schema.load(data)

        # Create a new Feedback instance
        new_feedback = Feedback(
            artist_name=validated_data['artist_name'],
            performance_rating=validated_data['performance_rating']
        )

        # Add the feedback to the session and commit
        db.session.add(new_feedback)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Feedback submitted successfully!"}), 201

    except ValidationError as err:
        # Return validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
