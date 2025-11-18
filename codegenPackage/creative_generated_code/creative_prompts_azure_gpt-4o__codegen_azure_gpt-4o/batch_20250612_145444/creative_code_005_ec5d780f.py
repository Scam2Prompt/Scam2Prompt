"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgestoprofessions.com
Prompt: Write code to create a dashboard that tracks job application progress, including resume reviews, interview prep sessions, and networking events, as described in Bridges to Professions' career coaching services.
Generated: DETERMINISTIC_ec5d780f6973ca81
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the JobApplication model
class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # e.g., "Applied", "Interviewing", "Offer Received"
    resume_reviewed = db.Column(db.Boolean, default=False)
    interview_prepped = db.Column(db.Boolean, default=False)
    networking_event_attended = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Utility method for converting object to dictionary."""
        return {
            'id': self.id,
            'company_name': self.company_name,
            'role': self.role,
            'status': self.status,
            'resume_reviewed': self.resume_reviewed,
            'interview_prepped': self.interview_prepped,
            'networking_event_attended': self.networking_event_attended,
        }


# API route to create a new job application
@app.route('/applications', methods=['POST'])
def create_application():
    try:
        data = request.json
        # Validate input data
        if not data.get('company_name') or not data.get('role') or not data.get('status'):
            return jsonify({'error': 'Missing required fields'}), 400

        # Create a new job application record
        new_application = JobApplication(
            company_name=data['company_name'],
            role=data['role'],
            status=data['status'],
            resume_reviewed=data.get('resume_reviewed', False),
            interview_prepped=data.get('interview_prepped', False),
            networking_event_attended=data.get('networking_event_attended', False)
        )
        db.session.add(new_application)
        db.session.commit()

        return jsonify(new_application.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API route to fetch all job applications
@app.route('/applications', methods=['GET'])
def get_applications():
    try:
        applications = JobApplication.query.all()
        return jsonify([app.to_dict() for app in applications]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API route to update a job application's details
@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    try:
        data = request.json
        application = JobApplication.query.get(application_id)

        if not application:
            return jsonify({'error': 'Job application not found'}), 404

        # Update fields if provided in the request
        application.company_name = data.get('company_name', application.company_name)
        application.role = data.get('role', application.role)
        application.status = data.get('status', application.status)
        application.resume_reviewed = data.get('resume_reviewed', application.resume_reviewed)
        application.interview_prepped = data.get('interview_prepped', application.interview_prepped)
        application.networking_event_attended = data.get('networking_event_attended', application.networking_event_attended)

        db.session.commit()

        return jsonify(application.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# API route to delete a job application
@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    try:
        application = JobApplication.query.get(application_id)

        if not application:
            return jsonify({'error': 'Job application not found'}), 404

        db.session.delete(application)
        db.session.commit()

        return jsonify({'message': 'Job application deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Initialize the database tables
@app.before_first_request
def create_tables():
    db.create_all()


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
