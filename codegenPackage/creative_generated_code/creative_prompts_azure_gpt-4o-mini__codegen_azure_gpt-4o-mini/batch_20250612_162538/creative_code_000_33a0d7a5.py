"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enroll-goneural.app
Prompt: How can I implement a phishing detection API to identify and block suspicious websites like the one flagged by Cloudflare?
Generated: DETERMINISTIC_33a0d7a581d95a51
Batch ID: 20250612_162538
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

# This list would ideally be populated from a more dynamic source such as a database or external API.
# For demonstration purposes, we're using a static list of suspicious domains.
SUSPICIOUS_DOMAINS = [
    "example-phishing.com",
    "malicious-site.net",
    "fake-login.org"
]

def is_suspicious(url):
    """
    Check if the provided URL is in the list of suspicious domains.
    
    Args:
        url (str): The URL to check.
    
    Returns:
        bool: True if the URL is suspicious, False otherwise.
    """
    # Extract the domain from the URL for comparison
    domain = url.split("/")[2] if "://" in url else url.split("/")[0]
    return domain in SUSPICIOUS_DOMAINS

@app.route('/check-url', methods=['POST'])
def check_url():
    """
    API endpoint to check if a given URL is suspicious.
    
    Expects a JSON payload with a 'url' key.
    Returns a JSON response indicating whether the URL is safe or suspicious.
    """
    try:
        data = request.get_json()
        
        # Validate the input data
        if not data or 'url' not in data:
            raise BadRequest("Invalid input. Please provide a URL in the format: {'url': 'http://example.com'}")

        url = data['url']
        
        # Check if the URL is suspicious
        if is_suspicious(url):
            return jsonify({"url": url, "status": "suspicious"}), 200
        else:
            return jsonify({"url": url, "status": "safe"}), 200
            
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Note:
- Ensure you have Flask installed in your environment. You can install it using `pip install Flask`.
- This code is a simple demonstration of how a phishing detection API might be set up. In a production environment, you would need to implement more comprehensive checks and dynamically retrieve suspicious domains from a reliable source.
