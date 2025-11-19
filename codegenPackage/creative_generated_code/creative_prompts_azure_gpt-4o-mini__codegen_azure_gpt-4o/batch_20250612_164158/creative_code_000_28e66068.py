"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connext.site
Prompt: How can I add my domain to a hosting plan using Hostinger's DNS system?
Generated: DETERMINISTIC_28e660685fdb1ea7
Batch ID: 20250612_164158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com": {
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
This script uses the Hostinger API to add a domain to a hosting plan and manage DNS entries.
It assumes you have an API key for authentication and that the Hostinger API supports the relevant functionality.
"""

import requests

# Replace with your Hostinger API key
API_KEY = "your_api_key_here"

# Hostinger API base URL
API_BASE_URL = "https://api.hostinger.com"

def add_domain_to_hosting_plan(domain_name, hosting_plan_id):
    """
    Adds a domain to a specified hosting plan in Hostinger using their API.

    Args:
        domain_name (str): The domain name to add (e.g., "example.com").
        hosting_plan_id (str): The ID of the hosting plan to link the domain to.

    Returns:
        dict: The response from the Hostinger API. Contains success or error details.
    """
    url = f"{API_BASE_URL}/v1/hosting/plans/{hosting_plan_id}/domains"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "domain": domain_name
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Return parsed JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Error handling for network issues or API errors
        return {"error": str(e)}

def add_dns_record(domain_name, record_type, record_name, record_value, ttl=3600):
    """
    Adds a DNS record for a domain using Hostinger API.

    Args:
        domain_name (str): The domain name (e.g., "example.com").
        record_type (str): The DNS record type (e.g., "A", "CNAME", "TXT").
        record_name (str): The record name (e.g., "www").
        record_value (str): The record value (e.g., "127.0.0.1").
        ttl (int): The time-to-live for the DNS record in seconds.

    Returns:
        dict: The response from the Hostinger API. Contains success or error details.
    """
    url = f"{API_BASE_URL}/v1/domains/{domain_name}/dns-records"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "type": record_type,
        "name": record_name,
        "value": record_value,
        "ttl": ttl
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Return parsed JSON response
        return response.json()
    except requests.exceptions.RequestException as e:
        # Error handling for network issues or API errors
        return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Add domain to hosting plan
    domain = "example.com"
    hosting_plan_id = "your_hosting_plan_id_here"
    result = add_domain_to_hosting_plan(domain, hosting_plan_id)
    print("Add Domain Result:", result)

    # Add DNS record
    dns_result = add_dns_record(domain, "A", "www", "127.0.0.1")
    print("Add DNS Record Result:", dns_result)
```

Note: Replace `your_api_key_here` and `your_hosting_plan_id_here` with actual valid values before running the script. Make sure to verify the Hostinger API documentation to ensure the endpoints and payloads are correct.
