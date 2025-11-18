"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Create a REST API for managing recruitment campaigns, including endpoints for candidate acquisition, job posting, and interview scheduling, similar to High Value Staffing's offerings.
Generated: DETERMINISTIC_823f147999e60d01
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    resume = db.Column(db.String(200), nullable=False)

# Define the JobPosting model
class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Interview model
class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    job_posting_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'), nullable=False)
    interview_date = db.Column(db.DateTime, nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new candidate
@app.route('/candidates', methods=['POST'])
def create_candidate():
    data = request.get_json()
    new_candidate = Candidate(name=data['name'], email=data['email'], resume=data['resume'])
    db.session.add(new_candidate)
    db.session.commit()
    return jsonify({'message': 'Candidate added', 'id': new_candidate.id}), 201

# Endpoint to list all candidates
@app.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email} for c in candidates]), 200

# Endpoint to add a new job posting
@app.route('/job-postings', methods=['POST'])
def create_job_posting():
    data = request.get_json()
    new_job = JobPosting(title=data['title'], description=data['description'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job posting created', 'id': new_job.id}), 201

# Endpoint to list all job postings
@app.route('/job-postings', methods=['GET'])
def get_job_postings():
    job_postings = JobPosting.query.all()
    return jsonify([{'id': jp.id, 'title': jp.title} for jp in job_postings]), 200

# Endpoint to schedule an interview
@app.route('/interviews', methods=['POST'])
def schedule_interview():
    data = request.get_json()
    if not data.get('candidate_id') or not data.get('job_posting_id') or not data.get('interview_date'):
        abort(400, description="Missing required fields")

    new_interview = Interview(
        candidate_id=data['candidate_id'],
        job_posting_id=data['job_posting_id'],
        interview_date=datetime.fromisoformat(data['interview_date'])
    )
    db.session.add(new_interview)
    db.session.commit()
    return jsonify({'message': 'Interview scheduled', 'id': new_interview.id}), 201

# Endpoint to list all interviews
@app.route('/interviews', methods=['GET'])
def get_interviews():
    interviews = Interview.query.all()
    return jsonify([
        {
            'id': i.id,
            'candidate_id': i.candidate_id,
            'job_posting_id': i.job_posting_id,
            'interview_date': i.interview_date.isoformat()
        } for i in interviews
    ]), 200

# Error handler for 404 errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 400 errors
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
