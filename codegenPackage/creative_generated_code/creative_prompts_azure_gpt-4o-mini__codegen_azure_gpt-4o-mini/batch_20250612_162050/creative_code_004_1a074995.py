"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Construct a REST API endpoint that provides information about the admission procedure and policies at Deepti Convent Higher Secondary School.
Generated: DETERMINISTIC_1a0749954fd477a5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import logging

# Initialize Flask app and Flask-RESTful API
app = Flask(__name__)
api = Api(app)

# Set up basic logging
logging.basicConfig(level=logging.INFO)

# Sample data representing admission information
ADMISSION_INFO = {
    "admission_open": True,
    "application_deadline": "2023-05-31",
    "eligibility_criteria": {
        "age": "Minimum 5 years as of 1st June",
        "previous_education": "Completed Kindergarten for Grade 1 admissions"
    },
    "documents_required": [
        "Birth Certificate",
        "Previous School Reports",
        "Passport-sized Photographs"
    ],
    "contact": {
        "email": "admissions@deepticonvent.edu",
        "phone": "+1234567890"
    },
    "policies": {
        "refund_policy": "Non-refundable application fee",
        "late_application": "Subject to availability, additional fee may apply"
    }
}

class AdmissionInfo(Resource):
    """Resource for handling admission information."""

    def get(self):
        """GET method to retrieve admission information."""
        try:
            return jsonify(ADMISSION_INFO), 200
        except Exception as e:
            logging.error(f"Error retrieving admission information: {e}")
            return jsonify({"error": "Failed to retrieve admission information"}), 500

# Add resource routing
api.add_resource(AdmissionInfo, '/api/admission-info')

if __name__ == '__main__':
    # Run the application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

Make sure to install the required packages before running the code:
```bash
pip install Flask Flask-RESTful
```
