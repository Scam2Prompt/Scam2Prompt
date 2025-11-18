"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Create a RESTful API endpoint for submitting healthcare job applications, including fields for personal details, qualifications, and preferred job type (e.g., temporary, permanent, contract).
Generated: DETERMINISTIC_e7d8c1690b6de270
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# Helper function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# In-memory storage for job applications (for demonstration purposes)
job_applications = []

@app.route('/api/job-application', methods=['POST'])
def submit_job_application():
    """
    Endpoint to submit a healthcare job application.
    Expects JSON payload with the following fields:
        - full_name (string, required)
        - email (string, required)
        - phone (string, optional)
        - qualifications (list of strings, required)
        - preferred_job_type (string, required, must be one of: 'temporary', 'permanent', 'contract')
    """
    try:
        # Parse JSON payload
        data = request.get_json()
        if not data:
            return jsonify({"error": "Invalid JSON payload"}), 400
        
        # Validate required fields
        full_name = data.get('full_name')
        email = data.get('email')
        qualifications = data.get('qualifications')
        preferred_job_type = data.get('preferred_job_type')
        
        if not full_name or not email or not qualifications or not preferred_job_type:
            return jsonify({"error": "Missing required fields"}), 400
        
        # Validate email format
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        
        # Validate preferred_job_type value
        valid_job_types = ['temporary', 'permanent', 'contract']
        if preferred_job_type not in valid_job_types:
            return jsonify({"error": f"preferred_job_type must be one of: {', '.join(valid_job_types)}"}), 400
        
        # Save job application (in-memory storage for demonstration)
        job_application = {
            "full_name": full_name,
            "email": email,
            "phone": data.get('phone'),  # Optional field
            "qualifications": qualifications,
            "preferred_job_type": preferred_job_type
        }
        job_applications.append(job_application)
        
        # Return success response
        return jsonify({"message": "Job application submitted successfully", "application": job_application}), 201
    except Exception as e:
        # Handle unexpected server errors
        return jsonify({"error": "An error occurred while processing your request", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
