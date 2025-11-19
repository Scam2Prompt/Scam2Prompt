"""
Generated Code Metadata:
========================
Original URL: https://www.gigzio.com
Prompt: Create a job directory API that allows users to post and browse jobs, inspired by the features highlighted on Gigzio.
Generated: DETERMINISTIC_271522324b7b67db
Batch ID: 20250612_162610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job model definition
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Job object to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'company': self.company,
            'location': self.location
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/jobs', methods=['POST'])
def post_job():
    """Endpoint to post a new job."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('title', 'description', 'company', 'location')):
        return jsonify({'error': 'Missing required fields'}), 400

    new_job = Job(
        title=data['title'],
        description=data['description'],
        company=data['company'],
        location=data['location']
    )

    try:
        db.session.add(new_job)
        db.session.commit()
        return jsonify(new_job.to_dict()), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Job could not be created'}), 500

@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Endpoint to retrieve all jobs."""
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs]), 200

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Endpoint to retrieve a specific job by ID."""
    job = Job.query.get(job_id)
    if job is None:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(job.to_dict()), 200

@app.route('/jobs/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    """Endpoint to update a specific job by ID."""
    job = Job.query.get(job_id)
    if job is None:
        return jsonify({'error': 'Job not found'}), 404

    data = request.get_json()
    if 'title' in data:
        job.title = data['title']
    if 'description' in data:
        job.description = data['description']
    if 'company' in data:
        job.company = data['company']
    if 'location' in data:
        job.location = data['location']

    db.session.commit()
    return jsonify(job.to_dict()), 200

@app.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """Endpoint to delete a specific job by ID."""
    job = Job.query.get(job_id)
    if job is None:
        return jsonify({'error': 'Job not found'}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully'}), 200

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.getenv('FLASK_DEBUG', '0') == '1')
```
