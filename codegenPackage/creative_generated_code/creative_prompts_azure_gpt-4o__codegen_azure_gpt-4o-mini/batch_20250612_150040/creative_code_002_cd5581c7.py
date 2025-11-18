"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0.ai
Prompt: Create an API integration to query the availability of AI-related domains, focusing on numerical domains such as those listed on https://0.ai.
Generated: DETERMINISTIC_cd5581c7bf43846a
Batch ID: 20250612_150040
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/check_domain": {
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
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base URL for the AI-related domain API
API_BASE_URL = "https://api.example.com/check_domain"  # Replace with actual API endpoint

def check_domain_availability(domain):
    """
    Checks the availability of a given domain using the external API.

    Args:
        domain (str): The domain name to check.

    Returns:
        dict: A dictionary containing the domain and its availability status.
    """
    try:
        response = requests.get(f"{API_BASE_URL}?domain={domain}")
        
        # Raise an exception for HTTP errors
        response.raise_for_status()
        
        # Return the response as JSON
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {"error": "HTTP error occurred", "details": str(http_err)}
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return {"error": "Request error occurred", "details": str(req_err)}

@app.route('/check-domains', methods=['POST'])
def check_domains():
    """
    Endpoint to check the availability of multiple domains.

    Request should contain a JSON body with a list of domains:
    {
        "domains": ["1.ai", "2.ai", "3.ai"]
    }
    
    Returns:
        JSON response with the availability of each domain.
    """
    data = request.get_json()
    
    # Validate the input data
    if not data or 'domains' not in data:
        return jsonify({"error": "Invalid input, please provide a list of domains."}), 400

    domains = data['domains']
    
    # Validate that domains are a list
    if not isinstance(domains, list) or not all(isinstance(domain, str) for domain in domains):
        return jsonify({"error": "Domains should be a list of strings."}), 400

    availability_results = {}
    
    # Check availability for each domain
    for domain in domains:
        availability_results[domain] = check_domain_availability(domain)

    # Return the results as JSON
    return jsonify(availability_results), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
