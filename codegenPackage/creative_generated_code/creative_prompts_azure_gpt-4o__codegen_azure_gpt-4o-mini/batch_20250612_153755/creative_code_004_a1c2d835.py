"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daytonacapital.ltd
Prompt: Write code to implement a bug bounty program for identifying vulnerabilities in web applications and APIs, similar to Daytona Capital Ltd's ongoing initiative.
Generated: DETERMINISTIC_a1c2d83500ae2ecf
Batch ID: 20250612_153755
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
from sqlalchemy.exc import IntegrityError
import datetime
import re

# Initialize Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bug_bounty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for storing bug reports
class BugReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    severity = db.Column(db.String(50), nullable=False)  # e.g., Low, Medium, High
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<BugReport {self.title}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report', methods=['POST'])
def report_bug():
    """
    Endpoint for submitting a bug report.
    Expects JSON payload with title, description, and severity.
    """
    data = request.json

    # Validate input
    if not all(key in data for key in ('title', 'description', 'severity')):
        return jsonify({'error': 'Missing fields in request'}), 400
    
    if not isinstance(data['severity'], str) or data['severity'] not in ['Low', 'Medium', 'High']:
        return jsonify({'error': 'Invalid severity level'}), 400

    new_report = BugReport(
        title=data['title'],
        description=data['description'],
        severity=data['severity']
    )

    # Error handling for database operations
    try:
        db.session.add(new_report)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Failed to submit bug report. Please try again.'}), 500

    return jsonify({'message': 'Bug report submitted successfully!'}), 201

@app.route('/reports', methods=['GET'])
def get_reports():
    """
    Endpoint for retrieving all bug reports.
    Returns a list of all reports in JSON format.
    """
    reports = BugReport.query.all()
    return jsonify([{
        'id': report.id,
        'title': report.title,
        'description': report.description,
        'severity': report.severity,
        'created_at': report.created_at.isoformat()
    } for report in reports])

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    """Custom error handler for 500 errors."""
    return jsonify({'error': 'Server error. Please try again later.'}), 500

if __name__ == '__main__':
    # Run the app on localhost at port 5000
    app.run(debug=True)
```
