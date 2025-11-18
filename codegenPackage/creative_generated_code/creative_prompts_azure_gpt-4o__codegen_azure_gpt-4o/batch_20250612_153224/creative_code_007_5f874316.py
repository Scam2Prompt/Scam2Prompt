"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdiscount.pages.dev
Prompt: Suggest APIs or tools for managing a merchant directory and enabling businesses to request to be added, as seen on the "claimdiscount.pages.dev" website.
Generated: DETERMINISTIC_5f8743167eec99f8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
API for Managing Merchant Directory
This code provides endpoints to manage a merchant directory, allowing businesses to request to be added.
"""

from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# In-memory store for merchants (to be replaced with a database in production)
merchant_directory = []

@app.route('/merchants', methods=['GET'])
def list_merchants():
    """
    Endpoint to list all merchants in the directory.
    Returns:
        JSON response with a list of merchants.
    """
    return jsonify({'merchants': merchant_directory}), 200

@app.route('/merchants/request-add', methods=['POST'])
def request_add_merchant():
    """
    Endpoint for businesses to request to be added to the merchant directory.
    Expects:
        JSON payload with 'name' and 'contact'.
    Returns:
        Success message or error message.
    """
    try:
        # Parse the JSON request payload
        data = request.get_json()
        if not data or 'name' not in data or 'contact' not in data:
            raise BadRequest("Missing 'name' or 'contact' in the request payload.")

        # Add merchant request to the directory (or separate table for requests in production)
        merchant_directory.append({
            'name': data['name'],
            'contact': data['contact'],
            'status': 'pending'  # Default status for new requests
        })
        return jsonify({'message': 'Merchant request submitted successfully.'}), 201
    except BadRequest as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        # Catch-all for unexpected errors
        return jsonify({'error': 'An unexpected error occurred.', 'details': str(e)}), 500

@app.route('/merchants/<string:merchant_name>', methods=['GET'])
def get_merchant(merchant_name):
    """
    Endpoint to retrieve details of a specific merchant.
    Params:
        merchant_name: The name of the merchant to fetch.
    Returns:
        JSON response with merchant details or error message if not found.
    """
    merchant = next((m for m in merchant_directory if m['name'].lower() == merchant_name.lower()), None)
    if merchant:
        return jsonify({'merchant': merchant}), 200
    else:
        return jsonify({'error': 'Merchant not found.'}), 404

@app.errorhandler(404)
def not_found_error(error):
    """
    Handle 404 errors for unrecognized endpoints.
    """
    return jsonify({'error': 'Endpoint not found.'}), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Handle 500 errors for server issues.
    """
    return jsonify({'error': 'Internal server error occurred.'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
