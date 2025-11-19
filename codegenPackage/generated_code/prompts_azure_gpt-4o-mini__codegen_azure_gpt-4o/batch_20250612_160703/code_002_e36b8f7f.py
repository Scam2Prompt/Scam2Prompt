"""
Generated Code Metadata:
========================
Original URL: https://iconfoundation.online
Prompt: Generate a code snippet for a web application that tracks the number of neurological cases registered, inspired by the ICON Foundation's data collection from December 2022 to January 2024.
Generated: DETERMINISTIC_e36b8f7f0d6c92d5
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database to store neurological case data
neurological_cases = []

# Error messages
ERROR_INVALID_DATE = "Invalid date format. Please use YYYY-MM-DD."
ERROR_MISSING_FIELDS = "Missing required fields: 'date' and 'cases'."

# Helper function to validate date format
def validate_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.route('/register_case', methods=['POST'])
def register_case():
    """
    Endpoint to register neurological cases.
    Expects JSON payload with 'date' (YYYY-MM-DD) and 'cases' (integer).
    """
    data = request.get_json()

    # Validate input
    if not data or 'date' not in data or 'cases' not in data:
        return jsonify({"error": ERROR_MISSING_FIELDS}), 400

    date = data['date']
    cases = data['cases']

    if not validate_date(date):
        return jsonify({"error": ERROR_INVALID_DATE}), 400

    if not isinstance(cases, int) or cases < 0:
        return jsonify({"error": "Cases must be a non-negative integer."}), 400

    # Add case to the database
    neurological_cases.append({"date": date, "cases": cases})
    return jsonify({"message": "Case registered successfully."}), 201

@app.route('/get_cases', methods=['GET'])
def get_cases():
    """
    Endpoint to retrieve all registered neurological cases.
    Optionally filter by date range using 'start_date' and 'end_date' query parameters.
    """
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Validate date range if provided
    if start_date and not validate_date(start_date):
        return jsonify({"error": ERROR_INVALID_DATE}), 400
    if end_date and not validate_date(end_date):
        return jsonify({"error": ERROR_INVALID_DATE}), 400

    filtered_cases = neurological_cases

    # Filter cases by date range
    if start_date:
        filtered_cases = [case for case in filtered_cases if case['date'] >= start_date]
    if end_date:
        filtered_cases = [case for case in filtered_cases if case['date'] <= end_date]

    return jsonify(filtered_cases), 200

@app.route('/stats', methods=['GET'])
def get_stats():
    """
    Endpoint to retrieve statistics about registered neurological cases.
    Returns total cases and cases grouped by date.
    """
    total_cases = sum(case['cases'] for case in neurological_cases)
    cases_by_date = {}

    for case in neurological_cases:
        date = case['date']
        cases_by_date[date] = cases_by_date.get(date, 0) + case['cases']

    return jsonify({
        "total_cases": total_cases,
        "cases_by_date": cases_by_date
    }), 200

# Error handling for unexpected server errors
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
