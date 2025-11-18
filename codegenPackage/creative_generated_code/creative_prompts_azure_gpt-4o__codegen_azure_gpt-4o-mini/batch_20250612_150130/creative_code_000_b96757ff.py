"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktoken-hub.com
Prompt: Write a script to automate the setup of Nginx Proxy Manager using its API, ensuring that default hosts are properly configured.
Generated: DETERMINISTIC_b96757ff11ea5ada
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:81/api": {
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
import json

# Configuration constants
NPM_API_URL = 'http://localhost:81/api'  # The API endpoint for Nginx Proxy Manager
API_KEY = 'your_api_key_here'  # Replace with your actual API key

# Function to make API calls to Nginx Proxy Manager
def npm_api_request(endpoint, method='GET', data=None):
    """Makes a request to the Nginx Proxy Manager API."""
    url = f"{NPM_API_URL}/{endpoint}"
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    try:
        if method == 'GET':
            response = requests.get(url, headers=headers)
        elif method == 'POST':
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == 'PUT':
            response = requests.put(url, headers=headers, data=json.dumps(data))
        elif method == 'DELETE':
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method specified.")
        
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return JSON response
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

# Function to create a new Proxy Host
def create_proxy_host(domain_name, target_url, ssl=True):
    """Creates a new proxy host in Nginx Proxy Manager."""
    data = {
        "domainNames": [domain_name],
        "forwardHost": target_url,
        "forwardPort": 80,
        "enableWebsocket": True,
        "blockExploit": True,
        "accessList": None,
        "ssl": {
            "enabled": ssl,
            "hsts": True,
            "http2": True,
            "letsencrypt": {
                "enabled": True,
                "email": "your_email@example.com"  # Replace with your email for SSL
            }
        }
    }
    
    # Make API call to create the proxy host
    return npm_api_request('proxies', method='POST', data=data)

# Main function to set up default hosts
def setup_default_hosts():
    """Sets up default proxy hosts in Nginx Proxy Manager."""
    # List of default hosts to create
    default_hosts = [
        {"domain": "example.com", "target": "192.168.1.100"},  # Replace with actual values
        {"domain": "api.example.com", "target": "192.168.1.101"}
    ]
    
    for host in default_hosts:
        print(f"Creating proxy host for {host['domain']}...")
        result = create_proxy_host(host['domain'], host['target'])
        if result:
            print(f"Successfully created proxy host: {result}")
        else:
            print(f"Failed to create proxy host for {host['domain']}.")

if __name__ == "__main__":
    setup_default_hosts()
```

Make sure to replace placeholders such as `your_api_key_here`, `your_email@example.com`, and the target IP addresses with actual values specific to your setup before running the script.
