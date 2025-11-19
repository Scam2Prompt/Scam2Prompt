"""
Generated Code Metadata:
========================
Original URL: https://theneuraluniverse.com
Prompt: Create an API endpoint that allows users to submit their experiences related to neurosurgery, inspired by the content on The Neural Universe.
Generated: DETERMINISTIC_a2755fd275f1657e
Batch ID: 20250612_162203
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

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///neurosurgery_experiences.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Experience model
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    experience_text = db.Column(db.Text, nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ExperienceSchema(Schema):
    user_name = fields.Str(required=True, validate=lambda s: len(s) > 0)
    experience_text = fields.Str(required=True, validate=lambda s: len(s) > 0)

# Initialize the schema
experience_schema = ExperienceSchema()

@app.route('/api/experiences', methods=['POST'])
def submit_experience():
    """
    API endpoint to submit a neurosurgery experience.
    Expects a JSON payload with 'user_name' and 'experience_text'.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = experience_schema.load(data)

        # Create a new Experience instance
        new_experience = Experience(
            user_name=validated_data['user_name'],
            experience_text=validated_data['experience_text']
        )

        # Add to the session and commit to the database
        db.session.add(new_experience)
        db.session.commit()

        # Return success response
        return jsonify({"message": "Experience submitted successfully!", "id": new_experience.id}), 201

    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Invalid input", "messages": err.messages}), 400

    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
