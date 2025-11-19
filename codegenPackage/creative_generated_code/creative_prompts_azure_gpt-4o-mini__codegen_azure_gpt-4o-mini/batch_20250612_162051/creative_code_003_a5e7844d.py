"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shravrav1.co.il
Prompt: Develop an API endpoint for a plumbing service that allows users to report issues such as pipe blockages or water leaks, referencing the services provided by the plumbing company in Tel Aviv.
Generated: DETERMINISTIC_a5e7844d1b62b8ad
Batch ID: 20250612_162051
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
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plumbing_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for reporting plumbing issues
class PlumbingIssue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    reported_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<PlumbingIssue {self.issue_type} - {self.id}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report_issue', methods=['POST'])
def report_issue():
    """
    Endpoint to report plumbing issues such as pipe blockages or water leaks.
    Expected JSON payload:
    {
        "issue_type": "string", (e.g., "Pipe Blockage", "Water Leak")
        "description": "string"  (e.g., "Details about the issue")
    }
    """
    try:
        # Parse and validate the JSON request
        data = request.get_json()
        if not data or 'issue_type' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input. 'issue_type' and 'description' are required."}), 400
        
        # Create a new PlumbingIssue instance
        new_issue = PlumbingIssue(issue_type=data['issue_type'], description=data['description'])
        
        # Add to the database
        db.session.add(new_issue)
        db.session.commit()

        return jsonify({"message": "Issue reported successfully!", "issue_id": new_issue.id}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
