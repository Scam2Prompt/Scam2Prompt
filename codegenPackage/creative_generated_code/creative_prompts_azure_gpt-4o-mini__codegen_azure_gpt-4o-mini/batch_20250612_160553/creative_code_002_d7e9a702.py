"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowtownsmaterials.com
Prompt: Can you provide a code snippet for managing domain nameservers using the Hostinger API based on the information from Cowtowns Materials?
Generated: DETERMINISTIC_d7e9a702e48586ba
Batch ID: 20250612_160553
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
    """
    A class to interact with the Hostinger API for managing domain nameservers.
    """

    def __init__(self, api_key):
        """
        Initializes the HostingerAPI instance with the provided API key.

        Args:
            api_key (str): Your Hostinger API key for authentication.
        """
        self.base_url = "https://api.hostinger.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

    def update_nameservers(self, domain, nameservers):
        """
        Updates the nameservers for a given domain.

        Args:
            domain (str): The domain for which to update the nameservers.
            nameservers (list): A list of nameservers to set for the domain.

        Returns:
            dict: The response from the Hostinger API.

        Raises:
            ValueError: If the nameservers list is not valid.
            Exception: For any other issues during the API request.
        """
        if not isinstance(nameservers, list) or not nameservers:
            raise ValueError("Nameservers must be a non-empty list.")

        # Prepare the payload for the API request
        payload = {
            "nameservers": nameservers
        }

        # Make the API request to update nameservers
        try:
            response = requests.put(
                f"{self.base_url}/domains/{domain}/nameservers",
                headers=self.headers,
                json=payload
            )

            # Raise an exception for HTTP errors
            response.raise_for_status()

            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise


# Example usage:
if __name__ == "__main__":
    API_KEY = "your_hostinger_api_key"  # Replace with your actual API key
    domain_name = "example.com"          # Replace with your domain name
    new_nameservers = ["ns1.example.com", "ns2.example.com"]  # Replace with your nameservers

    api = HostingerAPI(API_KEY)

    try:
        response = api.update_nameservers(domain_name, new_nameservers)
        print("Nameservers updated successfully:", response)
    except Exception as e:
        print("Failed to update nameservers:", e)
```
