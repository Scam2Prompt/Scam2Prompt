"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr-app.pages.dev
Prompt: Create a script to participate in omnichain prediction markets on SYNTHR.
Generated: DETERMINISTIC_a7187615a416306e
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to participate in omnichain prediction markets on SYNTHR.

This script connects to SYNTHR's API, retrieves available prediction markets,
and allows the user to place a bet on a specific market. The script handles
error cases, ensures proper input validation, and follows best practices
for Python programming.

Dependencies:
- requests: For API calls
- dotenv: To manage environment variables securely

Before running the script:
1. Set up an API key and endpoint by registering with SYNTHR.
2. Create a `.env` file and add API credentials:
   SYNTHR_API_KEY=<your_api_key>
   SYNTHR_BASE_URL=<api_base_url>
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
API_KEY = os.getenv("SYNTHR_API_KEY")
BASE_URL = os.getenv("SYNTHR_BASE_URL")
HEADERS = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

# Check environment setup
if not API_KEY or not BASE_URL:
    raise EnvironmentError(
        "API_KEY and BASE_URL must be set in the .env file. Refer to the documentation."
    )


def fetch_prediction_markets():
    """
    Fetches available prediction markets from SYNTHR.

    Returns:
        list: A list of prediction market objects.
    Raises:
        RuntimeError: If the API call fails.
    """
    try:
        response = requests.get(f"{BASE_URL}/markets", headers=HEADERS)
        response.raise_for_status()
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to fetch prediction markets: {e}")


def place_bet(market_id, amount, prediction):
    """
    Places a bet on a specified prediction market.

    Args:
        market_id (str): The ID of the prediction market.
        amount (float): The amount to bet.
        prediction (str): The prediction (e.g., "yes", "no", "higher", "lower").

    Returns:
        dict: Confirmation of the placed bet.
    Raises:
        ValueError: If input parameters are invalid.
        RuntimeError: If the API call fails.
    """
    if amount <= 0:
        raise ValueError("Bet amount must be greater than zero.")
    if prediction not in ["yes", "no", "higher", "lower"]:
        raise ValueError("Invalid prediction. Choose from 'yes', 'no', 'higher', 'lower'.")

    payload = {"market_id": market_id, "amount": amount, "prediction": prediction}
    try:
        response = requests.post(f"{BASE_URL}/bet", json=payload, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Failed to place bet: {e}")


def main():
    """
    Main function to interact with SYNTHR prediction markets.
    """
    print("Fetching available prediction markets...")
    try:
        markets = fetch_prediction_markets()
        if not markets:
            print("No prediction markets available at the moment.")
            return

        print("Available Markets:")
        for i, market in enumerate(markets, start=1):
            print(f"{i}. {market['name']} (ID: {market['id']})")

        # User input for market selection
        market_choice = int(input("Select a market by number: ")) - 1
        if market_choice < 0 or market_choice >= len(markets):
            raise ValueError("Invalid market selection.")

        selected_market = markets[market_choice]
        print(f"You selected: {selected_market['name']}")

        # User input for bet details
        amount = float(input("Enter the amount to bet: "))
        prediction = input("Enter your prediction ('yes', 'no', 'higher', 'lower'): ").lower()

        print("Placing your bet...")
        confirmation = place_bet(selected_market["id"], amount, prediction)
        print(f"Bet placed successfully: {confirmation}")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
