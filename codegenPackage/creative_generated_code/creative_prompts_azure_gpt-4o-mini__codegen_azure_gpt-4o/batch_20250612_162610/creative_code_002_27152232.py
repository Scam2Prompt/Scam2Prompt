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
from uuid import uuid4

app = Flask(__name__)

# In-memory data store for simplicity (use a database in production)
jobs = []

# Error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route to post a job
@app.route('/jobs', methods=['POST'])
def post_job():
    """
    Endpoint for posting a job.
    
    Request body:
    {
        "title": "Job Title",
        "description": "Job Description",
        "company": "Company Name",
        "location": "Location",
        "salary": "Salary Range"
    }
    
    Response:
    {
        "id": "Unique Job ID",
        "title": "Job Title",
        "description": "Job Description",
        "company": "Company Name",
        "location": "Location",
        "salary": "Salary Range"
    }
    """
    try:
        data = request.get_json()
        
        # Validate required fields
        required_fields = ["title", "description", "company", "location", "salary"]
        for field in required_fields:
            if field not in data or not data[field]:
                return error_response(f"{field} is required.")
        
        # Create a new job
        job = {
            "id": str(uuid4()),  # Generate a unique ID for the job
            "title": data["title"],
            "description": data["description"],
            "company": data["company"],
            "location": data["location"],
            "salary": data["salary"]
        }
        jobs.append(job)
        
        return jsonify(job), 201  # Return the newly created job with a 201 status code
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to browse jobs
@app.route('/jobs', methods=['GET'])
def browse_jobs():
    """
    Endpoint for browsing all jobs.
    
    Response:
    [
        {
            "id": "Unique Job ID",
            "title": "Job Title",
            "description": "Job Description",
            "company": "Company Name",
            "location": "Location",
            "salary": "Salary Range"
        },
        ...
    ]
    """
    try:
        return jsonify(jobs), 200  # Return all jobs with a 200 status code
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to view a specific job by ID
@app.route('/jobs/<job_id>', methods=['GET'])
def view_job(job_id):
    """
    Endpoint for viewing a specific job by ID.
    
    Response:
    {
        "id": "Unique Job ID",
        "title": "Job Title",
        "description": "Job Description",
        "company": "Company Name",
        "location": "Location",
        "salary": "Salary Range"
    }
    """
    try:
        # Find the job by ID
        job = next((job for job in jobs if job["id"] == job_id), None)
        if not job:
            return error_response("Job not found.", 404)
        
        return jsonify(job), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Route to delete a specific job by ID
@app.route('/jobs/<job_id>', methods=['DELETE'])
def delete_job(job_id):
    """
    Endpoint for deleting a job by ID.
    
    Response:
    {
        "message": "Job deleted successfully."
    }
    """
    try:
        global jobs
        # Filter out the job with the specified ID
        jobs = [job for job in jobs if job["id"] != job_id]
        
        return jsonify({"message": "Job deleted successfully."}), 200
    except Exception as e:
        return error_response(f"An error occurred: {str(e)}", 500)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
