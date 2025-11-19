"""
Generated Code Metadata:
========================
Original URL: https://sui-dapps.vercel.app
Prompt: Generate a tutorial for creating a gaming application on Sui that utilizes tradable in-game assets and customizable transfer policies.
Generated: DETERMINISTIC_d51ce23c4ab2e2b7
Batch ID: 20250612_162217
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from sui_sdk import SuiClient, TransactionBuilder, Asset, TransferPolicy
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class GameAssetManager:
    def __init__(self, client: SuiClient):
        """
        Initialize the GameAssetManager with a Sui client.

        :param client: An instance of SuiClient to interact with the Sui blockchain.
        """
        self.client = client

    def create_asset(self, asset_name: str, asset_value: float) -> Asset:
        """
        Create a new tradable in-game asset.

        :param asset_name: The name of the asset.
        :param asset_value: The value of the asset.
        :return: An instance of Asset representing the created asset.
        """
        try:
            asset = Asset(name=asset_name, value=asset_value)
            self.client.create_asset(asset)
            logging.info(f"Asset created: {asset_name} with value {asset_value}")
            return asset
        except Exception as e:
            logging.error(f"Error creating asset: {e}")
            raise

    def set_transfer_policy(self, asset: Asset, policy: TransferPolicy):
        """
        Set a customizable transfer policy for an asset.

        :param asset: The asset for which to set the transfer policy.
        :param policy: The transfer policy to apply.
        """
        try:
            asset.set_transfer_policy(policy)
            logging.info(f"Transfer policy set for asset: {asset.name}")
        except Exception as e:
            logging.error(f"Error setting transfer policy: {e}")
            raise

    def transfer_asset(self, asset: Asset, recipient_address: str):
        """
        Transfer an asset to a specified recipient.

        :param asset: The asset to transfer.
        :param recipient_address: The address of the recipient.
        """
        try:
            transaction = TransactionBuilder()
            transaction.add_transfer(asset, recipient_address)
            self.client.submit_transaction(transaction)
            logging.info(f"Asset {asset.name} transferred to {recipient_address}")
        except Exception as e:
            logging.error(f"Error transferring asset: {e}")
            raise

# Example usage
if __name__ == "__main__":
    # Initialize Sui client
    client = SuiClient(api_key="YOUR_API_KEY")

    # Create an instance of GameAssetManager
    asset_manager = GameAssetManager(client)

    # Create a new asset
    new_asset = asset_manager.create_asset("Sword of Destiny", 100.0)

    # Define a transfer policy
    transfer_policy = TransferPolicy(allow_trade=True, allow_gift=False)

    # Set the transfer policy for the new asset
    asset_manager.set_transfer_policy(new_asset, transfer_policy)

    # Transfer the asset to a recipient
    asset_manager.transfer_asset(new_asset, "recipient_address_here")
```
