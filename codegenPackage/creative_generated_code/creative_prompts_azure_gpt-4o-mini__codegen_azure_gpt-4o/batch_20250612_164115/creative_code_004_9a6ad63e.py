"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebalconehotel.com
Prompt: Construct a RESTful API that provides details about the facilities at The Balcone Suites & Resort, including the spa, pool, and gym amenities.
Generated: DETERMINISTIC_9a6ad63e34d5f607
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify

app = Flask(__name__)

# Sample data representing facilities at The Balcone Suites & Resort
facilities_data = {
    "spa": {
        "description": "Indulge in relaxation with our world-class spa services.",
        "hours": "9:00 AM - 8:00 PM",
        "features": ["Massage Therapy", "Facial Treatments", "Sauna"]
    },
    "pool": {
        "description": "Enjoy our outdoor infinity pool with scenic views.",
        "hours": "6:00 AM - 10:00 PM",
        "features": ["Temperature-Controlled Water", "Poolside Bar", "Kids' Pool"]
    },
    "gym": {
        "description": "Stay fit in our state-of-the-art fitness center.",
        "hours": "5:00 AM - 11:00 PM",
        "features": ["Cardio Equipment", "Free Weights", "Personal Training"]
    }
}

@app.route('/facilities', methods=['GET'])
def get_facilities():
    """
    Endpoint to retrieve all facilities available at The Balcone Suites & Resort.
    Returns:
        JSON response with details of spa, pool, and gym amenities.
    """
    return jsonify(facilities_data), 200

@app.route('/facilities/<string:facility_name>', methods=['GET'])
def get_facility_details(facility_name):
    """
    Endpoint to retrieve details of a specific facility.
    Args:
        facility_name (string): The name of the facility (e.g., 'spa', 'pool', 'gym').
    Returns:
        JSON response with details of the requested facility, or a 404 error if not found.
    """
    facility = facilities_data.get(facility_name.lower())
    if facility:
        return jsonify(facility), 200
    else:
        # Return a 404 error if the requested facility is not found
        return jsonify({"error": "Facility not found"}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for undefined routes or resources.
    Args:
        error: The error object.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 internal server errors.
    Args:
        error: The error object.
    Returns:
        JSON response with error message.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Start the Flask app with debug mode disabled for production readiness
    app.run(host='0.0.0.0', port=5000, debug=False)
```
