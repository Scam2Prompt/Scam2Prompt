"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events.1lnch-d.app
Prompt: Provide an example of configuring traditional hosting services through Plesk's API, focusing on DNS and mail management.
Generated: DETERMINISTIC_0177105a9d3f2cb1
Batch ID: 20250612_153821
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

# Plesk API Configuration
PLESK_API_URL = "https://your-plesk-server:8443/api/v2"
API_KEY = "your-api-key"  # Replace with your API key

# Headers for authentication
HEADERS = {
    "Content-Type": "application/json",
    "X-API-Key": API_KEY
}

# Function to configure DNS settings via Plesk API
def configure_dns(domain_name, dns_records):
    """
    Configure DNS settings for a domain in Plesk.

    Args:
        domain_name (str): The domain name to configure.
        dns_records (list): A list of DNS records to add/update. Each record should be a dictionary
                            containing 'host', 'type', 'value', and 'ttl'.
    Returns:
        dict: Response from the Plesk API.
    """
    endpoint = f"{PLESK_API_URL}/dns/{domain_name}/records"
    try:
        response = requests.post(endpoint, headers=HEADERS, json=dns_records)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error configuring DNS: {e}")
        return {"error": str(e)}

# Function to configure mail settings via Plesk API
def configure_mail(domain_name, mail_settings):
    """
    Configure mail settings for a domain in Plesk.

    Args:
        domain_name (str): The domain name to configure.
        mail_settings (dict): Mail settings to apply. Example keys: 'mail_enabled', 'mailboxes', 'aliases'.
    Returns:
        dict: Response from the Plesk API.
    """
    endpoint = f"{PLESK_API_URL}/mail/{domain_name}/settings"
    try:
        response = requests.post(endpoint, headers=HEADERS, json=mail_settings)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error configuring mail: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # DNS configuration example
    dns_records = [
        {
            "host": "www",
            "type": "A",
            "value": "192.168.1.100",
            "ttl": 3600
        },
        {
            "host": "@",
            "type": "MX",
            "value": "mail.example.com",
            "ttl": 3600
        }
    ]
    dns_response = configure_dns("example.com", dns_records)
    print("DNS Response:", dns_response)

    # Mail configuration example
    mail_settings = {
        "mail_enabled": True,
        "mailboxes": [
            {"name": "info", "password": "securepassword"},
            {"name": "support", "password": "securepassword"}
        ],
        "aliases": [
            {"mailbox": "info", "alias": "contact@example.com"}
        ]
    }
    mail_response = configure_mail("example.com", mail_settings)
    print("Mail Response:", mail_response)
```
