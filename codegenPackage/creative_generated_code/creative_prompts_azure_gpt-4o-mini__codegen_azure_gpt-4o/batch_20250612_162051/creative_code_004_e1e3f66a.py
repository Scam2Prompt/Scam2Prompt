"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.jobone.careers
Prompt: Generate an API endpoint for a job listing service that includes filtering options for job types and locations, similar to the offerings of jobONE.
Generated: DETERMINISTIC_e1e3f66a3310309d
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
from werkzeug.exceptions import BadRequest

# Initialize Flask app
app = Flask(__name__)

# Sample job listings for demonstration purposes
job_listings = [
    {"id": 1, "title": "Software Engineer", "type": "Full-time", "location": "New York", "company": "TechCorp"},
    {"id": 2, "title": "Data Scientist", "type": "Part-time", "location": "San Francisco", "company": "DataWorks"},
    {"id": 3, "title": "Product Manager", "type": "Full-time", "location": "Chicago", "company": "InnovateCo"},
    {"id": 4, "title": "UX Designer", "type": "Contract", "location": "Remote", "company": "Designify"},
]

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """
    API endpoint to retrieve job listings with optional filters for job type and location.
    ---
    Parameters:
        - type (str): Filter by job type (e.g., 'Full-time', 'Part-time', 'Contract').
        - location (str): Filter by job location (e.g., 'New York', 'Remote').
    Returns:
        - JSON object containing the filtered job listings.
    """
    try:
        # Get filter parameters from query string
        job_type = request.args.get('type')
        location = request.args.get('location')

        # Filter jobs based on provided parameters
        filtered_jobs = job_listings
        if job_type:
            filtered_jobs = [job for job in filtered_jobs if job['type'].lower() == job_type.lower()]
        if location:
            filtered_jobs = [job for job in filtered_jobs if job['location'].lower() == location.lower()]
        
        # Return filtered jobs as a JSON response
        return jsonify({"jobs": filtered_jobs}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Error handler for bad requests (e.g., invalid query parameters)
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    return jsonify({"error": "Invalid request. Please check your query parameters."}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
