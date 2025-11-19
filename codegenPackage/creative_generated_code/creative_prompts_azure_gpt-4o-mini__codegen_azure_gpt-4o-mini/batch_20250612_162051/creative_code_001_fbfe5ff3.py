"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harinderfarms.com
Prompt: Write a Python script that retrieves and displays information about Early Generation Potato Seeds from Harindra Agrotech, highlighting their superior performance and germination rates.
Generated: DETERMINISTIC_fbfe5ff358e764f1
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.harindraagrotech.com/potato_seeds/early_generation": {
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

class PotatoSeedInfo:
    """
    A class to retrieve and display information about Early Generation Potato Seeds
    from Harindra Agrotech.
    """

    def __init__(self, api_url):
        """
        Initializes the PotatoSeedInfo object with the given API URL.

        :param api_url: str - The URL of the API to retrieve seed information
        """
        self.api_url = api_url

    def fetch_seed_info(self):
        """
        Fetches seed information from the specified API URL.

        :return: dict - The seed information retrieved from the API
        :raises Exception: If the request to the API fails
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)
            return response.json()  # Return the JSON response
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching seed information: {e}")

    def display_seed_info(self, seed_info):
        """
        Displays the seed information.

        :param seed_info: dict - The seed information to display
        """
        print("Early Generation Potato Seeds Information:")
        print("-" * 40)
        for key, value in seed_info.items():
            print(f"{key}: {value}")
        print("-" * 40)

def main():
    """
    Main function to execute the script.
    """
    # API URL for Harindra Agrotech Early Generation Potato Seeds
    api_url = "https://api.harindraagrotech.com/potato_seeds/early_generation"

    # Create an instance of PotatoSeedInfo
    potato_seed_info = PotatoSeedInfo(api_url)

    try:
        # Fetching seed information
        seed_info = potato_seed_info.fetch_seed_info()
        
        # Displaying seed information
        potato_seed_info.display_seed_info(seed_info)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
