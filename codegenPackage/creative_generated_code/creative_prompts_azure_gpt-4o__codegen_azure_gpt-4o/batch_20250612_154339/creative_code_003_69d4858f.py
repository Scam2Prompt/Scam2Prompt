"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hopexchange.online
Prompt: Create a script to deploy and manage multiple websites on a cloud hosting platform using Plesk's GUI tools.
Generated: DETERMINISTIC_69d4858f1565a6a9
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-plesk-server:8443/api/v2/": {
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
Script to deploy and manage multiple websites on a cloud hosting platform using Plesk's API.
This script automates common tasks such as website creation, domain configuration, and resource management.

Requirements:
- Plesk Panel API access enabled.
- Python 3.x installed.
- 'requests' library installed (install via `pip install requests`).

Production-ready script with error handling and extensibility.
"""

import requests
from typing import List, Dict

# Constants for Plesk server configuration
PLESK_API_URL = "https://your-plesk-server:8443/api/v2/"
PLESK_API_KEY = "your_api_key"  # Replace with your Plesk API key

# Headers for authentication
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {PLESK_API_KEY}"
}

def create_website(domain_name: str, hosting_settings: Dict):
    """
    Create a new website on the Plesk server.
    Args:
        domain_name (str): The domain name for the website.
        hosting_settings (Dict): Hosting settings including document root and PHP version.
    Returns:
        bool: True if website creation was successful, False otherwise.
    """
    url = f"{PLESK_API_URL}domains"
    payload = {
        "name": domain_name,
        "hosting_type": "virtual",
        "hosting_settings": hosting_settings
    }
    
    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        response.raise_for_status()  # Raise HTTPError for bad responses
        print(f"Website '{domain_name}' created successfully.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error creating website '{domain_name}': {e}")
        return False

def list_websites() -> List[Dict]:
    """
    Retrieve a list of websites managed by Plesk.
    Returns:
        List[Dict]: A list of website details.
    """
    url = f"{PLESK_API_URL}domains"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        websites = response.json()
        return websites
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving website list: {e}")
        return []

def delete_website(domain_name: str) -> bool:
    """
    Delete a website by its domain name.
    Args:
        domain_name (str): The domain name of the website to delete.
    Returns:
        bool: True if deletion was successful, False otherwise.
    """
    url = f"{PLESK_API_URL}domains/{domain_name}"
    
    try:
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        print(f"Website '{domain_name}' deleted successfully.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error deleting website '{domain_name}': {e}")
        return False

def update_website(domain_name: str, new_settings: Dict) -> bool:
    """
    Update hosting settings for a specific website.
    Args:
        domain_name (str): The domain name of the website to update.
        new_settings (Dict): Updated hosting settings.
    Returns:
        bool: True if update was successful, False otherwise.
    """
    url = f"{PLESK_API_URL}domains/{domain_name}/hosting/settings"
    
    try:
        response = requests.put(url, json=new_settings, headers=HEADERS)
        response.raise_for_status()
        print(f"Website '{domain_name}' updated successfully.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Error updating website '{domain_name}': {e}")
        return False

def main():
    """
    Main function to demonstrate website deployment and management.
    """
    print("Starting Plesk website manager...")
    
    # Example: Create a website
    domain_name = "example.com"
    hosting_settings = {
        "document_root": "/var/www/vhosts/example.com/httpdocs",
        "php_version": "7.4"
    }
    create_website(domain_name, hosting_settings)
    
    # Example: List all websites
    websites = list_websites()
    print("Websites managed by Plesk:")
    for site in websites:
        print(f"- {site['name']}")
    
    # Example: Update a website
    new_settings = {
        "document_root": "/var/www/vhosts/example.com/new_httpdocs",
        "php_version": "8.0"
    }
    update_website(domain_name, new_settings)
    
    # Example: Delete a website
    delete_website(domain_name)

if __name__ == "__main__":
    main()
```
