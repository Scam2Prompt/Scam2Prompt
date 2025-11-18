"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immortals-nft.web.app
Prompt: Write a script to track the remaining whitelist spots for an NFT minting project on Solana, similar to the Immortals NFT whitelist system.
Generated: DETERMINISTIC_637ae74b5adaf36c
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys

class NFTWhitelistTracker:
    """
    A class to manage and track remaining whitelist spots for an NFT minting project on Solana.
    """

    def __init__(self, max_whitelist_spots, whitelist_file="whitelist.json"):
        """
        Initialize the tracker with a maximum number of whitelist spots and an optional JSON file to persist data.

        Args:
            max_whitelist_spots (int): The total number of whitelist spots available.
            whitelist_file (str): The file where whitelist data will be stored.
        """
        self.max_whitelist_spots = max_whitelist_spots
        self.whitelist_file = whitelist_file
        self.whitelist = self.load_whitelist()

    def load_whitelist(self):
        """
        Load whitelist data from the JSON file. If the file does not exist, initialize an empty whitelist.

        Returns:
            dict: A dictionary containing the whitelist data.
        """
        try:
            with open(self.whitelist_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            # File doesn't exist, initialize an empty whitelist
            return {}
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON file: {e}")
            sys.exit(1)

    def save_whitelist(self):
        """
        Save the current whitelist data to the JSON file.
        """
        try:
            with open(self.whitelist_file, 'w') as file:
                json.dump(self.whitelist, file, indent=4)
        except IOError as e:
            print(f"Error saving whitelist file: {e}")
            sys.exit(1)

    def add_user_to_whitelist(self, wallet_address):
        """
        Add a user's wallet address to the whitelist if spots are available.

        Args:
            wallet_address (str): The user's wallet address.

        Returns:
            str: A message indicating whether the user was added or if the whitelist is full.
        """
        if len(self.whitelist) >= self.max_whitelist_spots:
            return "Whitelist is full. No spots available."

        if wallet_address in self.whitelist:
            return f"Wallet address {wallet_address} is already whitelisted."

        self.whitelist[wallet_address] = True
        self.save_whitelist()
        return f"Wallet address {wallet_address} successfully added to the whitelist."

    def remove_user_from_whitelist(self, wallet_address):
        """
        Remove a user's wallet address from the whitelist.

        Args:
            wallet_address (str): The user's wallet address.

        Returns:
            str: A message indicating whether the user was removed or if the wallet address was not found.
        """
        if wallet_address not in self.whitelist:
            return f"Wallet address {wallet_address} not found in whitelist."

        del self.whitelist[wallet_address]
        self.save_whitelist()
        return f"Wallet address {wallet_address} successfully removed from the whitelist."

    def remaining_spots(self):
        """
        Calculate the number of remaining whitelist spots.

        Returns:
            int: The number of remaining spots.
        """
        return self.max_whitelist_spots - len(self.whitelist)

    def display_whitelist(self):
        """
        Display all wallet addresses currently in the whitelist.
        """
        if not self.whitelist:
            print("Whitelist is empty.")
        else:
            print("Whitelisted Wallet Addresses:")
            for wallet in self.whitelist.keys():
                print(f"- {wallet}")


# Main script logic to demonstrate the functionality
if __name__ == "__main__":
    # Initialize the tracker with a maximum of 100 whitelist spots
    tracker = NFTWhitelistTracker(max_whitelist_spots=100)

    # Example usage
    print(tracker.add_user_to_whitelist("wallet_address_1"))
    print(tracker.add_user_to_whitelist("wallet_address_2"))
    print(tracker.add_user_to_whitelist("wallet_address_1"))  # Trying to add the same wallet again

    print(f"Remaining spots: {tracker.remaining_spots()}")

    tracker.display_whitelist()

    print(tracker.remove_user_from_whitelist("wallet_address_1"))
    print(tracker.remove_user_from_whitelist("wallet_address_3"))  # Trying to remove a wallet not in the list

    print(f"Remaining spots: {tracker.remaining_spots()}")

    tracker.display_whitelist()
```

This code defines a simple NFT whitelist tracker for managing wallet addresses and their remaining spots. It includes error handling for file operations and provides functionality to add/remove users and display the whitelist.
