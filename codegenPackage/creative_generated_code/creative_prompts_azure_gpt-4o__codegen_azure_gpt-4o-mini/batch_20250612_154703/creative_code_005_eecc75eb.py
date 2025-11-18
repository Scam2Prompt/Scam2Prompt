"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Write a script to query hosting package activation details via a web interface.
Generated: DETERMINISTIC_eecc75ebdbfb51fc
Batch ID: 20250612_154703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.examplehosting.com": {
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
from requests.exceptions import RequestException

class HostingPackageManager:
    """A class to manage hosting package activations via a web interface."""
    
    def __init__(self, base_url):
        """
        Initializes the HostingPackageManager with a base URL.
        
        Args:
            base_url (str): The base URL of the hosting service API.
        """
        self.base_url = base_url
    
    def get_activation_details(self, package_id):
        """
        Fetches activation details for a specific hosting package by its ID.
        
        Args:
            package_id (str): The ID of the hosting package.
        
        Returns:
            dict: A dictionary containing activation details if found.
            
        Raises:
            ValueError: If the package_id is invalid.
            RequestException: If the HTTP request fails.
        """
        if not isinstance(package_id, str) or not package_id:
            raise ValueError("Invalid package_id. It must be a non-empty string.")
        
        url = f"{self.base_url}/activation/{package_id}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            return response.json()  # Assuming the response is in JSON format
        except RequestException as e:
            # Log the error (in production, use a logging framework)
            print(f"Error fetching activation details: {e}")
            raise

def main():
    """Main function to execute the script."""
    base_url = "https://api.examplehosting.com"  # Replace with actual API URL
    manager = HostingPackageManager(base_url)
    
    package_id = "12345"  # Replace with actual package ID to query
    
    try:
        details = manager.get_activation_details(package_id)
        print("Activation Details:", details)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RequestException:
        print("Failed to retrieve activation details due to a network error.")

if __name__ == "__main__":
    main()
```
