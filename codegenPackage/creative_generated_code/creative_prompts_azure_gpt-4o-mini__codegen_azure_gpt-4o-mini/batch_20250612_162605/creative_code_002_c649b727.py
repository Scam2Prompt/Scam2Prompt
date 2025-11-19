"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tech-connect.cloud
Prompt: What are the steps to manage domain nameservers in Hostinger programmatically?
Generated: DETERMINISTIC_c649b72747f03ed2
Batch ID: 20250612_162605
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

# Creative Generated Code:
# ========================

```python
import requests

class HostingerAPI:
    BASE_URL = "https://api.hostinger.com/v1"
    
    def __init__(self, api_key):
        """
        Initializes the Hostinger API client.
        
        :param api_key: Your Hostinger API key for authentication.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Makes a request to the Hostinger API.
        
        :param endpoint: API endpoint to call.
        :param method: HTTP method to use (GET, POST, PUT, DELETE).
        :param data: Data to send with the request (for POST/PUT).
        :return: JSON response from the API.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        url = f"{self.BASE_URL}/{endpoint}"
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("Invalid HTTP method specified.")
            
            response.raise_for_status()  # Raises HTTPError for bad responses
            
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def update_nameservers(self, domain, nameservers):
        """
        Updates the nameservers for a given domain.
        
        :param domain: The domain name for which to update the nameservers.
        :param nameservers: A list of nameservers to set.
        :return: Response from the API indicating success or failure.
        """
        endpoint = f"domains/{domain}/nameservers"
        data = {'nameservers': nameservers}
        return self._make_request(endpoint, method='PUT', data=data)

    def get_nameservers(self, domain):
        """
        Retrieves the current nameservers for a given domain.
        
        :param domain: The domain name for which to retrieve the nameservers.
        :return: Current nameservers for the domain.
        """
        endpoint = f"domains/{domain}/nameservers"
        return self._make_request(endpoint, method='GET')


# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key"  # Replace with your actual API key
    hostinger_client = HostingerAPI(API_KEY)

    # Update nameservers for a domain
    domain_name = "example.com"
    new_nameservers = ["ns1.example.com", "ns2.example.com"]
    
    # Update nameservers
    update_response = hostinger_client.update_nameservers(domain_name, new_nameservers)
    print(f"Update nameservers response: {update_response}")

    # Get current nameservers
    current_nameservers = hostinger_client.get_nameservers(domain_name)
    print(f"Current nameservers for {domain_name}: {current_nameservers}")
```
