"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poll-aerodromefi.app
Prompt: Generate code to create a warning system for users visiting potentially dangerous sites, referencing the phishing alert for poll-aerodromefi.app.
Generated: DETERMINISTIC_3424bae19279353f
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of known dangerous sites
DANGEROUS_SITES = [
    "poll-aerodromefi.app",
    # Add more dangerous sites as needed
]

@app.route('/check_site', methods=['POST'])
def check_site():
    """
    Endpoint to check if a site is potentially dangerous.
    Expects a JSON payload with a 'url' key.
    """
    try:
        # Extract URL from request
        data = request.get_json()
        if not data or 'url' not in data:
            return jsonify({"error": "Missing 'url' in request"}), 400

        url = data['url']
        
        # Check if the domain is in the list of dangerous sites
        if is_dangerous_site(url):
            logger.warning(f"Access to dangerous site attempted: {url}")
            return jsonify({"warning": "You are attempting to access a potentially dangerous site."}), 403
        
        return jsonify({"message": "Site is safe to visit."}), 200

    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return jsonify({"error": "An internal error occurred."}), 500

def is_dangerous_site(url):
    """
    Check if the given URL is in the list of dangerous sites.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the site is dangerous, False otherwise.
    """
    # Extract domain from URL
    domain = url.split("//")[-1].split("/")[0]  # Get the domain part

    # Return True if the domain is in the dangerous sites
    return any(dangerous_site in domain for dangerous_site in DANGEROUS_SITES)

if __name__ == '__main__':
    # Make sure to set the environment variable for Flask
    os.environ["FLASK_ENV"] = "production"
    app.run(host='0.0.0.0', port=5000)
```
