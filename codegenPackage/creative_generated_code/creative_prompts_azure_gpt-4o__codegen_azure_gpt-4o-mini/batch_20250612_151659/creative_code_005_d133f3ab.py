"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-staking-xi.vercel.app
Prompt: Create a script to query the Exeptra NFT-staking Dapp for details about staked NFTs and their associated $EXP token rewards.
Generated: DETERMINISTIC_d133f3ab2ec99e6c
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.exeptra.com/staking": {
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

class ExeptraNFTStaking:
    """Class to interact with the Exeptra NFT Staking DApp."""

    BASE_URL = "https://api.exeptra.com/staking"  # Base URL of the Exeptra API

    def __init__(self, wallet_address):
        """Initialize the staking client with a wallet address.

        Args:
            wallet_address (str): The wallet address to query for staked NFTs.
        """
        self.wallet_address = wallet_address

    def get_staked_nfts(self):
        """Retrieve the list of staked NFTs for the given wallet.

        Returns:
            list: A list of dictionaries containing staked NFT details.
        """
        url = f"{self.BASE_URL}/nfts?wallet={self.wallet_address}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response as a Python dictionary
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return []

    def get_token_rewards(self):
        """Retrieve the $EXP token rewards for the given wallet.

        Returns:
            float: The total $EXP rewards associated with staked NFTs.
        """
        url = f"{self.BASE_URL}/rewards?wallet={self.wallet_address}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            rewards_data = response.json()
            return rewards_data.get("total_rewards", 0.0)  # Return total rewards with a default of 0.0
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return 0.0
        except requests.exceptions.RequestException as err:
            print(f"Error occurred: {err}")
            return 0.0

    def display_info(self):
        """Fetch and display the staked NFTs and their associated rewards."""
        staked_nfts = self.get_staked_nfts()
        total_rewards = self.get_token_rewards()

        print(f"Wallet Address: {self.wallet_address}")
        print(f"Total $EXP Rewards: {total_rewards:.2f}")
        print("Staked NFTs:")
        if staked_nfts:
            for nft in staked_nfts:
                print(f"- ID: {nft.get('id')}, Name: {nft.get('name')}, Rarity: {nft.get('rarity')}")
        else:
            print("No NFTs staked.")


if __name__ == "__main__":
    # Example usage
    wallet_address = "0xYourWalletAddressHere"  # Replace with your wallet address
    staking_client = ExeptraNFTStaking(wallet_address)
    staking_client.display_info()
```
