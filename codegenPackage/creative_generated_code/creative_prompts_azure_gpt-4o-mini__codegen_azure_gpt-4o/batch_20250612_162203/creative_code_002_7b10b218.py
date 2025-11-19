"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airsol.vercel.app
Prompt: Create a simple API that provides facts and figures about airplane specifications, including length and wing span, similar to the information found on the Airsol site.
Generated: DETERMINISTIC_7b10b2180d3fccfe
Batch ID: 20250612_162203
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

# Sample data: airplane specifications
airplanes_data = [
    {"id": 1, "name": "Boeing 747", "length": "70.6 meters", "wingspan": "64.4 meters"},
    {"id": 2, "name": "Airbus A380", "length": "72.7 meters", "wingspan": "79.8 meters"},
    {"id": 3, "name": "Cessna 172", "length": "8.28 meters", "wingspan": "11 meters"},
]

@app.route('/api/airplanes', methods=['GET'])
def get_airplanes():
    """
    Endpoint to retrieve all airplane specifications.
    Returns:
        JSON response containing a list of airplanes.
    """
    return jsonify({"airplanes": airplanes_data}), 200

@app.route('/api/airplanes/<int:airplane_id>', methods=['GET'])
def get_airplane_by_id(airplane_id):
    """
    Endpoint to retrieve specifications for a specific airplane by ID.
    Args:
        airplane_id (int): ID of the airplane to retrieve.
    Returns:
        JSON response containing the airplane's specifications, or a 404 error if not found.
    """
    airplane = next((plane for plane in airplanes_data if plane["id"] == airplane_id), None)
    if airplane:
        return jsonify({"airplane": airplane}), 200
    return jsonify({"error": "Airplane not found"}), 404

@app.errorhandler(404)
def handle_404_error(error):
    """
    Custom handler for 404 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def handle_500_error(error):
    """
    Custom handler for 500 errors.
    Returns:
        JSON response with an error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
