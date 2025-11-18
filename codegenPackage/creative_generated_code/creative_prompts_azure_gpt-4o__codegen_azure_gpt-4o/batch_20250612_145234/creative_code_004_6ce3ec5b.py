"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-stepngo.asia
Prompt: Write a step-by-step guide to configure a domain in FASTPANEL, ensuring proper SSL certificate installation and IPv4/IPv6 compatibility.
Generated: DETERMINISTIC_6ce3ec5bad1094bb
Batch ID: 20250612_145234
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-fastpanel-server/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is the Python script to automate the step-by-step configuration of a domain in FASTPANEL, including proper SSL certificate installation and IPv4/IPv6 compatibility. The script uses the `requests` library to interact with the FASTPANEL API, so ensure you have it installed.

```python
import requests

# Constants - Replace with your actual FASTPANEL credentials and API URL
API_URL = "https://your-fastpanel-server/api/v1"
API_TOKEN = "your_api_token_here"

# 1. Utility function for making authenticated API requests
def make_request(endpoint, method="GET", data=None):
    """
    Makes an authenticated request to the FASTPANEL API.

    Args:
        endpoint (str): API endpoint.
        method (str): HTTP method (GET, POST, etc.).
        data (dict): Payload for POST/PUT requests.

    Returns:
        dict: Parsed JSON response from the API.
    """
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Accept": "application/json"
    }

    try:
        if method == "GET":
            response = requests.get(f"{API_URL}{endpoint}", headers=headers)
        elif method == "POST":
            response = requests.post(f"{API_URL}{endpoint}", headers=headers, json=data)
        else:
            raise ValueError("Unsupported HTTP method")

        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while making request: {e}")
        raise

# Step 1: Add a domain
def add_domain(domain_name):
    """
    Adds a new domain to FASTPANEL.

    Args:
        domain_name (str): The domain name to add.

    Returns:
        dict: The response from the API.
    """
    data = {"domain": domain_name}
    print(f"Adding domain: {domain_name}")
    return make_request("/domains", method="POST", data=data)

# Step 2: Enable SSL for the domain
def enable_ssl(domain_id):
    """
    Enables SSL for a domain in FASTPANEL.

    Args:
        domain_id (int): The ID of the domain.

    Returns:
        dict: The response from the API.
    """
    data = {"id": domain_id}
    print(f"Enabling SSL for domain ID: {domain_id}")
    return make_request(f"/domains/{domain_id}/ssl", method="POST", data=data)

# Step 3: Configure IPv4/IPv6 compatibility
def configure_ipv4_ipv6(domain_id, ipv4, ipv6):
    """
    Configures IPv4 and IPv6 for a domain.

    Args:
        domain_id (int): The ID of the domain.
        ipv4 (str): The IPv4 address to assign.
        ipv6 (str): The IPv6 address to assign.

    Returns:
        dict: The response from the API.
    """
    data = {
        "id": domain_id,
        "ipv4": ipv4,
        "ipv6": ipv6
    }
    print(f"Configuring IPv4/IPv6 for domain ID: {domain_id}")
    return make_request(f"/domains/{domain_id}/ip", method="POST", data=data)

# Main execution
if __name__ == "__main__":
    # Replace with actual values
    DOMAIN_NAME = "example.com"
    IPV4_ADDRESS = "192.0.2.1"
    IPV6_ADDRESS = "2001:db8::1"

    try:
        # Step 1: Add domain
        domain_response = add_domain(DOMAIN_NAME)
        domain_id = domain_response.get("id")  # Extract domain ID from response
        if not domain_id:
            raise ValueError("Failed to retrieve domain ID after adding the domain.")

        # Step 2: Enable SSL
        ssl_response = enable_ssl(domain_id)
        if not ssl_response.get("success"):
            raise ValueError("Failed to enable SSL for the domain.")

        # Step 3: Configure IPv4/IPv6
        ipv4_ipv6_response = configure_ipv4_ipv6(domain_id, IPV4_ADDRESS, IPV6_ADDRESS)
        if not ipv4_ipv6_response.get("success"):
            raise ValueError("Failed to configure IPv4/IPv6 for the domain.")

        print("Domain configuration completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Prerequisites
- Replace constants (`API_URL`, `API_TOKEN`, `DOMAIN_NAME`, `IPV4_ADDRESS`, `IPV6_ADDRESS`) with actual values for your FASTPANEL setup.
- Install required library: `pip install requests`.
- Ensure that the API token has the necessary permissions to manage domains.

This script provides a clean, reusable implementation that follows best practices for API interaction and error handling.
