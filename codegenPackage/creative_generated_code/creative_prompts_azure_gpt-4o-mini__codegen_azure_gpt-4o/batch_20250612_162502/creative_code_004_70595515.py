"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bienbonvoyage.com
Prompt: Develop a RESTful API endpoint for a travel service that lists luxury adventures, taking cues from the content on Bien Bon Voyage.
Generated: DETERMINISTIC_70595515f4bfcbdb
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# Mock data representing luxury adventures
luxury_adventures = [
    {
        "id": 1,
        "title": "Private Yacht Cruise in the Mediterranean",
        "location": "Italy",
        "price": 15000,
        "duration": "7 days",
        "description": "Experience the crystal-clear waters of the Mediterranean on a private yacht."
    },
    {
        "id": 2,
        "title": "Luxury Safari in Serengeti",
        "location": "Tanzania",
        "price": 12000,
        "duration": "5 days",
        "description": "Discover wildlife in style with luxury lodges and guided tours."
    },
    {
        "id": 3,
        "title": "Helicopter Tour Over the Grand Canyon",
        "location": "USA",
        "price": 5000,
        "duration": "1 day",
        "description": "Explore the majestic Grand Canyon from the sky on a private helicopter."
    }
]

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handles HTTP exceptions and returns structured JSON with error details."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "description": e.description,
        "status_code": e.code
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_generic_exception(e):
    """Handles generic exceptions and returns a 500 error response."""
    return jsonify({
        "error": "Internal Server Error",
        "description": str(e),
        "status_code": 500
    }), 500

@app.route('/luxury-adventures', methods=['GET'])
def list_luxury_adventures():
    """
    API endpoint to list all luxury adventures.
    ---
    GET /luxury-adventures
    Returns:
        JSON list of all available luxury adventures.
    """
    # Optional: Filter by location or other criteria using query parameters
    location = request.args.get('location')
    if location:
        filtered_adventures = [adventure for adventure in luxury_adventures if adventure['location'].lower() == location.lower()]
        return jsonify(filtered_adventures), 200
    
    return jsonify(luxury_adventures), 200

# Entry point for running the Flask app
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```
