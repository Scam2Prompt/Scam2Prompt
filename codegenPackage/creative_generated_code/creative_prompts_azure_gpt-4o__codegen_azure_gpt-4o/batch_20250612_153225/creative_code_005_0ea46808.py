"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Suggest an API for implementing expatriate recruitment services, allowing organizations to find and manage international candidates, as highlighted by High Value Staffing.
Generated: DETERMINISTIC_0ea46808538d40e0
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock database for demonstration purposes
# In production, replace this with a real database
database = {
    "candidates": [],
    "organizations": [],
    "jobs": [],
    "applications": []
}

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    """Handle exceptions and return JSON error responses."""
    response = {
        "success": False,
        "error": str(e)
    }
    if isinstance(e, HTTPException):
        response["status_code"] = e.code
        return jsonify(response), e.code
    else:
        response["status_code"] = 500
        return jsonify(response), 500


# API Routes
@app.route('/api/candidates', methods=['POST'])
def register_candidate():
    """
    Register a new candidate.
    Expected JSON format:
    {
        "name": "John Doe",
        "skills": ["Python", "Django"],
        "location": "Germany",
        "visa_status": "Work Permit"
    }
    """
    try:
        data = request.json
        candidate_id = len(database["candidates"]) + 1
        candidate = {
            "id": candidate_id,
            "name": data["name"],
            "skills": data["skills"],
            "location": data["location"],
            "visa_status": data["visa_status"]
        }
        database["candidates"].append(candidate)
        return jsonify({"success": True, "candidate": candidate}), 201
    except KeyError as e:
        return jsonify({"success": False, "error": f"Missing field: {str(e)}"}), 400


@app.route('/api/organizations', methods=['POST'])
def register_organization():
    """
    Register a new organization.
    Expected JSON format:
    {
        "name": "TechCorp",
        "industry": "IT",
        "location": "USA"
    }
    """
    try:
        data = request.json
        organization_id = len(database["organizations"]) + 1
        organization = {
            "id": organization_id,
            "name": data["name"],
            "industry": data["industry"],
            "location": data["location"]
        }
        database["organizations"].append(organization)
        return jsonify({"success": True, "organization": organization}), 201
    except KeyError as e:
        return jsonify({"success": False, "error": f"Missing field: {str(e)}"}), 400


@app.route('/api/jobs', methods=['POST'])
def post_job():
    """
    Post a new job by an organization.
    Expected JSON format:
    {
        "organization_id": 1,
        "title": "Software Engineer",
        "description": "Develop web applications",
        "location": "USA",
        "required_skills": ["Python", "Flask"]
    }
    """
    try:
        data = request.json
        job_id = len(database["jobs"]) + 1
        job = {
            "id": job_id,
            "organization_id": data["organization_id"],
            "title": data["title"],
            "description": data["description"],
            "location": data["location"],
            "required_skills": data["required_skills"]
        }
        database["jobs"].append(job)
        return jsonify({"success": True, "job": job}), 201
    except KeyError as e:
        return jsonify({"success": False, "error": f"Missing field: {str(e)}"}), 400


@app.route('/api/applications', methods=['POST'])
def apply_for_job():
    """
    Apply for a job.
    Expected JSON format:
    {
        "candidate_id": 1,
        "job_id": 2,
        "message": "I am passionate about this role."
    }
    """
    try:
        data = request.json
        application_id = len(database["applications"]) + 1
        application = {
            "id": application_id,
            "candidate_id": data["candidate_id"],
            "job_id": data["job_id"],
            "message": data["message"]
        }
        database["applications"].append(application)
        return jsonify({"success": True, "application": application}), 201
    except KeyError as e:
        return jsonify({"success": False, "error": f"Missing field: {str(e)}"}), 400


@app.route('/api/match', methods=['GET'])
def match_candidates_to_jobs():
    """
    Match candidates to jobs based on skills.
    Returns a list of jobs with matched candidates.
    """
    try:
        matches = []
        for job in database["jobs"]:
            matched_candidates = []
            for candidate in database["candidates"]:
                if any(skill in job["required_skills"] for skill in candidate["skills"]):
                    matched_candidates.append(candidate)
            matches.append({
                "job": job,
                "matched_candidates": matched_candidates
            })
        return jsonify({"success": True, "matches": matches}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    # Run the server
    app.run(debug=True)
```
