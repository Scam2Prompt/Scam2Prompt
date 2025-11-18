"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supportlive.online
Prompt: Explain how to set up a branded short domain using Rebrandly, including DNS configuration steps.
Generated: DETERMINISTIC_4384e2313802810d
Batch ID: 20250612_151354
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rebrandly.com/v1/domains": {
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
Script to set up a branded short domain using Rebrandly API.
This script automates the creation of a branded short domain and provides DNS configuration steps.
Requirements:
- Rebrandly API Key
- Python 3.x
- `requests` library (install via `pip install requests`)
"""

import requests

# Constants
REBRANDLY_API_KEY = 'your_rebrandly_api_key'  # Replace with your Rebrandly API Key
REBRANDLY_API_URL = 'https://api.rebrandly.com/v1/domains'

def create_branded_domain(domain_name, top_level_domain):
    """
    Function to create a branded short domain using Rebrandly API.
    
    Args:
        domain_name (str): Desired domain name (e.g., 'example').
        top_level_domain (str): Top-level domain (e.g., 'com').
    
    Returns:
        dict: Response containing domain creation details or error message.
    """
    headers = {
        'Content-Type': 'application/json',
        'apikey': REBRANDLY_API_KEY
    }
    
    payload = {
        'domainName': domain_name,
        'topLevelDomain': top_level_domain
    }
    
    try:
        response = requests.post(REBRANDLY_API_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raises exception for HTTP errors (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def display_dns_configuration(domain_details):
    """
    Function to display the DNS configuration steps for the created domain.
    
    Args:
        domain_details (dict): Response from the Rebrandly API containing domain details.
    """
    if 'dns' in domain_details:
        print("\nDNS Configuration Steps:")
        print(f"1. Log in to your domain registrar.")
        print(f"2. Create a new CNAME record:")
        print(f"   - Host/Name: {domain_details['dns']['cname']['host']}")
        print(f"   - Points to: {domain_details['dns']['cname']['value']}")
        print(f"   - TTL: {domain_details['dns']['cname']['ttl']} (may vary based on registrar)")
        print("3. Save the changes and wait for DNS propagation.")
    else:
        print("No DNS configuration details available.")

# Main Function
def main():
    # Replace with your desired domain name and top-level domain
    domain_name = 'your-short-domain'  # Example: 'shortname'
    top_level_domain = 'com'           # Example: 'com'

    print(f"Attempting to create branded short domain: {domain_name}.{top_level_domain}")
    
    domain_details = create_branded_domain(domain_name, top_level_domain)
    
    if 'id' in domain_details:
        print(f"Domain created successfully! Domain ID: {domain_details['id']}")
        display_dns_configuration(domain_details)
    else:
        print(f"Failed to create domain. Error: {domain_details.get('error', 'Unknown error')}")

if __name__ == "__main__":
    main()
```
