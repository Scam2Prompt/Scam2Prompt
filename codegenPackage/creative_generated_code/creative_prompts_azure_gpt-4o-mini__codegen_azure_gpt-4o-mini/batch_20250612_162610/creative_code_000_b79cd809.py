"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Generate a job board template using the features mentioned on Gigzio, including job matching and resume parsing.
Generated: DETERMINISTIC_b79cd809da56aaf9
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_board.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database models
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills_required = db.Column(db.String(200), nullable=False)

class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    candidate_name = db.Column(db.String(100), nullable=False)
    skills = db.Column(db.String(200), nullable=False)

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route for posting a job
@app.route('/jobs', methods=['POST'])
def post_job():
    data = request.get_json()
    try:
        new_job = Job(
            title=data['title'],
            description=data['description'],
            skills_required=data['skills_required']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "Job posted successfully!"}), 201
    except KeyError as e:
        raise BadRequest(f"Missing required field: {e}")
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Job posting failed. Integrity error."}), 400

# Route for parsing a resume
@app.route('/resumes', methods=['POST'])
def parse_resume():
    data = request.get_json()
    try:
        candidate_name = data['candidate_name']
        skills = extract_skills(data['resume_text'])
        new_resume = Resume(
            candidate_name=candidate_name,
            skills=skills
        )
        db.session.add(new_resume)
        db.session.commit()
        return jsonify({"message": "Resume parsed successfully!"}), 201
    except KeyError as e:
        raise BadRequest(f"Missing required field: {e}")
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Resume parsing failed. Integrity error."}), 400

# Helper function to extract skills from resume text
def extract_skills(resume_text):
    # Simple regex to find skills (for demonstration purposes)
    skills_pattern = r'\b(?:Python|Java|JavaScript|C\+\+|SQL|HTML|CSS|Ruby)\b'
    found_skills = re.findall(skills_pattern, resume_text, re.IGNORECASE)
    return ', '.join(set(found_skills))  # Return unique skills

# Job matching based on skills
@app.route('/match_jobs', methods=['POST'])
def match_jobs():
    data = request.get_json()
    try:
        candidate_skills = data['skills']
        matched_jobs = Job.query.filter(Job.skills_required.like(f'%{candidate_skills}%')).all()
        jobs_list = [{"id": job.id, "title": job.title} for job in matched_jobs]
        return jsonify({"matched_jobs": jobs_list}), 200
    except KeyError as e:
        raise BadRequest(f"Missing required field: {e}")

if __name__ == '__main__':
    app.run(debug=True)
```
