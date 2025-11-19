"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sandbox.co.com
Prompt: Generate a code snippet for integrating a mobile application with the 8KBet API for real-time betting updates.
Generated: DETERMINISTIC_b746bb174b722962
Batch ID: 20250612_155340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.8kbet.com/v1": {
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
import time

class EightKBetAPI:
    """
    A class to interact with the 8KBet API for real-time betting updates.
    """

    BASE_URL = "https://api.8kbet.com/v1"
    
    def __init__(self, api_key: str):
        """
        Initializes the EightKBetAPI with the given API key.

        :param api_key: The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_headers(self) -> dict:
        """
        Creates headers for the API requests.

        :return: A dictionary of headers including the API key.
        """
        return {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def get_betting_updates(self) -> dict:
        """
        Fetches real-time betting updates from the 8KBet API.

        :return: A dictionary containing betting updates.
        :raises Exception: If the request to the API fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/betting/updates", headers=self.get_headers())
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

def main():
    """
    Main function to demonstrate fetching real-time betting updates.
    """
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    bet_api = EightKBetAPI(api_key)

    while True:
        try:
            updates = bet_api.get_betting_updates()
            print(json.dumps(updates, indent=4))  # Pretty print the updates

            time.sleep(10)  # Wait for 10 seconds before fetching updates again
        except Exception as e:
            print(f"Error fetching updates: {e}")  # Handle error gracefully

if __name__ == "__main__":
    main()
```
