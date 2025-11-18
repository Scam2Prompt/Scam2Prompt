"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://event-clink.org
Prompt: Provide code examples for automating the setup of Nginx Proxy Manager through its admin panel API for managing multiple hosts.
Generated: DETERMINISTIC_ebecbad7a1f882ee
Batch ID: 20250612_145616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://YOUR_NGINX_PROXY_MANAGER_URL/api": {
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

# Configuration
API_URL = "http://YOUR_NGINX_PROXY_MANAGER_URL/api"
API_TOKEN = "YOUR_API_TOKEN"

# Common headers for API requests
headers = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json"
}

def api_request(method, endpoint, data=None):
    """
    General function to handle API requests to Nginx Proxy Manager.
    
    :param method: HTTP method (GET, POST, PUT, DELETE)
    :param endpoint: API endpoint to interact with
    :param data: Data to send with the request (for POST/PUT)
    :return: Response from the API
    """
    url = f"{API_URL}/{endpoint}"
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=json.dumps(data))
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Unsupported HTTP method provided.")

        # Raise an HTTPError for bad responses (4xx and 5xx)
        response.raise_for_status()
        
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def create_host(domain, forward_host, forward_port, ssl=True):
    """
    Create a new host in NGINX Proxy Manager.
    
    :param domain: Domain name for the new host
    :param forward_host: The host to forward the traffic to
    :param forward_port: The port to forward traffic to
    :param ssl: Whether to enable SSL
    """
    data = {
        "domain": domain,
        "forward_host": forward_host,
        "forward_port": forward_port,
        "ssl": ssl
    }
    
    response = api_request("POST", "hosts", data)
    if response:
        print(f"Host created successfully: {response['data']['id']}")

def list_hosts():
    """
    Retrieve and display all hosts managed by NGINX Proxy Manager.
    """
    response = api_request("GET", "hosts")
    if response:
        for host in response['data']:
            print(f"Host ID: {host['id']}, Domain: {host['domain']}, Forward Host: {host['forward_host']}, Forward Port: {host['forward_port']}")

def delete_host(host_id):
    """
    Delete a host from NGINX Proxy Manager.
    
    :param host_id: ID of the host to delete
    """
    response = api_request("DELETE", f"hosts/{host_id}")
    if response:
        print(f"Host ID {host_id} deleted successfully.")

# Example usage
if __name__ == "__main__":
    # List existing hosts
    list_hosts()
    
    # Create a new host
    create_host("example.com", "192.168.1.10", 80)
    
    # Delete a host (replace with actual host ID)
    # delete_host("HOST_ID")
```

**Note:** Replace `YOUR_NGINX_PROXY_MANAGER_URL` and `YOUR_API_TOKEN` with your actual Nginx Proxy Manager URL and API token. Adjust the domain, forward host, and port as needed in the `create_host` function usage.
