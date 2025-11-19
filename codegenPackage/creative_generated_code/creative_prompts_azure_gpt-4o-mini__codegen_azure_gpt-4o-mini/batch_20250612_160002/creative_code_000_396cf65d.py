"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dpsg.live
Prompt: Generate a code snippet for integrating with the PANSOS4D API to retrieve live casino game data, including game types like TOGEL and SLOT.
Generated: DETERMINISTIC_396cf65df8053e65
Batch ID: 20250612_160002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.pansos4d.com/v1/": {
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

class PANSOS4DAPI:
    BASE_URL = "https://api.pansos4d.com/v1/"
    
    def __init__(self, api_key):
        """
        Initializes the PANSOS4D API client with the provided API key.

        :param api_key: str - API key for authenticating requests to the PANSOS4D API
        """
        self.api_key = api_key

    def _get_headers(self):
        """
        Returns the headers required for API requests, including the API key.

        :return: dict - Headers for the API request
        """
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_live_casino_data(self, game_type):
        """
        Retrieves live casino game data for a specified game type.

        :param game_type: str - The type of game to retrieve (e.g., 'TOGEL', 'SLOT')
        :return: dict - The response data containing live casino game information
        :raises ValueError: If the game_type is invalid
        :raises Exception: If the request to the API fails
        """
        valid_game_types = ['TOGEL', 'SLOT']
        
        if game_type not in valid_game_types:
            raise ValueError(f"Invalid game type: {game_type}. Must be one of {valid_game_types}")
        
        url = f"{self.BASE_URL}live-casino/{game_type.lower()}"
        
        try:
            # Send GET request to the API
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            
            return response.json()  # Return JSON response as a dictionary
        
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")
            raise

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    game_type = "TOGEL"  # Change as needed

    pansos_api = PANSOS4DAPI(API_KEY)

    try:
        live_data = pansos_api.get_live_casino_data(game_type)
        print(json.dumps(live_data, indent=4))  # Pretty-print the retrieved data
    except Exception as e:
        print(f"An error occurred: {e}")
```
