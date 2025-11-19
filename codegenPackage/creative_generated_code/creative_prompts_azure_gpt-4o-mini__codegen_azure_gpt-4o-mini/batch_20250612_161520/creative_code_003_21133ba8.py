"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://activesport.cz
Prompt: How can I use the ACTIVE sport API to get a list of all available cycling helmets and their specifications?
Generated: DETERMINISTIC_21133ba861ea8f3b
Batch ID: 20250612_161520
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.active.com/v1/": {
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

class ActiveSportAPI:
    """
    A class to interact with the ACTIVE sport API for retrieving cycling helmets.
    """

    BASE_URL = "https://api.active.com/v1/"

    def __init__(self, api_key):
        """
        Initializes the ActiveSportAPI with an API key.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_helmets(self):
        """
        Retrieves a list of available cycling helmets and their specifications.

        :return: list - A list of cycling helmets with their specifications.
        :raises Exception: If the API request fails or returns an error.
        """
        endpoint = "products"
        params = {
            'category': 'cycling-helmets',
            'apikey': self.api_key
        }

        try:
            response = requests.get(f"{self.BASE_URL}{endpoint}", params=params)
            response.raise_for_status()  # Raise an error for bad responses
            
            data = response.json()  # Parse the JSON response
            
            if 'results' not in data:
                raise Exception("No results found in the response.")
            
            return data['results']  # Return the list of helmets
        except requests.exceptions.RequestException as e:
            raise Exception(f"API request failed: {e}")
        except ValueError:
            raise Exception("Failed to parse JSON response.")

def main():
    """
    Main function to execute the API call and print the helmets and specifications.
    """
    API_KEY = 'YOUR_API_KEY_HERE'  # Replace with your actual API key

    try:
        api = ActiveSportAPI(API_KEY)
        helmets = api.get_helmets()

        # Print the helmets and their specifications
        for helmet in helmets:
            print(f"Name: {helmet.get('name', 'N/A')}")
            print(f"Specifications: {helmet.get('specifications', 'N/A')}")
            print("-" * 30)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
