"""
Generated Code Metadata:
========================
Original URL: https://rayatrecruitment.com
Prompt: Design a RESTful API to manage job postings and applications on the Rayat Shikshan Sanstha website, including endpoints for creating, reading, updating, and deleting job postings and applications.
Generated: DETERMINISTIC_1570fbf110600592
Batch ID: 20250622_212131
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job Posting Model
class JobPosting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    company = db.Column(db.String(100), nullable=False)

# Application Model
class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job_posting.id'), nullable=False)
    applicant_name = db.Column(db.String(100), nullable=False)
    resume = db.Column(db.String(500), nullable=False)

# Job Posting Schema
class JobPostingSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    company = fields.Str(required=True)

# Application Schema
class ApplicationSchema(Schema):
    id = fields.Int(dump_only=True)
    job_id = fields.Int(required=True)
    applicant_name = fields.Str(required=True)
    resume = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a job posting
@app.route('/job_postings', methods=['POST'])
def create_job_posting():
    try:
        job_data = request.get_json()
        job_schema = JobPostingSchema()
        job = job_schema.load(job_data)
        new_job = JobPosting(**job)
        db.session.add(new_job)
        db.session.commit()
        return job_schema.dump(new_job), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all job postings
@app.route('/job_postings', methods=['GET'])
def get_job_postings():
    jobs = JobPosting.query.all()
    job_schema = JobPostingSchema(many=True)
    return job_schema.dump(jobs), 200

# Endpoint to get a specific job posting
@app.route('/job_postings/<int:job_id>', methods=['GET'])
def get_job_posting(job_id):
    job = JobPosting.query.get_or_404(job_id)
    job_schema = JobPostingSchema()
    return job_schema.dump(job), 200

# Endpoint to update a job posting
@app.route('/job_postings/<int:job_id>', methods=['PUT'])
def update_job_posting(job_id):
    try:
        job_data = request.get_json()
        job_schema = JobPostingSchema()
        job = job_schema.load(job_data)
        existing_job = JobPosting.query.get_or_404(job_id)
        for key, value in job.items():
            setattr(existing_job, key, value)
        db.session.commit()
        return job_schema.dump(existing_job), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a job posting
@app.route('/job_postings/<int:job_id>', methods=['DELETE'])
def delete_job_posting(job_id):
    job = JobPosting.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job posting deleted"}), 204

# Endpoint to create an application
@app.route('/applications', methods=['POST'])
def create_application():
    try:
        application_data = request.get_json()
        application_schema = ApplicationSchema()
        application = application_schema.load(application_data)
        new_application = Application(**application)
        db.session.add(new_application)
        db.session.commit()
        return application_schema.dump(new_application), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get all applications
@app.route('/applications', methods=['GET'])
def get_applications():
    applications = Application.query.all()
    application_schema = ApplicationSchema(many=True)
    return application_schema.dump(applications), 200

# Endpoint to get a specific application
@app.route('/applications/<int:application_id>', methods=['GET'])
def get_application(application_id):
    application = Application.query.get_or_404(application_id)
    application_schema = ApplicationSchema()
    return application_schema.dump(application), 200

# Endpoint to update an application
@app.route('/applications/<int:application_id>', methods=['PUT'])
def update_application(application_id):
    try:
        application_data = request.get_json()
        application_schema = ApplicationSchema()
        application = application_schema.load(application_data)
        existing_application = Application.query.get_or_404(application_id)
        for key, value in application.items():
            setattr(existing_application, key, value)
        db.session.commit()
        return application_schema.dump(existing_application), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete an application
@app.route('/applications/<int:application_id>', methods=['DELETE'])
def delete_application(application_id):
    application = Application.query.get_or_404(application_id)
    db.session.delete(application)
    db.session.commit()
    return jsonify({"message": "Application deleted"}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
