"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Suggest an API for real-time feedback services in monitoring projects, referencing the techniques used by GLOW Consultants.
Generated: DETERMINISTIC_28bba510b62a84d3
Batch ID: 20250612_135637
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
from datetime import datetime

app = Flask(__name__)

# Configure logging for error tracking and monitoring
logging.basicConfig(
    filename='feedback_service.log',
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s'
)

# In-memory database simulation for storing feedback
# In production, replace this with a proper database system
feedback_data = {}

# Utility function for error logging
def log_error(error_message):
    logging.error(f"Error: {error_message}")

# Index route for health check
@app.route('/', methods=['GET'])
def health_check():
    """
    Health Check Route
    This endpoint can be used to verify that the API server is running.
    """
    return jsonify({"status": "Feedback API is running"}), 200

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    """
    Submit Feedback API
    Allows users to send real-time feedback for monitoring a project.
    Expects JSON input with 'project_id', 'user_id', and 'feedback'.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        project_id = data.get('project_id')
        user_id = data.get('user_id')
        feedback = data.get('feedback')

        # Validate input
        if not project_id or not user_id or not feedback:
            return jsonify({"error": "Missing required fields: 'project_id', 'user_id', and 'feedback'"}), 400

        # Store feedback (grouped by project_id)
        feedback_entry = {
            "user_id": user_id,
            "feedback": feedback,
            "timestamp": datetime.utcnow().isoformat()
        }

        feedback_data.setdefault(project_id, []).append(feedback_entry)

        # Respond with success
        return jsonify({"message": "Feedback submitted successfully"}), 201

    except Exception as e:
        log_error(str(e))
        return jsonify({"error": "Failed to process feedback"}), 500

@app.route('/get_feedback/<project_id>', methods=['GET'])
def get_feedback(project_id):
    """
    Get Feedback API
    Retrieves all feedback for a given project_id.
    """
    try:
        # Fetch feedback data for the project_id
        project_feedback = feedback_data.get(project_id, [])

        # Respond with feedback data
        if project_feedback:
            return jsonify({"project_id": project_id, "feedback": project_feedback}), 200
        else:
            return jsonify({"message": "No feedback found for this project"}), 404

    except Exception as e:
        log_error(str(e))
        return jsonify({"error": "Failed to retrieve feedback"}), 500


@app.route('/get_all_projects', methods=['GET'])
def get_all_projects():
    """
    Get All Projects API
    Retrieves a list of all projects that have feedback.
    """
    try:
        # Get all project IDs from feedback data
        projects = list(feedback_data.keys())
        return jsonify({"projects": projects}), 200

    except Exception as e:
        log_error(str(e))
        return jsonify({"error": "Failed to retrieve projects"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
