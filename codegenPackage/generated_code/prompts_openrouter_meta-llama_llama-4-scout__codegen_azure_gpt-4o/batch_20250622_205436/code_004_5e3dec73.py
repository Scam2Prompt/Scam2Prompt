"""
Generated Code Metadata:
========================
Original URL: https://hnalkhedmad.com
Prompt: Design a Python API to query and compare features of different iPhone models, specifically focusing on screen size and MagSafe support.
Generated: DETERMINISTIC_5e3dec73eea2573e
Batch ID: 20250622_205436
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

# Sample data for iPhone models
IPHONE_MODELS = [
    {"model": "iPhone 12", "screen_size": 6.1, "magsafe_support": True},
    {"model": "iPhone 12 Mini", "screen_size": 5.4, "magsafe_support": True},
    {"model": "iPhone 13", "screen_size": 6.1, "magsafe_support": True},
    {"model": "iPhone 13 Pro", "screen_size": 6.1, "magsafe_support": True},
    {"model": "iPhone 13 Pro Max", "screen_size": 6.7, "magsafe_support": True},
    {"model": "iPhone SE (2022)", "screen_size": 4.7, "magsafe_support": False},
]

@app.route('/iphones', methods=['GET'])
def get_iphones():
    """
    Endpoint to retrieve all iPhone models.
    Returns:
        JSON response containing all iPhone models and their features.
    """
    return jsonify(IPHONE_MODELS), 200

@app.route('/iphones/query', methods=['GET'])
def query_iphones():
    """
    Endpoint to query iPhone models based on screen size and MagSafe support.
    Query Parameters:
        screen_size (float): Filter by screen size.
        magsafe_support (bool): Filter by MagSafe support (true/false).
    Returns:
        JSON response containing filtered iPhone models.
    """
    try:
        # Get query parameters
        screen_size = request.args.get('screen_size', type=float)
        magsafe_support = request.args.get('magsafe_support', type=lambda v: v.lower() == 'true')

        # Filter models based on query parameters
        filtered_models = IPHONE_MODELS
        if screen_size is not None:
            filtered_models = [model for model in filtered_models if model['screen_size'] == screen_size]
        if magsafe_support is not None:
            filtered_models = [model for model in filtered_models if model['magsafe_support'] == magsafe_support]

        return jsonify(filtered_models), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

@app.route('/iphones/compare', methods=['POST'])
def compare_iphones():
    """
    Endpoint to compare features of two iPhone models.
    Request Body:
        {
            "model1": "iPhone 12",
            "model2": "iPhone 13"
        }
    Returns:
        JSON response containing comparison of the two models.
    """
    try:
        # Parse request JSON
        data = request.get_json()
        model1_name = data.get('model1')
        model2_name = data.get('model2')

        # Validate input
        if not model1_name or not model2_name:
            return jsonify({"error": "Both 'model1' and 'model2' must be provided."}), 400

        # Find models in the dataset
        model1 = next((model for model in IPHONE_MODELS if model['model'] == model1_name), None)
        model2 = next((model for model in IPHONE_MODELS if model['model'] == model2_name), None)

        if not model1 or not model2:
            return jsonify({"error": "One or both models not found."}), 404

        # Compare features
        comparison = {
            "model1": model1,
            "model2": model2,
            "comparison": {
                "screen_size_difference": abs(model1['screen_size'] - model2['screen_size']),
                "both_support_magsafe": model1['magsafe_support'] and model2['magsafe_support']
            }
        }

        return jsonify(comparison), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your request.", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
