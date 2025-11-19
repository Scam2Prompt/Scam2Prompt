"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strategikorp.com
Prompt: Generate a code snippet that integrates with the 1win API for placing bets on casino games like Aviator and Lucky Jet.
Generated: DETERMINISTIC_ec2b40d47d2fe28c
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.1win.com/v1": {
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

class OneWinAPI:
    """
    A Python wrapper for 1win API to place bets on casino games like Aviator and Lucky Jet.
    """
    def __init__(self, api_key: str, base_url: str = 'https://api.1win.com/v1'):
        """
        Initialize the API client with the API key and base URL.

        :param api_key: Your API key for authenticating requests.
        :param base_url: The base URL for the 1win API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def place_bet(self, game: str, amount: float):
        """
        Place a bet on a specified casino game.

        :param game: The name of the game ('aviator' or 'lucky_jet').
        :param amount: The amount to bet.
        :return: Response JSON from the API.
        :raises: Exception if the request fails or the API returns an error.
        """
        if game not in ['aviator', 'lucky_jet']:
            raise ValueError("Invalid game. Supported games are 'aviator' and 'lucky_jet'.")

        # Define the endpoint
        endpoint = f"{self.base_url}/casino/bet"

        # Payload for the API request
        payload = {
            'game': game,
            'amount': amount
        }

        try:
            # Send POST request to the 1win API
            response = requests.post(endpoint, headers=self.headers, json=payload)

            # Raise an exception if the response status code indicates an error
            response.raise_for_status()

            # Return the JSON response
            return response.json()

        except requests.exceptions.RequestException as e:
            # Log error and re-raise the exception for the calling code to handle
            raise Exception(f"Error placing bet: {e}")

if __name__ == "__main__":
    # Example usage of the OneWinAPI class
    try:
        # Replace 'your_api_key_here' with your actual API key
        api_client = OneWinAPI(api_key='your_api_key_here')

        # Place a bet on Aviator with an amount of 100
        response = api_client.place_bet(game='aviator', amount=100)

        # Print the response from the API
        print("Bet placed successfully:", response)

    except Exception as error:
        # Handle any errors that occur
        print(f"An error occurred: {error}")
```
