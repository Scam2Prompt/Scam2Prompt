"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tgdrop.cc
Prompt: Generate code to simulate a "free spin" feature for a TON-based reward system, including NFT or USDT qualification checks.
Generated: DETERMINISTIC_2edd0c8701d18862
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Union

class FreeSpinFeature:
    def __init__(self):
        # Initialize the qualified users list and rewards pool
        self.qualified_users = set()  # Set of users that qualify for spins
        self.rewards_pool = ['10 USDT', '20 USDT', '1 NFT', '5 USDT', 'Bonus Spin', 'No Reward']
    
    def qualify_user(self, user_id: str, balance: float, has_nft: bool):
        """
        Check if a user qualifies for free spins based on their balance and NFT ownership.
        
        :param user_id: Unique identifier for the user.
        :param balance: User's USDT balance.
        :param has_nft: Boolean indicating if the user owns an NFT.
        """
        if balance >= 10 or has_nft:
            self.qualified_users.add(user_id)
            print(f"User {user_id} qualified for free spins.")
        else:
            print(f"User {user_id} did not qualify for free spins.")
        
    def perform_free_spin(self, user_id: str) -> Union[str, None]:
        """
        Simulate a free spin for a qualified user and return the reward.
        
        :param user_id: Unique identifier for the user.
        :return: The reward for the user or None if the user is not qualified.
        """
        if user_id not in self.qualified_users:
            print(f"User {user_id} is not qualified for free spins.")
            return None
        
        # Randomly select a reward from the rewards pool
        reward = random.choice(self.rewards_pool)
        print(f"User {user_id} spun the wheel and received: {reward}")
        return reward
    
    def reset_qualifications(self):
        """
        Resets the qualifications for all users. Call this function to start fresh.
        """
        self.qualified_users.clear()
        print("All user qualifications have been reset.")

# Example usage
if __name__ == "__main__":
    spin_feature = FreeSpinFeature()
    
    # Qualifying users
    spin_feature.qualify_user("user1", 15.0, False)  # Qualified
    spin_feature.qualify_user("user2", 5.0, False)   # Not qualified
    spin_feature.qualify_user("user3", 0.0, True)    # Qualified
    
    # Performing free spins
    spin_feature.perform_free_spin("user1")
    spin_feature.perform_free_spin("user2")  # Should not qualify
    spin_feature.perform_free_spin("user3")
    
    # Reset qualifications
    spin_feature.reset_qualifications()
```
