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
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import logging
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issue_reports.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database model for issue reports
class IssueReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    issue_title = db.Column(db.String(200), nullable=False)
    issue_description = db.Column(db.Text, nullable=False)
    urgency_level = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='Open')

    def to_dict(self):
        return {
            'id': self.id,
            'user_name': self.user_name,
            'user_email': self.user_email,
            'issue_title': self.issue_title,
            'issue_description': self.issue_description,
            'urgency_level': self.urgency_level,
            'timestamp': self.timestamp.isoformat(),
            'status': self.status
        }

# Create database tables
with app.app_context():
    db.create_all()

# Error handler
@app.errorhandler(Exception)
def handle_error(e):
    code = 500
    if isinstance(e, HTTPException):
        code = e.code
    logger.error(f"Error: {str(e)}")
    return jsonify(error=str(e)), code

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/report', methods=['POST'])
def report_issue():
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['user_name', 'user_email', 'issue_title', 'issue_description', 'urgency_level']
        for field in required_fields:
            if field not in data or not data[field]:
                return jsonify({'error': f'Missing required field: {field}'}), 400
        
        # Create new issue report
        new_report = IssueReport(
            user_name=data['user_name'],
            user_email=data['user_email'],
            issue_title=data['issue_title'],
            issue_description=data['issue_description'],
            urgency_level=data['urgency_level']
        )
        
        db.session.add(new_report)
        db.session.commit()
        
        logger.info(f"New issue reported by {data['user_email']}: {data['issue_title']}")
        return jsonify(new_report.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error reporting issue: {str(e)}")
        return jsonify({'error': 'Failed to report issue'}), 500

@app.route('/api/issues', methods=['GET'])
def get_issues():
    try:
        issues = IssueReport.query.order_by(IssueReport.timestamp.desc()).all()
        return jsonify([issue.to_dict() for issue in issues]), 200
    except Exception as e:
        logger.error(f"Error fetching issues: {str(e)}")
        return jsonify({'error': 'Failed to fetch issues'}), 500

@app.route('/api/issues/<int:issue_id>', methods=['GET'])
def get_issue(issue_id):
    try:
        issue = IssueReport.query.get_or_404(issue_id)
        return jsonify(issue.to_dict()), 200
    except Exception as e:
        logger.error(f"Error fetching issue {issue_id}: {str(e)}")
        return jsonify({'error': 'Issue not found'}), 404

@app.route('/api/issues/<int:issue_id>/status', methods=['PUT'])
def update_issue_status(issue_id):
    try:
        data = request.get_json()
        if 'status' not in data:
            return jsonify({'error': 'Missing status field'}), 400
            
        issue = IssueReport.query.get_or_404(issue_id)
        issue.status = data['status']
        db.session.commit()
        
        logger.info(f"Updated status for issue {issue_id} to {data['status']}")
        return jsonify(issue.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error updating issue {issue_id}: {str(e)}")
        return jsonify({'error': 'Failed to update issue'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```
