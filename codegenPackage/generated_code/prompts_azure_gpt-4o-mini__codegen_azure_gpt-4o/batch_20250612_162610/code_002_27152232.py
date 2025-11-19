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
from uuid import uuid4

app = Flask(__name__)

# In-memory database for jobs
jobs = {}

# Error messages
JOB_NOT_FOUND = {"error": "Job not found"}
INVALID_PAYLOAD = {"error": "Invalid payload"}

# Helper function to validate job payload
def validate_job_payload(payload):
    required_fields = ["title", "description", "company", "location", "salary"]
    return all(field in payload for field in required_fields)

# Route to post a new job
@app.route('/jobs', methods=['POST'])
def post_job():
    try:
        data = request.json
        if not validate_job_payload(data):
            return jsonify(INVALID_PAYLOAD), 400
        
        job_id = str(uuid4())  # Generate a unique ID for the job
        jobs[job_id] = {
            "id": job_id,
            "title": data["title"],
            "description": data["description"],
            "company": data["company"],
            "location": data["location"],
            "salary": data["salary"]
        }
        return jsonify(jobs[job_id]), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to browse all jobs
@app.route('/jobs', methods=['GET'])
def browse_jobs():
    try:
        return jsonify(list(jobs.values())), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific job by ID
@app.route('/jobs/<job_id>', methods=['GET'])
def get_job(job_id):
    try:
        job = jobs.get(job_id)
        if not job:
            return jsonify(JOB_NOT_FOUND), 404
        return jsonify(job), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a job by ID
@app.route('/jobs/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    try:
        job = jobs.pop(job_id, None)
        if not job:
            return jsonify(JOB_NOT_FOUND), 404
        return jsonify({"message": "Job deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a job by ID
@app.route('/jobs/<job_id>', methods=['PUT'])
def update_job(job_id):
    try:
        data = request.json
        if not validate_job_payload(data):
            return jsonify(INVALID_PAYLOAD), 400
        
        job = jobs.get(job_id)
        if not job:
            return jsonify(JOB_NOT_FOUND), 404
        
        # Update job details
        job.update({
            "title": data["title"],
            "description": data["description"],
            "company": data["company"],
            "location": data["location"],
            "salary": data["salary"]
        })
        return jsonify(job), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
