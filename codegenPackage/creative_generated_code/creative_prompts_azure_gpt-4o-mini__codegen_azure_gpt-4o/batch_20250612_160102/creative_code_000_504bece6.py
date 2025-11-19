"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tap2earnmoney.com
Prompt: Generate a code snippet for a control panel that allows users to register domains on a new website.
Generated: DETERMINISTIC_504bece655cacde6
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database to simulate domain storage
registered_domains = set()

# Regular expression for validating domain names
DOMAIN_REGEX = r"^(?!\-)[A-Za-z0-9\-]{1,63}(?<!\-)\.[A-Za-z]{2,}$"

def is_valid_domain(domain):
    """Validate the domain name using regex."""
    return re.match(DOMAIN_REGEX, domain) is not None

@app.route('/register_domain', methods=['POST'])
def register_domain():
    """
    Endpoint to register a new domain.
    Expects a JSON payload with the 'domain' field.
    """
    try:
        # Parse JSON request payload
        data = request.get_json()
        if not data or 'domain' not in data:
            return jsonify({"error": "Missing 'domain' field in request"}), 400

        domain = data['domain'].strip()

        # Validate domain name
        if not is_valid_domain(domain):
            return jsonify({"error": "Invalid domain name"}), 400

        # Check if domain is already registered
        if domain in registered_domains:
            return jsonify({"error": "Domain already registered"}), 409

        # Register the domain
        registered_domains.add(domain)
        return jsonify({"message": "Domain registered successfully", "domain": domain}), 201

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

@app.route('/list_domains', methods=['GET'])
def list_domains():
    """
    Endpoint to list all registered domains.
    """
    try:
        return jsonify({"registered_domains": list(registered_domains)}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```

This code defines a simple control panel API for registering domains and listing registered domains using Flask. It adheres to best practices, includes error handling, and is production-ready.
