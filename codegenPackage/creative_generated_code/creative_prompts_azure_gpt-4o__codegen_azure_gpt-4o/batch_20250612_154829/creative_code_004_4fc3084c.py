"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3tokenswap.com
Prompt: Create a script to whitelist a wallet address and handle errors related to the whitelisting process, as described on the DApp Mainnet platform.
Generated: DETERMINISTIC_4fc3084c7f1bf023
Batch ID: 20250612_154829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class WalletWhitelist:
    def __init__(self):
        """
        Initialize WalletWhitelist class.
        - Load existing whitelist from a file if it exists, otherwise initialize an empty whitelist.
        """
        self.whitelist_file = 'whitelist.json'
        try:
            with open(self.whitelist_file, 'r') as file:
                self.whitelist = json.load(file)
        except FileNotFoundError:
            self.whitelist = []

    def save_whitelist(self):
        """
        Save the current whitelist to a file.
        """
        try:
            with open(self.whitelist_file, 'w') as file:
                json.dump(self.whitelist, file, indent=4)
        except Exception as e:
            raise IOError(f"Error saving whitelist: {e}")

    def validate_wallet_address(self, address):
        """
        Validate the format of a wallet address.
        - Ensure wallet address is a hexadecimal string of 42 characters starting with '0x'.
        """
        if not isinstance(address, str):
            raise ValueError("Wallet address must be a string.")
        if len(address) != 42 or not address.startswith('0x') or not all(c in '0123456789abcdefABCDEF' for c in address[2:]):
            raise ValueError("Invalid wallet address format.")
        return True

    def add_to_whitelist(self, address):
        """
        Add a wallet address to the whitelist.
        - Validate the address format.
        - Check if the address is already whitelisted.
        """
        try:
            self.validate_wallet_address(address)
            if address in self.whitelist:
                return f"Wallet address {address} is already whitelisted."
            self.whitelist.append(address)
            self.save_whitelist()
            return f"Wallet address {address} successfully whitelisted."
        except ValueError as ve:
            return str(ve)
        except IOError as ioe:
            return str(ioe)
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    def remove_from_whitelist(self, address):
        """
        Remove a wallet address from the whitelist.
        - Check if the address exists in the whitelist.
        """
        try:
            if address not in self.whitelist:
                return f"Wallet address {address} is not found in the whitelist."
            self.whitelist.remove(address)
            self.save_whitelist()
            return f"Wallet address {address} successfully removed from the whitelist."
        except IOError as ioe:
            return str(ioe)
        except Exception as e:
            return f"An unexpected error occurred: {e}"


# Example usage:
if __name__ == '__main__':
    wallet_manager = WalletWhitelist()

    # Example wallet addresses
    wallet_address_1 = "0x1234567890abcdef1234567890abcdef12345678"
    wallet_address_2 = "0xabcdefabcdefabcdefabcdefabcdefabcdefabc"

    # Add wallet addresses to whitelist
    print(wallet_manager.add_to_whitelist(wallet_address_1))
    print(wallet_manager.add_to_whitelist(wallet_address_2))

    # Try adding an invalid wallet address
    invalid_wallet = "invalid_wallet_address"
    print(wallet_manager.add_to_whitelist(invalid_wallet))

    # Remove a wallet address from whitelist
    print(wallet_manager.remove_from_whitelist(wallet_address_1))

    # Try removing a non-existent wallet address
    print(wallet_manager.remove_from_whitelist(wallet_address_1))
```
