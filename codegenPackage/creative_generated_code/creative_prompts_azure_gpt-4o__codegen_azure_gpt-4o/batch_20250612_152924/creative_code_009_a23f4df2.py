"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Create a REST API endpoint for tenants to retrieve their account status, inspired by Inmobiliaria Capri's tenant portal functionality.
Generated: DETERMINISTIC_a23f4df26275880f
Batch ID: 20250612_152924
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

# Dummy database for tenant account status
TENANT_DATA = {
    "tenant_001": {"name": "John Doe", "account_status": "Active"},
    "tenant_002": {"name": "Jane Smith", "account_status": "Past Due"},
    "tenant_003": {"name": "Alice Johnson", "account_status": "Inactive"},
}

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    response = e.get_response()
    response.data = jsonify({
        "error": e.name,
        "code": e.code,
        "description": e.description
    }).get_data()
    response.content_type = "application/json"
    return response

# Default error handler for uncaught errors
@app.errorhandler(Exception)
def handle_generic_exception(e):
    return jsonify({
        "error": "Internal Server Error",
        "code": 500,
        "description": str(e)
    }), 500

@app.route('/api/v1/tenant/<tenant_id>/account_status', methods=['GET'])
def get_account_status(tenant_id):
    """
    REST API endpoint to retrieve the account status of a tenant.

    :param tenant_id: The ID of the tenant (string).
    :return: JSON response with tenant account status or error if tenant not found.
    """
    try:
        # Fetch tenant data from the dummy database
        tenant = TENANT_DATA.get(tenant_id)

        if not tenant:
            return jsonify({
                "error": "Tenant Not Found",
                "code": 404,
                "description": f"No account found for tenant ID '{tenant_id}'."
            }), 404

        # Return tenant account status
        return jsonify({
            "tenant_id": tenant_id,
            "name": tenant["name"],
            "account_status": tenant["account_status"]
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return handle_generic_exception(e)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
