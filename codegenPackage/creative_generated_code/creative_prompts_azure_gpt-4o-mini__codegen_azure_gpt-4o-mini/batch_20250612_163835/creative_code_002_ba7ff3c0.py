"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snso.com.cn
Prompt: What are the best practices for managing multiple blockchain assets securely using TPWallet?
Generated: DETERMINISTIC_ba7ff3c016d7114b
Batch ID: 20250612_163835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import logging
from tp_wallet import TPWalletAPI, WalletError

# Configure logging for debugging and error tracking
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class MultiAssetManager:
    def __init__(self, api_key: str):
        """
        Initialize the MultiAssetManager with the TPWallet API key.
        
        Args:
            api_key (str): The API key for TPWallet to authenticate requests.
        """
        self.api_key = api_key
        self.wallet_api = TPWalletAPI(api_key)
    
    def get_assets(self):
        """
        Retrieve the list of blockchain assets from the wallet.

        Returns:
            list: A list of assets managed in the wallet.
        """
        try:
            assets = self.wallet_api.get_assets()
            logging.info("Assets retrieved successfully.")
            return assets
        except WalletError as e:
            logging.error(f"Failed to retrieve assets: {e}")
            sys.exit(1)
    
    def transfer_asset(self, asset_id: str, amount: float, recipient: str):
        """
        Transfer a specified amount of a blockchain asset to a recipient.

        Args:
            asset_id (str): The ID of the asset to transfer.
            amount (float): The amount of the asset to transfer.
            recipient (str): The address of the recipient.
        """
        try:
            self.wallet_api.transfer(asset_id, amount, recipient)
            logging.info(f"Successfully transferred {amount} of asset {asset_id} to {recipient}.")
        except WalletError as e:
            logging.error(f"Transfer failed: {e}")
            sys.exit(1)

    def create_asset(self, asset_name: str, initial_supply: float):
        """
        Create a new blockchain asset.

        Args:
            asset_name (str): The name of the new asset.
            initial_supply (float): The initial supply of the asset.
        
        Returns:
            str: The ID of the newly created asset.
        """
        try:
            asset_id = self.wallet_api.create_asset(asset_name, initial_supply)
            logging.info(f"Asset '{asset_name}' created successfully with ID: {asset_id}.")
            return asset_id
        except WalletError as e:
            logging.error(f"Asset creation failed: {e}")
            sys.exit(1)

# Example usage
if __name__ == "__main__":
    api_key = "your_api_key_here"  # Replace with your actual API key
    manager = MultiAssetManager(api_key)

    # Get current assets
    assets = manager.get_assets()
    print(assets)

    # Create a new asset
    new_asset_id = manager.create_asset("MyToken", 1000000)

    # Transfer an asset
    manager.transfer_asset(new_asset_id, 100, "recipient_wallet_address")
```
