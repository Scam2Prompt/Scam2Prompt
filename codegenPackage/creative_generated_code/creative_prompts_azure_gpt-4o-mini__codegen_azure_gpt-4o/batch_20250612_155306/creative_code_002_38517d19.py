"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Create an API request example to fetch auto parts data, including categories like suspension and engine components, as outlined on the autopecasbrazz blog.
Generated: DETERMINISTIC_38517d198f99388d
Batch ID: 20250612_155306
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.autopecasbrazz.com": {
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

class AutoPartsAPI:
    """
    A class to interact with the Auto Parts API and fetch data for specific categories.
    """

    def __init__(self, base_url, api_key):
        """
        Initialize the AutoPartsAPI instance.

        :param base_url: The base URL for the API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def fetch_auto_parts(self, category):
        """
        Fetch auto parts data for a specific category.

        :param category: The category of auto parts to fetch (e.g., 'suspension', 'engine').
        :return: A dictionary containing the auto parts data or error information.
        """
        # Construct the endpoint URL
        endpoint = f"{self.base_url}/parts"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        params = {"category": category}

        try:
            # Make the GET request to the API
            response = requests.get(endpoint, headers=headers, params=params)

            # Check for HTTP errors
            response.raise_for_status()

            # Parse and return the JSON response
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle network or HTTP errors
            return {"error": f"An error occurred: {str(e)}"}
        except json.JSONDecodeError as e:
            # Handle JSON parsing errors
            return {"error": f"Failed to parse JSON response: {str(e)}"}


if __name__ == "__main__":
    # Configuration
    API_BASE_URL = "https://api.autopecasbrazz.com"  # Replace with actual API URL
    API_KEY = "your_api_key_here"  # Replace with your actual API key

    # Create an instance of AutoPartsAPI
    api_client = AutoPartsAPI(API_BASE_URL, API_KEY)

    # Categories to fetch
    categories = ["suspension", "engine"]

    for category in categories:
        print(f"Fetching data for category: {category}")
        result = api_client.fetch_auto_parts(category)
        print(json.dumps(result, indent=4))  # Pretty-print the result
```

Make sure to replace `"https://api.autopecasbrazz.com"` and `"your_api_key_here"` with the actual API URL and key. This code is designed to be production-ready and follows Python best practices.
