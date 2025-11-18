"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sui-dapps.vercel.app
Prompt: Provide a code example for implementing asset ownership and evolution onchain using Sui's unique features.
Generated: DETERMINISTIC_17490ce075834b61
Batch ID: 20250612_155006
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://testnet.sui.io": {
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
# Import necessary modules from the Sui SDK
from sui import SuiClient, TransactionBuilder, ObjectType, MoveCall

# Define constants for the Sui network
SUI_NETWORK_URL = "https://testnet.sui.io"
ASSET_MODULE = "0xYourModuleAddress"  # Replace with your asset module address

class AssetManager:
    def __init__(self):
        """Initialize the SuiClient for interacting with the Sui blockchain."""
        self.client = SuiClient(SUI_NETWORK_URL)

    def create_asset(self, owner_address: str, asset_name: str, metadata: dict) -> str:
        """
        Create a new asset on the Sui blockchain.

        :param owner_address: The address of the asset owner
        :param asset_name: The name of the asset
        :param metadata: Additional metadata for the asset
        :return: The transaction ID of the created asset
        """
        try:
            # Build the transaction to create an asset
            tx_builder = TransactionBuilder()
            tx_builder.move_call(
                function=f"{ASSET_MODULE}::create_asset",
                args=[owner_address, asset_name, metadata],
                type_arguments=[],
            )
            # Execute the transaction
            response = self.client.execute_transaction(tx_builder.build())
            return response['transaction_id']
        except Exception as e:
            print(f"Failed to create asset: {str(e)}")
            return None

    def transfer_asset(self, asset_id: str, new_owner_address: str) -> str:
        """
        Transfer ownership of an asset to a new owner.

        :param asset_id: The ID of the asset to transfer
        :param new_owner_address: The new owner's address
        :return: The transaction ID of the transfer
        """
        try:
            # Build the transaction to transfer an asset
            tx_builder = TransactionBuilder()
            tx_builder.move_call(
                function=f"{ASSET_MODULE}::transfer_asset",
                args=[asset_id, new_owner_address],
                type_arguments=[],
            )
            # Execute the transaction
            response = self.client.execute_transaction(tx_builder.build())
            return response['transaction_id']
        except Exception as e:
            print(f"Failed to transfer asset: {str(e)}")
            return None

    def evolve_asset(self, asset_id: str, new_data: dict) -> str:
        """
        Evolve an asset by updating its metadata or properties.

        :param asset_id: The ID of the asset to evolve
        :param new_data: The new data to update the asset with
        :return: The transaction ID of the evolution
        """
        try:
            # Build the transaction to evolve an asset
            tx_builder = TransactionBuilder()
            tx_builder.move_call(
                function=f"{ASSET_MODULE}::evolve_asset",
                args=[asset_id, new_data],
                type_arguments=[],
            )
            # Execute the transaction
            response = self.client.execute_transaction(tx_builder.build())
            return response['transaction_id']
        except Exception as e:
            print(f"Failed to evolve asset: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    asset_manager = AssetManager()
    
    # Create a new asset
    asset_id = asset_manager.create_asset("0xOwnerAddress", "MyAsset", {"description": "This is my asset."})
    if asset_id:
        print(f"Asset created with ID: {asset_id}")
        
        # Transfer the asset
        transfer_id = asset_manager.transfer_asset(asset_id, "0xNewOwnerAddress")
        if transfer_id:
            print(f"Asset transferred. Transaction ID: {transfer_id}")
        
        # Evolve the asset
        evolve_id = asset_manager.evolve_asset(asset_id, {"description": "Updated description."})
        if evolve_id:
            print(f"Asset evolved. Transaction ID: {evolve_id}")
```
