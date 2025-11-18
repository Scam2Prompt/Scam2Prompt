"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonfreespin.com
Prompt: Write code to display a welcome bonus for users who own a specific NFT, similar to the "Welcome bonus- For User TON" feature on TONfreespin.com.
Generated: DETERMINISTIC_7a19a95fd04a26a5
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nftservice.com/user": {
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
import json
import requests

class NFTBonusManager:
    """
    A class to manage welcome bonuses for users who hold specific NFTs.
    """

    def __init__(self, nft_contract_address: str, api_endpoint: str):
        """
        Initializes the NFTBonusManager with the NFT contract address and the API endpoint.

        :param nft_contract_address: The address of the NFT contract to check ownership against.
        :param api_endpoint: The API endpoint to fetch user NFT data.
        """
        self.nft_contract_address = nft_contract_address
        self.api_endpoint = api_endpoint

    def get_user_nft_data(self, user_address: str) -> dict:
        """
        Fetches the NFT data for a given user address.

        :param user_address: The wallet address of the user.
        :return: A dictionary containing user's NFT data.
        """
        try:
            response = requests.get(f"{self.api_endpoint}/{user_address}")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Parse and return the JSON response
        except requests.RequestException as e:
            print(f"Error fetching NFT data: {e}")
            return {}

    def user_eligible_for_bonus(self, user_nft_data: dict) -> bool:
        """
        Checks if the user is eligible for a welcome bonus based on their NFT ownership.

        :param user_nft_data: A dictionary containing user's NFT data.
        :return: True if eligible for a bonus, False otherwise.
        """
        # Assuming the NFT we are checking for is represented in the user's NFT data as a specific token ID
        required_nft_token_id = "specific-nft-token-id"  # Replace with the actual token ID
        return any(nft['token_id'] == required_nft_token_id for nft in user_nft_data.get('nfts', []))

    def display_welcome_bonus(self, user_address: str) -> None:
        """
        Displays the welcome bonus for the user if they hold the specific NFT.

        :param user_address: The wallet address of the user.
        """
        user_nft_data = self.get_user_nft_data(user_address)

        if not user_nft_data:
            print("No NFT data found for the user.")
            return

        if self.user_eligible_for_bonus(user_nft_data):
            print(f"Welcome bonus awarded to user {user_address}!")
        else:
            print(f"No welcome bonus for user {user_address}. NFT ownership not verified.")

# Example usage
if __name__ == "__main__":
    # Initialize the NFTBonusManager with the NFT contract address and API endpoint
    nft_contract_address = "0xYourNftContractAddress"  # Replace with actual contract address
    api_endpoint = "https://api.nftservice.com/user"  # Replace with actual API endpoint

    bonus_manager = NFTBonusManager(nft_contract_address, api_endpoint)
    
    # Replace with the actual user address to check
    user_address = "0xUserWalletAddress"  # Example user wallet address
    bonus_manager.display_welcome_bonus(user_address)
```
