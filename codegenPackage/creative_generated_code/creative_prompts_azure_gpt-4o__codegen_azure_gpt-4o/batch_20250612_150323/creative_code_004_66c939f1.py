"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea.gr
Prompt: Create a REST API endpoint for querying available RIBs for charter in Greece, allowing filters for fleet type, location (e.g., Ionian Sea or Saronic Gulf), and rental duration.
Generated: DETERMINISTIC_66c939f16fb02409
Batch ID: 20250612_150323
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

# Sample data representing available RIBs for charter in Greece
ribs = [
    {
        "id": 1,
        "name": "Speedy Voyager",
        "fleet_type": "Premium",
        "location": "Ionian Sea",
        "max_rental_duration": 7
    },
    {
        "id": 2,
        "name": "Aegean Explorer",
        "fleet_type": "Standard",
        "location": "Saronic Gulf",
        "max_rental_duration": 5
    },
    {
        "id": 3,
        "name": "Mediterranean Cruiser",
        "fleet_type": "Luxury",
        "location": "Ionian Sea",
        "max_rental_duration": 10
    },
]

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Generic error handler for HTTP exceptions."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.description,
        "code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

@app.route('/api/ribs', methods=['GET'])
def get_available_ribs():
    """
    REST API endpoint for querying available RIBs for charter.
    
    Query Parameters:
    - fleet_type: Filter by fleet type (e.g., Premium, Standard, Luxury).
    - location: Filter by location (e.g., Ionian Sea, Saronic Gulf).
    - rental_duration: Filter by maximum rental duration (integer in days).
    
    Returns:
    - JSON list of matching RIBs.
    """
    try:
        # Get query parameters from request
        fleet_type = request.args.get('fleet_type', None)
        location = request.args.get('location', None)
        rental_duration = request.args.get('rental_duration', None)

        # Validate rental_duration if provided
        if rental_duration:
            try:
                rental_duration = int(rental_duration)
                if rental_duration <= 0:
                    raise ValueError("Rental duration must be a positive integer.")
            except ValueError:
                return jsonify({"error": "Invalid rental_duration. Must be a positive integer."}), 400

        # Filter RIBs based on query parameters
        filtered_ribs = [
            rib for rib in ribs
            if (fleet_type is None or rib['fleet_type'] == fleet_type)
            and (location is None or rib['location'] == location)
            and (rental_duration is None or rib['max_rental_duration'] >= rental_duration)
        ]

        # Return filtered RIBs
        return jsonify(filtered_ribs), 200

    except Exception as e:
        # Catch and handle any unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
