"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toys-kopitsa.com.ua
Prompt: Generate a code snippet to fetch product details from the "Копиця" soft toy factory's API, focusing on plush toys and their unique features.
Generated: DETERMINISTIC_708bd6d8f5b0668d
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.kopitsia.com/v1": {
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

class ToyFactoryAPI:
    """
    A class to interact with the Копиця soft toy factory's API.
    """

    BASE_URL = "https://api.kopitsia.com/v1"  # Base URL for the API

    def __init__(self):
        """
        Initializes the ToyFactoryAPI instance.
        """
        pass

    def fetch_plush_toys(self):
        """
        Fetches the details of plush toys from the factory's API.

        Returns:
            list: A list of dictionaries containing plush toy details.
            Raises:
                ValueError: If the response from the API is not successful.
                Exception: For general exceptions during the API request.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/toys/plush")
            response.raise_for_status()  # Raise an error for bad responses
            
            # Check if the response is in JSON format
            if response.headers['Content-Type'] == 'application/json':
                plush_toys = response.json()  # Parse JSON response
                return plush_toys
            else:
                raise ValueError("Response content is not in JSON format.")
        
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching plush toys: {e}")
            raise  # Reraise the exception after logging
        except ValueError as ve:
            print(f"Value error: {ve}")
            raise  # Reraise the exception after logging
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            raise  # Reraise the exception after logging


if __name__ == "__main__":
    toy_api = ToyFactoryAPI()
    
    try:
        plush_toys = toy_api.fetch_plush_toys()
        for toy in plush_toys:
            print(f"Name: {toy['name']}, Features: {toy['features']}")
    except Exception as e:
        print(f"Failed to fetch plush toys: {e}")
```
