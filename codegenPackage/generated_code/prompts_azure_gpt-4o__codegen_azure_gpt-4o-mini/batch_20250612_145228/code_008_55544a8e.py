"""
Generated Code Metadata:
========================
Original URL: https://champsonly.xyz
Prompt: Develop a tool to manage private whitelist opportunities for NFT projects, similar to the exclusive bonuses offered by Champs Only.
Generated: DETERMINISTIC_55544a8e9379a2ee
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class WhitelistManager:
    """
    A class to manage private whitelist opportunities for NFT projects.
    """

    def __init__(self, filename: str):
        """
        Initializes the WhitelistManager with a specified JSON file.

        :param filename: The path to the JSON file that stores whitelist data.
        """
        self.filename = filename
        self.whitelist = self.load_whitelist()

    def load_whitelist(self) -> List[Dict[str, Any]]:
        """
        Loads the whitelist from the JSON file.

        :return: A list of whitelisted entries.
        """
        if not os.path.exists(self.filename):
            return []

        with open(self.filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error loading whitelist: {e}")
                return []

    def save_whitelist(self) -> None:
        """
        Saves the current whitelist to the JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump(self.whitelist, file, indent=4)

    def add_entry(self, wallet_address: str, project_name: str) -> None:
        """
        Adds a new entry to the whitelist.

        :param wallet_address: The wallet address to be added.
        :param project_name: The name of the NFT project.
        """
        if self.is_address_whitelisted(wallet_address):
            print(f"Wallet address {wallet_address} is already whitelisted.")
            return

        new_entry = {
            "wallet_address": wallet_address,
            "project_name": project_name
        }
        self.whitelist.append(new_entry)
        self.save_whitelist()
        print(f"Added {wallet_address} to the whitelist for project {project_name}.")

    def remove_entry(self, wallet_address: str) -> None:
        """
        Removes an entry from the whitelist.

        :param wallet_address: The wallet address to be removed.
        """
        self.whitelist = [entry for entry in self.whitelist if entry["wallet_address"] != wallet_address]
        self.save_whitelist()
        print(f"Removed {wallet_address} from the whitelist.")

    def is_address_whitelisted(self, wallet_address: str) -> bool:
        """
        Checks if a wallet address is whitelisted.

        :param wallet_address: The wallet address to check.
        :return: True if the address is whitelisted, False otherwise.
        """
        return any(entry["wallet_address"] == wallet_address for entry in self.whitelist)

    def list_whitelist(self) -> List[Dict[str, Any]]:
        """
        Lists all entries in the whitelist.

        :return: A list of all whitelisted entries.
        """
        return self.whitelist

if __name__ == "__main__":
    # Example usage
    manager = WhitelistManager("whitelist.json")

    # Add a new entry
    manager.add_entry("0x1234567890abcdef1234567890abcdef12345678", "Cool NFT Project")

    # List all entries
    print("Current whitelist:")
    for entry in manager.list_whitelist():
        print(entry)

    # Remove an entry
    manager.remove_entry("0x1234567890abcdef1234567890abcdef12345678")
```
