"""
Generated Code Metadata:
========================
Original URL: https://pushd-claim.pages.dev
Prompt: Generate code for a bug bounty program for a blockchain marketplace, similar to Pushd's roadmap stage for incentivizing developers to identify and fix bugs.
Generated: DETERMINISTIC_11cff6205bc7a1ab
Batch ID: 20250612_145923
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Configure database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bug_bounty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the BugReport model
class BugReport(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), default='open')  # open, in_progress, resolved
    reward = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'reward': self.reward
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/bug_reports', methods=['POST'])
def submit_bug_report():
    """Endpoint to submit a new bug report."""
    data = request.json
    try:
        new_report = BugReport(
            title=data['title'],
            description=data['description'],
            reward=data['reward']
        )
        db.session.add(new_report)
        db.session.commit()
        return jsonify(new_report.to_dict()), 201
    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'error': 'Missing required fields'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Database integrity error'}), 500
    except Exception as e:
        logging.error(f'Error submitting bug report: {e}')
        return jsonify({'error': 'An error occurred while submitting the report'}), 500

@app.route('/bug_reports', methods=['GET'])
def get_bug_reports():
    """Endpoint to retrieve all bug reports."""
    reports = BugReport.query.all()
    return jsonify([report.to_dict() for report in reports]), 200

@app.route('/bug_reports/<int:report_id>', methods=['PUT'])
def update_bug_report(report_id):
    """Endpoint to update the status of a bug report."""
    data = request.json
    report = BugReport.query.get(report_id)
    if not report:
        return jsonify({'error': 'Bug report not found'}), 404

    report.status = data.get('status', report.status)
    db.session.commit()
    return jsonify(report.to_dict()), 200

@app.route('/bug_reports/<int:report_id>', methods=['DELETE'])
def delete_bug_report(report_id):
    """Endpoint to delete a bug report."""
    report = BugReport.query.get(report_id)
    if not report:
        return jsonify({'error': 'Bug report not found'}), 404

    db.session.delete(report)
    db.session.commit()
    return jsonify({'message': 'Bug report deleted successfully'}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
