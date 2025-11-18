"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate code for a web application that matches healthcare professionals (e.g., nurses, doctors, AHPs) with job opportunities based on their qualifications and location preferences.
Generated: DETERMINISTIC_db823b4ce9157e75
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# healthcare_matching_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, validate, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model for Healthcare Professionals
class HealthcareProfessional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    qualifications = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Database Model for Job Opportunities
class JobOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String(100), nullable=False)
    qualifications_required = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Schema for input validation using Marshmallow
class HealthcareProfessionalSchema(Schema):
    name = fields.Str(required=True)
    qualifications = fields.Str(required=True)
    location = fields.Str(required=True)

class JobOpportunitySchema(Schema):
    position = fields.Str(required=True)
    qualifications_required = fields.Str(required=True)
    location = fields.Str(required=True)

# Initialize schemas
professional_schema = HealthcareProfessionalSchema()
job_schema = JobOpportunitySchema()

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Route to add a healthcare professional
@app.route('/professionals', methods=['POST'])
def add_professional():
    try:
        data = request.get_json()
        professional_data = professional_schema.load(data)
        new_professional = HealthcareProfessional(**professional_data)
        db.session.add(new_professional)
        db.session.commit()
        return jsonify({"message": "Healthcare professional added successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to add a job opportunity
@app.route('/jobs', methods=['POST'])
def add_job():
    try:
        data = request.get_json()
        job_data = job_schema.load(data)
        new_job = JobOpportunity(**job_data)
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job opportunity added successfully."}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to match healthcare professionals with job opportunities
@app.route('/match', methods=['GET'])
def match_jobs():
    try:
        location = request.args.get('location')
        qualifications = request.args.get('qualifications').split(',')
        
        jobs = JobOpportunity.query.filter(JobOpportunity.location == location).all()
        matched_jobs = [job for job in jobs if any(q.strip() in job.qualifications_required for q in qualifications)]

        return jsonify(matched_jobs), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages before running the application:
```bash
pip install Flask Flask-SQLAlchemy marshmallow
```
