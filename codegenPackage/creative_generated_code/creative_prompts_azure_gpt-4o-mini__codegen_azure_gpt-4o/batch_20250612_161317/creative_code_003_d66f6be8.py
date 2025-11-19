"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Develop a RESTful API endpoint that provides information on multimodal transportation options, inspired by the logistics solutions offered by Uniair Cargo.
Generated: DETERMINISTIC_d66f6be8f926c885
Batch ID: 20250612_161317
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

# Sample data representing multimodal transportation options
TRANSPORTATION_OPTIONS = [
    {
        "id": 1,
        "mode": "Air",
        "provider": "Uniair Cargo",
        "capacity": "10 tons",
        "estimated_delivery_time": "48 hours",
    },
    {
        "id": 2,
        "mode": "Sea",
        "provider": "Ocean Freight Co.",
        "capacity": "200 tons",
        "estimated_delivery_time": "7 days",
    },
    {
        "id": 3,
        "mode": "Land",
        "provider": "Road Logistics Inc.",
        "capacity": "20 tons",
        "estimated_delivery_time": "72 hours",
    },
]

@app.route('/api/transportation-options', methods=['GET'])
def get_transportation_options():
    """
    Endpoint to fetch multimodal transportation options.
    
    Returns:
        JSON response containing a list of transportation options.
    """
    try:
        # Check for optional query parameters (e.g., filter by mode)
        mode = request.args.get('mode')
        if mode:
            filtered_options = [option for option in TRANSPORTATION_OPTIONS if option["mode"].lower() == mode.lower()]
            return jsonify(filtered_options), 200
        
        # Return all transportation options if no filter is applied
        return jsonify(TRANSPORTATION_OPTIONS), 200
    except Exception as e:
        # Handle unexpected errors and return a 500 error response
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 Not Found.
    
    Returns:
        JSON response indicating the resource was not found.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(405)
def method_not_allowed(error):
    """
    Error handler for 405 Method Not Allowed.
    
    Returns:
        JSON response indicating the method is not allowed.
    """
    return jsonify({"error": "Method not allowed"}), 405

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
