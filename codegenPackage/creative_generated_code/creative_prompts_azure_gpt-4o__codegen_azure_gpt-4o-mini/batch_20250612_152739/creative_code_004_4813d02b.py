"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theheist-giveaways.web.app
Prompt: Develop a function to verify recipient addresses for Solana-based payments, inspired by Helio's "Unverified Recipient" feature.
Generated: DETERMINISTIC_4813d02bebfd846c
Batch ID: 20250612_152739
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mainnet-beta.solana.com": {
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

class SolanaAddressVerifier:
    """
    A class to verify Solana addresses using the Solana blockchain API.
    """

    def __init__(self, api_url: str):
        """
        Initialize the SolanaAddressVerifier with the provided API URL.

        :param api_url: URL of the Solana JSON RPC API
        """
        self.api_url = api_url

    def is_valid_address(self, address: str) -> bool:
        """
        Validate the format of a Solana address.

        :param address: Solana address to validate
        :return: True if the address is valid, False otherwise
        """
        # A valid Solana address is 44 characters long and base58 encoded
        return len(address) == 44 and all(c in self.base58_alphabet() for c in address)

    @staticmethod
    def base58_alphabet() -> str:
        """
        Returns the base58 alphabet used in Solana addresses.

        :return: A string containing the base58 alphabet
        """
        return "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

    def verify_address(self, address: str) -> dict:
        """
        Verify the existence of a Solana address on the blockchain.

        :param address: The Solana address to verify
        :return: A dictionary containing verification results
        """
        if not self.is_valid_address(address):
            raise ValueError("Invalid Solana address format.")

        try:
            response = requests.post(
                self.api_url,
                json={"jsonrpc": "2.0", "id": 1, "method": "getAccountInfo", "params": [address]}
            )
            response.raise_for_status()  # Raise an error for HTTP issues
            data = response.json()

            # Check if the address exists on the blockchain
            if 'result' in data and data['result'] is not None:
                return {"address": address, "exists": True, "data": data['result']}
            else:
                return {"address": address, "exists": False}

        except requests.RequestException as e:
            # Handle network-related errors
            raise RuntimeError(f"Network error occurred: {e}")
        except ValueError as e:
            # Handle JSON decoding errors
            raise RuntimeError(f"Error decoding response: {e}")

# Example usage:
if __name__ == "__main__":
    api_url = "https://api.mainnet-beta.solana.com"  # Mainnet Solana API
    verifier = SolanaAddressVerifier(api_url)

    try:
        result = verifier.verify_address("YourSolanaAddressHere")
        print(result)
    except ValueError as ve:
        print(f"Validation error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
```
