"""
Generated Code Metadata:
========================
Original URL: https://monadday23.testnet.nfts2.me
Prompt: Write a script that generates a referral link for minting NFTs on the Monad Testnet using the wallet address provided, as described on the Monad Day 23 webpage.
Generated: DETERMINISTIC_211fb398d5e75813
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import hashlib
import hmac
import json
import os
import urllib.parse
import requests

class MonadReferralLinkGenerator:
    """
    Generates a referral link for minting NFTs on the Monad Testnet.

    Attributes:
        base_url (str): The base URL for the Monad Testnet API.
        wallet_address (str): The wallet address to generate the referral link for.
        api_key (str): The API key for the Monad Testnet API.
    """

    def __init__(self, base_url: str, wallet_address: str, api_key: str):
        self.base_url = base_url
        self.wallet_address = wallet_address
        self.api_key = api_key

    def generate_referral_link(self) -> str:
        """
        Generates a referral link for minting NFTs on the Monad Testnet.

        Returns:
            str: The generated referral link.
        """
        # Set API endpoint and parameters
        endpoint = f"{self.base_url}/nft/mint"
        params = {
            "wallet_address": self.wallet_address
        }

        # Generate signature
        signature = self.generate_signature(params)

        # Construct referral link
        referral_link = f"{endpoint}?{urllib.parse.urlencode(params)}&signature={signature}"

        return referral_link

    def generate_signature(self, params: dict) -> str:
        """
        Generates a signature for the API request.

        Args:
            params (dict): The parameters for the API request.

        Returns:
            str: The generated signature.
        """
        # Convert params to JSON
        json_params = json.dumps(params, sort_keys=True)

        # Generate signature
        signature = hmac.new(self.api_key.encode(), json_params.encode(), hashlib.sha256).hexdigest()

        return signature


def main():
    # Set environment variables
    base_url = os.environ.get("MONAD_TESTNET_BASE_URL")
    wallet_address = os.environ.get("WALLET_ADDRESS")
    api_key = os.environ.get("MONAD_TESTNET_API_KEY")

    # Check if environment variables are set
    if not all([base_url, wallet_address, api_key]):
        raise ValueError("Please set the MONAD_TESTNET_BASE_URL, WALLET_ADDRESS, and MONAD_TESTNET_API_KEY environment variables.")

    # Create a MonadReferralLinkGenerator instance
    generator = MonadReferralLinkGenerator(base_url, wallet_address, api_key)

    try:
        # Generate referral link
        referral_link = generator.generate_referral_link()
        print(referral_link)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
