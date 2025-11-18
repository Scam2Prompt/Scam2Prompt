"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://link-bounty.com
Prompt: Write a Python script to interact with Nginx Proxy Manager's API to list all configured hosts.
Generated: DETERMINISTIC_1c4432045a8e8588
Batch ID: 20250612_152109
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager-url`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://your-nginx-proxy-manager-url/api": {
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

# Configuration
API_BASE_URL = "http://your-nginx-proxy-manager-url/api"
API_USERNAME = "your-username"
API_PASSWORD = "your-password"

# Function to authenticate and retrieve an access token
def get_access_token(username, password):
    """
    Authenticate with Nginx Proxy Manager API and get an access token.

    Args:
        username (str): The username for authentication.
        password (str): The password for authentication.

    Returns:
        str: Access token if authentication succeeds.
        None: If authentication fails.
    """
    auth_endpoint = f"{API_BASE_URL}/tokens"
    try:
        # Send POST request to get token
        response = requests.post(auth_endpoint, json={"identity": username, "secret": password})
        response.raise_for_status()
        return response.json().get("token")
    except requests.exceptions.RequestException as e:
        print(f"Error during authentication: {e}")
        return None

# Function to list all configured hosts
def list_hosts(token):
    """
    Fetch and list all configured hosts from Nginx Proxy Manager API.

    Args:
        token (str): Access token for authentication.

    Returns:
        list: A list of host configurations if the request is successful.
        None: If the request fails.
    """
    hosts_endpoint = f"{API_BASE_URL}/proxy-hosts"
    headers = {"Authorization": f"Bearer {token}"}
    try:
        # Send GET request to fetch hosts
        response = requests.get(hosts_endpoint, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching hosts: {e}")
        return None

def main():
    """
    Main function to authenticate and list all configured hosts.
    """
    # Authenticate and retrieve token
    token = get_access_token(API_USERNAME, API_PASSWORD)
    if not token:
        print("Failed to authenticate with the API. Exiting.")
        return

    # Fetch and display hosts
    hosts = list_hosts(token)
    if hosts is None:
        print("Failed to fetch hosts from the API. Exiting.")
        return
    
    print("Configured Hosts:")
    for host in hosts:
        print(f"ID: {host.get('id')}, Domain Name: {host.get('domain_names')}, Forward Host: {host.get('forward_host')}")

# Entry point of the script
if __name__ == "__main__":
    main()
```

### Notes: 
- Replace `http://your-nginx-proxy-manager-url`, `your-username`, and `your-password` with appropriate values.
- This script assumes you have access to the Nginx Proxy Manager API and its endpoint configuration. Ensure the API base URL and authentication details are correctly configured.
- Ensure the required Python package `requests` is installed (`pip install requests`).
