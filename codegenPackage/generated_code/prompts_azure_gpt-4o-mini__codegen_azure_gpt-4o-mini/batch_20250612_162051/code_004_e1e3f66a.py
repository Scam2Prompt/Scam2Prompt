"""
Generated Code Metadata:
========================
Original URL: https://www.jobone.careers
Prompt: Generate an API endpoint for a job listing service that includes filtering options for job types and locations, similar to the offerings of jobONE.
Generated: DETERMINISTIC_e1e3f66a3310309d
Batch ID: 20250612_162051
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
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job model representing the job listings in the database
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    job_type = db.Column(db.String(50), nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Job object to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'job_type': self.job_type,
            'location': self.location
        }

# Create the database and the Job table
with app.app_context():
    db.create_all()

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """
    API endpoint to retrieve job listings with optional filtering.
    Query parameters:
    - job_type: Filter by job type (e.g., 'full-time', 'part-time')
    - location: Filter by job location (e.g., 'New York', 'Remote')
    """
    try:
        job_type = request.args.get('job_type')
        location = request.args.get('location')

        # Build the query based on provided filters
        query = Job.query
        if job_type:
            query = query.filter(Job.job_type == job_type)
        if location:
            query = query.filter(Job.location == location)

        jobs = query.all()
        return jsonify([job.to_dict() for job in jobs]), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # Set debug to False in production
```
