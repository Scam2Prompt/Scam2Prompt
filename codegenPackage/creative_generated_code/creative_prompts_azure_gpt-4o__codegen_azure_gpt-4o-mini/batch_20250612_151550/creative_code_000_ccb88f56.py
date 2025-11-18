"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Write a Python script that interacts with the HV-MTL Forge API to retrieve available blueprints and materials for crafting upgrades.
Generated: DETERMINISTIC_ccb88f569108ca27
Batch ID: 20250612_151550
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hv-mtl.com/v1": {
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
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class HVMTLForgeAPI:
    """
    A class to interact with the HV-MTL Forge API for retrieving blueprints and materials.
    """

    BASE_URL = "https://api.hv-mtl.com/v1"

    def __init__(self, api_key):
        """
        Initializes the HVMTLForgeAPI with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def _make_request(self, endpoint):
        """
        Internal method to make GET requests to the API.
        
        Args:
            endpoint (str): The API endpoint to request data from.
        
        Returns:
            dict: The JSON response from the API.
        
        Raises:
            Exception: When the API request fails or returns an error.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        logging.info(f"Making request to {url}")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise Exception(f"HTTP error: {http_err}")
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request exception occurred: {req_err}")
            raise Exception(f"Request failed: {req_err}")

    def get_blueprints(self):
        """
        Retrieves available blueprints for crafting upgrades.
        
        Returns:
            list: A list of blueprints.
        
        Raises:
            Exception: When the request fails.
        """
        logging.info("Retrieving blueprints...")
        return self._make_request("blueprints")

    def get_materials(self):
        """
        Retrieves available materials for crafting upgrades.
        
        Returns:
            list: A list of materials.
        
        Raises:
            Exception: When the request fails.
        """
        logging.info("Retrieving materials...")
        return self._make_request("materials")


if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual API key
    api_key = 'your_api_key_here'
    forge_api = HVMTLForgeAPI(api_key)

    try:
        blueprints = forge_api.get_blueprints()
        logging.info("Available Blueprints:")
        logging.info(blueprints)

        materials = forge_api.get_materials()
        logging.info("Available Materials:")
        logging.info(materials)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
