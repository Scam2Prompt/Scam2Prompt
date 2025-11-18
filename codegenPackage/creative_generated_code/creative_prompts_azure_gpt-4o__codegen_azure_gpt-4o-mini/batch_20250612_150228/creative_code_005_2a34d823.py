"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicstr6f6nebuy7tjlpjgzecshw3segkzgnu4rzkkzrr6hrawmofg4.ipfs.dweb.link
Prompt: Create a code snippet to fetch and display the total supply of `rsTAO` and `wrsTAO` tokens from the Rivus Connect Wallet system.
Generated: DETERMINISTIC_2a34d8234258369b
Batch ID: 20250612_150228
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.rivusconnect.com/v1": {
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

class RivusWalletAPI:
    BASE_URL = "https://api.rivusconnect.com/v1"  # Base URL for the Rivus Connect API

    @staticmethod
    def fetch_token_supply(token_name):
        """
        Fetch the total supply of a specified token from the Rivus Connect Wallet.

        Args:
            token_name (str): The name of the token to fetch the supply for.

        Returns:
            float: The total supply of the token.

        Raises:
            ValueError: If the token supply cannot be fetched.
            Exception: For other general errors.
        """
        try:
            response = requests.get(f"{RivusWalletAPI.BASE_URL}/tokens/{token_name}/supply")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()
            return float(data['totalSupply'])  # Assumes the API returns a float value for total supply
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise ValueError(f"Failed to fetch supply for {token_name}.")
        except KeyError:
            print("Error: Unexpected data format received from the API.")  # Handle unexpected data format
            raise ValueError(f"Failed to fetch supply for {token_name}.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Catch all other exceptions
            raise

def display_token_supplies():
    """
    Fetch and display the total supply of rsTAO and wrsTAO tokens.
    """
    tokens = ['rsTAO', 'wrsTAO']
    for token in tokens:
        try:
            supply = RivusWalletAPI.fetch_token_supply(token)
            print(f"The total supply of {token} is: {supply}")
        except ValueError as ve:
            print(ve)

if __name__ == "__main__":
    display_token_supplies()  # Entry point to fetch and display token supplies
```
