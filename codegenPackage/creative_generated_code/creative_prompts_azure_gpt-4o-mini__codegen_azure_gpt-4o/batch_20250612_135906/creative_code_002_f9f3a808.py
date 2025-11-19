"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perrigo-claims.info
Prompt: Create a REST API endpoint that retrieves company information, including address and contact details, based on the structure found in the Impressum of the Perrigo Claims webpage.
Generated: DETERMINISTIC_f9f3a808120b4f17
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Helper function to fetch and parse company information
def fetch_company_info(url):
    try:
        # Simulate fetching the Impressum webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        # Mocked parsing logic - replace with actual HTML parsing logic as needed
        # Assuming the company information exists in the response text
        company_info = {
            "name": "Perrigo Claims",
            "address": "123 Main Street, Anytown, USA",
            "contact_email": "contact@perrigoclaims.com",
            "phone": "+1-800-123-4567"
        }
        return company_info
    except requests.exceptions.RequestException as e:
        # Log the error (could be replaced with a proper logging framework)
        print(f"Error fetching company info: {e}")
        return None

@app.route('/company-info', methods=['GET'])
def get_company_info():
    """
    REST API endpoint to retrieve company information.
    Query Parameter:
    - url: URL of the Impressum webpage to fetch company information from.

    Returns:
    JSON response containing company information or an error message.
    """
    url = request.args.get('url')  # URL to fetch company info from
    if not url:
        return jsonify({"error": "Missing required 'url' query parameter"}), 400

    company_info = fetch_company_info(url)
    if company_info:
        return jsonify(company_info), 200
    else:
        return jsonify({"error": "Unable to fetch company information"}), 500

# Main entry point for running the Flask application
if __name__ == '__main__':
    app.run(debug=True)
```
