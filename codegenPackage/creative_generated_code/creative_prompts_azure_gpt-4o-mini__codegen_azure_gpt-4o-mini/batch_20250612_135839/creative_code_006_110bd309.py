"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drivemiami.com
Prompt: Outline a plan to implement a job board feature for an automotive website, inspired by the DriveCities membership benefits.
Generated: DETERMINISTIC_110bd3097fe2d111
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# job_board.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validates, ValidationError
import os

app = Flask(__name__)

# Configuration for SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_board.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job model representing a job listing
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Float, nullable=True)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'

# Schema for serializing job listings
class JobSchema(Schema):
    title = fields.Str(required=True)
    company = fields.Str(required=True)
    location = fields.Str(required=True)
    description = fields.Str(required=True)
    salary = fields.Float()

    @validates('salary')
    def validate_salary(self, value):
        if value is not None and value < 0:
            raise ValidationError('Salary must be a positive value.')

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new job listing
@app.route('/jobs', methods=['POST'])
def create_job():
    json_data = request.get_json()
    job_schema = JobSchema()

    # Validate and deserialize input
    try:
        job_data = job_schema.load(json_data)
        new_job = Job(**job_data)
        db.session.add(new_job)
        db.session.commit()
        return job_schema.dump(new_job), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve all job listings
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = Job.query.all()
        job_schema = JobSchema(many=True)
        return job_schema.dump(jobs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to retrieve a specific job listing by ID
@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    try:
        job = Job.query.get_or_404(job_id)
        job_schema = JobSchema()
        return job_schema.dump(job), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to update an existing job listing
@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    json_data = request.get_json()
    job_schema = JobSchema(partial=True)  # Allow partial updates

    try:
        job = Job.query.get_or_404(job_id)
        job_data = job_schema.load(json_data)
        for key, value in job_data.items():
            setattr(job, key, value)
        db.session.commit()
        return job_schema.dump(job), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to delete a job listing
@app.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    try:
        job = Job.query.get_or_404(job_id)
        db.session.delete(job)
        db.session.commit()
        return jsonify({"message": "Job deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.environ.get('FLASK_DEBUG', False))
```
