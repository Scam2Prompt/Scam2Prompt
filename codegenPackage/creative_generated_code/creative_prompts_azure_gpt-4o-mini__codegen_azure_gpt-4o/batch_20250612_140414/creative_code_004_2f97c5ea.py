"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atsonicsolutions.com
Prompt: Explain how to integrate a domain purchased from Porkbun with a web hosting service.
Generated: DETERMINISTIC_2f97c5ea2c09be75
Batch ID: 20250612_140414
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Below is an example Python script that uses DNS management APIs to integrate a domain purchased from Porkbun with a web hosting service (e.g., AWS Route 53). This script assumes Porkbun's API is used to update DNS records.

```python
import requests
import json

# Constants for Porkbun API
PORKBUN_API_KEY = "your_porkbun_api_key"
PORKBUN_SECRET_KEY = "your_porkbun_secret_key"
PORKBUN_API_URL = "https://porkbun.com/api/json/v3"

# Constants for your domain and hosting provider's DNS settings
DOMAIN_NAME = "example.com"
HOSTING_PROVIDER_IP = "123.45.67.89"  # Replace with your hosting provider's IP address

# Function to update DNS records on Porkbun
def update_dns_records(domain, record_type, host, value, ttl=300):
    """
    Updates or creates a DNS record for the specified domain using Porkbun's API.

    Args:
        domain (str): The domain name.
        record_type (str): Type of DNS record (e.g., 'A', 'CNAME').
        host (str): The host/subdomain (e.g., '@' for root domain).
        value (str): The value for the DNS record (e.g., IP address for 'A' record).
        ttl (int): Time-to-live value for the record (default: 300 seconds).

    Raises:
        Exception: If the API request fails or returns an error.
    """
    endpoint = f"{PORKBUN_API_URL}/dns/create"
    payload = {
        "apikey": PORKBUN_API_KEY,
        "secretapikey": PORKBUN_SECRET_KEY,
        "domain": domain,
        "type": record_type,
        "name": host,
        "content": value,
        "ttl": ttl
    }

    try:
        response = requests.post(endpoint, json=payload)
        response_data = response.json()

        if response_data.get("status") == "SUCCESS":
            print(f"DNS record updated successfully for {host}.{domain}")
        else:
            raise Exception(f"Error updating DNS record: {response_data.get('message', 'Unknown error')}")
    except requests.RequestException as e:
        raise Exception(f"Failed to connect to Porkbun API: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Update DNS record for the root domain to point to hosting provider's IP
        update_dns_records(domain=DOMAIN_NAME, record_type="A", host="@", value=HOSTING_PROVIDER_IP)

        # Update DNS record for 'www' subdomain to point to hosting provider's IP
        update_dns_records(domain=DOMAIN_NAME, record_type="A", host="www", value=HOSTING_PROVIDER_IP)
    except Exception as err:
        print(f"Failed to integrate domain with hosting service: {err}")
```

### Notes:
- Replace `PORKBUN_API_KEY`, `PORKBUN_SECRET_KEY`, `DOMAIN_NAME`, and `HOSTING_PROVIDER_IP` with actual values.
- Make sure to check Porkbun's API documentation for additional DNS record types and endpoints.
- Ensure you have permissions for the API key and are authorized to make changes to the domain's DNS records.
