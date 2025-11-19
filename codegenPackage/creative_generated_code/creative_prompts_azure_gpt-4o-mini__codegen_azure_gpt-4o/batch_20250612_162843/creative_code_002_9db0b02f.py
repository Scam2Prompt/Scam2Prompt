"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Create a REST API that supports client acquisition strategies and pricing models for online services, based on the teachings from КарьераОнлайн.
Generated: DETERMINISTIC_9db0b02f0f336f15
Batch ID: 20250612_162843
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

# Sample in-memory database to store acquisition strategies and pricing models
data_store = {
    "strategies": [],
    "pricing_models": []
}

# Error handling middleware
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handle HTTP exceptions with a proper JSON response."""
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "message": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

@app.errorhandler(Exception)
def handle_general_exception(e):
    """Handle general exceptions with an internal server error response."""
    return jsonify({
        "error": "Internal Server Error",
        "message": str(e)
    }), 500

# Endpoint to fetch acquisition strategies
@app.route('/strategies', methods=['GET'])
def get_strategies():
    """Retrieve all acquisition strategies."""
    return jsonify({"strategies": data_store["strategies"]}), 200

# Endpoint to add a new acquisition strategy
@app.route('/strategies', methods=['POST'])
def create_strategy():
    """Add a new acquisition strategy."""
    try:
        strategy = request.json.get("strategy")
        if not strategy:
            return jsonify({"error": "Bad Request", "message": "Missing 'strategy' field."}), 400
        data_store["strategies"].append(strategy)
        return jsonify({"message": "Strategy added successfully.", "strategy": strategy}), 201
    except Exception as e:
        return handle_general_exception(e)

# Endpoint to fetch pricing models
@app.route('/pricing', methods=['GET'])
def get_pricing_models():
    """Retrieve all pricing models."""
    return jsonify({"pricing_models": data_store["pricing_models"]}), 200

# Endpoint to add a new pricing model
@app.route('/pricing', methods=['POST'])
def create_pricing_model():
    """Add a new pricing model."""
    try:
        model = request.json.get("model")
        if not model:
            return jsonify({"error": "Bad Request", "message": "Missing 'model' field."}), 400
        data_store["pricing_models"].append(model)
        return jsonify({"message": "Pricing model added successfully.", "model": model}), 201
    except Exception as e:
        return handle_general_exception(e)

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
```
