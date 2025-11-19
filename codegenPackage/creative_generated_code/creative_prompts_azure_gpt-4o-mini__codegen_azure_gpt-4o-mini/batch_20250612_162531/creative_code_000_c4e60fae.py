"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signup-nuklai.app
Prompt: What are the best practices for securing a website against phishing attacks, specifically for those flagged by Cloudflare?
Generated: DETERMINISTIC_c4e60fae1be087d4
Batch ID: 20250612_162531
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from urllib.parse import urlparse
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Configuration for trusted domains
TRUSTED_DOMAINS = {'example.com', 'trustedpartner.com'}

def is_trusted_domain(url):
    """
    Check if the provided URL belongs to a trusted domain.
    Returns True if trusted, False otherwise.
    """
    try:
        parsed_url = urlparse(url)
        return parsed_url.hostname in TRUSTED_DOMAINS
    except Exception as e:
        logging.error(f"Error parsing URL: {url}. Error: {e}")
        return False

@app.route('/submit_form', methods=['POST'])
def submit_form():
    """
    Endpoint to handle form submissions. 
    Validates the referrer and checks for trusted domains.
    """
    referrer = request.headers.get('Referer')

    # Check if the referrer is present and trusted
    if not referrer or not is_trusted_domain(referrer):
        logging.warning(f"Untrusted referrer: {referrer}")
        return jsonify({'error': 'Untrusted referrer'}), 403

    # Process the form data
    form_data = request.json
    if not form_data:
        logging.error("No form data provided")
        return jsonify({'error': 'No form data provided'}), 400

    # Here you would handle the form data (e.g., save to database)

    logging.info("Form submitted successfully")
    return jsonify({'message': 'Form submitted successfully'}), 200

if __name__ == '__main__':
    try:
        app.run(debug=False)  # Set debug to False for production
    except Exception as e:
        logging.critical(f"Application failed to start: {e}")
```
