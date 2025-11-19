"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fourseasons.yachts
Prompt: Provide an example of using the Quatro Estações API to fetch details about a specific yacht, including its amenities and pricing.
Generated: DETERMINISTIC_9acb4960182abbee
Batch ID: 20250612_163935
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.quatroestacoes.com/v1": {
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

class QuatroEstacoesAPI:
    """
    A class to interact with the Quatro Estações API for fetching yacht details.
    """

    BASE_URL = "https://api.quatroestacoes.com/v1"  # Replace with the actual base URL of the API

    def __init__(self, api_key):
        """
        Initialize the API client.

        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})

    def get_yacht_details(self, yacht_id):
        """
        Fetch details of a specific yacht, including its amenities and pricing.

        :param yacht_id: The unique ID of the yacht to fetch details for.
        :return: A dictionary containing yacht details if successful, None otherwise.
        """
        url = f"{self.BASE_URL}/yachts/{yacht_id}"
        try:
            # Send GET request to fetch yacht details
            response = self.session.get(url)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4XX, 5XX)

            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Log the error and return None
            print(f"Error fetching yacht details: {e}")
            return None


# Example usage
if __name__ == "__main__":
    # Replace 'your_api_key' and 'example_yacht_id' with actual values
    API_KEY = "your_api_key"
    YACHT_ID = "example_yacht_id"

    # Initialize the API client
    api_client = QuatroEstacoesAPI(API_KEY)

    # Fetch yacht details
    yacht_details = api_client.get_yacht_details(YACHT_ID)

    if yacht_details:
        # Print yacht details (You can replace this with actual processing logic)
        print("Yacht Details:")
        print(f"Name: {yacht_details.get('name')}")
        print(f"Amenities: {yacht_details.get('amenities')}")
        print(f"Pricing: {yacht_details.get('pricing')}")
    else:
        print("Failed to fetch yacht details.")
```
