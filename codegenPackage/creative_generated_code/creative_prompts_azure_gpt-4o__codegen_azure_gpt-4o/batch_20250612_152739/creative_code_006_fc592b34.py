"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://decentralizedchains-cp6.pages.dev
Prompt: Develop a tool to connect multiple wallets and manage positions using advanced actions, as described on the webpage. Include functionality for tracking recently connected wallets.
Generated: DETERMINISTIC_fc592b342a17eadc
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class WalletManager:
    """
    A class to manage multiple wallets, track recently connected wallets, 
    and perform advanced actions on positions.
    """

    # File to store recently connected wallets
    RECENT_WALLETS_FILE = "recent_wallets.json"

    def __init__(self):
        """
        Initializes the WalletManager and loads recently connected wallets.
        """
        self.wallets = {}  # Dictionary to store wallet addresses and their positions
        self.recent_wallets = self._load_recent_wallets()

    def connect_wallet(self, wallet_address):
        """
        Connects a wallet and tracks it as recently connected.
        
        :param wallet_address: The address of the wallet to connect.
        """
        if wallet_address in self.wallets:
            print(f"Wallet {wallet_address} is already connected.")
        else:
            self.wallets[wallet_address] = {"positions": []}  # Initialize wallet positions
            print(f"Wallet {wallet_address} connected successfully.")
        
        self._track_recent_wallet(wallet_address)

    def manage_positions(self, wallet_address, action, position_data=None):
        """
        Performs advanced actions on wallet positions.
        
        :param wallet_address: The address of the wallet to manage positions for.
        :param action: The action to perform ('add', 'remove', 'update').
        :param position_data: The data for the position (required for 'add' and 'update').
        
        :raises ValueError: If the wallet is not connected or invalid action.
        """
        if wallet_address not in self.wallets:
            raise ValueError(f"Wallet {wallet_address} is not connected.")

        if action == "add":
            if not position_data:
                raise ValueError("Position data is required for 'add' action.")
            self.wallets[wallet_address]["positions"].append(position_data)
            print(f"Position added successfully for wallet {wallet_address}.")
        
        elif action == "remove":
            if not position_data:
                raise ValueError("Position data is required for 'remove' action.")
            if position_data in self.wallets[wallet_address]["positions"]:
                self.wallets[wallet_address]["positions"].remove(position_data)
                print(f"Position removed successfully for wallet {wallet_address}.")
            else:
                print("Position not found.")
        
        elif action == "update":
            if not position_data:
                raise ValueError("Position data is required for 'update' action.")
            # Update logic can be implemented here
            print("Position updated successfully.")
        
        else:
            raise ValueError(f"Invalid action: {action}.")

    def _track_recent_wallet(self, wallet_address):
        """
        Tracks the wallet as recently connected and saves the list.
        
        :param wallet_address: The wallet address to track.
        """
        if wallet_address not in self.recent_wallets:
            self.recent_wallets.append(wallet_address)
            # Save the recent wallets to a file
            self._save_recent_wallets()
            print(f"Wallet {wallet_address} added to recently connected wallets.")

    def _load_recent_wallets(self):
        """
        Loads the list of recently connected wallets from a file.
        
        :return: List of recently connected wallets.
        """
        if os.path.exists(self.RECENT_WALLETS_FILE):
            try:
                with open(self.RECENT_WALLETS_FILE, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Failed to load recent wallets. Starting fresh.")
        return []

    def _save_recent_wallets(self):
        """
        Saves the list of recently connected wallets to a file.
        """
        try:
            with open(self.RECENT_WALLETS_FILE, "w") as file:
                json.dump(self.recent_wallets, file)
        except IOError as e:
            print(f"Failed to save recent wallets: {e}")

    def list_recent_wallets(self):
        """
        Lists recently connected wallets.
        
        :return: List of recently connected wallets.
        """
        return self.recent_wallets

if __name__ == "__main__":
    # Example usage of the WalletManager
    manager = WalletManager()

    # Connect wallets
    manager.connect_wallet("0x123")
    manager.connect_wallet("0x456")

    # Manage positions
    manager.manage_positions("0x123", "add", {"token": "ETH", "amount": 1.5})
    manager.manage_positions("0x123", "remove", {"token": "ETH", "amount": 1.5})

    # List recently connected wallets
    print("Recently connected wallets:", manager.list_recent_wallets())
```
