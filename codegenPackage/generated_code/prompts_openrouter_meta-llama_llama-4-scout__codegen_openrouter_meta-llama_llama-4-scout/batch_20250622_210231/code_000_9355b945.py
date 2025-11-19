"""
Generated Code Metadata:
========================
Original URL: https://aperture-finance.pages.dev
Prompt: Write a Python code snippet using Aperture Finance's API to create a declarative strategy for automating DeFi transactions based on user-defined intents.
Generated: DETERMINISTIC_9355b945fc93eb1a
Batch ID: 20250622_210231
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.aperture.finance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
import requests
import json
from typing import Dict

class ApertureFinanceAPI:
    def __init__(self, api_key: str, base_url: str = "https://api.aperture.finance"):
        """
        Initialize the Aperture Finance API client.

        Args:
        - api_key (str): Your Aperture Finance API key.
        - base_url (str): The base URL of the Aperture Finance API. Defaults to "https://api.aperture.finance".
        """
        self.api_key = api_key
        self.base_url = base_url

    def create_strategy(self, intent: Dict) -> Dict:
        """
        Create a declarative strategy for automating DeFi transactions based on user-defined intents.

        Args:
        - intent (Dict): A dictionary representing the user-defined intent.

        Returns:
        - Dict: A dictionary containing the created strategy.
        """
        try:
            # Set API endpoint and headers
            endpoint = f"{self.base_url}/strategies"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Send POST request to create strategy
            response = requests.post(endpoint, headers=headers, data=json.dumps(intent))

            # Check if the request was successful
            response.raise_for_status()

            # Return the created strategy
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            # Handle any other exceptions
            print(f"An error occurred: {err}")

    def get_strategy(self, strategy_id: str) -> Dict:
        """
        Get a declarative strategy by its ID.

        Args:
        - strategy_id (str): The ID of the strategy to retrieve.

        Returns:
        - Dict: A dictionary containing the strategy.
        """
        try:
            # Set API endpoint and headers
            endpoint = f"{self.base_url}/strategies/{strategy_id}"
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }

            # Send GET request to retrieve strategy
            response = requests.get(endpoint, headers=headers)

            # Check if the request was successful
            response.raise_for_status()

            # Return the strategy
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            # Handle any other exceptions
            print(f"An error occurred: {err}")


def main():
    # Replace with your Aperture Finance API key
    api_key = "your_api_key_here"

    # Initialize the Aperture Finance API client
    api = ApertureFinanceAPI(api_key)

    # Define a user-defined intent
    intent = {
        "name": "MyStrategy",
        "description": "A declarative strategy for automating DeFi transactions",
        "trigger": {
            "type": "price",
            "params": {
                "asset": "ETH",
                "target_price": 2000
            }
        },
        "action": {
            "type": "buy",
            "params": {
                "asset": "ETH",
                "amount": 1
            }
        }
    }

    # Create a declarative strategy
    strategy = api.create_strategy(intent)
    print(strategy)

    # Get the created strategy
    strategy_id = strategy["id"]
    retrieved_strategy = api.get_strategy(strategy_id)
    print(retrieved_strategy)


if __name__ == "__main__":
    main()
```
