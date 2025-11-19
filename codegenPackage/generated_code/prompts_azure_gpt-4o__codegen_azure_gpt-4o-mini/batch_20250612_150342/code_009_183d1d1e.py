"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Develop a web application for recruitment in the construction industry, tailored to companies like 株式会社タイコーテクノ, with features for job postings and applicant tracking.
Generated: DETERMINISTIC_183d1d1ea1785a73
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recruitment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Job {self.title}>'

# Define the Applicant model
class Applicant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    resume = db.Column(db.Text, nullable=False)
    date_applied = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Applicant {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to post a new job
@app.route('/jobs', methods=['POST'])
def post_job():
    try:
        data = request.get_json()
        new_job = Job(title=data['title'], description=data['description'], company=data['company'])
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job posted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        jobs = Job.query.all()
        return jsonify([{'id': job.id, 'title': job.title, 'description': job.description, 'company': job.company, 'date_posted': job.date_posted} for job in jobs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to apply for a job
@app.route('/apply', methods=['POST'])
def apply_job():
    try:
        data = request.get_json()
        new_applicant = Applicant(name=data['name'], email=data['email'], job_id=data['job_id'], resume=data['resume'])
        db.session.add(new_applicant)
        db.session.commit()
        return jsonify({'message': 'Application submitted successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all applicants for a job
@app.route('/jobs/<int:job_id>/applicants', methods=['GET'])
def get_applicants(job_id):
    try:
        applicants = Applicant.query.filter_by(job_id=job_id).all()
        return jsonify([{'id': applicant.id, 'name': applicant.name, 'email': applicant.email, 'date_applied': applicant.date_applied} for applicant in applicants]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
- Install Flask and Flask-SQLAlchemy:
```bash
pip install Flask Flask-SQLAlchemy
```

### Database
- The application uses SQLite for simplicity. For production, consider using a more robust database like PostgreSQL or MySQL.
