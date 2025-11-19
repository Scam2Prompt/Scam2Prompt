"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://childnepal.org
Prompt: Design a mobile app that encourages community participation in child rights issues, inspired by Child Nepal's strategies.
Generated: DETERMINISTIC_c5494b699afa7ba4
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for building a mobile app
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///child_rights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the ChildRightsIssue model for the database
class ChildRightsIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

# Schema for validating input data
class ChildRightsIssueSchema(Schema):
    title = fields.Str(required=True)
    description = fields.Str(required=True)

# Initialize the schema
issue_schema = ChildRightsIssueSchema()
issues_schema = ChildRightsIssueSchema(many=True)

# Endpoint to create a new child rights issue
@app.route('/issues', methods=['POST'])
def create_issue():
    """
    Create a new child rights issue.
    Expects JSON with 'title' and 'description'.
    """
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = issue_schema.load(data)
        
        # Create a new issue instance
        new_issue = ChildRightsIssue(**validated_data)
        
        # Add the issue to the session and commit to the database
        db.session.add(new_issue)
        db.session.commit()
        
        return issue_schema.jsonify(new_issue), 201  # Return the created issue
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return general errors

# Endpoint to get all child rights issues
@app.route('/issues', methods=['GET'])
def get_issues():
    """
    Retrieve all child rights issues.
    """
    try:
        issues = ChildRightsIssue.query.all()
        return issues_schema.jsonify(issues), 200  # Return the list of issues
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return general errors

# Endpoint to get a specific child rights issue by ID
@app.route('/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    """
    Retrieve a specific child rights issue by its ID.
    """
    try:
        issue = ChildRightsIssue.query.get_or_404(issue_id)
        return issue_schema.jsonify(issue), 200  # Return the issue
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Return general errors

# Initialize the database
@app.before_first_request
def create_tables():
    """
    Create database tables before the first request.
    """
    db.create_all()

# Run the application
if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
