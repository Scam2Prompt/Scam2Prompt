"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Suggest tools or APIs to develop an online form submission system for MBA applications, similar to the one described on the SOMTU website.
Generated: DETERMINISTIC_a631062560209d1b
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError
import os

# Initialize Flask application
app = Flask(__name__)

# Configure database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mba_applications.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Application model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    gpa = db.Column(db.Float, nullable=False)
    statement_of_purpose = db.Column(db.Text, nullable=False)

# Define the schema for input validation
class ApplicationSchema(Schema):
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    gpa = fields.Float(required=True)
    statement_of_purpose = fields.Str(required=True)

# Initialize the schema
application_schema = ApplicationSchema()

@app.route('/apply', methods=['POST'])
def apply():
    """
    Endpoint to submit an MBA application.
    Expects a JSON payload with the application details.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = application_schema.load(data)

        # Create a new application instance
        new_application = Application(**validated_data)

        # Add the application to the database
        db.session.add(new_application)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Application submitted successfully!", "id": new_application.id}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({"error": str(e)}), 500

@app.route('/applications', methods=['GET'])
def get_applications():
    """
    Endpoint to retrieve all submitted MBA applications.
    """
    try:
        applications = Application.query.all()
        return jsonify(application_schema.dump(applications, many=True)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Requirements
To run this code, ensure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate marshmallow
```

### Database Setup
Before running the application, initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
``` 

### Environment Variables
Set the `DATABASE_URL` environment variable to configure the database connection string as needed.
