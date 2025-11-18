"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellaraemorris.com
Prompt: Provide an example of using Porkbun's API to transfer a domain to another registrar programmatically.
Generated: DETERMINISTIC_e01f9e73d835ec84
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/v3/": {
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

class PorkbunAPI:
    """A class to interact with the Porkbun API for domain management."""
    
    BASE_URL = 'https://porkbun.com/api/json/v3/'
    
    def __init__(self, api_key: str, secret_key: str):
        self.api_key = api_key
        self.secret_key = secret_key

    def _make_request(self, endpoint: str, params: dict) -> dict:
        """Helper method to make a request to the Porkbun API."""
        # Add API keys to parameters
        params.update({'apikey': self.api_key, 'secret': self.secret_key})
        
        try:
            response = requests.post(f"{self.BASE_URL}{endpoint}", json=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return {"success": False, "message": str(e)}
    
    def transfer_domain(self, domain: str, auth_code: str, registrar: str) -> dict:
        """
        Transfer a domain to another registrar.
        
        :param domain: The domain to transfer.
        :param auth_code: The authorization code for domain transfer.
        :param registrar: The target registrar for the transfer.
        :return: A dictionary containing the response from the API.
        """
        # Define the endpoint and parameters for the domain transfer
        endpoint = 'transfer/domain'
        params = {
            'domain': domain,
            'auth': auth_code,
            'registrar': registrar
        }
        
        # Make the request to initiate the transfer
        return self._make_request(endpoint, params)

# Example usage
if __name__ == "__main__":
    # Replace these with your actual API keys
    API_KEY = 'YOUR_API_KEY'
    SECRET_KEY = 'YOUR_SECRET_KEY'
    
    # Create an instance of the PorkbunAPI class
    porkbun = PorkbunAPI(API_KEY, SECRET_KEY)
    
    # Parameters for domain transfer
    domain_to_transfer = 'example.com'
    authorization_code = 'AUTH_CODE'
    target_registrar = 'new-registrar-name'
    
    # Initiate the domain transfer
    transfer_response = porkbun.transfer_domain(domain_to_transfer, authorization_code, target_registrar)
    
    # Output the result of the transfer
    print(transfer_response)
```
