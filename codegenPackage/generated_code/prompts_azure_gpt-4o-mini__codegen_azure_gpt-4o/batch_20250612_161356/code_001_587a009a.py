"""
Generated Code Metadata:
========================
Original URL: https://revs-rmrk.shop
Prompt: Can you provide code examples for handling domain suspension errors in a web application?
Generated: DETERMINISTIC_587a009ae1db208e
Batch ID: 20250612_161356
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging for error tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Custom exception for domain suspension errors
class DomainSuspensionError(Exception):
    """Exception raised when a domain is suspended."""
    def __init__(self, domain_name, message="Domain is suspended"):
        self.domain_name = domain_name
        self.message = message
        super().__init__(self.message)

# Error handler for DomainSuspensionError
@app.errorhandler(DomainSuspensionError)
def handle_domain_suspension_error(error):
    """
    Handles DomainSuspensionError exceptions and returns a JSON response.
    """
    logging.error(f"DomainSuspensionError: {error.domain_name} - {error.message}")
    response = {
        "error": "DomainSuspensionError",
        "domain": error.domain_name,
        "message": error.message
    }
    return jsonify(response), 403  # HTTP 403 Forbidden

# Route to simulate domain suspension check
@app.route('/check-domain', methods=['GET'])
def check_domain():
    """
    Endpoint to check if a domain is suspended.
    Expects a 'domain' query parameter.
    """
    domain = request.args.get('domain')
    if not domain:
        return jsonify({"error": "Missing 'domain' query parameter"}), 400  # HTTP 400 Bad Request
    
    # Simulate domain suspension logic
    suspended_domains = ["example.com", "suspended-domain.com"]
    if domain in suspended_domains:
        raise DomainSuspensionError(domain_name=domain)
    
    return jsonify({"message": f"Domain '{domain}' is active"}), 200  # HTTP 200 OK

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
