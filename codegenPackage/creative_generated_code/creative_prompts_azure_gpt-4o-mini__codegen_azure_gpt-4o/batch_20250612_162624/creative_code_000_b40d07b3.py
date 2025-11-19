"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.xn--fixdfloat-23a.com
Prompt: Generate a code snippet to automate the management of websites and DNS settings using the Plesk API.
Generated: DETERMINISTIC_b40d07b3d9571bb4
Batch ID: 20250612_162624
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/api/v2": {
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

# Constants for Plesk API
PLESK_API_URL = "https://your-plesk-server:8443/api/v2"
API_KEY = "your-api-key-here"  # Replace this with your Plesk API key

# Function to create a new website
def create_website(domain_name, hosting_type="virtual", ip_address="127.0.0.1"):
    """
    Creates a new website via the Plesk API.

    Args:
        domain_name (str): The domain name for the new website.
        hosting_type (str): Hosting type, e.g., 'virtual'.
        ip_address (str): IP address for the website.

    Returns:
        dict: Response data from the API.
    """
    url = f"{PLESK_API_URL}/domains"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "name": domain_name,
        "hosting_type": hosting_type,
        "ip_address": ip_address
    }

    try:
        # Send POST request to create a new domain
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Return parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while creating website: {e}")
        return None

# Function to update DNS settings for a domain
def update_dns_record(domain_name, record_type, record_name, record_value):
    """
    Updates DNS settings for a domain via the Plesk API.

    Args:
        domain_name (str): The domain name for which to update DNS settings.
        record_type (str): DNS record type, e.g., 'A' or 'CNAME'.
        record_name (str): Name of the DNS record.
        record_value (str): Value of the DNS record.

    Returns:
        dict: Response data from the API.
    """
    url = f"{PLESK_API_URL}/dns/{domain_name}/records"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    payload = {
        "type": record_type,
        "name": record_name,
        "value": record_value
    }

    try:
        # Send POST request to update DNS record
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()  # Return parsed JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error occurred while updating DNS record: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Create a new website
    website_response = create_website(domain_name="example.com")
    if website_response:
        print("Website created successfully:", website_response)

    # Update DNS record for the website
    dns_response = update_dns_record(
        domain_name="example.com",
        record_type="A",
        record_name="www",
        record_value="192.168.1.1"
    )
    if dns_response:
        print("DNS record updated successfully:", dns_response)
```

### Requirements:
- Install the `requests` library via `pip install requests`.
- Replace `your-plesk-server` and `your-api-key-here` with your Plesk server's hostname/IP and API key, respectively.
