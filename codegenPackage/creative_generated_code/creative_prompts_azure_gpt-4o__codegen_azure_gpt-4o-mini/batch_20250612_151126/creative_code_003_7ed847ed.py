"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint-usdc.web.app
Prompt: Generate code to verify if a user is eligible for free minting rights based on their token holder status, using a whitelist system similar to the one described on the USDC Whitelist Mint page.
Generated: DETERMINISTIC_7ed847ed2ecdfb6d
Batch ID: 20250612_151126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WhitelistMinting:
    def __init__(self):
        # Initialize an empty set to store eligible token holders
        self.whitelist = set()

    def add_to_whitelist(self, user_id):
        """
        Adds a user to the whitelist.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If user_id is not provided or is already in the whitelist
        """
        if not user_id:
            raise ValueError("User ID must be provided.")
        if user_id in self.whitelist:
            raise ValueError("User is already in the whitelist.")
        
        self.whitelist.add(user_id)
        print(f"User {user_id} has been added to the whitelist.")

    def remove_from_whitelist(self, user_id):
        """
        Removes a user from the whitelist.
        
        :param user_id: Unique identifier for the user
        :raises ValueError: If user_id is not provided or is not in the whitelist
        """
        if not user_id:
            raise ValueError("User ID must be provided.")
        if user_id not in self.whitelist:
            raise ValueError("User is not in the whitelist.")
        
        self.whitelist.remove(user_id)
        print(f"User {user_id} has been removed from the whitelist.")

    def is_eligible_for_minting(self, user_id):
        """
        Checks if a user is eligible for free minting rights based on their token holder status.
        
        :param user_id: Unique identifier for the user
        :return: True if the user is eligible, False otherwise
        :raises ValueError: If user_id is not provided
        """
        if not user_id:
            raise ValueError("User ID must be provided.")
        
        eligible = user_id in self.whitelist
        if eligible:
            print(f"User {user_id} is eligible for free minting rights.")
        else:
            print(f"User {user_id} is NOT eligible for free minting rights.")
        
        return eligible
```

This code defines a `WhitelistMinting` class that manages a whitelist of users eligible for free minting rights. The class includes methods to add and remove users from the whitelist, as well as a method to check if a user is eligible for minting. Each method has appropriate error handling to ensure robustness.
