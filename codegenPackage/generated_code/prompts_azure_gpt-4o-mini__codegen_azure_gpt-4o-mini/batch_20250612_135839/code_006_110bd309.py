"""
Generated Code Metadata:
========================
Original URL: https://drivemiami.com
Prompt: Outline a plan to implement a job board feature for an automotive website, inspired by the DriveCities membership benefits.
Generated: DETERMINISTIC_110bd3097fe2d111
Batch ID: 20250612_135839
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# job_board.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application and the database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job_board.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Job {self.title} at {self.company}>'

# Create the database and the Job table
with app.app_context():
    db.create_all()

# Route to create a new job listing
@app.route('/jobs', methods=['POST'])
def create_job():
    """Create a new job listing."""
    data = request.get_json()
    
    # Validate input data
    if not all(key in data for key in ('title', 'company', 'location', 'description')):
        return jsonify({'error': 'Missing data'}), 400

    new_job = Job(
        title=data['title'],
        company=data['company'],
        location=data['location'],
        description=data['description']
    )

    try:
        db.session.add(new_job)
        db.session.commit()
        return jsonify({'message': 'Job created successfully', 'job_id': new_job.id}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Job listing could not be created'}), 500

# Route to get all job listings
@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Retrieve all job listings."""
    jobs = Job.query.all()
    return jsonify([{
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'description': job.description
    } for job in jobs]), 200

# Route to get a specific job listing by ID
@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Retrieve a specific job listing by ID."""
    job = Job.query.get_or_404(job_id)
    return jsonify({
        'id': job.id,
        'title': job.title,
        'company': job.company,
        'location': job.location,
        'description': job.description
    }), 200

# Route to delete a job listing
@app.route('/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """Delete a job listing by ID."""
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted successfully'}), 200

# Error handling for 404 errors
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
