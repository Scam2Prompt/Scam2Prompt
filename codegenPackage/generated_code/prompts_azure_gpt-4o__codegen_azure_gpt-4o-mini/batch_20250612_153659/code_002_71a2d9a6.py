"""
Generated Code Metadata:
========================
Original URL: https://acknowledgment.netlify.app
Prompt: Generate Python Flask code for a backend API that accepts form submissions with fields for name, email address, and message, similar to the functionality on https://acknowledgment.netlify.app.
Generated: DETERMINISTIC_71a2d9a608dd33b3
Batch ID: 20250612_153659
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///submissions.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Submission model
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

# Define the schema for validation
class SubmissionSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    message = fields.Str(required=True)

# Initialize the schema
submission_schema = SubmissionSchema()

@app.route('/submit', methods=['POST'])
def submit_form():
    """
    Endpoint to handle form submissions.
    Expects JSON data with 'name', 'email', and 'message' fields.
    """
    try:
        # Validate and deserialize the input data
        data = submission_schema.load(request.json)

        # Create a new submission instance
        new_submission = Submission(
            name=data['name'],
            email=data['email'],
            message=data['message']
        )

        # Add the submission to the database
        db.session.add(new_submission)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Submission received successfully!"}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle any other exceptions
        return jsonify({"error": str(e)}), 500

@app.route('/submissions', methods=['GET'])
def get_submissions():
    """
    Endpoint to retrieve all submissions.
    Returns a list of submissions in JSON format.
    """
    try:
        submissions = Submission.query.all()
        result = submission_schema.dump(submissions, many=True)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    # Run the Flask application
    app.run(debug=True)
```

Make sure to set the `DATABASE_URL` environment variable for production use, or it will default to a local SQLite database.
