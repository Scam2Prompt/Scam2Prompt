"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gigzio.com
Prompt: Create a job directory API that allows users to post and browse jobs, inspired by the features highlighted on Gigzio.
Generated: DETERMINISTIC_271522324b7b67db
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
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Job model
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    company = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert Job object to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'company': self.company,
            'location': self.location,
            'posted_at': self.posted_at.isoformat()
        }

# Create the database
with app.app_context():
    db.create_all()

@app.route('/jobs', methods=['POST'])
def post_job():
    """API endpoint to post a new job."""
    data = request.get_json()
    
    try:
        # Validate input data
        if not all(key in data for key in ('title', 'description', 'company', 'location')):
            return jsonify({"error": "Missing data"}), 400
        
        # Create a new job
        new_job = Job(
            title=data['title'],
            description=data['description'],
            company=data['company'],
            location=data['location']
        )
        
        # Save job to the database
        db.session.add(new_job)
        db.session.commit()
        
        return jsonify(new_job.to_dict()), 201
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/jobs', methods=['GET'])
def browse_jobs():
    """API endpoint to browse all jobs."""
    try:
        jobs = Job.query.all()
        return jsonify([job.to_dict() for job in jobs]), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

@app.route('/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """API endpoint to get a specific job by ID."""
    try:
        job = Job.query.get_or_404(job_id)
        return jsonify(job.to_dict()), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
```
