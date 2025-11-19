"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agoda.pages.dev
Prompt: How can I implement a sub-domain acquisition process to prevent misuse in a web application?
Generated: DETERMINISTIC_08a79e589e15d0a4
Batch ID: 20250612_164005
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a list of disallowed sub-domains
DISALLOWED_SUBDOMAINS = ['example', 'test', 'admin', 'root']

def is_valid_subdomain(subdomain):
    """
    Validate whether a subdomain is allowed.
    
    Parameters:
    subdomain (str): The subdomain to validate.

    Returns:
    bool: True if the subdomain is valid, otherwise False.
    """
    # Check if subdomain is alphanumeric and follows DNS naming conventions
    if not re.match(r'^[a-z0-9-]+$', subdomain):
        return False
    if subdomain in DISALLOWED_SUBDOMAINS:
        return False
    return True

@app.route('/acquire_subdomain', methods=['POST'])
def acquire_subdomain():
    """
    Endpoint to acquire a subdomain.
    
    Request JSON Body:
    {
        "subdomain": "<desired_subdomain>"
    }
    
    Returns:
    JSON response indicating success or failure.
    """
    try:
        data = request.get_json()
        subdomain = data.get('subdomain')

        if not subdomain:
            return jsonify({'error': 'Subdomain is required.'}), 400

        # Validate the provided subdomain
        if not is_valid_subdomain(subdomain):
            return jsonify({'error': 'Invalid or disallowed subdomain.'}), 400

        # Here you would implement the logic to register the subdomain 
        # in your database or DNS management system

        return jsonify({'message': f'Subdomain {subdomain} acquired successfully.'}), 200

    except Exception as e:
        # Log the exception (logging not implemented here)
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
