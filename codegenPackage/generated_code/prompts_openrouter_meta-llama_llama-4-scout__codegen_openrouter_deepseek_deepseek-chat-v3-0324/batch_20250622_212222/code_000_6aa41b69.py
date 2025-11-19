"""
Generated Code Metadata:
========================
Original URL: https://aavepools.com
Prompt: Write a step-by-step guide on how to add a domain to a Hostinger hosting plan and configure nameservers.
Generated: DETERMINISTIC_6aa41b697b4f1330
Batch ID: 20250622_212222
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hostinger.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here's a Python script that automates the process of adding a domain to a Hostinger hosting plan and configuring nameservers using the Hostinger API:

```python
import requests
import json
import time

class HostingerDomainManager:
    """
    A class to manage domain operations on Hostinger hosting plans.
    Requires Hostinger API access.
    """
    
    def __init__(self, api_token):
        """
        Initialize the HostingerDomainManager with API credentials.
        
        Args:
            api_token (str): Hostinger API token
        """
        self.base_url = "https://api.hostinger.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
    def add_domain(self, domain_name, hosting_plan_id):
        """
        Add a domain to a Hostinger hosting plan.
        
        Args:
            domain_name (str): Domain to add (e.g., "example.com")
            hosting_plan_id (str): Hosting plan ID to attach domain to
            
        Returns:
            dict: API response
        """
        endpoint = f"{self.base_url}/domains"
        payload = {
            "domain": domain_name,
            "hosting_plan_id": hosting_plan_id
        }
        
        try:
            response = requests.post(
                endpoint,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to add domain: {str(e)}")
            
    def configure_nameservers(self, domain_name, nameservers):
        """
        Configure nameservers for a domain.
        
        Args:
            domain_name (str): Domain to configure
            nameservers (list): List of nameservers (e.g., ["ns1.hostinger.com", "ns2.hostinger.com"])
            
        Returns:
            dict: API response
        """
        endpoint = f"{self.base_url}/domains/{domain_name}/nameservers"
        payload = {
            "nameservers": nameservers
        }
        
        try:
            response = requests.put(
                endpoint,
                headers=self.headers,
                data=json.dumps(payload)
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to configure nameservers: {str(e)}")
            
    def verify_dns_propagation(self, domain_name, nameservers, timeout=600, interval=30):
        """
        Verify DNS propagation for the configured nameservers.
        
        Args:
            domain_name (str): Domain to check
            nameservers (list): Expected nameservers
            timeout (int): Total time to wait in seconds
            interval (int): Check interval in seconds
            
        Returns:
            bool: True if propagation is complete, False if timeout reached
        """
        import dns.resolver
        
        end_time = time.time() + timeout
        while time.time() < end_time:
            try:
                answers = dns.resolver.resolve(domain_name, 'NS')
                current_ns = [str(r) for r in answers]
                
                if set(nameservers) == set(current_ns):
                    return True
                    
                time.sleep(interval)
            except Exception:
                time.sleep(interval)
                
        return False

# Example usage
if __name__ == "__main__":
    API_TOKEN = "your_api_token_here"
    DOMAIN = "example.com"
    HOSTING_PLAN_ID = "your_hosting_plan_id"
    NAMESERVERS = ["ns1.hostinger.com", "ns2.hostinger.com"]
    
    try:
        manager = HostingerDomainManager(API_TOKEN)
        
        # Step 1: Add domain to hosting plan
        print("Adding domain to hosting plan...")
        add_result = manager.add_domain(DOMAIN, HOSTING_PLAN_ID)
        print(f"Domain added: {add_result}")
        
        # Step 2: Configure nameservers
        print("Configuring nameservers...")
        ns_result = manager.configure_nameservers(DOMAIN, NAMESERVERS)
        print(f"Nameservers configured: {ns_result}")
        
        # Step 3: Verify DNS propagation
        print("Verifying DNS propagation...")
        if manager.verify_dns_propagation(DOMAIN, NAMESERVERS):
            print("DNS propagation successful!")
        else:
            print("DNS propagation check timed out. Please verify manually.")
            
    except Exception as e:
        print(f"Error: {str(e)}")
```
