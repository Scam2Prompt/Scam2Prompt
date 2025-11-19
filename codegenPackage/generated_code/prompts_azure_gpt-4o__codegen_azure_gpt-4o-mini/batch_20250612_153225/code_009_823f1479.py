"""
Generated Code Metadata:
========================
Original URL: https://highvaluestaffing.com
Prompt: Create a REST API for managing recruitment campaigns, including endpoints for candidate acquisition, job posting, and interview scheduling, similar to High Value Staffing's offerings.
Generated: DETERMINISTIC_823f147999e60d01
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment_campaigns.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Candidate model
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    applied_on = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)

# Define the Interview model
class Interview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidate.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    interview_date = db.Column(db.DateTime, nullable=False)
    candidate = db.relationship('Candidate', backref='interviews')
    job = db.relationship('Job', backref='interviews')

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to add a new candidate
@app.route('/candidates', methods=['POST'])
def add_candidate():
    data = request.get_json()
    if not data or not all(k in data for k in ('name', 'email', 'phone')):
        abort(400, 'Missing candidate information')
    
    new_candidate = Candidate(name=data['name'], email=data['email'], phone=data['phone'])
    db.session.add(new_candidate)
    db.session.commit()
    return jsonify({'id': new_candidate.id}), 201

# Endpoint to get all candidates
@app.route('/candidates', methods=['GET'])
def get_candidates():
    candidates = Candidate.query.all()
    return jsonify([{'id': c.id, 'name': c.name, 'email': c.email, 'phone': c.phone} for c in candidates])

# Endpoint to add a new job posting
@app.route('/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    if not data or not all(k in data for k in ('title', 'description')):
        abort(400, 'Missing job information')
    
    new_job = Job(title=data['title'], description=data['description'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'id': new_job.id}), 201

# Endpoint to get all job postings
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': j.id, 'title': j.title, 'description': j.description} for j in jobs])

# Endpoint to schedule an interview
@app.route('/interviews', methods=['POST'])
def schedule_interview():
    data = request.get_json()
    if not data or not all(k in data for k in ('candidate_id', 'job_id', 'interview_date')):
        abort(400, 'Missing interview information')
    
    new_interview = Interview(candidate_id=data['candidate_id'], job_id=data['job_id'], interview_date=data['interview_date'])
    db.session.add(new_interview)
    db.session.commit()
    return jsonify({'id': new_interview.id}), 201

# Endpoint to get all interviews
@app.route('/interviews', methods=['GET'])
def get_interviews():
    interviews = Interview.query.all()
    return jsonify([{'id': i.id, 'candidate_id': i.candidate_id, 'job_id': i.job_id, 'interview_date': i.interview_date.isoformat()} for i in interviews])

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
