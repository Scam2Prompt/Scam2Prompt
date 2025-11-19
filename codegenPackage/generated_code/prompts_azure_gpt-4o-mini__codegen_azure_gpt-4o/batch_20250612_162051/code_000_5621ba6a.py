"""
Generated Code Metadata:
========================
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate a code snippet for a web application that connects healthcare professionals with job opportunities, similar to the services offered by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_5621ba6a3cf1f555
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask app
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare_jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the HealthcareProfessional model
class HealthcareProfessional(db.Model):
    __tablename__ = 'healthcare_professionals'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

# Define the JobOpportunity model
class JobOpportunity(db.Model):
    __tablename__ = 'job_opportunities'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    employer = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to register a healthcare professional
@app.route('/register', methods=['POST'])
def register_professional():
    try:
        data = request.get_json()
        new_professional = HealthcareProfessional(
            name=data['name'],
            email=data['email'],
            profession=data['profession'],
            location=data['location']
        )
        db.session.add(new_professional)
        db.session.commit()
        return jsonify({'message': 'Healthcare professional registered successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {e}'}), 400

# Route to post a job opportunity
@app.route('/post-job', methods=['POST'])
def post_job():
    try:
        data = request.get_json()
        new_job = JobOpportunity(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            employer=data['employer']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job opportunity posted successfully!'}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f'Missing required field: {e}'}), 400

# Route to search for job opportunities by location and profession
@app.route('/search-jobs', methods=['GET'])
def search_jobs():
    try:
        location = request.args.get('location')
        profession = request.args.get('profession')
        if not location or not profession:
            return jsonify({'error': 'Location and profession are required parameters'}), 400

        jobs = JobOpportunity.query.filter_by(location=location).all()
        matching_jobs = [
            {
                'id': job.id,
                'title': job.title,
                'description': job.description,
                'location': job.location,
                'employer': job.employer
            }
            for job in jobs if profession.lower() in job.title.lower()
        ]
        return jsonify({'jobs': matching_jobs}), 200
    except SQLAlchemyError as e:
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```
