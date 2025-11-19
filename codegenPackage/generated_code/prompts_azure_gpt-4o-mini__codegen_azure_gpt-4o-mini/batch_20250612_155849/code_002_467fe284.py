"""
Generated Code Metadata:
========================
Original URL: https://blocprest.ro
Prompt: Generate a code snippet for a web application that allows users to report technical issues 24/7, inspired by the support services provided by BlocPrest.
Generated: DETERMINISTIC_467fe28417a8b25b
Batch ID: 20250612_155849
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Issue model
class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Issue {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to report a new issue
@app.route('/report', methods=['POST'])
def report_issue():
    try:
        # Get JSON data from the request
        data = request.get_json()

        # Validate input data
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({'error': 'Title and description are required.'}), 400

        # Create a new issue
        new_issue = Issue(title=data['title'], description=data['description'])
        db.session.add(new_issue)
        db.session.commit()

        # Log the issue reporting
        logging.info(f"Issue reported: {new_issue.title}")

        return jsonify({'message': 'Issue reported successfully!', 'issue_id': new_issue.id}), 201

    except Exception as e:
        logging.error(f"Error reporting issue: {str(e)}")
        return jsonify({'error': 'An error occurred while reporting the issue.'}), 500

# Route to get all reported issues
@app.route('/issues', methods=['GET'])
def get_issues():
    try:
        issues = Issue.query.all()
        return jsonify([{'id': issue.id, 'title': issue.title, 'description': issue.description, 'created_at': issue.created_at} for issue in issues]), 200

    except Exception as e:
        logging.error(f"Error fetching issues: {str(e)}")
        return jsonify({'error': 'An error occurred while fetching issues.'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
