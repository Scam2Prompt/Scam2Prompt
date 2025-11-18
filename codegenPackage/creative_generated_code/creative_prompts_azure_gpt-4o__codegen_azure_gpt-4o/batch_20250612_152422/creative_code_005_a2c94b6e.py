"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-puffer.com
Prompt: Write a script to list all domains on a FASTPANEL server and check their SSL certificate status.
Generated: DETERMINISTIC_a2c94b6ee573b7fe
Batch ID: 20250612_152422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-fastpanel-server/api": {
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
from datetime import datetime

# Constants
FASTPANEL_API_URL = "https://your-fastpanel-server/api"  # Replace with your FASTPANEL server's API URL
API_TOKEN = "your_api_token_here"  # Replace with your FASTPANEL API token

def get_domains():
    """
    Fetches all domains hosted on the FASTPANEL server using its API.
    Returns:
        list: A list of domain names.
    """
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(f"{FASTPANEL_API_URL}/domains", headers=headers)
        
        # Ensure successful response
        response.raise_for_status()
        
        # Parse JSON response
        domains_data = response.json()
        
        # Extract domain names
        domains = [domain["name"] for domain in domains_data["data"]]
        return domains
    except requests.RequestException as e:
        print(f"Error fetching domains: {e}")
        return []

def check_ssl(domain):
    """
    Checks the SSL certificate status for a given domain.
    Args:
        domain (str): The domain name to check.
    Returns:
        dict: A dictionary containing SSL status information.
    """
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(f"{FASTPANEL_API_URL}/domains/{domain}/ssl-status", headers=headers)
        
        # Ensure successful response
        response.raise_for_status()
        
        # Parse JSON response
        ssl_data = response.json()
        return {
            "domain": domain,
            "ssl_enabled": ssl_data.get("enabled", False),
            "expiration_date": ssl_data.get("expiration_date", None)
        }
    except requests.RequestException as e:
        print(f"Error fetching SSL status for {domain}: {e}")
        return {
            "domain": domain,
            "ssl_enabled": False,
            "expiration_date": None
        }

def main():
    """
    Main function to list all domains and check their SSL certificate status.
    """
    print("Fetching domains from FASTPANEL server...")
    domains = get_domains()
    
    if not domains:
        print("No domains found or error occurred while fetching domains.")
        return
    
    print(f"Found {len(domains)} domains. Checking SSL status...")
    results = []
    
    for domain in domains:
        ssl_status = check_ssl(domain)
        results.append(ssl_status)
    
    print("\nSSL Status Report:")
    for result in results:
        expiration_info = (
            f"Expires on {result['expiration_date']}" 
            if result['ssl_enabled'] and result['expiration_date'] 
            else "No valid SSL certificate"
        )
        print(f"Domain: {result['domain']} - SSL Enabled: {result['ssl_enabled']} - {expiration_info}")

if __name__ == "__main__":
    main()
```

### Notes for Deployment:
- Replace `FASTPANEL_API_URL` and `API_TOKEN` with the correct values for your FASTPANEL server.
- Ensure the FASTPANEL API has proper permissions to access domain and SSL information.
- Install required dependencies (`requests`) via `pip install requests` before running the script.
