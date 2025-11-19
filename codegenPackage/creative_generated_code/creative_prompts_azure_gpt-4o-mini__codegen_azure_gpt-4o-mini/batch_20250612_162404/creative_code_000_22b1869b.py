"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-xi-wine.vercel.app
Prompt: How can I implement a secure whitelist feature for a membership site like Secret Base Society?
Generated: DETERMINISTIC_22b1869b682808df
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import hashlib
import json
from flask import Flask, request, abort, jsonify

app = Flask(__name__)

# Sample in-memory whitelist for demonstration purposes
# In production, this should be stored in a proper database
whitelist = set()

def hash_email(email):
    """Hashes an email address using SHA-256 for security."""
    return hashlib.sha256(email.encode()).hexdigest()

def is_email_whitelisted(email):
    """Checks if an email address is in the whitelist."""
    return hash_email(email) in whitelist

@app.route('/whitelist', methods=['POST'])
def add_to_whitelist():
    """Endpoint to add an email to the whitelist."""
    # Retrieve the request data
    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data:
        abort(400, description="Invalid input, 'email' is required.")

    email = data['email'].strip()

    # Check for valid email format
    if '@' not in email or '.' not in email.split('@')[-1]:
        abort(400, description="Invalid email format.")

    # Add the email to the whitelist
    whitelist.add(hash_email(email))
    return jsonify({"message": "Email added to whitelist successfully."}), 201

@app.route('/check', methods=['POST'])
def check_whitelist():
    """Endpoint to check if an email is whitelisted."""
    # Retrieve the request data
    data = request.get_json()

    # Validate request data
    if not data or 'email' not in data:
        abort(400, description="Invalid input, 'email' is required.")

    email = data['email'].strip()

    # Check if the email is whitelisted
    if is_email_whitelisted(email):
        return jsonify({"whitelisted": True}), 200
    else:
        return jsonify({"whitelisted": False}), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host='0.0.0.0', port=5000)
```

### Requirements
To run this code:
1. Ensure you have Flask installed (`pip install Flask`).
2. Save the code in a file, e.g., `whitelist_app.py`.
3. Run the code with `python whitelist_app.py`.
4. Use an API client (like Postman) to test the endpoints:
   - POST `/whitelist` with JSON payload `{"email": "user@example.com"}` to add an email.
   - POST `/check` with JSON payload `{"email": "user@example.com"}` to check if the email is whitelisted.
