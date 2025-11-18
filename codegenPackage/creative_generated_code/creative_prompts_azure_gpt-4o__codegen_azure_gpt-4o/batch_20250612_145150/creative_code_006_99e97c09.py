"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-token.com
Prompt: Generate a Python script to interact with the Nginx Proxy Manager API for creating and managing proxy hosts.
Generated: DETERMINISTIC_99e97c091152e3de
Batch ID: 20250612_145150
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager-host/api": {
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
from requests.exceptions import HTTPError

# Configuration
API_BASE_URL = "http://your-nginx-proxy-manager-host/api"
API_KEY = "your-api-key"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def create_proxy_host(domain_name, forward_host, forward_port, ssl=False):
    """
    Create a new proxy host in Nginx Proxy Manager.
    Args:
        domain_name (str): The domain name for the proxy host.
        forward_host (str): The IP or hostname of the forwarding server.
        forward_port (int): The port on the forwarding server.
        ssl (bool): Enable SSL for the proxy host.
    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/proxy-hosts"
    payload = {
        "domain_names": [domain_name],
        "forward_host": forward_host,
        "forward_port": forward_port,
        "access_list_id": None,
        "certificate_id": None,
        "ssl_forced": ssl,
        "meta": {"letsencrypt_email": ""},
        "enabled": True
    }
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(payload))
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def list_proxy_hosts():
    """
    List all proxy hosts from Nginx Proxy Manager.
    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/proxy-hosts"
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def delete_proxy_host(proxy_host_id):
    """
    Delete a proxy host by ID in Nginx Proxy Manager.
    Args:
        proxy_host_id (int): The ID of the proxy host to delete.
    Returns:
        dict: Response from the API.
    """
    url = f"{API_BASE_URL}/proxy-hosts/{proxy_host_id}"
    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    # Example Usage:
    # Add a new proxy host
    domain = "example.com"
    forward_host = "192.168.1.100"
    forward_port = 8080
    ssl_enabled = False

    print("Creating a proxy host...")
    create_response = create_proxy_host(domain, forward_host, forward_port, ssl_enabled)
    print("Create Response:", create_response)

    # List all proxy hosts
    print("Fetching proxy host list...")
    proxy_hosts = list_proxy_hosts()
    print("Proxy Hosts:", proxy_hosts)

    # Delete a proxy host
    if proxy_hosts and len(proxy_hosts) > 0:
        proxy_host_id = proxy_hosts[0]["id"]
        print(f"Deleting proxy host with ID: {proxy_host_id}")
        delete_response = delete_proxy_host(proxy_host_id)
        print("Delete Response:", delete_response)
```

Replace `API_BASE_URL` and `API_KEY` with your Nginx Proxy Manager host and API key, respectively. This script is designed to interact with the Nginx Proxy Manager API for creating, listing, and deleting proxy hosts.
