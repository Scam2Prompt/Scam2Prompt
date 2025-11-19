"""
Generated Code Metadata:
========================
Original URL: https://synspad.web.app
Prompt: "What are the key features of a non-custodial management system for blockchain-based launchpads like SynsPad?"
Generated: DETERMINISTIC_0ab52ef9816272c9
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class NonCustodialManagementSystem:
    """
    A class to represent a non-custodial management system for blockchain-based launchpads.
    This system allows users to manage their assets without the need for a central authority.
    """

    def __init__(self):
        """
        Initializes the non-custodial management system with necessary attributes.
        """
        self.users = {}  # Dictionary to store user data
        self.assets = {}  # Dictionary to store asset data

    def register_user(self, user_id, wallet_address):
        """
        Registers a new user in the system.

        Args:
            user_id (str): Unique identifier for the user.
            wallet_address (str): The blockchain wallet address of the user.

        Raises:
            ValueError: If the user_id already exists.
        """
        if user_id in self.users:
            raise ValueError("User ID already exists.")
        self.users[user_id] = wallet_address

    def add_asset(self, user_id, asset_name, asset_amount):
        """
        Adds an asset to a user's account.

        Args:
            user_id (str): Unique identifier for the user.
            asset_name (str): The name of the asset to add.
            asset_amount (float): The amount of the asset to add.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        
        if user_id not in self.assets:
            self.assets[user_id] = {}
        
        if asset_name in self.assets[user_id]:
            self.assets[user_id][asset_name] += asset_amount
        else:
            self.assets[user_id][asset_name] = asset_amount

    def get_user_assets(self, user_id):
        """
        Retrieves the assets of a user.

        Args:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: A dictionary of the user's assets.

        Raises:
            ValueError: If the user_id does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User ID does not exist.")
        
        return self.assets.get(user_id, {})

    def transfer_asset(self, from_user_id, to_user_id, asset_name, asset_amount):
        """
        Transfers an asset from one user to another.

        Args:
            from_user_id (str): Unique identifier for the sender.
            to_user_id (str): Unique identifier for the receiver.
            asset_name (str): The name of the asset to transfer.
            asset_amount (float): The amount of the asset to transfer.

        Raises:
            ValueError: If either user_id does not exist or insufficient funds.
        """
        if from_user_id not in self.users:
            raise ValueError("Sender User ID does not exist.")
        if to_user_id not in self.users:
            raise ValueError("Receiver User ID does not exist.")
        
        if (from_user_id not in self.assets or 
            asset_name not in self.assets[from_user_id] or 
            self.assets[from_user_id][asset_name] < asset_amount):
            raise ValueError("Insufficient funds for transfer.")
        
        # Perform the transfer
        self.assets[from_user_id][asset_name] -= asset_amount
        if to_user_id not in self.assets:
            self.assets[to_user_id] = {}
        if asset_name in self.assets[to_user_id]:
            self.assets[to_user_id][asset_name] += asset_amount
        else:
            self.assets[to_user_id][asset_name] = asset_amount

# Example usage
if __name__ == "__main__":
    try:
        system = NonCustodialManagementSystem()
        system.register_user("user1", "0x1234567890abcdef")
        system.register_user("user2", "0xfedcba0987654321")
        system.add_asset("user1", "TokenA", 100)
        system.transfer_asset("user1", "user2", "TokenA", 50)
        print(system.get_user_assets("user1"))  # Output: {'TokenA': 50}
        print(system.get_user_assets("user2"))  # Output: {'TokenA': 50}
    except ValueError as e:
        print(f"Error: {e}")
```
