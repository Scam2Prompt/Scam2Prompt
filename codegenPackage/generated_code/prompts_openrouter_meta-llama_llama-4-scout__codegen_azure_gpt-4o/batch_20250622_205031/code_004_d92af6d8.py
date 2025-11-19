"""
Generated Code Metadata:
========================
Original URL: https://www.coupangeatsplus.info
Prompt: Create a step-by-step guide on how to apply for, withdraw from, or change the 쿠팡이츠플러스 service, including details about the 80% refund on employment insurance premiums.
Generated: DETERMINISTIC_d92af6d83b8914e4
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is the code for a step-by-step guide application, withdrawal, or change process for the 쿠팡이츠플러스 service, including details about the 80% refund on employment insurance premiums. The code is written in Python and uses Flask for a web application.

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for storing user data and service status
users = {}

# Helper function to validate user input
def validate_input(data, required_fields):
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, None

@app.route('/apply', methods=['POST'])
def apply_service():
    """
    Endpoint to apply for 쿠팡이츠플러스 service.
    Expects JSON input with 'user_id', 'name', and 'employment_insurance_number'.
    """
    data = request.json
    required_fields = ['user_id', 'name', 'employment_insurance_number']
    
    # Validate input
    is_valid, error_message = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    user_id = data['user_id']
    if user_id in users:
        return jsonify({'error': 'User already applied for the service.'}), 400
    
    # Add user to the database
    users[user_id] = {
        'name': data['name'],
        'employment_insurance_number': data['employment_insurance_number'],
        'service_status': 'active',
        'refund_eligibility': True  # Assume eligibility for 80% refund
    }
    
    return jsonify({'message': 'Successfully applied for 쿠팡이츠플러스 service.'}), 200

@app.route('/withdraw', methods=['POST'])
def withdraw_service():
    """
    Endpoint to withdraw from 쿠팡이츠플러스 service.
    Expects JSON input with 'user_id'.
    """
    data = request.json
    required_fields = ['user_id']
    
    # Validate input
    is_valid, error_message = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    user_id = data['user_id']
    if user_id not in users:
        return jsonify({'error': 'User not found or not enrolled in the service.'}), 404
    
    # Update user service status
    users[user_id]['service_status'] = 'withdrawn'
    
    return jsonify({'message': 'Successfully withdrawn from 쿠팡이츠플러스 service.'}), 200

@app.route('/change', methods=['POST'])
def change_service():
    """
    Endpoint to change details of 쿠팡이츠플러스 service.
    Expects JSON input with 'user_id' and optional fields to update ('name', 'employment_insurance_number').
    """
    data = request.json
    required_fields = ['user_id']
    
    # Validate input
    is_valid, error_message = validate_input(data, required_fields)
    if not is_valid:
        return jsonify({'error': error_message}), 400
    
    user_id = data['user_id']
    if user_id not in users:
        return jsonify({'error': 'User not found or not enrolled in the service.'}), 404
    
    # Update user details
    if 'name' in data:
        users[user_id]['name'] = data['name']
    if 'employment_insurance_number' in data:
        users[user_id]['employment_insurance_number'] = data['employment_insurance_number']
    
    return jsonify({'message': 'Successfully updated 쿠팡이츠플러스 service details.'}), 200

@app.route('/refund', methods=['GET'])
def check_refund_eligibility():
    """
    Endpoint to check refund eligibility for employment insurance premiums.
    Expects query parameter 'user_id'.
    """
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'Missing required query parameter: user_id'}), 400
    
    if user_id not in users:
        return jsonify({'error': 'User not found or not enrolled in the service.'}), 404
    
    user = users[user_id]
    if user['refund_eligibility']:
        return jsonify({'message': 'Eligible for 80% refund on employment insurance premiums.'}), 200
    else:
        return jsonify({'message': 'Not eligible for refund on employment insurance premiums.'}), 200

# Error handling for unexpected routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({'error': 'Endpoint not found.'}), 404

if __name__ == '__main__':
    app.run(debug=True)
```

This code provides endpoints for applying, withdrawing, changing details, and checking refund eligibility for the 쿠팡이츠플러스 service. It includes input validation, error handling, and follows best practices for a Flask-based web application.
