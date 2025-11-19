"""
Generated Code Metadata:
========================
Original URL: https://ecbc.online
Prompt: Create an API endpoint that allows users to submit their own radio program ideas to ECBC Radio, incorporating the submission process outlined in the content.
Generated: DETERMINISTIC_807eb30c0f853801
Batch ID: 20250612_155751
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///radio_programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the ProgramIdea model
class ProgramIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    submitted_by = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class ProgramIdeaSchema(Schema):
    title = fields.Str(required=True, validate=lambda s: len(s) > 0)
    description = fields.Str(required=True, validate=lambda s: len(s) > 0)
    submitted_by = fields.Str(required=True, validate=lambda s: len(s) > 0)

# Initialize the schema
program_idea_schema = ProgramIdeaSchema()

@app.route('/api/program_ideas', methods=['POST'])
def submit_program_idea():
    """
    API endpoint to submit a new radio program idea.
    Expects a JSON payload with title, description, and submitted_by fields.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = program_idea_schema.load(data)

        # Create a new ProgramIdea instance
        new_idea = ProgramIdea(
            title=validated_data['title'],
            description=validated_data['description'],
            submitted_by=validated_data['submitted_by']
        )

        # Add the new idea to the database
        db.session.add(new_idea)
        db.session.commit()

        # Log the successful submission
        logging.info(f"New program idea submitted: {new_idea.title} by {new_idea.submitted_by}")

        # Return a success response
        return jsonify({"message": "Program idea submitted successfully!", "id": new_idea.id}), 201

    except ValidationError as err:
        # Handle validation errors
        logging.error(f"Validation error: {err.messages}")
        return jsonify({"error": "Validation error", "messages": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
