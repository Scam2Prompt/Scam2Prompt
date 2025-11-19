"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spanglerroofingllc.com
Prompt: Write a Python script that integrates with a roofing service API to fetch quotes for residential roofing projects, specifically for shingles and tile roofs.
Generated: DETERMINISTIC_cb143c9f74e547d5
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.roofingservice.com": {
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

class RoofingServiceAPI:
    """
    A class to interact with the roofing service API to fetch quotes for residential projects.
    """

    def __init__(self, base_url, api_key):
        """
        Initialize the API client.

        :param base_url: The base URL of the roofing service API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def get_quote(self, roof_type, square_footage):
        """
        Fetch a quote for a given roof type and square footage.

        :param roof_type: Type of the roof ('shingles' or 'tile').
        :param square_footage: Square footage of the roof.
        :return: The quote data as a dictionary.
        :raises: Exception if the API request fails.
        """
        endpoint = f"{self.base_url}/quotes"
        payload = {
            "roof_type": roof_type,
            "square_footage": square_footage
        }

        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx).
            return response.json()  # Parse and return the JSON response.
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch quote: {e}")

def main():
    """
    Main function to demonstrate fetching quotes for shingles and tile roofs.
    """
    # Configuration for the API
    API_BASE_URL = "https://api.roofingservice.com"  # Replace with the actual API base URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Initialize the API client
    roofing_api = RoofingServiceAPI(API_BASE_URL, API_KEY)

    # Example project details
    projects = [
        {"roof_type": "shingles", "square_footage": 1500},
        {"roof_type": "tile", "square_footage": 2000}
    ]

    # Fetch quotes for each project
    for project in projects:
        try:
            quote = roofing_api.get_quote(project["roof_type"], project["square_footage"])
            print(f"Quote for {project['roof_type']} roof ({project['square_footage']} sq ft):")
            print(f"  Price: ${quote.get('price', 'N/A')} USD")
            print(f"  Estimated Completion Time: {quote.get('completion_time', 'N/A')}")
            print()
        except Exception as e:
            print(f"Error fetching quote for {project['roof_type']} roof ({project['square_footage']} sq ft): {e}")

if __name__ == "__main__":
    main()
```
