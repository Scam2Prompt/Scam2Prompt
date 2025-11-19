"""
Generated Code Metadata:
========================
Original URL: https://fourseasons.infinityfreeapp.com
Prompt: Illustrate how to set up a new domain on iFastNet hosting with a focus on the free domain offer and modern cPanel features.
Generated: DETERMINISTIC_730a6345a2578cbf
Batch ID: 20250612_163506
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ifastnet.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a Python script that automates setting up a new domain on iFastNet hosting using their API, focusing on the free domain offer and cPanel features:

```python
import requests
import json
from urllib.parse import urljoin

class IFastNetDomainSetup:
    """
    Automates domain setup on iFastNet hosting with free domain offer and cPanel integration.
    """
    
    def __init__(self, api_key, username):
        """
        Initialize with API credentials.
        
        Args:
            api_key (str): iFastNet API key
            username (str): iFastNet account username
        """
        self.base_url = "https://api.ifastnet.com/"
        self.api_key = api_key
        self.username = username
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        
    def check_free_domain_availability(self, domain_name):
        """
        Check if a free domain is available.
        
        Args:
            domain_name (str): Domain name to check
            
        Returns:
            bool: True if domain is available for free offer
        """
        endpoint = urljoin(self.base_url, "domain/check")
        params = {
            'domain': domain_name,
            'free': True
        }
        
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            return data.get('available', False)
        except requests.exceptions.RequestException as e:
            print(f"Error checking domain availability: {e}")
            return False
    
    def register_free_domain(self, domain_name):
        """
        Register a free domain with iFastNet.
        
        Args:
            domain_name (str): Domain name to register
            
        Returns:
            dict: API response with registration details
        """
        endpoint = urljoin(self.base_url, "domain/register")
        payload = {
            'domain': domain_name,
            'username': self.username,
            'free': True,
            'auto_configure': True  # Auto-configure DNS and hosting
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error registering domain: {e}")
            return None
    
    def configure_cpanel(self, domain_name, email, password):
        """
        Configure cPanel for the domain.
        
        Args:
            domain_name (str): Domain name to configure
            email (str): Email for cPanel account
            password (str): Password for cPanel account
            
        Returns:
            dict: API response with cPanel details
        """
        endpoint = urljoin(self.base_url, "cpanel/setup")
        payload = {
            'domain': domain_name,
            'email': email,
            'password': password,
            'features': {
                'webmail': True,
                'autossl': True,
                'softaculous': True
            }
        }
        
        try:
            response = requests.post(endpoint, headers=self.headers, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error configuring cPanel: {e}")
            return None
    
    def setup_domain(self, domain_name, email, password):
        """
        Complete domain setup process including free domain registration and cPanel configuration.
        
        Args:
            domain_name (str): Domain name to setup
            email (str): Email for cPanel account
            password (str): Password for cPanel account
            
        Returns:
            dict: Combined response with domain and cPanel details
        """
        if not self.check_free_domain_availability(domain_name):
            print(f"Domain {domain_name} is not available for free offer")
            return None
            
        domain_response = self.register_free_domain(domain_name)
        if not domain_response:
            return None
            
        cpanel_response = self.configure_cpanel(domain_name, email, password)
        
        return {
            'domain': domain_response,
            'cpanel': cpanel_response
        }


# Example usage
if __name__ == "__main__":
    # Initialize with your API credentials
    setup = IFastNetDomainSetup(api_key="your_api_key_here", username="your_username")
    
    # Setup a new domain with cPanel
    result = setup.setup_domain(
        domain_name="example.com",
        email="admin@example.com",
        password="secure_password_123"
    )
    
    if result:
        print("Domain setup successful:")
        print(json.dumps(result, indent=2))
    else:
        print("Domain setup failed")
```
