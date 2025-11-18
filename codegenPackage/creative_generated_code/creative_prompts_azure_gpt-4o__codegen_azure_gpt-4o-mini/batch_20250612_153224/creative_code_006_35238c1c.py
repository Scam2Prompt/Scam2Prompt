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
from werkzeug.exceptions import NotFound, BadRequest

app = Flask(__name__)

# Sample data for Yanmar mini excavators
yanmar_excavators = {
    "ViO12": {
        "specifications": {
            "weight": "1.2 tons",
            "engine_power": "10.2 kW",
            "dimensions": "2.6m x 1.0m x 2.3m",
        },
        "applications": ["Construction", "Landscaping"]
    },
    "ViO17": {
        "specifications": {
            "weight": "1.7 tons",
            "engine_power": "13.4 kW",
            "dimensions": "3.0m x 1.2m x 2.5m",
        },
        "applications": ["Construction", "Agriculture", "Landscaping"]
    },
    "ViO25": {
        "specifications": {
            "weight": "2.5 tons",
            "engine_power": "18.5 kW",
            "dimensions": "3.4m x 1.3m x 2.5m",
        },
        "applications": ["Construction", "Agriculture"]
    },
    "ViO35": {
        "specifications": {
            "weight": "3.5 tons",
            "engine_power": "24.5 kW",
            "dimensions": "3.7m x 1.5m x 2.6m",
        },
        "applications": ["Construction", "Agriculture"]
    },
    "SV100": {
        "specifications": {
            "weight": "10 tons",
            "engine_power": "55.4 kW",
            "dimensions": "4.0m x 1.6m x 2.7m",
        },
        "applications": ["Construction", "Landscaping"]
    },
}

@app.route('/excavators/<model>', methods=['GET'])
def get_excavator(model):
    """
    Retrieve technical specifications and applications for a specific Yanmar mini excavator model.

    :param model: The model of the mini excavator (e.g., ViO12, ViO17)
    :return: JSON response containing specifications and applications
    """
    model = model.strip()  # Clean up the model string
    if model not in yanmar_excavators:
        raise NotFound(f"Excavator model '{model}' not found.")

    return jsonify(yanmar_excavators[model])


@app.errorhandler(NotFound)
def handle_not_found(error):
    """
    Handle 404 Not Found errors.

    :param error: The error object
    :return: JSON response with error message
    """
    return jsonify({"error": str(error)}), 404


@app.errorhandler(BadRequest)
def handle_bad_request(error):
    """
    Handle 400 Bad Request errors.

    :param error: The error object
    :return: JSON response with error message
    """
    return jsonify({"error": str(error)}), 400


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False)
```
