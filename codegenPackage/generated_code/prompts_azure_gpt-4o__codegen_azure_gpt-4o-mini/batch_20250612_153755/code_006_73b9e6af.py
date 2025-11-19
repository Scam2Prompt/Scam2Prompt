"""
Generated Code Metadata:
========================
Original URL: https://globalinvest-financial.com
Prompt: Develop a bug bounty program submission form for identifying vulnerabilities in web applications and APIs, inspired by GlobalInvest's active bug bounty program.
Generated: DETERMINISTIC_73b9e6af9420ddff
Batch ID: 20250612_153755
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
from werkzeug.exceptions import BadRequest
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///bug_bounty.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the BugSubmission model
class BugSubmission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    submitted_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<BugSubmission {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/submit', methods=['POST'])
def submit_bug():
    """
    Endpoint to submit a bug report.
    Expects a JSON payload with the following fields:
    - title: str
    - description: str
    - severity: str
    - url: str
    """
    try:
        # Parse the JSON request
        data = request.get_json()

        # Validate the input data
        if not all(key in data for key in ('title', 'description', 'severity', 'url')):
            raise BadRequest("Missing required fields: title, description, severity, url")

        # Create a new bug submission
        new_submission = BugSubmission(
            title=data['title'],
            description=data['description'],
            severity=data['severity'],
            url=data['url']
        )

        # Add the submission to the database
        db.session.add(new_submission)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Bug submission successful", "id": new_submission.id}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
