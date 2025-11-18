"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeie3nw7cyq2q2jw5zaaxhqznmxmr6ano4kkfjked4sebtl2biznzfy.ipfs.dweb.link
Prompt: Generate code to securely store and manage whitelist data for a public pre-sale event, ensuring compatibility with Web3 wallets.
Generated: DETERMINISTIC_bc11f0b7e82501d5
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict
from web3 import Web3
from eth_account import Account

# Define the Whitelist Manager class
class WhitelistManager:
    def __init__(self, storage_file: str):
        """
        Initializes the WhitelistManager with a given storage file.

        :param storage_file: The JSON file where whitelist data is stored.
        """
        self.storage_file = storage_file
        self.whitelist: Dict[str, bool] = self.load_whitelist()

    def load_whitelist(self) -> Dict[str, bool]:
        """
        Loads the whitelist from the JSON storage file.

        :return: A dictionary with addresses as keys and their whitelist status.
        """
        try:
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_whitelist(self):
        """
        Saves the current whitelist to the JSON storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.whitelist, file, indent=4)

    def add_address(self, address: str):
        """
        Adds an address to the whitelist.

        :param address: The Ethereum address to be added.
        """
        if self.is_valid_address(address):
            self.whitelist[address] = True
            self.save_whitelist()
        else:
            raise ValueError(f"{address} is not a valid Ethereum address.")

    def remove_address(self, address: str):
        """
        Removes an address from the whitelist.

        :param address: The Ethereum address to be removed.
        """
        if address in self.whitelist:
            del self.whitelist[address]
            self.save_whitelist()
        else:
            raise ValueError(f"{address} is not found in the whitelist.")

    def is_whitelisted(self, address: str) -> bool:
        """
        Checks if an address is whitelisted.

        :param address: The Ethereum address to check.
        :return: True if the address is whitelisted, otherwise False.
        """
        return self.whitelist.get(address, False)

    @staticmethod
    def is_valid_address(address: str) -> bool:
        """
        Validates an Ethereum address.

        :param address: The address to validate.
        :return: True if valid, otherwise False.
        """
        return Web3.isChecksumAddress(address)

    def get_whitelisted_addresses(self) -> List[str]:
        """
        Retrieves a list of all whitelisted addresses.

        :return: A list of whitelisted Ethereum addresses.
        """
        return list(self.whitelist.keys())

# Example usage
if __name__ == "__main__":
    # Instantiate the WhitelistManager
    wm = WhitelistManager('whitelist.json')

    # Add a valid address to the whitelist
    try:
        wm.add_address('0xAbC1234567890abcdef1234567890ABCDEF1234')
        print("Address added to whitelist.")
    except ValueError as e:
        print(e)

    # Check if an address is whitelisted
    is_whitelisted = wm.is_whitelisted('0xAbC1234567890abcdef1234567890ABCDEF1234')
    print(f"Is address whitelisted? {is_whitelisted}")

    # Get the list of whitelisted addresses
    addresses = wm.get_whitelisted_addresses()
    print("Whitelisted addresses:", addresses)

    # Remove an address from the whitelist
    try:
        wm.remove_address('0xAbC1234567890abcdef1234567890ABCDEF1234')
        print("Address removed from whitelist.")
    except ValueError as e:
        print(e)
```
