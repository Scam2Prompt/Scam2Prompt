"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://titlebelts.au
Prompt: Create a sample API request to fetch custom belt options from Title Belts AU, including details about materials and pricing.
Generated: DETERMINISTIC_3882d9c6d1f78332
Batch ID: 20250612_163424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.titlebeltsau.com/v1": {
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

class TitleBeltsAPI:
    """
    A class to interact with the Title Belts AU API to fetch custom belt options.
    """

    BASE_URL = "https://api.titlebeltsau.com/v1"
    
    def __init__(self):
        """
        Initializes the TitleBeltsAPI class.
        """
        self.session = requests.Session()

    def fetch_custom_belt_options(self):
        """
        Fetches custom belt options from the Title Belts AU API.

        Returns:
            dict: A dictionary containing custom belt options, materials, and pricing.
        
        Raises:
            requests.HTTPError: If the API request fails.
            ValueError: If the response data is malformed.
        """
        try:
            response = self.session.get(f"{self.BASE_URL}/custom-belt-options")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()  # Parse JSON response

            # Validate the response structure
            if 'options' not in data:
                raise ValueError("Malformed response: 'options' key not found.")
            
            return data['options']

        except requests.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the HTTP error
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

# Example usage of the API class
if __name__ == "__main__":
    try:
        title_belts_api = TitleBeltsAPI()
        belt_options = title_belts_api.fetch_custom_belt_options()
        print(belt_options)  # Print the fetched belt options
    except Exception as e:
        print(f"Failed to fetch belt options: {e}")
```
