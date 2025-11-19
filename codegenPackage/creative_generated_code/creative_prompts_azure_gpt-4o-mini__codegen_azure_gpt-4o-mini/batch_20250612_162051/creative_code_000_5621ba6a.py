"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Generate a code snippet for a web application that connects healthcare professionals with job opportunities, similar to the services offered by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_5621ba6a3cf1f555
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.exceptions import NotFound, BadRequest

# Initialize Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity; change as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    healthcare_professional = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert Job object to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'location': self.location,
            'healthcare_professional': self.healthcare_professional
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get a list of jobs
@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Fetch all job listings."""
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs]), 200

# Route to post a new job
@app.route('/jobs', methods=['POST'])
def create_job():
    """Add a new job listing."""
    try:
        data = request.json
        # Validate incoming data
        if not all(key in data for key in ('title', 'description', 'location', 'healthcare_professional')):
            raise BadRequest("Missing required fields.")
        
        new_job = Job(
            title=data['title'],
            description=data['description'],
            location=data['location'],
            healthcare_professional=data['healthcare_professional']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify(new_job.to_dict()), 201

    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the job.'}), 500

# Route to get a job by ID
@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Fetch a specific job listing by ID."""
    job = Job.query.get(job_id)
    if job is None:
        raise NotFound("Job not found.")
    return jsonify(job.to_dict()), 200

# Error handler for NotFound
@app.errorhandler(NotFound)
def handle_not_found(error):
    """Handle 404 Not Found errors."""
    return jsonify({'error': str(error)}), 404

# Error handler for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """Handle 400 Bad Request errors."""
    return jsonify({'error': str(error)}), 400

# Main block to run the application
if __name__ == '__main__':
    app.run(debug=True)  # Set debug=False for production
```
