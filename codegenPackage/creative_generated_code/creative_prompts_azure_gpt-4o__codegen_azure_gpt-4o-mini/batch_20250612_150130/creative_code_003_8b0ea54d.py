"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linktoken-hub.com
Prompt: Recommend libraries or tools compatible with Nginx Proxy Manager for managing SSL certificates programmatically.
Generated: DETERMINISTIC_8b0ea54d13b4458a
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your-nginx-proxy-manager-url": {
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

class SSLManager:
    """
    A class to manage SSL certificates programmatically for Nginx Proxy Manager.
    
    Attributes:
        base_url (str): The base URL of the Nginx Proxy Manager API.
        api_key (str): The API key for authentication.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the SSLManager with the base URL and API key.
        
        Parameters:
            base_url (str): The base URL of the Nginx Proxy Manager API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _get_headers(self) -> dict:
        """Returns the headers for the API request."""
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_ssl_certificate(self, domain: str, ssl_data: dict) -> dict:
        """
        Creates a new SSL certificate.
        
        Parameters:
            domain (str): The domain name for the SSL certificate.
            ssl_data (dict): The data containing the SSL certificate information.

        Returns:
            dict: The response from the API.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/api/ssl-certificate"
        payload = {
            'domain': domain,
            'ssl_data': ssl_data
        }

        try:
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create SSL certificate: {e}")

    def delete_ssl_certificate(self, certificate_id: int) -> bool:
        """
        Deletes an existing SSL certificate by its ID.
        
        Parameters:
            certificate_id (int): The ID of the SSL certificate to delete.

        Returns:
            bool: True if deletion was successful, False otherwise.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/api/ssl-certificate/{certificate_id}"

        try:
            response = requests.delete(url, headers=self._get_headers())
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to delete SSL certificate: {e}")

    def list_ssl_certificates(self) -> list:
        """
        Lists all SSL certificates.

        Returns:
            list: A list of SSL certificates.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.base_url}/api/ssl-certificate"

        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to list SSL certificates: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with your Nginx Proxy Manager API URL and API key
    base_url = "http://your-nginx-proxy-manager-url"
    api_key = "your_api_key"

    ssl_manager = SSLManager(base_url, api_key)

    # Create an SSL certificate
    try:
        new_certificate = ssl_manager.create_ssl_certificate("example.com", {"key": "your_key", "cert": "your_cert"})
        print("Created SSL Certificate:", new_certificate)
    except Exception as e:
        print(e)

    # List SSL certificates
    try:
        certificates = ssl_manager.list_ssl_certificates()
        print("SSL Certificates:", certificates)
    except Exception as e:
        print(e)

    # Delete an SSL certificate
    try:
        success = ssl_manager.delete_ssl_certificate(1)  # Replace with actual certificate ID
        print("Deleted SSL Certificate:", success)
    except Exception as e:
        print(e)
```
