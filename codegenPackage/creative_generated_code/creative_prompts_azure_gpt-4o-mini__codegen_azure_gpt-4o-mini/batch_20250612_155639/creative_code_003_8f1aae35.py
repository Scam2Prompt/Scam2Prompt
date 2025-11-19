"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://celestia.top
Prompt: Create a REST API endpoint that allows users to submit their architectural projects for review and feedback through the Études platform.
Generated: DETERMINISTIC_8f1aae35e2cbec39
Batch ID: 20250612_155639
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
from werkzeug.exceptions import BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///projects.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Project model
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitter_email = db.Column(db.String(255), nullable=False)

    def __init__(self, title, description, submitter_email):
        self.title = title
        self.description = description
        self.submitter_email = submitter_email

# Project schema for serialization
class ProjectSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Project

# Initialize the database
with app.app_context():
    db.create_all()

# Route to submit a project
@app.route('/api/projects', methods=['POST'])
def submit_project():
    """
    Submit a new architectural project for review.

    Request body must contain:
    - title: str
    - description: str
    - submitter_email: str
    """
    try:
        # Parse and validate the request JSON
        data = request.get_json()
        if not data:
            raise BadRequest("No input data provided.")

        title = data.get('title')
        description = data.get('description')
        submitter_email = data.get('submitter_email')

        if not title or not description or not submitter_email:
            raise BadRequest("Missing required fields: 'title', 'description', 'submitter_email'.")

        # Create a new project instance
        new_project = Project(title=title, description=description, submitter_email=submitter_email)

        # Add the project to the database
        db.session.add(new_project)
        db.session.commit()

        # Serialize the new project
        project_schema = ProjectSchema()
        return jsonify(project_schema.dump(new_project)), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log unhandled exceptions for further investigation
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
