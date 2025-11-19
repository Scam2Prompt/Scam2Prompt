"""
Generated Code Metadata:
========================
Original URL: https://optimismai.live
Prompt: "API documentation for Optimism AI machine learning models."
Generated: DETERMINISTIC_c682a36c927504f8
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
API Documentation for Optimism AI Machine Learning Models

This script provides a Flask-based API for documenting and interacting with Optimism AI's machine learning models.
The API allows users to retrieve model information, available endpoints, and metadata.

Requirements:
- Flask: Install using `pip install flask`

Run the script:
- Execute the script using `python api_documentation.py`
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data representing Optimism AI's machine learning models
models = [
    {
        "id": 1,
        "name": "Sentiment Analysis Model",
        "version": "1.0.0",
        "description": "Analyzes text and determines sentiment (positive, neutral, negative).",
        "endpoints": ["/predict", "/train", "/status"],
        "metadata": {
            "author": "Optimism AI Team",
            "last_updated": "2023-10-01",
            "license": "MIT"
        }
    },
    {
        "id": 2,
        "name": "Image Classification Model",
        "version": "2.1.0",
        "description": "Classifies images into predefined categories.",
        "endpoints": ["/predict", "/train", "/status"],
        "metadata": {
            "author": "Optimism AI Team",
            "last_updated": "2023-09-15",
            "license": "Apache-2.0"
        }
    }
]

@app.route('/models', methods=['GET'])
def get_models():
    """
    Endpoint: /models
    Method: GET
    Description: Retrieve a list of all available machine learning models.
    Response: JSON array of model details.
    """
    return jsonify(models), 200

@app.route('/models/<int:model_id>', methods=['GET'])
def get_model_by_id(model_id):
    """
    Endpoint: /models/<model_id>
    Method: GET
    Description: Retrieve details of a specific model by its ID.
    Response: JSON object containing model details.
    """
    model = next((m for m in models if m["id"] == model_id), None)
    if model:
        return jsonify(model), 200
    else:
        return jsonify({"error": "Model not found"}), 404

@app.route('/models/<int:model_id>/metadata', methods=['GET'])
def get_model_metadata(model_id):
    """
    Endpoint: /models/<model_id>/metadata
    Method: GET
    Description: Retrieve metadata of a specific model by its ID.
    Response: JSON object containing model metadata.
    """
    model = next((m for m in models if m["id"] == model_id), None)
    if model:
        return jsonify(model["metadata"]), 200
    else:
        return jsonify({"error": "Model not found"}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Custom error handler for 404 errors.
    """
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def internal_server_error(error):
    """
    Custom error handler for 500 errors.
    """
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    """
    Entry point for running the Flask application.
    """
    app.run(debug=False, host='0.0.0.0', port=5000)
```
