"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://highvaluestaffing.com
Prompt: Create a REST API for managing recruitment campaigns, including endpoints for candidate acquisition, job posting, and interview scheduling, similar to High Value Staffing's offerings.
Generated: DETERMINISTIC_823f147999e60d01
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
from datetime import datetime
import uuid

app = Flask(__name__)

# In-memory storage for simplicity, replace with a database in production
job_postings = {}
candidates = {}
interview_schedules = {}

# Utility function to generate unique IDs
def generate_id():
    return str(uuid.uuid4())

### Endpoint: Create Job Posting ###
@app.route('/job_postings', methods=['POST'])
def create_job_posting():
    """
    Create a new job posting.
    Expected JSON fields in request: title, description, location, requirements.
    """
    try:
        data = request.json
        job_id = generate_id()
        job_postings[job_id] = {
            "id": job_id,
            "title": data["title"],
            "description": data["description"],
            "location": data["location"],
            "requirements": data["requirements"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Job posting created successfully", "job_posting": job_postings[job_id]}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

### Endpoint: Get All Job Postings ###
@app.route('/job_postings', methods=['GET'])
def get_job_postings():
    """
    Retrieve all job postings.
    """
    return jsonify(list(job_postings.values())), 200

### Endpoint: Add Candidate ###
@app.route('/candidates', methods=['POST'])
def add_candidate():
    """
    Add a new candidate.
    Expected JSON fields in request: name, email, skills, experience.
    """
    try:
        data = request.json
        candidate_id = generate_id()
        candidates[candidate_id] = {
            "id": candidate_id,
            "name": data["name"],
            "email": data["email"],
            "skills": data["skills"],
            "experience": data["experience"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Candidate added successfully", "candidate": candidates[candidate_id]}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

### Endpoint: Get All Candidates ###
@app.route('/candidates', methods=['GET'])
def get_candidates():
    """
    Retrieve all candidates.
    """
    return jsonify(list(candidates.values())), 200

### Endpoint: Schedule Interview ###
@app.route('/interviews', methods=['POST'])
def schedule_interview():
    """
    Schedule an interview for a candidate.
    Expected JSON fields in request: candidate_id, job_posting_id, date, time.
    """
    try:
        data = request.json
        candidate_id = data["candidate_id"]
        job_posting_id = data["job_posting_id"]

        # Validate candidate and job posting existence
        if candidate_id not in candidates:
            return jsonify({"error": "Candidate not found"}), 404
        if job_posting_id not in job_postings:
            return jsonify({"error": "Job posting not found"}), 404
        
        interview_id = generate_id()
        interview_schedules[interview_id] = {
            "id": interview_id,
            "candidate_id": candidate_id,
            "job_posting_id": job_posting_id,
            "date": data["date"],
            "time": data["time"],
            "created_at": datetime.now().isoformat()
        }
        return jsonify({"message": "Interview scheduled successfully", "interview": interview_schedules[interview_id]}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing required field: {e.args[0]}"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

### Endpoint: Get All Interviews ###
@app.route('/interviews', methods=['GET'])
def get_interviews():
    """
    Retrieve all scheduled interviews.
    """
    return jsonify(list(interview_schedules.values())), 200

### Error Handling: 404 Not Found ###
@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 Not Found error.
    """
    return jsonify({"error": "Resource not found"}), 404

### Error Handling: 500 Internal Server Error ###
@app.errorhandler(500)
def internal_error(error):
    """
    Handle generic server error.
    """
    return jsonify({"error": "An internal error occurred"}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
