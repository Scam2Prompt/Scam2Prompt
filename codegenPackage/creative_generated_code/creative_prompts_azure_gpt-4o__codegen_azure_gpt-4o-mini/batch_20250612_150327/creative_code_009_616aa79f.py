"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frax-foundation-site.pages.dev
Prompt: Suggest ways to use the Frax Foundation's tools to facilitate seamless integration of stablecoin transactions into legacy financial systems.
Generated: DETERMINISTIC_616aa79f19a15bec
Batch ID: 20250612_150327
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.frax.finance": {
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

class FraxStablecoinIntegration:
    """
    A class to facilitate the integration of Frax stablecoin transactions
    into legacy financial systems using the Frax Foundation's APIs.
    """

    FRAx_API_URL = "https://api.frax.finance"  # Base API URL for Frax Foundation

    def __init__(self, api_key):
        """
        Initializes the integration class with an API key.

        :param api_key: str - The API key for authenticating with the Frax API.
        """
        self.api_key = api_key

    def get_stablecoin_balance(self, wallet_address):
        """
        Retrieves the FRAX balance of the specified wallet address.

        :param wallet_address: str - The Ethereum address of the wallet.
        :return: float - The balance of FRAX in the wallet.
        :raises ValueError: If the wallet address is invalid or the response is invalid.
        """
        if not self.validate_address(wallet_address):
            raise ValueError("Invalid wallet address provided.")

        url = f"{self.FRAx_API_URL}/balance/{wallet_address}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data.get("balance", 0.0)

        except requests.RequestException as e:
            print(f"An error occurred while fetching balance: {e}")
            return 0.0

    def validate_address(self, address):
        """
        Validates Ethereum wallet address format.

        :param address: str - The wallet address to validate.
        :return: bool - True if valid, False otherwise.
        """
        # Simple validation for Ethereum address format (not exhaustive)
        return len(address) == 42 and address.startswith("0x")

    def create_transaction(self, from_address, to_address, amount):
        """
        Creates a transaction from one wallet to another.

        :param from_address: str - The sender's wallet address.
        :param to_address: str - The recipient's wallet address.
        :param amount: float - The amount of FRAX to send.
        :return: dict - Response from the transaction creation API.
        :raises ValueError: If any addresses are invalid or the amount is non-positive.
        """
        if not self.validate_address(from_address) or not self.validate_address(to_address):
            raise ValueError("One or both wallet addresses are invalid.")
        if amount <= 0:
            raise ValueError("Transaction amount must be greater than zero.")

        url = f"{self.FRAx_API_URL}/transaction"
        headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = {
            "from": from_address,
            "to": to_address,
            "amount": amount
        }

        try:
            response = requests.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()

        except requests.RequestException as e:
            print(f"An error occurred while creating transaction: {e}")
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    frax_integration = FraxStablecoinIntegration(api_key)

    wallet_address = "0xYourWalletAddressHere"
    try:
        balance = frax_integration.get_stablecoin_balance(wallet_address)
        print(f"FRAX Balance: {balance}")

        # Create a transaction example
        transaction_response = frax_integration.create_transaction(wallet_address, "0xRecipientAddressHere", 10.0)
        print(f"Transaction Response: {transaction_response}")

    except ValueError as ve:
        print(f"Value Error: {ve}")
```
