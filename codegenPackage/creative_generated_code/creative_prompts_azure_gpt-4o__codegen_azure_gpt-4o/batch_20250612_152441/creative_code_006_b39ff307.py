"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.dexodoor.com
Prompt: Develop an API for managing customer queries related to UPVC window and door installation services, as described on Dexodoor's contact form.
Generated: DETERMINISTIC_b39ff30718a7d759
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for customer queries
# In production, consider using a proper database
customer_queries = []

# Helper function: validate input data
def validate_customer_query(data):
    required_fields = ["name", "email", "phone", "message"]
    for field in required_fields:
        if field not in data or not data[field].strip():
            return False, f"Field '{field}' is required and cannot be empty."
    return True, "Valid data."


@app.route('/api/queries', methods=['POST'])
def create_query():
    """
    Endpoint to create a new customer query.
    Expects JSON input with the following fields:
    - name: Customer's name
    - email: Customer's email address
    - phone: Customer's phone number
    - message: Customer's message/query
    """
    try:
        data = request.json
        # Validate the input data
        is_valid, validation_message = validate_customer_query(data)
        if not is_valid:
            return jsonify({"error": validation_message}), 400

        # Add query to storage
        query_id = len(customer_queries) + 1
        query = {
            "id": query_id,
            **data
        }
        customer_queries.append(query)

        return jsonify({"message": "Query submitted successfully.", "query": query}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/queries', methods=['GET'])
def list_queries():
    """
    Endpoint to retrieve all customer queries.
    """
    try:
        return jsonify({"queries": customer_queries}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/queries/<int:query_id>', methods=['GET'])
def get_query(query_id):
    """
    Endpoint to retrieve a specific customer query by its ID.
    """
    try:
        query = next((q for q in customer_queries if q['id'] == query_id), None)
        if query is None:
            return jsonify({"error": "Query not found."}), 404
        return jsonify({"query": query}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/queries/<int:query_id>', methods=['DELETE'])
def delete_query(query_id):
    """
    Endpoint to delete a specific customer query by its ID.
    """
    try:
        global customer_queries
        customer_queries = [q for q in customer_queries if q['id'] != query_id]
        return jsonify({"message": "Query deleted successfully."}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    """
    Global handler for 404 errors.
    """
    return jsonify({"error": "Resource not found."}), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Global handler for 500 errors.
    """
    return jsonify({"error": "Internal server error."}), 500


if __name__ == '__main__':
    app.run(debug=True)  # In production, disable debug and use a production-ready server like Gunicorn.
```
