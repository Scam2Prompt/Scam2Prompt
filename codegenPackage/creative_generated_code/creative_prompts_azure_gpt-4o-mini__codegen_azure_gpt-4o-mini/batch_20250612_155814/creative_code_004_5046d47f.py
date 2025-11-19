"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alphaonsol.net
Prompt: Construct a web application feature that allows users to submit feedback on Authentic Oil's product ideas, integrating their commitment to customer insights and collaboration.
Generated: DETERMINISTIC_5046d47ffac771c7
Batch ID: 20250612_155814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration engine
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Database model for Feedback
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_idea = db.Column(db.String(255), nullable=False)
    user_email = db.Column(db.String(120), nullable=False)
    comments = db.Column(db.Text, nullable=True)

# Schema for validating feedback data
class FeedbackSchema(Schema):
    product_idea = fields.String(required=True, validate=validate.Length(max=255))
    user_email = fields.Email(required=True)
    comments = fields.String(allow_none=True)

# Initialize the schema
feedback_schema = FeedbackSchema()

@app.route('/feedback', methods=['POST'])
def submit_feedback():
    """
    Endpoint to submit user feedback on product ideas.
    Expects JSON with product_idea, user_email, and optional comments.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = feedback_schema.load(data)

        # Create a new feedback entry
        feedback = Feedback(
            product_idea=validated_data['product_idea'],
            user_email=validated_data['user_email'],
            comments=validated_data.get('comments')
        )

        # Add the feedback to the session and commit to the database
        db.session.add(feedback)
        db.session.commit()

        return jsonify({'message': 'Feedback submitted successfully!'}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they do not exist
    with app.app_context():
        db.create_all()
    # Run the application
    app.run(debug=True)
```

### Requirements
- Install Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow to run the application.
- Use the command:
  ```bash
  pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
  ```
- Run the application with:
  ```bash
  python app.py
  ```

### Notes
- The database will be created automatically in the same directory as `feedback.db`.
- You can submit feedback using a tool like Postman or CURL with the appropriate JSON payload.
