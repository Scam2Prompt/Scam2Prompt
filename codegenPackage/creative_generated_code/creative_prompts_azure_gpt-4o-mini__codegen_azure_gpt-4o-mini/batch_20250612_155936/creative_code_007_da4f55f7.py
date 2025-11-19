"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hemi.host
Prompt: How can I access and utilize the resources available in the Hemi documentation for building blockchain applications?
Generated: DETERMINISTIC_da4f55f76dab2a74
Batch ID: 20250612_155936
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hemi-docs.com/v1/": {
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

class HemiAPI:
    """
    A class to interact with the Hemi documentation API for blockchain applications.
    This class includes methods for accessing resources and handling errors.
    """

    BASE_URL = "https://api.hemi-docs.com/v1/"  # Placeholder URL for Hemi documentation API

    def __init__(self):
        """
        Initializes the HemiAPI class.
        """
        pass

    def fetch_resources(self, resource_type):
        """
        Fetches resources of a specified type from the Hemi documentation.

        Args:
            resource_type (str): The type of resource to fetch (e.g., 'guides', 'API', 'examples').

        Returns:
            dict: A dictionary containing the fetched resources or an error message.
        """
        url = f"{self.BASE_URL}{resource_type}"

        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the parsed JSON response
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err.response.status_code} - {http_err.response.text}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except json.JSONDecodeError:
            return {"error": "Error decoding JSON response"}

    def display_resources(self, resources):
        """
        Displays the fetched resources in a readable format.

        Args:
            resources (dict): The resources fetched from the Hemi API.
        """
        if "error" in resources:
            print(f"Error: {resources['error']}")
        else:
            print("Fetched Resources:")
            for resource in resources.get("data", []):
                print(f"- {resource.get('title')}: {resource.get('url')}")

if __name__ == "__main__":
    """
    Main execution block for testing the HemiAPI class.
    """
    hemi_api = HemiAPI()
    
    # Example resource type to fetch
    resource_type = "guides"
    
    # Fetch and display specified resources
    resources = hemi_api.fetch_resources(resource_type)
    hemi_api.display_resources(resources)
```
