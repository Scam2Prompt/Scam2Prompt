"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taiko-t.com
Prompt: Develop a web application for recruitment in the construction industry, tailored to companies like 株式会社タイコーテクノ, with features for job postings and applicant tracking.
Generated: DETERMINISTIC_183d1d1ea1785a73
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import Schema, fields, validate
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company_name = db.Column(db.String(100), nullable=False)

# Define the Applicant model
class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)

# Create a schema for job validation
class JobSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    company_name = fields.String(required=True)

# Create a schema for applicant validation
class ApplicantSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    job_id = fields.Integer(required=True)

# Initialize the schemas
job_schema = JobSchema()
applicant_schema = ApplicantSchema()

# Route to post a new job
@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        data = request.get_json()
        job = job_schema.load(data)
        new_job = Job(**job)
        db.session.add(new_job)
        db.session.commit()
        return jsonify(job_schema.dump(new_job)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify(job_schema.dump(jobs, many=True)), 200

# Route to apply for a job
@app.route('/apply', methods=['POST'])
def apply_job():
    try:
        data = request.get_json()
        applicant = applicant_schema.load(data)
        new_applicant = Applicant(**applicant)
        db.session.add(new_applicant)
        db.session.commit()
        return jsonify(applicant_schema.dump(new_applicant)), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Route to get all applicants for a specific job
@app.route('/jobs/<int:job_id>/applicants', methods=['GET'])
def get_applicants(job_id):
    applicants = Applicant.query.filter_by(job_id=job_id).all()
    return jsonify(applicant_schema.dump(applicants, many=True)), 200

# Run the application
if __name__ == '__main__':
    # Create the database tables if they don't exist
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```

To run this code, ensure you have Flask, Flask-SQLAlchemy, Flask-Migrate, and Marshmallow installed. Set up a virtual environment and run the application. The database will automatically create tables for jobs and applicants on the first run.
