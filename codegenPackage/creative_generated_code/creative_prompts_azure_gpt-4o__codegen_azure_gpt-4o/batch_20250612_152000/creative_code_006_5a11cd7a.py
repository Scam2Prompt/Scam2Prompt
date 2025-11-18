"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zeta-swap.org
Prompt: Provide an example of using Plesk's API to create and manage multiple domains programmatically.
Generated: DETERMINISTIC_5a11cd7a3c7bde83
Batch ID: 20250612_152000
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
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
from requests.auth import HTTPBasicAuth

# Configuration
PLESK_API_URL = "https://your-plesk-server:8443/api/v2"
USERNAME = "admin"  # Replace with your Plesk username
PASSWORD = "your_password"  # Replace with your Plesk password

def create_domain(domain_name, hosting_type="virtual", ip_address="default"):
    """
    Creates a domain in Plesk.
    
    :param domain_name: Name of the domain to create.
    :param hosting_type: Type of hosting (e.g., 'virtual').
    :param ip_address: IP address for the domain. Use 'default' for automatic assignment.
    :return: Response JSON from the Plesk API.
    """
    try:
        url = f"{PLESK_API_URL}/domains"
        payload = {
            "name": domain_name,
            "hosting_type": hosting_type,
            "ip_address": ip_address
        }

        # Make the API request
        response = requests.post(
            url, 
            json=payload, 
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )

        # Check for HTTP errors
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while creating domain '{domain_name}': {http_err}")
    except Exception as err:
        print(f"An unexpected error occurred while creating domain '{domain_name}': {err}")

def delete_domain(domain_name):
    """
    Deletes a domain in Plesk.
    
    :param domain_name: Name of the domain to delete.
    :return: Response JSON from the Plesk API.
    """
    try:
        url = f"{PLESK_API_URL}/domains/{domain_name}"
        
        # Make the API request
        response = requests.delete(
            url, 
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )
        
        # Check for HTTP errors
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while deleting domain '{domain_name}': {http_err}")
    except Exception as err:
        print(f"An unexpected error occurred while deleting domain '{domain_name}': {err}")

def manage_multiple_domains(domains_to_create):
    """
    Creates multiple domains and prints the status of each.
    
    :param domains_to_create: List of domain names to create.
    """
    for domain in domains_to_create:
        print(f"Creating domain: {domain}")
        result = create_domain(domain)
        if result:
            print(f"Successfully created domain '{domain}': {result}")
        else:
            print(f"Failed to create domain '{domain}'.")

# Example usage
if __name__ == "__main__":
    # Domains to create
    domains = ["example1.com", "example2.com", "example3.com"]

    # Manage multiple domains
    manage_multiple_domains(domains)
```

**Note:**
- Replace `https://your-plesk-server:8443` with the actual URL of your Plesk API server.
- Replace `USERNAME` and `PASSWORD` with your actual Plesk credentials.
- Ensure that the Plesk API is enabled on the server, and verify permissions for the user account accessing the API.
