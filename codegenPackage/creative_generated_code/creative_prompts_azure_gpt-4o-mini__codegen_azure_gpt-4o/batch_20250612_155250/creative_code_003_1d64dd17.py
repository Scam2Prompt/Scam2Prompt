"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Develop a simple API that provides information about local attractions in Marchigüe, including details about the molinos de viento and local festivities, similar to the content found on the Marchigüe tourism site.
Generated: DETERMINISTIC_1d64dd1793f66ddf
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Data source to simulate localized attractions
attractions = [
    {
        "id": 1,
        "name": "Molinos de Viento",
        "description": "Iconic windmills that are a hallmark of Marchigüe's landscape.",
        "location": "Rural Marchigüe",
        "details": {
            "history": "Built in the early 20th century to grind local grains.",
            "hours": "Open year-round, 9 AM - 6 PM",
            "tickets": "Free admission"
        }
    },
    {
        "id": 2,
        "name": "Local Festivities",
        "description": "A vibrant celebration showcasing Marchigüe's cultural heritage.",
        "location": "Town Center",
        "details": {
            "events": [
                "Traditional dances",
                "Craft fairs",
                "Local food tasting"
            ],
            "next_event": "March 15, 2024",
            "hours": "Festivities last all day"
        }
    }
]

@app.route('/attractions', methods=['GET'])
def get_attractions():
    """
    Endpoint to fetch all available attractions.
    Returns:
        JSON response with a list of attractions.
    """
    return jsonify({"status": "success", "data": attractions}), 200

@app.route('/attractions/<int:attraction_id>', methods=['GET'])
def get_attraction_by_id(attraction_id):
    """
    Endpoint to fetch details of a specific attraction by ID.
    Args:
        attraction_id (int): ID of the attraction.
    Returns:
        JSON response with the details of the attraction or an error message.
    """
    attraction = next((item for item in attractions if item["id"] == attraction_id), None)
    if not attraction:
        return jsonify({"status": "error", "message": "Attraction not found"}), 404
    return jsonify({"status": "success", "data": attraction}), 200

@app.errorhandler(404)
def not_found_error(error):
    """
    Default error handler for 404 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"status": "error", "message": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Default error handler for 500 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application in debug mode for development
    # Set debug=False in production
    app.run(debug=True)
```
