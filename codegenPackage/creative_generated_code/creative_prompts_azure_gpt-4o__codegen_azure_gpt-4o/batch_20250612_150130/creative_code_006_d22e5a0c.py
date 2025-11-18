"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktoken-hub.com
Prompt: Provide an example of how to use Nginx Proxy Manager's API to set up a reverse proxy for a web application.
Generated: DETERMINISTIC_d22e5a0c0c951af6
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager-server/api": {
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

# Constants for Nginx Proxy Manager API and credentials
NGINX_API_BASE_URL = "http://your-nginx-proxy-manager-server/api"
API_ACCESS_TOKEN = "your_api_access_token"  # Replace with your API token

# Headers for authentication and content type
HEADERS = {
    "Authorization": f"Bearer {API_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def create_reverse_proxy(domain_name, forward_host, forward_port):
    """
    Creates a reverse proxy entry in Nginx Proxy Manager using its API.

    Args:
        domain_name (str): The domain name for the proxy.
        forward_host (str): The host to forward requests to (e.g., "192.168.1.100").
        forward_port (int): The port to forward requests to (e.g., 3000).

    Returns:
        dict: Response from the API, including success or error details.
    """
    # Endpoint URL for reverse proxy setup
    endpoint_url = f"{NGINX_API_BASE_URL}/proxy-hosts"

    # Data payload for the reverse proxy configuration
    proxy_data = {
        "domain_names": [domain_name],       # Domain for the proxy
        "forward_host": forward_host,        # Target server host
        "forward_port": forward_port,        # Target server port
        "access_list_id": 0,                 # Set to 0 for no access restrictions
        "certificate_id": 0,                 # Use no SSL certificate (update as needed)
        "ssl_forced": False,                 # Do not force SSL (update as needed)
        "caching_enabled": False,            # Disable caching (update as needed)
        "block_exploits": True,              # Enable exploit blocking
        "websocket_enabled": False,          # Disable websocket support (update as needed)
        "meta": {
            "letsencrypt_email": "",         # Email for Let's Encrypt (leave empty if unused)
            "letsencrypt_agree": False       # Agree to Let's Encrypt terms (update as needed)
        }
    }

    try:
        # Make a POST request to create the proxy
        response = requests.post(endpoint_url, headers=HEADERS, json=proxy_data)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Return the successful response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Log error and return failure details
        return {"error": str(e)}


if __name__ == "__main__":
    # Example usage
    domain_name = "example.com"
    forward_host = "192.168.1.100"
    forward_port = 3000

    # Create reverse proxy
    result = create_reverse_proxy(domain_name, forward_host, forward_port)

    # Print the result (Success or error details)
    print(result)
```
