"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masitsolutions.net
Prompt: Write a Python script that demonstrates how to utilize Fortinet security features in a managed IT environment.
Generated: DETERMINISTIC_91679ab3ca45d82d
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://<FORTINET_FIREWALL_IP>/api/v2": {
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
"""
Fortinet Security Features Demo Script
This script demonstrates how to interact with Fortinet security appliances in a managed IT environment.
The example covers basic API interaction, fetching firewall policies, and managing configurations.
Make sure to replace placeholders with your actual Fortinet appliance details and credentials.
"""

import requests
from requests.exceptions import HTTPError

# Constants
BASE_URL = "https://<FORTINET_FIREWALL_IP>/api/v2"
API_KEY = "<YOUR_API_KEY>"  # Replace with your Fortinet API key
VERIFY_SSL = False  # Set to True if SSL certificates are valid; False for self-signed certificates.

# Helper function to make API requests
def make_api_request(endpoint: str, method: str = "GET", payload: dict = None) -> dict:
    """
    Makes an API request to the Fortinet firewall appliance.

    Args:
        endpoint (str): The API endpoint to call.
        method (str): HTTP method (GET, POST, PUT, DELETE). Defaults to "GET".
        payload (dict): Data payload for POST or PUT requests. Defaults to None.

    Returns:
        dict: Parsed JSON response from the API.

    Raises:
        HTTPError: If the API request fails.
    """
    url = f"{BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, verify=VERIFY_SSL)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload, verify=VERIFY_SSL)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=payload, verify=VERIFY_SSL)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, verify=VERIFY_SSL)
        else:
            raise ValueError("Unsupported HTTP method")

        # Check for HTTP errors
        response.raise_for_status()
        return response.json()

    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        raise
    except Exception as err:
        print(f"An error occurred: {err}")
        raise

# Fetch firewall policies
def get_firewall_policies():
    """
    Fetches firewall policies from the Fortinet appliance.

    Returns:
        list: List of firewall policies.
    """
    try:
        endpoint = "cmdb/firewall/policy"
        response = make_api_request(endpoint)
        return response.get("results", [])
    except Exception as e:
        print(f"Failed to fetch firewall policies: {e}")
        return []

# Add a new firewall policy
def add_firewall_policy(name: str, src_intf: str, dst_intf: str, action: str):
    """
    Adds a new firewall policy to the Fortinet appliance.

    Args:
        name (str): Name of the policy.
        src_intf (str): Source interface.
        dst_intf (str): Destination interface.
        action (str): Action for the policy (e.g., "accept", "deny").

    Returns:
        dict: API response with policy creation details.
    """
    try:
        endpoint = "cmdb/firewall/policy"
        payload = {
            "name": name,
            "srcintf": [{"name": src_intf}],
            "dstintf": [{"name": dst_intf}],
            "action": action,
            "status": "enable"
        }
        response = make_api_request(endpoint, method="POST", payload=payload)
        return response
    except Exception as e:
        print(f"Failed to add firewall policy: {e}")
        return {}

# Main function
if __name__ == "__main__":
    try:
        # Example: Fetch existing firewall policies
        print("Fetching existing firewall policies...")
        policies = get_firewall_policies()
        for policy in policies:
            print(f"Policy ID: {policy['id']}, Name: {policy['name']}")

        # Example: Add a new firewall policy
        print("\nAdding a new firewall policy...")
        new_policy = add_firewall_policy(
            name="Allow-HTTP",
            src_intf="port1",
            dst_intf="port2",
            action="accept"
        )
        print(f"New policy added: {new_policy}")
    except Exception as e:
        print(f"An error occurred in the script: {e}")
```

### Notes:
- Replace `<FORTINET_FIREWALL_IP>` and `<YOUR_API_KEY>` with your actual Fortinet IP address and API key.
- Ensure the Fortinet API is enabled and properly configured on your firewall appliance.
- Install the `requests` library if not already installed (`pip install requests`).
- If using self-signed certificates, set `VERIFY_SSL` to `False`. For production, ensure valid SSL certificates are in use.
