"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nano-39g.pages.dev
Prompt: What are the steps to select sync types for various wallets in the MultiChainsFI framework?
Generated: DETERMINISTIC_c4e4de9a225317fc
Batch ID: 20250612_161435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MultiChainsFI:
    """
    A class to manage different wallet types and their sync methods within the MultiChainsFI framework.
    """

    def __init__(self):
        # Initialize a dictionary to hold wallet sync types
        self.wallet_sync_types = {
            "Bitcoin": None,
            "Ethereum": None,
            "Litecoin": None
        }

    def select_sync_type(self, wallet_name: str, sync_type: str) -> None:
        """
        Selects a sync type for a given wallet.

        :param wallet_name: The name of the wallet (e.g., 'Bitcoin', 'Ethereum').
        :param sync_type: The sync type to be set (e.g., 'full', 'light').
        :raises ValueError: If the wallet name or sync type is invalid.
        """
        # Validate wallet name
        if wallet_name not in self.wallet_sync_types:
            raise ValueError(f"Invalid wallet name: {wallet_name}. Supported wallets are: {list(self.wallet_sync_types.keys())}")

        # Validate sync type
        valid_sync_types = ['full', 'light', 'none']
        if sync_type not in valid_sync_types:
            raise ValueError(f"Invalid sync type: {sync_type}. Supported sync types are: {valid_sync_types}")

        # Set the sync type for the wallet
        self.wallet_sync_types[wallet_name] = sync_type
        print(f"Sync type for {wallet_name} set to {sync_type}.")

    def get_sync_type(self, wallet_name: str) -> str:
        """
        Retrieves the current sync type for a given wallet.

        :param wallet_name: The name of the wallet to query.
        :return: The sync type of the specified wallet.
        :raises ValueError: If the wallet name is invalid.
        """
        # Validate wallet name
        if wallet_name not in self.wallet_sync_types:
            raise ValueError(f"Invalid wallet name: {wallet_name}. Supported wallets are: {list(self.wallet_sync_types.keys())}")

        sync_type = self.wallet_sync_types[wallet_name]
        return sync_type if sync_type else "No sync type set."

    def list_wallets(self) -> None:
        """
        Lists all wallets and their current sync types.
        """
        for wallet, sync_type in self.wallet_sync_types.items():
            sync_info = sync_type if sync_type else "No sync type set."
            print(f"{wallet}: {sync_info}")


# Example usage
if __name__ == "__main__":
    try:
        multi_chains_fi = MultiChainsFI()
        multi_chains_fi.select_sync_type("Bitcoin", "full")
        multi_chains_fi.list_wallets()
        print(multi_chains_fi.get_sync_type("Bitcoin"))
    except ValueError as e:
        print(f"Error: {e}")
```
