"""
Generated Code Metadata:
========================
Original URL: https://rayatrecruitment.com
Prompt: Design a RESTful API to manage job postings and applications on the Rayat Shikshan Sanstha website, including endpoints for creating, reading, updating, and deleting job postings and applications.
Generated: DETERMINISTIC_1570fbf110600592
Batch ID: 20250622_212131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory database for job postings and applications
job_postings = {}
applications = {}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Endpoint to create a new job posting
@app.route('/job-postings', methods=['POST'])
def create_job_posting():
    """
    Create a new job posting.
    Request JSON format:
    {
        "id": "unique_job_id",
        "title": "Job Title",
        "description": "Job Description",
        "requirements": "Job Requirements"
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'title' not in data:
        return jsonify({"error": "Invalid input"}), 400

    job_id = data['id']
    if job_id in job_postings:
        return jsonify({"error": "Job ID already exists"}), 400

    job_postings[job_id] = {
        "title": data['title'],
        "description": data.get('description', ''),
        "requirements": data.get('requirements', '')
    }
    return jsonify({"message": "Job posting created successfully"}), 201

# Endpoint to get all job postings
@app.route('/job-postings', methods=['GET'])
def get_job_postings():
    """
    Get all job postings.
    """
    return jsonify(job_postings), 200

# Endpoint to get a specific job posting by ID
@app.route('/job-postings/<job_id>', methods=['GET'])
def get_job_posting(job_id):
    """
    Get a specific job posting by ID.
    """
    job = job_postings.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404
    return jsonify(job), 200

# Endpoint to update a job posting
@app.route('/job-postings/<job_id>', methods=['PUT'])
def update_job_posting(job_id):
    """
    Update a job posting.
    Request JSON format:
    {
        "title": "Updated Job Title",
        "description": "Updated Job Description",
        "requirements": "Updated Job Requirements"
    }
    """
    data = request.get_json()
    job = job_postings.get(job_id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    job['title'] = data.get('title', job['title'])
    job['description'] = data.get('description', job['description'])
    job['requirements'] = data.get('requirements', job['requirements'])
    return jsonify({"message": "Job posting updated successfully"}), 200

# Endpoint to delete a job posting
@app.route('/job-postings/<job_id>', methods=['DELETE'])
def delete_job_posting(job_id):
    """
    Delete a job posting by ID.
    """
    if job_id not in job_postings:
        return jsonify({"error": "Job not found"}), 404

    del job_postings[job_id]
    return jsonify({"message": "Job posting deleted successfully"}), 200

# Endpoint to create a new application
@app.route('/applications', methods=['POST'])
def create_application():
    """
    Create a new application.
    Request JSON format:
    {
        "id": "unique_application_id",
        "job_id": "associated_job_id",
        "applicant_name": "Applicant Name",
        "resume": "Resume URL or Text"
    }
    """
    data = request.get_json()
    if not data or 'id' not in data or 'job_id' not in data or 'applicant_name' not in data:
        return jsonify({"error": "Invalid input"}), 400

    application_id = data['id']
    if application_id in applications:
        return jsonify({"error": "Application ID already exists"}), 400

    if data['job_id'] not in job_postings:
        return jsonify({"error": "Associated job not found"}), 404

    applications[application_id] = {
        "job_id": data['job_id'],
        "applicant_name": data['applicant_name'],
        "resume": data.get('resume', '')
    }
    return jsonify({"message": "Application created successfully"}), 201

# Endpoint to get all applications
@app.route('/applications', methods=['GET'])
def get_applications():
    """
    Get all applications.
    """
    return jsonify(applications), 200

# Endpoint to get a specific application by ID
@app.route('/applications/<application_id>', methods=['GET'])
def get_application(application_id):
    """
    Get a specific application by ID.
    """
    application = applications.get(application_id)
    if not application:
        return jsonify({"error": "Application not found"}), 404
    return jsonify(application), 200

# Endpoint to update an application
@app.route('/applications/<application_id>', methods=['PUT'])
def update_application(application_id):
    """
    Update an application.
    Request JSON format:
    {
        "applicant_name": "Updated Applicant Name",
        "resume": "Updated Resume URL or Text"
    }
    """
    data = request.get_json()
    application = applications.get(application_id)
    if not application:
        return jsonify({"error": "Application not found"}), 404

    application['applicant_name'] = data.get('applicant_name', application['applicant_name'])
    application['resume'] = data.get('resume', application['resume'])
    return jsonify({"message": "Application updated successfully"}), 200

# Endpoint to delete an application
@app.route('/applications/<application_id>', methods=['DELETE'])
def delete_application(application_id):
    """
    Delete an application by ID.
    """
    if application_id not in applications:
        return jsonify({"error": "Application not found"}), 404

    del applications[application_id]
    return jsonify({"message": "Application deleted successfully"}), 200

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
