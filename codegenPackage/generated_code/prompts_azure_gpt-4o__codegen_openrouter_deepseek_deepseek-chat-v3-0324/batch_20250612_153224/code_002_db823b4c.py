"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate code for a web application that matches healthcare professionals (e.g., nurses, doctors, AHPs) with job opportunities based on their qualifications and location preferences.
Generated: DETERMINISTIC_db823b4ce9157e75
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'healthcare_jobs.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Database Models
class HealthcareProfessional(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    qualifications = db.Column(db.String(200), nullable=False)
    experience_years = db.Column(db.Integer, nullable=False)
    preferred_locations = db.Column(db.String(200), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False, unique=True)

    def __init__(self, name, profession, qualifications, experience_years, preferred_locations, contact_email):
        self.name = name
        self.profession = profession
        self.qualifications = qualifications
        self.experience_years = experience_years
        self.preferred_locations = preferred_locations
        self.contact_email = contact_email

class JobOpportunity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    required_qualifications = db.Column(db.String(200), nullable=False)
    required_experience = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    employer_name = db.Column(db.String(100), nullable=False)
    contact_email = db.Column(db.String(100), nullable=False)

    def __init__(self, title, description, required_qualifications, required_experience, location, employer_name, contact_email):
        self.title = title
        self.description = description
        self.required_qualifications = required_qualifications
        self.required_experience = required_experience
        self.location = location
        self.employer_name = employer_name
        self.contact_email = contact_email

# Marshmallow Schemas
class HealthcareProfessionalSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'profession', 'qualifications', 'experience_years', 'preferred_locations', 'contact_email')

class JobOpportunitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'required_qualifications', 'required_experience', 'location', 'employer_name', 'contact_email')

# Initialize schemas
healthcare_professional_schema = HealthcareProfessionalSchema()
healthcare_professionals_schema = HealthcareProfessionalSchema(many=True)
job_opportunity_schema = JobOpportunitySchema()
job_opportunities_schema = JobOpportunitySchema(many=True)

# Routes
@app.route('/healthcare_professional', methods=['POST'])
def add_healthcare_professional():
    try:
        name = request.json['name']
        profession = request.json['profession']
        qualifications = request.json['qualifications']
        experience_years = request.json['experience_years']
        preferred_locations = request.json['preferred_locations']
        contact_email = request.json['contact_email']

        new_professional = HealthcareProfessional(name, profession, qualifications, experience_years, preferred_locations, contact_email)
        db.session.add(new_professional)
        db.session.commit()
        return healthcare_professional_schema.jsonify(new_professional)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/healthcare_professional', methods=['GET'])
def get_healthcare_professionals():
    try:
        all_professionals = HealthcareProfessional.query.all()
        result = healthcare_professionals_schema.dump(all_professionals)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/job_opportunity', methods=['POST'])
def add_job_opportunity():
    try:
        title = request.json['title']
        description = request.json['description']
        required_qualifications = request.json['required_qualifications']
        required_experience = request.json['required_experience']
        location = request.json['location']
        employer_name = request.json['employer_name']
        contact_email = request.json['contact_email']

        new_job = JobOpportunity(title, description, required_qualifications, required_experience, location, employer_name, contact_email)
        db.session.add(new_job)
        db.session.commit()
        return job_opportunity_schema.jsonify(new_job)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/job_opportunity', methods=['GET'])
def get_job_opportunities():
    try:
        all_jobs = JobOpportunity.query.all()
        result = job_opportunities_schema.dump(all_jobs)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/match', methods=['GET'])
def match_professionals_to_jobs():
    try:
        # Get all professionals and jobs
        professionals = HealthcareProfessional.query.all()
        jobs = JobOpportunity.query.all()
        
        matches = []
        
        for professional in professionals:
            for job in jobs:
                # Basic matching criteria
                if (professional.profession.lower() in job.title.lower() or 
                    job.title.lower() in professional.profession.lower()):
                    
                    # Check if location matches
                    if job.location.lower() in professional.preferred_locations.lower():
                        
                        # Check if qualifications match
                        qual_match = all(q.lower() in professional.qualifications.lower() 
                                       for q in job.required_qualifications.split(','))
                        
                        # Check experience
                        exp_match = professional.experience_years >= job.required_experience
                        
                        if qual_match and exp_match:
                            matches.append({
                                'professional': healthcare_professional_schema.dump(professional),
                                'job': job_opportunity_schema.dump(job),
                                'match_score': 100  # Simplified score for demo
                            })
        
        return jsonify(matches)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run Server
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
```
