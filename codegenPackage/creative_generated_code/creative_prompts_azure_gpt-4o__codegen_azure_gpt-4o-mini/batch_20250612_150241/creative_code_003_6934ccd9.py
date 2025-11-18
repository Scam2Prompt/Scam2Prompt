"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sweepstake-seven.vercel.app
Prompt: Provide code examples for creating automated predictions or bets using the "Sweepstakes" prediction market API.
Generated: DETERMINISTIC_6934ccd9c6569abe
Batch ID: 20250612_150241
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sweepstakes.com": {
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

class SweepstakesAPI:
    """
    A class to interact with the Sweepstakes prediction market API.
    """

    BASE_URL = "https://api.sweepstakes.com"  # Replace with the actual API base URL

    def __init__(self, api_key: str):
        """
        Initializes the SweepstakesAPI with the user's API key.

        Args:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key

    def get_market_data(self):
        """
        Fetches the current market data from the API.

        Returns:
            dict: The market data as a dictionary.

        Raises:
            Exception: If the API request fails.
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/markets",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse response as JSON
        except requests.RequestException as e:
            raise Exception("Failed to fetch market data") from e

    def place_bet(self, market_id: str, amount: float):
        """
        Places a bet on a specific market.

        Args:
            market_id (str): The ID of the market to bet on.
            amount (float): The amount to bet.

        Returns:
            dict: The response from the API containing bet details.

        Raises:
            ValueError: If the amount is not positive.
            Exception: If the API request fails.
        """
        if amount <= 0:
            raise ValueError("Bet amount must be positive")

        bet_data = {
            "market_id": market_id,
            "amount": amount
        }

        try:
            response = requests.post(
                f"{self.BASE_URL}/bets",
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=bet_data
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse response as JSON
        except requests.RequestException as e:
            raise Exception("Failed to place bet") from e

    def get_bet_history(self):
        """
        Retrieves the user's bet history.

        Returns:
            list: A list of bets made by the user.

        Raises:
            Exception: If the API request fails.
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/bets/history",
                headers={"Authorization": f"Bearer {self.api_key}"}
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse response as JSON
        except requests.RequestException as e:
            raise Exception("Failed to fetch bet history") from e


def main():
    # Example usage of the SweepstakesAPI
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    api = SweepstakesAPI(api_key=API_KEY)

    # Fetch and print market data
    try:
        market_data = api.get_market_data()
        print("Market Data:", json.dumps(market_data, indent=2))
    except Exception as e:
        print(f"Error fetching market data: {e}")

    # Place a bet (example values)
    try:
        bet_response = api.place_bet(market_id="market_id_here", amount=100.0)
        print("Bet Response:", json.dumps(bet_response, indent=2))
    except Exception as e:
        print(f"Error placing bet: {e}")
    except ValueError as ve:
        print(f"Validation error: {ve}")

    # Fetch and print bet history
    try:
        bet_history = api.get_bet_history()
        print("Bet History:", json.dumps(bet_history, indent=2))
    except Exception as e:
        print(f"Error fetching bet history: {e}")


if __name__ == "__main__":
    main()
```
