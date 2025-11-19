"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecbc.online
Prompt: Create an API endpoint that allows users to submit their own radio program ideas to ECBC Radio, incorporating the submission process outlined in the content.
Generated: DETERMINISTIC_807eb30c0f853801
Batch ID: 20250612_155751
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
import logging

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///programs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the ProgramIdea model
class ProgramIdea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    submitted_by = db.Column(db.String(100), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for input validation using Marshmallow
class ProgramIdeaSchema(Schema):
    title = fields.Str(required=True, validate=lambda s: len(s) > 0)
    description = fields.Str(required=True, validate=lambda s: len(s) > 0)
    submitted_by = fields.Str(required=True, validate=lambda s: len(s) > 0)

# API endpoint to submit a program idea
@app.route('/api/programs/submit', methods=['POST'])
def submit_program():
    # Validate and deserialize input
    try:
        data = request.get_json()
        program_idea_schema = ProgramIdeaSchema()
        validated_data = program_idea_schema.load(data)
    except (ValidationError, TypeError) as e:
        logging.error(f"Input validation error: {str(e)}")
        return jsonify({"error": str(e)}), 400

    # Create a new ProgramIdea instance
    new_program = ProgramIdea(
        title=validated_data['title'],
        description=validated_data['description'],
        submitted_by=validated_data['submitted_by']
    )

    # Add the new program idea to the database
    try:
        db.session.add(new_program)
        db.session.commit()
    except Exception as e:
        logging.error(f"Database error: {str(e)}")
        db.session.rollback()
        return jsonify({"error": "Failed to submit the program idea. Please try again."}), 500

    # Return a success response
    return jsonify({"message": "Program idea submitted successfully!", "id": new_program.id}), 201

# Run the application
if __name__ == '__main__':
    app.run(debug=False)
```
