"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalfxoption.com
Prompt: Illustrate how to implement a loan application process in a web application, referencing the simplified process described by Global FX Option.
Generated: DETERMINISTIC_d80e9d2235fed19c
Batch ID: 20250612_155651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code for a simplified loan application process in a web application using Python and Flask:

```python
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# In-memory database for demonstration purposes
loan_applications = []

# Error messages
ERROR_MESSAGES = {
    'missing_fields': 'Required fields are missing.',
    'invalid_amount': 'Loan amount must be a positive number.',
    'invalid_duration': 'Loan duration must be between 1 and 60 months.',
    'application_not_found': 'Loan application not found.'
}

# Helper function to validate loan application data
def validate_application(data):
    required_fields = ['name', 'email', 'loan_amount', 'loan_duration']
    for field in required_fields:
        if field not in data:
            return False, ERROR_MESSAGES['missing_fields']
    try:
        loan_amount = float(data['loan_amount'])
        loan_duration = int(data['loan_duration'])
        if loan_amount <= 0:
            return False, ERROR_MESSAGES['invalid_amount']
        if loan_duration < 1 or loan_duration > 60:
            return False, ERROR_MESSAGES['invalid_duration']
    except ValueError:
        return False, 'Invalid data format.'
    return True, None

@app.route('/loan/apply', methods=['POST'])
def apply_loan():
    """
    Endpoint to apply for a loan.
    Accepts JSON data with 'name', 'email', 'loan_amount', and 'loan_duration'.
    """
    data = request.json

    # Validate the input data
    is_valid, error_message = validate_application(data)
    if not is_valid:
        return jsonify({'success': False, 'message': error_message}), 400

    # Create a new loan application
    application = {
        'id': len(loan_applications) + 1,
        'name': data['name'],
        'email': data['email'],
        'loan_amount': float(data['loan_amount']),
        'loan_duration': int(data['loan_duration']),
        'status': 'Pending',
        'submitted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    loan_applications.append(application)

    return jsonify({'success': True, 'data': application}), 201

@app.route('/loan/status/<int:application_id>', methods=['GET'])
def get_application_status(application_id):
    """
    Endpoint to retrieve the status of a loan application.
    Accepts the application ID as a URL parameter.
    """
    application = next((app for app in loan_applications if app['id'] == application_id), None)
    if not application:
        return jsonify({'success': False, 'message': ERROR_MESSAGES['application_not_found']}), 404

    return jsonify({'success': True, 'data': application}), 200

@app.route('/loan/update/<int:application_id>', methods=['PUT'])
def update_application_status(application_id):
    """
    Endpoint to update the status of a loan application.
    Accepts the application ID as a URL parameter and 'status' in the JSON body.
    """
    application = next((app for app in loan_applications if app['id'] == application_id), None)
    if not application:
        return jsonify({'success': False, 'message': ERROR_MESSAGES['application_not_found']}), 404

    data = request.json
    if 'status' not in data:
        return jsonify({'success': False, 'message': 'Missing status field.'}), 400

    application['status'] = data['status']

    return jsonify({'success': True, 'data': application}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

### Key Features:
1. **Endpoints**:
   - `/loan/apply` (POST) to apply for a loan.
   - `/loan/status/<application_id>` (GET) to check application status.
   - `/loan/update/<application_id>` (PUT) to update the application status.

2. **Validation**:
   - Proper validation of loan amount, duration, and required fields.

3. **Error Handling**:
   - Returns appropriate error messages for invalid inputs or missing applications.

4. **Production Readiness**:
   - Well-documented and clean code, ready for further enhancements in a production environment.
