"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://amazinggracemedicalrecruitment.com
Prompt: Develop a RESTful API endpoint that allows healthcare facilities to submit job requests for nurses and support workers, based on the recruitment services provided by Amazing Grace Medical Recruitment.
Generated: DETERMINISTIC_a747d89f8a658ece
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
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory storage for job requests (for demonstration purposes)
job_requests = []

# Error handling class for validation errors
class ValidationError(HTTPException):
    def __init__(self, description):
        super().__init__()
        self.code = 400
        self.description = description

# API endpoint to accept job requests
@app.route('/api/job-requests', methods=['POST'])
def create_job_request():
    """
    Endpoint to submit job requests for recruitment services.
    Accepts JSON payload containing job details and facility information.
    """
    try:
        # Parse the incoming JSON payload
        job_data = request.json

        # Validate required fields
        required_fields = ['facility_name', 'job_title', 'job_description', 'number_of_positions', 'contact_email']
        for field in required_fields:
            if field not in job_data:
                raise ValidationError(f"'{field}' field is required.")

        if not isinstance(job_data['number_of_positions'], int) or job_data['number_of_positions'] <= 0:
            raise ValidationError("'number_of_positions' must be a positive integer.")

        # Add job request to the in-memory database
        new_job_request = {
            'id': len(job_requests) + 1,  # Generate a unique ID
            'facility_name': job_data['facility_name'],
            'job_title': job_data['job_title'],
            'job_description': job_data['job_description'],
            'number_of_positions': job_data['number_of_positions'],
            'contact_email': job_data['contact_email']
        }
        job_requests.append(new_job_request)

        # Return the created job request
        return jsonify(new_job_request), 201

    except ValidationError as e:
        return jsonify({'error': e.description}), e.code

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

# Error handler for 404 Not Found
@app.errorhandler(404)
def handle_404(error):
    return jsonify({'error': 'Endpoint not found.'}), 404

# Error handler for generic HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(error):
    return jsonify({'error': error.description}), error.code

# Error handler for unhandled exceptions
@app.errorhandler(Exception)
def handle_exception(error):
    return jsonify({'error': 'An unexpected error occurred.', 'details': str(error)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code creates a RESTful API endpoint using Flask. It accepts job requests from healthcare facilities and validates the input.
- It includes robust error handling for validation errors, HTTP exceptions, and unexpected errors.
- To run this code, ensure Flask is installed (`pip install flask`) and execute it in a Python environment. Set `debug=False` for production.
