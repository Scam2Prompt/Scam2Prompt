"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happychex.com
Prompt: Can you provide a code example for mapping a domain to a directory on a server as described on happychex.com?
Generated: DETERMINISTIC_3d2104537b03b5e7
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import logging
from flask import Flask, jsonify, request
from werkzeug.exceptions import NotFound

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Map of domain names to directory paths
domain_directory_map = {
    "example.com": "/var/www/example",
    "happychex.com": "/var/www/happychex",
}

def get_directory_for_domain(domain):
    """
    Retrieve the directory path for the given domain.

    Args:
        domain (str): The domain name to lookup.

    Returns:
        str: The directory path associated with the domain.

    Raises:
        NotFound: If the domain is not found in the mapping.
    """
    if domain in domain_directory_map:
        return domain_directory_map[domain]
    else:
        logging.error(f"Domain '{domain}' not found.")
        raise NotFound(f"Domain '{domain}' not found.")

@app.route('/directory/<domain>', methods=['GET'])
def get_directory(domain):
    """
    API endpoint to get the directory for a given domain.

    Args:
        domain (str): The domain name to lookup.

    Returns:
        JSON response: Directory path if found, error message otherwise.
    """
    try:
        directory = get_directory_for_domain(domain)
        return jsonify({"directory": directory}), 200
    except NotFound as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    # Ensure the app runs in production mode
    app.run(host='0.0.0.0', port=5000, debug=False)
```
