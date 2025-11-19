"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mainnet-8wr.pages.dev
Prompt: Generate a function that allows users to select the sync type for their wallets in the MultiChainsFI system.
Generated: DETERMINISTIC_ccd77db6fbc86c5e
Batch ID: 20250612_163200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WalletSyncType:
    """Enumeration of possible wallet sync types."""
    FULL = "full"
    PARTIAL = "partial"
    NONE = "none"

class Wallet:
    """Class representing a user's wallet in the MultiChainsFI system."""

    def __init__(self, wallet_id: str):
        """Initialize the Wallet instance.

        Args:
            wallet_id (str): Unique identifier for the wallet.
        """
        if not wallet_id:
            raise ValueError("wallet_id cannot be empty.")
        self.wallet_id = wallet_id
        self.sync_type = WalletSyncType.NONE

    def set_sync_type(self, sync_type: str):
        """Set the synchronization type for the wallet.

        Args:
            sync_type (str): The sync type to be set. Should be one of 'full', 'partial', or 'none'.

        Raises:
            ValueError: If the provided sync type is invalid.
        """
        if sync_type not in (WalletSyncType.FULL, WalletSyncType.PARTIAL, WalletSyncType.NONE):
            raise ValueError(f"Invalid sync type: {sync_type}. Must be one of {', '.join([WalletSyncType.FULL, WalletSyncType.PARTIAL, WalletSyncType.NONE])}.")
        
        self.sync_type = sync_type
        print(f"Sync type for wallet {self.wallet_id} set to {self.sync_type}.")

# Example usage
def main():
    """Main function to demonstrate wallet sync type setting."""
    try:
        wallet = Wallet(wallet_id="123456")
        wallet.set_sync_type(WalletSyncType.FULL)  # Set to full sync
        wallet.set_sync_type("invalid_sync")  # This will raise an error
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
