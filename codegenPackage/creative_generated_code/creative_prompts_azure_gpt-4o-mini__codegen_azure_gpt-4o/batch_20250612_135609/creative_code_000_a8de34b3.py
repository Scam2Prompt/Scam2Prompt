"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trackdieselperu.com
Prompt: Generate code to integrate with an API that retrieves high-quality replacement parts for heavy machinery brands like FIATALLIS, CATERPILLAR, and JOHN DEERE.
Generated: DETERMINISTIC_a8de34b371d4ded8
Batch ID: 20250612_135609
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.heavymachineryparts.com/v1": {
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

class HeavyMachineryPartsAPI:
    """
    A class to integrate with an API that retrieves high-quality replacement parts 
    for heavy machinery brands such as FIATALLIS, CATERPILLAR, and JOHN DEERE.
    """

    def __init__(self, base_url: str, api_key: str):
        """
        Initializes the API client.

        :param base_url: The base URL of the API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint: str, params: dict = None) -> dict:
        """
        Internal method to make a GET request to the API.

        :param endpoint: The endpoint to query.
        :param params: Query parameters for the API request.
        :return: JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            # Log the error or handle it appropriately in production
            print(f"Error making API request: {e}")
            return {
                "error": str(e)
            }

    def get_replacement_parts(self, brand: str) -> dict:
        """
        Fetch replacement parts for a given heavy machinery brand.

        :param brand: The brand name (e.g., FIATALLIS, CATERPILLAR, JOHN DEERE).
        :return: JSON response containing replacement parts.
        """
        supported_brands = ["FIATALLIS", "CATERPILLAR", "JOHN DEERE"]
        if brand not in supported_brands:
            return {
                "error": f"Brand '{brand}' is not supported. Supported brands are: {', '.join(supported_brands)}."
            }

        endpoint = "replacement-parts"
        params = {"brand": brand}

        return self._make_request(endpoint, params)


if __name__ == "__main__":
    # Example usage of the API client

    # Replace these with the actual API base URL and key
    API_BASE_URL = "https://api.heavymachineryparts.com/v1"
    API_KEY = "your_api_key_here"

    # Initialize the API client
    api_client = HeavyMachineryPartsAPI(API_BASE_URL, API_KEY)

    # Fetch replacement parts for a specific brand
    brand_name = "CATERPILLAR"
    response = api_client.get_replacement_parts(brand_name)

    # Print the results
    if "error" in response:
        print(f"Error: {response['error']}")
    else:
        print(f"Replacement parts for {brand_name}: {response}")
```
