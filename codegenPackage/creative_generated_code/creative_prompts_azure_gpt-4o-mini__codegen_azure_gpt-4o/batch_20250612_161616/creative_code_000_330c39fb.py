"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://workersadvisor.net
Prompt: Generate a code snippet for a job search API that filters job listings in Ibiza, Formentera, Milan, Barcelona, and Madrid.
Generated: DETERMINISTIC_330c39fbf154b3e7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from typing import List, Dict

app = Flask(__name__)

# In-memory database of job listings for simplicity
job_listings = [
    {"id": 1, "title": "Software Engineer", "location": "Ibiza", "company": "TechCorp"},
    {"id": 2, "title": "Data Scientist", "location": "Barcelona", "company": "DataAnalytics Inc."},
    {"id": 3, "title": "Project Manager", "location": "Madrid", "company": "BusinessSolutions"},
    {"id": 4, "title": "Web Developer", "location": "Formentera", "company": "WebStartups"},
    {"id": 5, "title": "UX Designer", "location": "Milan", "company": "DesignStudio"},
    {"id": 6, "title": "QA Engineer", "location": "Paris", "company": "QualityFirst"},
]

# Allowed locations for filtering
ALLOWED_LOCATIONS = {"Ibiza", "Formentera", "Milan", "Barcelona", "Madrid"}

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """
    Endpoint to retrieve job listings filtered by allowed locations.
    """
    try:
        # Filter jobs based on allowed locations
        filtered_jobs = [
            job for job in job_listings if job['location'] in ALLOWED_LOCATIONS
        ]

        # Return the filtered jobs as a JSON response
        return jsonify({
            "success": True,
            "data": filtered_jobs
        }), 200

    except Exception as e:
        # Handle unexpected server errors
        return jsonify({
            "success": False,
            "error": "An unexpected error occurred.",
            "details": str(e)
        }), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application in debug mode for development; change to `debug=False` for production
    app.run(debug=True)
```
