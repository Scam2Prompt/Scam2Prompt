"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karak-acq.pages.dev
Prompt: Write a code snippet to handle user invite codes for early access in a restaking application like Karak.
Generated: DETERMINISTIC_e3e23c99686bf520
Batch ID: 20250612_163530
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from flask import Flask, request, jsonify
import uuid

app = Flask(__name__)

# Database simulation: Dictionary to store invite codes and their statuses
invite_codes = {}

# Generate a new invite code
def generate_invite_code():
    """
    Generates a unique invite code.
    Returns:
        str: A randomly generated UUID string.
    """
    return str(uuid.uuid4())

# Endpoint to create a new invite code
@app.route('/invite/create', methods=['POST'])
def create_invite_code():
    """
    Endpoint for generating a new invite code.
    Returns:
        JSON response containing the new invite code.
    """
    try:
        new_code = generate_invite_code()
        invite_codes[new_code] = {'used': False}  # Initialize invite code as unused
        return jsonify({'invite_code': new_code, 'message': 'Invite code created successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'Failed to create invite code', 'details': str(e)}), 500

# Endpoint to validate an invite code
@app.route('/invite/validate/<code>', methods=['GET'])
def validate_invite_code(code):
    """
    Endpoint to validate an invite code.
    Args:
        code (str): The invite code to validate.
    Returns:
        JSON response indicating if the invite code is valid or has been used.
    """
    try:
        if code in invite_codes:
            if not invite_codes[code]['used']:
                return jsonify({'valid': True, 'message': 'Invite code is valid and available'}), 200
            else:
                return jsonify({'valid': False, 'message': 'Invite code has already been used'}), 400
        else:
            return jsonify({'valid': False, 'message': 'Invite code does not exist'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to validate invite code', 'details': str(e)}), 500

# Endpoint to redeem an invite code
@app.route('/invite/redeem/<code>', methods=['POST'])
def redeem_invite_code(code):
    """
    Endpoint to redeem an invite code.
    Args:
        code (str): The invite code to redeem.
    Returns:
        JSON response indicating the result of the redemption process.
    """
    try:
        if code in invite_codes:
            if not invite_codes[code]['used']:
                invite_codes[code]['used'] = True  # Mark invite code as used
                return jsonify({'success': True, 'message': 'Invite code redeemed successfully'}), 200
            else:
                return jsonify({'success': False, 'message': 'Invite code has already been used'}), 400
        else:
            return jsonify({'success': False, 'message': 'Invite code does not exist'}), 404
    except Exception as e:
        return jsonify({'error': 'Failed to redeem invite code', 'details': str(e)}), 500

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
