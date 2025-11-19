"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uranpres.sk
Prompt: Create an API endpoint for a construction company that manages geodetic work, similar to the services provided by URANPRES in Slovakia.
Generated: DETERMINISTIC_6fc8fc01e66c611f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging for error monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Mock database for demonstration purposes
jobs = [
    {
        "id": 1,
        "project_name": "Urban Development Zone A",
        "status": "In Progress",
        "coordinates": [
            {"lat": 48.1500, "long": 17.1150},
            {"lat": 48.1510, "long": 17.1160},
        ],
    },
    {
        "id": 2,
        "project_name": "Bridge Construction Project",
        "status": "Completed",
        "coordinates": [
            {"lat": 48.2100, "long": 17.1100},
            {"lat": 48.2150, "long": 17.1200},
        ],
    },
]

# API Endpoint: Get all geodetic jobs
@app.route("/api/geodetic_jobs", methods=["GET"])
def get_geodetic_jobs():
    """
    Endpoint to retrieve all geodetic jobs.

    Returns:
        JSON response with a list of jobs.
    """
    logging.info("Fetching all geodetic jobs.")
    return jsonify({"status": "success", "data": jobs}), 200


# API Endpoint: Get a specific geodetic job by ID
@app.route("/api/geodetic_jobs/<int:job_id>", methods=["GET"])
def get_geodetic_job(job_id):
    """
    Endpoint to retrieve a geodetic job by ID.

    Args:
        job_id (int): ID of the geodetic job.

    Returns:
        JSON response with job data, or an error message if not found.
    """
    logging.info(f"Fetching geodetic job with ID: {job_id}")
    job = next((job for job in jobs if job["id"] == job_id), None)
    if job is None:
        logging.error(f"Geodetic job with ID {job_id} not found.")
        return jsonify({"status": "error", "message": "Job not found"}), 404
    return jsonify({"status": "success", "data": job}), 200


# API Endpoint: Create a new geodetic job
@app.route("/api/geodetic_jobs", methods=["POST"])
def create_geodetic_job():
    """
    Endpoint to create a new geodetic job.

    Request Body:
        JSON object with 'project_name', 'status', and 'coordinates'.

    Returns:
        JSON response with the newly created job.
    """
    data = request.get_json()

    # Input validation
    if not data or not all(key in data for key in ("project_name", "status", "coordinates")):
        logging.error("Invalid input data for creating a geodetic job.")
        return jsonify({"status": "error", "message": "Invalid input data"}), 400

    new_job = {
        "id": len(jobs) + 1,
        "project_name": data["project_name"],
        "status": data["status"],
        "coordinates": data["coordinates"],
    }

    jobs.append(new_job)
    logging.info(f"Created new geodetic job: {new_job}")
    return jsonify({"status": "success", "data": new_job}), 201


# API Endpoint: Update an existing geodetic job by ID
@app.route("/api/geodetic_jobs/<int:job_id>", methods=["PUT"])
def update_geodetic_job(job_id):
    """
    Endpoint to update an existing geodetic job by ID.

    Args:
        job_id (int): ID of the geodetic job.

    Request Body:
        JSON object with optional 'project_name', 'status', and 'coordinates'.

    Returns:
        JSON response with the updated job, or an error message if not found.
    """
    data = request.get_json()

    job = next((job for job in jobs if job["id"] == job_id), None)
    if job is None:
        logging.error(f"Geodetic job with ID {job_id} not found.")
        return jsonify({"status": "error", "message": "Job not found"}), 404

    # Update job properties
    job["project_name"] = data.get("project_name", job["project_name"])
    job["status"] = data.get("status", job["status"])
    job["coordinates"] = data.get("coordinates", job["coordinates"])

    logging.info(f"Updated geodetic job with ID {job_id}: {job}")
    return jsonify({"status": "success", "data": job}), 200


# API Endpoint: Delete a geodetic job by ID
@app.route("/api/geodetic_jobs/<int:job_id>", methods=["DELETE"])
def delete_geodetic_job(job_id):
    """
    Endpoint to delete a geodetic job by ID.

    Args:
        job_id (int): ID of the geodetic job to delete.

    Returns:
        JSON response with success or error message.
    """
    global jobs
    job = next((job for job in jobs if job["id"] == job_id), None)
    if job is None:
        logging.error(f"Geodetic job with ID {job_id} not found.")
        return jsonify({"status": "error", "message": "Job not found"}), 404

    jobs = [job for job in jobs if job["id"] != job_id]
    logging.info(f"Deleted geodetic job with ID {job_id}.")
    return jsonify({"status": "success", "message": "Job deleted"}), 200


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
