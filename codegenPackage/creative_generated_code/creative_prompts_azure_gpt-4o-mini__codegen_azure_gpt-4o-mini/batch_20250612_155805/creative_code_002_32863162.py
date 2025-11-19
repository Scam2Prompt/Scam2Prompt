"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vinescoin.net
Prompt: Create a REST API endpoint that allows users to submit feedback on specialty cooking oils, incorporating the values of quality and sustainability discussed by Authentic Oil.
Generated: DETERMINISTIC_32863162db628f51
Batch ID: 20250612_155805
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

# Initialize Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quality_rating = db.Column(db.Integer, nullable=False)
    sustainability_rating = db.Column(db.Integer, nullable=False)
    comments = db.Column(db.String(500), nullable=True)

# Feedback schema for validation
class FeedbackSchema(Schema):
    quality_rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    sustainability_rating = fields.Int(required=True, validate=lambda n: 1 <= n <= 5)
    comments = fields.Str(missing=None)

# Initialize the feedback schema
feedback_schema = FeedbackSchema()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit feedback on specialty cooking oils.
    Expects a JSON payload with quality and sustainability ratings.
    Returns a success message or error details.
    """
    try:
        # Validate incoming JSON data
        data = request.get_json()
        feedback_data = feedback_schema.load(data)

        # Create a new feedback entry
        feedback = Feedback(
            quality_rating=feedback_data['quality_rating'],
            sustainability_rating=feedback_data['sustainability_rating'],
            comments=feedback_data.get('comments')
        )
        db.session.add(feedback)
        db.session.commit()

        return jsonify({"message": "Feedback submitted successfully."}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
