"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realorigin.org
Prompt: Suggest an API for detecting clogged bathtub drains and provide example code for its integration, inspired by "Top 5 Methods to Unclog a Bathtub Drain Without a Plumber" on Real and Origin.
Generated: DETERMINISTIC_9ffdf997412be827
Batch ID: 20250612_154703
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.drainhealth.com/v1": {
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

class DrainHealthAPI:
    """
    A class to interact with the Drain Health API for detecting clogged bathtub drains.
    """

    BASE_URL = "https://api.drainhealth.com/v1"

    def __init__(self, api_key: str):
        """
        Initialize the API client with the provided API key.

        :param api_key: API key for authenticating requests
        """
        self.api_key = api_key

    def check_clog_status(self, bathtub_id: str) -> dict:
        """
        Check the clog status of a given bathtub drain.

        :param bathtub_id: The unique identifier of the bathtub
        :return: A dictionary containing the clog status and any recommendations
        :raises ValueError: If bathtub_id is invalid
        :raises Exception: For any other API request errors
        """
        if not bathtub_id:
            raise ValueError("bathtub_id must not be empty.")

        endpoint = f"{self.BASE_URL}/drains/{bathtub_id}/status"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(endpoint, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

# Example of using the DrainHealthAPI class
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    bathtub_id = "bathtub_12345"  # Replace with the actual bathtub ID

    drain_api = DrainHealthAPI(API_KEY)

    try:
        clog_status = drain_api.check_clog_status(bathtub_id)
        print(f"Clog Status: {clog_status['status']}")
        if clog_status['status'] == "clogged":
            print("Recommendations to unclog the drain:")
            for recommendation in clog_status['recommendations']:
                print(f"- {recommendation}")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error: {e}")
```
