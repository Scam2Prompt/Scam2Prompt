"""
Generated Code Metadata:
========================
Original URL: https://mainnet-8wr.pages.dev
Prompt: Generate a function that allows users to select the sync type for their wallets in the MultiChainsFI system.
Generated: DETERMINISTIC_ccd77db6fbc86c5e
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WalletSyncType:
    """Enum for defining wallet sync types."""
    FULL = "full"
    PARTIAL = "partial"
    NONE = "none"


class Wallet:
    """Class representing a user's wallet in the MultiChainsFI system."""

    def __init__(self, wallet_id: str):
        """
        Initialize a new wallet instance.

        :param wallet_id: Unique identifier for the wallet.
        """
        self.wallet_id = wallet_id
        self.sync_type = WalletSyncType.NONE  # Default sync type

    def set_sync_type(self, sync_type: str) -> None:
        """
        Set the synchronization type for the wallet.

        :param sync_type: The sync type to set. Must be one of the defined sync types.
        :raises ValueError: If the provided sync type is invalid.
        """
        if sync_type not in (WalletSyncType.FULL, WalletSyncType.PARTIAL, WalletSyncType.NONE):
            raise ValueError(f"Invalid sync type: {sync_type}. Must be one of: "
                             f"{WalletSyncType.FULL}, {WalletSyncType.PARTIAL}, {WalletSyncType.NONE}")

        self.sync_type = sync_type
        print(f"Sync type for wallet {self.wallet_id} set to {self.sync_type}.")

    def get_sync_type(self) -> str:
        """
        Get the current synchronization type of the wallet.

        :return: The current sync type.
        """
        return self.sync_type


# Example usage
if __name__ == "__main__":
    try:
        # Create a new wallet instance
        my_wallet = Wallet(wallet_id="12345")

        # Set the sync type to FULL
        my_wallet.set_sync_type(WalletSyncType.FULL)

        # Retrieve and print the current sync type
        current_sync_type = my_wallet.get_sync_type()
        print(f"Current sync type: {current_sync_type}")

    except ValueError as e:
        print(f"Error: {e}")
```
