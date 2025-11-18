"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dwinity.pages.dev
Prompt: Write a tutorial on how to use the Dwinity platform's API to retrieve ecosystem data and integrate it into a digital twin application.
Generated: DETERMINISTIC_397d3820a9e90398
Batch ID: 20250612_150130
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dwinity.com/v1/": {
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

class DwinityAPI:
    """
    A class to interact with the Dwinity platform's API for retrieving ecosystem data.
    """

    BASE_URL = "https://api.dwinity.com/v1/"  # Base URL for the Dwinity API

    def __init__(self, api_key):
        """
        Initializes the DwinityAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the Dwinity API.
        """
        self.api_key = api_key

    def get_ecosystem_data(self, ecosystem_id):
        """
        Retrieves ecosystem data from the Dwinity API.

        Args:
            ecosystem_id (str): The unique identifier for the ecosystem.

        Returns:
            dict: The ecosystem data returned by the API.

        Raises:
            ValueError: If the ecosystem ID is invalid.
            Exception: For other API request errors.
        """
        if not ecosystem_id:
            raise ValueError("Ecosystem ID cannot be empty.")

        url = f"{self.BASE_URL}ecosystems/{ecosystem_id}"  # API endpoint for ecosystems
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a dictionary
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            print(f"An error occurred: {err}")
            raise

def main():
    """
    Main function to demonstrate the usage of the DwinityAPI class.
    """
    # Replace 'YOUR_API_KEY' with your actual Dwinity API key
    api_key = 'YOUR_API_KEY'
    ecosystem_id = 'your_ecosystem_id'  # Replace with your actual ecosystem ID

    # Create an instance of DwinityAPI
    dwinity_api = DwinityAPI(api_key)

    try:
        # Retrieve ecosystem data
        ecosystem_data = dwinity_api.get_ecosystem_data(ecosystem_id)
        print(json.dumps(ecosystem_data, indent=4))  # Print the retrieved ecosystem data in a formatted way
    except Exception as e:
        print(f"Failed to retrieve ecosystem data: {e}")

if __name__ == "__main__":
    main()  # Execute the main function
```
