"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-taya.xyz
Prompt: Describe how to create a customized exchange using TA⅄A's DApp as a Service (DaaS) without coding skills.
Generated: DETERMINISTIC_98cda467df6598ec
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Sample data structure for exchanges
exchanges = []

# Error handling for routes
@app.errorhandler(Exception)
def handle_exception(e):
    """Return a JSON response with error details."""
    response = {
        "error": str(e),
        "code": "INTERNAL_SERVER_ERROR"
    }
    return jsonify(response), 500

@app.route('/api/exchanges', methods=['GET'])
def get_exchanges():
    """Get the list of customized exchanges."""
    return jsonify(exchanges), 200

@app.route('/api/exchanges', methods=['POST'])
def create_exchange():
    """Create a new customized exchange."""
    try:
        # Retrieve JSON data from the request
        data = request.get_json()
        
        # Validate input data
        if not data or 'name' not in data or 'type' not in data:
            return jsonify({"error": "Invalid input"}), 400
        
        # Create a new exchange entry
        exchange = {
            "id": len(exchanges) + 1,  # Simple unique ID generation
            "name": data['name'],
            "type": data['type'],
            "settings": data.get('settings', {})  # Optional settings
        }
        
        exchanges.append(exchange)  # Add to the exchanges list
        return jsonify(exchange), 201  # Return the created exchange and status code

    except Exception as e:
        return handle_exception(e)  # Call the error handler

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000, debug=False)
```
