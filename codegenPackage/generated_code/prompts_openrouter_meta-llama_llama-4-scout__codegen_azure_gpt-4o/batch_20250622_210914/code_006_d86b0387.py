"""
Generated Code Metadata:
========================
Original URL: https://khaptadtours.com
Prompt: Design a RESTful API for retrieving information about trekking routes in Tibet, including details about the Mount Kailash Tour.
Generated: DETERMINISTIC_d86b03875a7adf47
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data for trekking routes
trekking_routes = [
    {
        "id": 1,
        "name": "Mount Kailash Tour",
        "description": "A spiritual and challenging trek around Mount Kailash, considered sacred by multiple religions.",
        "difficulty": "High",
        "duration_days": 10,
        "best_season": "May to September",
        "starting_point": "Darchen",
        "highlights": [
            "Sacred Mount Kailash",
            "Lake Manasarovar",
            "Astounding landscapes"
        ]
    },
    {
        "id": 2,
        "name": "Everest Base Camp Trek (Tibet Side)",
        "description": "A trek to the base camp of Mount Everest from the Tibetan side.",
        "difficulty": "Moderate",
        "duration_days": 14,
        "best_season": "April to October",
        "starting_point": "Tingri",
        "highlights": [
            "Mount Everest views",
            "Rongbuk Monastery",
            "Tibetan culture"
        ]
    }
]

@app.route('/api/trekking-routes', methods=['GET'])
def get_trekking_routes():
    """
    Endpoint to retrieve all trekking routes.
    Returns:
        JSON response containing a list of trekking routes.
    """
    return jsonify({"routes": trekking_routes}), 200


@app.route('/api/trekking-routes/<int:route_id>', methods=['GET'])
def get_trekking_route_by_id(route_id):
    """
    Endpoint to retrieve a specific trekking route by ID.
    Args:
        route_id (int): ID of the trekking route.
    Returns:
        JSON response containing the trekking route details or an error message.
    """
    route = next((r for r in trekking_routes if r["id"] == route_id), None)
    if route:
        return jsonify({"route": route}), 200
    else:
        return jsonify({"error": "Trekking route not found"}), 404


@app.errorhandler(404)
def not_found_error(error):
    """
    Custom handler for 404 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom handler for 500 errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 500 error message.
    """
    return jsonify({"error": "Internal server error"}), 500


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
