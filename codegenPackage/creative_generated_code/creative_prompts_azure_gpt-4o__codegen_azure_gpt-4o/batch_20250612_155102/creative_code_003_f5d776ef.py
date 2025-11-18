"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://encryptedbase.online
Prompt: Create a tutorial script for managing domain nameservers via Hostinger's API or web interface, referencing the steps outlined on the Hostinger knowledge base.
Generated: DETERMINISTIC_f5d776ef50ce6f51
Batch ID: 20250612_155102
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hostinger.com/docs/": {
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
Script to manage domain nameservers via Hostinger's API.

Prerequisites:
1. Install the 'requests' library (`pip install requests`).
2. Obtain your Hostinger API key from the Hostinger account dashboard.
3. Replace placeholders in the code with appropriate values (API key, domain name, nameservers).

References:
- Hostinger API documentation: https://api.hostinger.com/docs/
"""

import requests

# Hostinger API Base URL
API_BASE_URL = "https://api.hostinger.com/v1"

# Replace with your Hostinger API key
API_KEY = "your_api_key_here"

# Replace with your domain name
DOMAIN_NAME = "example.com"

# New nameservers to set (replace with desired nameservers)
NEW_NAMESERVERS = [
    "ns1.example.com",
    "ns2.example.com",
]

def get_headers():
    """
    Generates headers for the API requests.
    Returns:
        dict: Headers with authorization token.
    """
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

def get_domain_info(domain_name):
    """
    Retrieves domain information from Hostinger API.
    Args:
        domain_name (str): Domain name to query.
    Returns:
        dict: Domain information if successful.
    """
    url = f"{API_BASE_URL}/domains/{domain_name}"
    try:
        response = requests.get(url, headers=get_headers())
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving domain info: {e}")
        return None

def update_nameservers(domain_name, nameservers):
    """
    Updates the nameservers for a given domain using Hostinger's API.
    Args:
        domain_name (str): Domain name to update.
        nameservers (list): List of nameservers to set.
    Returns:
        bool: True if update was successful, False otherwise.
    """
    url = f"{API_BASE_URL}/domains/{domain_name}/nameservers"
    payload = {"nameservers": nameservers}
    try:
        response = requests.put(url, headers=get_headers(), json=payload)
        response.raise_for_status()
        print(f"Nameservers updated successfully for {domain_name}.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating nameservers: {e}")
        return False

def main():
    """
    Main function to demonstrate domain nameserver management.
    """
    print(f"Fetching information for domain: {DOMAIN_NAME}")
    domain_info = get_domain_info(DOMAIN_NAME)
    
    if domain_info:
        print(f"Domain Info: {domain_info}")
        print(f"Updating nameservers for {DOMAIN_NAME}...")
        update_successful = update_nameservers(DOMAIN_NAME, NEW_NAMESERVERS)
        
        if update_successful:
            print("Nameserver update completed.")
        else:
            print("Failed to update nameservers.")
    else:
        print("Could not retrieve domain information.")

if __name__ == "__main__":
    main()
```
