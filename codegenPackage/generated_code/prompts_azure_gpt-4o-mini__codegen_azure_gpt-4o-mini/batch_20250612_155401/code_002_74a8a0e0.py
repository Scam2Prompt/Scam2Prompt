"""
Generated Code Metadata:
========================
Original URL: https://meetagreatamerican.com
Prompt: Create a REST API endpoint that allows users to submit their stories to be featured on Meet A Great American, including fields for name, achievements, and a brief biography.
Generated: DETERMINISTIC_74a8a0e0501737bd
Batch ID: 20250612_155401
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stories.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Story model
class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    achievements = db.Column(db.String(255), nullable=False)
    biography = db.Column(db.Text, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Define the schema for input validation
class StorySchema(Schema):
    name = fields.Str(required=True)
    achievements = fields.Str(required=True)
    biography = fields.Str(required=True)

# Initialize the schema
story_schema = StorySchema()

@app.route('/submit_story', methods=['POST'])
def submit_story():
    """
    Endpoint to submit a story.
    Expects a JSON payload with 'name', 'achievements', and 'biography'.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = story_schema.load(data)

        # Create a new Story instance
        new_story = Story(
            name=validated_data['name'],
            achievements=validated_data['achievements'],
            biography=validated_data['biography']
        )

        # Add the new story to the database
        db.session.add(new_story)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Story submitted successfully!", "id": new_story.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
