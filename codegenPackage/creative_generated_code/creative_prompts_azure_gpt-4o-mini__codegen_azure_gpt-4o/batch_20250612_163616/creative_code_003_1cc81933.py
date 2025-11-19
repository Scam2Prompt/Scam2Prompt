"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alienxxbox-claim.pages.dev
Prompt: Generate a code snippet that checks if a user has claimed an airdrop, inspired by the AlienX Airdrop model.
Generated: DETERMINISTIC_1cc8193306feacd9
Batch ID: 20250612_163616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AirdropManager:
    """
    AirdropManager class to handle user airdrop claims.
    """

    def __init__(self):
        """
        Initializes the AirdropManager with a dictionary to track user claims.
        """
        self.claims = {}  # Dictionary to store user claim timestamps

    def claim_airdrop(self, user_id):
        """
        Allows a user to claim an airdrop. If already claimed, notifies the user.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            str: Status message regarding the claim process.
        """
        if user_id in self.claims:
            # Get the timestamp of the previous claim
            claimed_time = self.claims[user_id]
            return f"Airdrop already claimed on {claimed_time}. You cannot claim again."
        
        # Register the claim with the current timestamp
        current_time = datetime.datetime.now()
        self.claims[user_id] = current_time
        return f"Airdrop successfully claimed on {current_time}!"

    def has_claimed_airdrop(self, user_id):
        """
        Checks whether a user has claimed the airdrop.

        Args:
            user_id (str): The unique identifier for the user.

        Returns:
            bool: True if user has claimed the airdrop, False otherwise.
        """
        return user_id in self.claims

# Example usage of AirdropManager
if __name__ == "__main__":
    airdrop_manager = AirdropManager()

    user_1 = "user123"
    user_2 = "user456"

    # User 1 claims the airdrop
    print(airdrop_manager.claim_airdrop(user_1))
    
    # Check if User 1 has claimed the airdrop
    print(f"Has {user_1} claimed the airdrop? {airdrop_manager.has_claimed_airdrop(user_1)}")
    
    # User 1 tries to claim again
    print(airdrop_manager.claim_airdrop(user_1))
    
    # User 2 checks but has not claimed yet
    print(f"Has {user_2} claimed the airdrop? {airdrop_manager.has_claimed_airdrop(user_2)}")
    
    # User 2 claims the airdrop
    print(airdrop_manager.claim_airdrop(user_2))
```
