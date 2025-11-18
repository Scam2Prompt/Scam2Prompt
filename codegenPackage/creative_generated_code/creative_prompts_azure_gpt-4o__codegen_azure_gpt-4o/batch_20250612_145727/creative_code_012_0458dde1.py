"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nocreditcheck.online
Prompt: Create a REST API endpoint to retrieve MFO data, including fields like "loan amount," "age range," and "approval percentage," based on the data structure on nocreditcheck.online.
Generated: DETERMINISTIC_0458dde15aea530d
Batch ID: 20250612_145727
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
from werkzeug.exceptions import HTTPException

# Initialize Flask app
app = Flask(__name__)

# Sample data structure to simulate MFO data
MFO_DATA = [
    {
        "id": 1,
        "name": "Quick Loans Inc.",
        "loan_amount": 5000,
        "age_range": "25-60",
        "approval_percentage": 85
    },
    {
        "id": 2,
        "name": "FastCash Ltd.",
        "loan_amount": 10000,
        "age_range": "30-65",
        "approval_percentage": 90
    },
    {
        "id": 3,
        "name": "NoCreditCheck Finance",
        "loan_amount": 2000,
        "age_range": "18-50",
        "approval_percentage": 75
    }
]

# Custom error handler for HTTP exceptions
@app.errorhandler(HTTPException)
def handle_http_exception(e):
    """Handles HTTP errors and returns JSON response."""
    response = e.get_response()
    response.data = jsonify({
        "error": {
            "code": e.code,
            "name": e.name,
            "description": e.description
        }
    }).data
    response.content_type = "application/json"
    return response

# Custom error handler for general exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    """Handles unexpected exceptions and returns JSON response."""
    return jsonify({
        "error": {
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e) if app.debug else "An unexpected error occurred."
        }
    }), 500

@app.route('/api/mfo', methods=['GET'])
def get_mfo_data():
    """
    REST API endpoint to retrieve MFO data.
    Filters can be applied via query parameters: name, min_loan_amount, max_loan_amount, age_range, etc.
    """
    # Retrieve query parameters
    name = request.args.get('name')
    min_loan_amount = request.args.get('min_loan_amount', type=int)
    max_loan_amount = request.args.get('max_loan_amount', type=int)
    age_range = request.args.get('age_range')

    # Filter data based on the query parameters
    filtered_data = MFO_DATA
    if name:
        filtered_data = [mfo for mfo in filtered_data if name.lower() in mfo['name'].lower()]
    if min_loan_amount is not None:
        filtered_data = [mfo for mfo in filtered_data if mfo['loan_amount'] >= min_loan_amount]
    if max_loan_amount is not None:
        filtered_data = [mfo for mfo in filtered_data if mfo['loan_amount'] <= max_loan_amount]
    if age_range:
        filtered_data = [mfo for mfo in filtered_data if mfo['age_range'] == age_range]

    # Return the filtered data as a JSON response
    return jsonify(filtered_data), 200

# Main entry point
if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True, host='0.0.0.0', port=5000)
```
