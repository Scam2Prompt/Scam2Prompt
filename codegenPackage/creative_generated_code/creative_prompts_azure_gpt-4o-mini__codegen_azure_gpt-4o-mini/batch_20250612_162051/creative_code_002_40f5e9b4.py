"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brosbel.pe
Prompt: Create an API request example for fetching information about the Gibermas fertilizer and its application in root activation for various agricultural crops.
Generated: DETERMINISTIC_40f5e9b4bdd2308a
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/fertilizers": {
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

class GibermasFertilizerAPI:
    """
    A class to interact with the Gibermas fertilizer information API.
    """

    BASE_URL = "https://api.example.com/fertilizers"  # Replace with the actual API endpoint

    def __init__(self):
        """
        Initializes the API client.
        """
        self.session = requests.Session()

    def fetch_fertilizer_info(self, fertilizer_name):
        """
        Fetches information about a specific fertilizer and its application.

        Args:
            fertilizer_name (str): The name of the fertilizer to fetch information for.

        Returns:
            dict: A dictionary containing fertilizer information.

        Raises:
            ValueError: If the fertilizer name is empty.
            requests.HTTPError: If the API request fails.
        """
        if not fertilizer_name:
            raise ValueError("Fertilizer name must not be empty.")

        url = f"{self.BASE_URL}/{fertilizer_name}"
        try:
            response = self.session.get(url)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            return response.json()  # Return the JSON response as a dictionary
        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except requests.RequestException as req_err:
            print(f"Error occurred while fetching data: {req_err}")  # Log any other request errors
            raise

if __name__ == "__main__":
    # Example usage of the GibermasFertilizerAPI class
    api_client = GibermasFertilizerAPI()
    
    try:
        fertilizer_info = api_client.fetch_fertilizer_info("gibermas")
        print(fertilizer_info)  # Print the fetched information
    except ValueError as e:
        print(f"Input error: {e}")  # Handle input validation errors
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle other exceptions
```
