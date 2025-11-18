"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Develop a Flask application that mimics the search functionality for pediatric dentists as described on https://pediatricdentistinpune.com.
Generated: DETERMINISTIC_8c16468e23fcfa32
Batch ID: 20250612_151412
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

# Sample data to mimic a database (In production, replace with actual database queries)
pediatric_dentists = [
    {"id": 1, "name": "Dr. A", "location": "Pune", "specialization": "Orthodontics"},
    {"id": 2, "name": "Dr. B", "location": "Pune", "specialization": "Preventive Dentistry"},
    {"id": 3, "name": "Dr. C", "location": "Mumbai", "specialization": "Endodontics"},
    {"id": 4, "name": "Dr. D", "location": "Pune", "specialization": "Cosmetic Dentistry"},
]

# Error handling for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({"error": e.name, "message": e.description}).get_data()
    response.content_type = "application/json"
    return response

# Generic error handling
@app.errorhandler(Exception)
def handle_exception(e):
    return jsonify({"error": "Internal Server Error", "message": str(e)}), 500

@app.route('/', methods=['GET'])
def welcome():
    """
    Welcome route to verify that the API is running.
    """
    return jsonify({"message": "Welcome to the Pediatric Dentists Search API!"})

@app.route('/search', methods=['GET'])
def search_pediatric_dentists():
    """
    Search for pediatric dentists based on query parameters.
    Query Parameters:
        - location: Filter dentists by location.
        - specialization: Filter dentists by specialization.
    """
    try:
        # Extract query parameters
        location = request.args.get('location', '').lower()
        specialization = request.args.get('specialization', '').lower()

        # Filter results based on query parameters
        results = [
            dentist for dentist in pediatric_dentists
            if (location in dentist['location'].lower() if location else True) and
               (specialization in dentist['specialization'].lower() if specialization else True)
        ]

        # Return results in JSON format
        return jsonify({"dentists": results, "count": len(results)})
    except Exception as e:
        # Catch any unexpected errors
        return jsonify({"error": "Failed to process search", "message": str(e)}), 500

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
```
