"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kleanproutah.com
Prompt: Generate a code snippet for a mobile power washing service that includes features for scheduling and tracking jobs, similar to Klean-Pro Utah's offerings.
Generated: DETERMINISTIC_a6261eecc4e02f44
Batch ID: 20250612_155128
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from datetime import datetime
from flask import Flask, request, jsonify
import json

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for scheduled jobs
jobs = []

class Job:
    """Class to represent a Power Washing job."""
    def __init__(self, client_name, address, date_time, job_id):
        self.client_name = client_name
        self.address = address
        self.date_time = date_time
        self.job_id = job_id

    def to_dict(self):
        """Convert job details to a dictionary format for easy JSON serialization."""
        return {
            'job_id': self.job_id,
            'client_name': self.client_name,
            'address': self.address,
            'date_time': self.date_time.strftime("%Y-%m-%d %H:%M:%S")
        }

@app.route('/schedule', methods=['POST'])
def schedule_job():
    """Endpoint to schedule a new power washing job."""
    try:
        # Parse the input data
        data = request.get_json()
        client_name = data['client_name']
        address = data['address']
        date_time = datetime.strptime(data['date_time'], "%Y-%m-%d %H:%M:%S")

        # Create a new job instance
        job_id = len(jobs) + 1  # Simple job ID generation
        new_job = Job(client_name, address, date_time, job_id)
        jobs.append(new_job)

        return jsonify(new_job.to_dict()), 201  # Respond with the created job details
    except KeyError as e:
        return jsonify({'error': f'Missing parameter: {str(e)}'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid date format. Use YYYY-MM-DD HH:MM:SS'}), 400

@app.route('/jobs', methods=['GET'])
def get_jobs():
    """Endpoint to retrieve all scheduled jobs."""
    return jsonify([job.to_dict() for job in jobs]), 200

@app.route('/job/<int:job_id>', methods=['GET'])
def get_job(job_id):
    """Endpoint to retrieve a specific job by job ID."""
    job = next((job for job in jobs if job.job_id == job_id), None)
    if job is not None:
        return jsonify(job.to_dict()), 200
    else:
        return jsonify({'error': 'Job not found'}), 404

@app.route('/job/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    """Endpoint to cancel a scheduled job by job ID."""
    global jobs
    job = next((job for job in jobs if job.job_id == job_id), None)
    if job is not None:
        jobs = [job for job in jobs if job.job_id != job_id]
        return jsonify({'message': 'Job cancelled successfully'}), 200
    else:
        return jsonify({'error': 'Job not found'}), 404

if __name__ == '__main__':
    # Run the application on the specified port
    app.run(debug=True, port=5000)
```
