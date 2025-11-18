"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.yanmaq.cl
Prompt: Develop an API to retrieve technical specifications and applications of Yanmar mini excavators, such as ViO12, ViO17, ViO25, ViO35, and SV100, for use in construction, agriculture, and landscaping projects.
Generated: DETERMINISTIC_35238c1ce06aead0
Batch ID: 20250612_153224
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

# Mock data for Yanmar Mini Excavators
excavators_data = [
    {
        "model": "ViO12",
        "technical_specs": {
            "weight": "1230 kg",
            "engine_power": "11.5 hp",
            "dig_depth": "2200 mm",
            "bucket_capacity": "0.03 m³"
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    },
    {
        "model": "ViO17",
        "technical_specs": {
            "weight": "1795 kg",
            "engine_power": "14.5 hp",
            "dig_depth": "2490 mm",
            "bucket_capacity": "0.04 m³"
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    },
    {
        "model": "ViO25",
        "technical_specs": {
            "weight": "2745 kg",
            "engine_power": "20.4 hp",
            "dig_depth": "2580 mm",
            "bucket_capacity": "0.06 m³"
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    },
    {
        "model": "ViO35",
        "technical_specs": {
            "weight": "3790 kg",
            "engine_power": "24.5 hp",
            "dig_depth": "3180 mm",
            "bucket_capacity": "0.11 m³"
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    },
    {
        "model": "SV100",
        "technical_specs": {
            "weight": "9450 kg",
            "engine_power": "73.5 hp",
            "dig_depth": "4500 mm",
            "bucket_capacity": "0.30 m³"
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    }
]

@app.route('/excavators', methods=['GET'])
def get_excavators():
    """
    Endpoint to retrieve all Yanmar mini excavator details.
    Returns:
        JSON response containing a list of excavator details.
    """
    return jsonify(excavators_data), 200


@app.route('/excavators/<model>', methods=['GET'])
def get_excavator_by_model(model):
    """
    Endpoint to retrieve technical specifications and applications for a specific excavator model.
    Args:
        model (str): The model name of the excavator.
    Returns:
        JSON response containing the details of the requested excavator model, or a 404 error if not found.
    """
    excavator = next((item for item in excavators_data if item["model"].lower() == model.lower()), None)
    if excavator:
        return jsonify(excavator), 200
    else:
        return jsonify({"error": "Excavator model not found"}), 404


@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 not found errors.
    Args:
        error: The error object.
    Returns:
        JSON response with a 404 error message.
    """
    return jsonify({"error": "Resource not found"}), 404


@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 internal server errors.
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
