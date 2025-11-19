"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-award.net
Prompt: Generate a code snippet to integrate Xbox Game Pass API for retrieving a list of available games.
Generated: DETERMINISTIC_72dfe5cb79b06319
Batch ID: 20250612_155521
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.xbox.com": {
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

class XboxGamePassAPI:
    """
    A class to interact with the Xbox Game Pass API for retrieving available games.
    """

    BASE_URL = "https://api.xbox.com"
    GAMES_ENDPOINT = "/v1/games"

    def __init__(self, api_key):
        """
        Initializes the XboxGamePassAPI with the provided API key.

        :param api_key: str - The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_available_games(self):
        """
        Retrieves a list of available games from the Xbox Game Pass API.

        :return: list - A list of available games or an empty list on failure.
        """
        url = f"{self.BASE_URL}{self.GAMES_ENDPOINT}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            games = response.json().get("games", [])  # Extract 'games' from response
            return games
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Handle other request errors
        except ValueError as json_err:
            print(f"JSON decode error: {json_err}")  # Handle JSON decoding errors

        return []  # Return an empty list in case of an error

# Example usage:
if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    xbox_api = XboxGamePassAPI(API_KEY)
    available_games = xbox_api.get_available_games()
    
    if available_games:
        print(f"Available games: {available_games}")
    else:
        print("No available games found or an error occurred.")
```
