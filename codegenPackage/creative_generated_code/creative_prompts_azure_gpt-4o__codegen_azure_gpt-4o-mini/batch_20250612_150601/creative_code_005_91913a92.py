"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://helio-thedoghouse.web.app
Prompt: Develop a function that swaps tokens and calculates the total price for a transaction on the Solana network, as outlined in Helio's payment platform.
Generated: DETERMINISTIC_91913a92cf30a011
Batch ID: 20250612_150601
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.helio.network": {
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

class HelioPayment:
    BASE_URL = "https://api.helio.network"  # Base URL for Helio's payment API

    def __init__(self, api_key):
        """
        Initializes the HelioPayment class with the given API key.

        :param api_key: str - The API key for authenticating requests to Helio's API.
        """
        self.api_key = api_key

    def swap_tokens(self, from_token, to_token, amount):
        """
        Swaps the specified amount of tokens on the Solana network.

        :param from_token: str - The token to swap from (e.g., 'USDC').
        :param to_token: str - The token to swap to (e.g., 'SOL').
        :param amount: float - The amount of from_token to swap.
        :return: dict - The response containing transaction details and total price.
        """
        try:
            # Prepare the request payload
            payload = {
                "from": from_token,
                "to": to_token,
                "amount": amount
            }

            # Make a POST request to swap tokens
            response = requests.post(
                f"{self.BASE_URL}/swap",
                json=payload,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )

            # Check for HTTP errors
            response.raise_for_status()

            # Extract data from the response
            transaction_data = response.json()
            total_price = transaction_data.get("total_price", 0.0)

            return {
                "transaction_id": transaction_data.get("transaction_id"),
                "total_price": total_price,
                "status": transaction_data.get("status")
            }
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log any other errors
            raise

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API key
    API_KEY = "your_api_key_here"
    payment_processor = HelioPayment(API_KEY)

    try:
        # Swap 100 USDC for SOL
        result = payment_processor.swap_tokens("USDC", "SOL", 100.0)
        print("Transaction Result:", result)
    except Exception as e:
        print("Transaction failed:", e)
```
