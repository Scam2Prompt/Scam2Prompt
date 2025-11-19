"""
Generated Code Metadata:
========================
Original URL: https://dymwizard.top
Prompt: Create a simple staking system for Genesis NFTs on the Super Champs HQ platform using a suitable programming language.
Generated: DETERMINISTIC_270105836008b7cd
Batch ID: 20250622_211819
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Simple Staking System for Genesis NFTs on Super Champs HQ

class StakingSystem:
    def __init__(self):
        # Dictionary to hold user stakes
        self.user_stakes = {}
        # Dictionary to hold NFT rewards
        self.nft_rewards = {}
    
    def stake_nft(self, user_id, nft_id):
        """
        Allows a user to stake their NFT.
        
        :param user_id: Unique identifier for the user
        :param nft_id: Unique identifier for the NFT
        :raises ValueError: If the NFT is already staked by the user
        """
        if user_id not in self.user_stakes:
            self.user_stakes[user_id] = []
        
        if nft_id in self.user_stakes[user_id]:
            raise ValueError(f"NFT {nft_id} is already staked by user {user_id}.")
        
        self.user_stakes[user_id].append(nft_id)
        print(f"User {user_id} has staked NFT {nft_id}.")
    
    def unstake_nft(self, user_id, nft_id):
        """
        Allows a user to unstake their NFT.
        
        :param user_id: Unique identifier for the user
        :param nft_id: Unique identifier for the NFT
        :raises ValueError: If the NFT is not staked by the user
        """
        if user_id not in self.user_stakes or nft_id not in self.user_stakes[user_id]:
            raise ValueError(f"NFT {nft_id} is not staked by user {user_id}.")
        
        self.user_stakes[user_id].remove(nft_id)
        print(f"User {user_id} has unstaked NFT {nft_id}.")
    
    def calculate_rewards(self, user_id):
        """
        Calculates rewards for a user based on their staked NFTs.
        
        :param user_id: Unique identifier for the user
        :return: Total rewards for the user
        """
        if user_id not in self.user_stakes:
            return 0
        
        # Example reward calculation: 10 rewards per staked NFT
        rewards = len(self.user_stakes[user_id]) * 10
        self.nft_rewards[user_id] = rewards
        print(f"User {user_id} has earned {rewards} rewards.")
        return rewards
    
    def get_user_stakes(self, user_id):
        """
        Returns the list of NFTs staked by a user.
        
        :param user_id: Unique identifier for the user
        :return: List of staked NFTs
        """
        return self.user_stakes.get(user_id, [])

# Example usage
if __name__ == "__main__":
    staking_system = StakingSystem()
    
    try:
        staking_system.stake_nft("user1", "nft1")
        staking_system.stake_nft("user1", "nft2")
        staking_system.calculate_rewards("user1")
        staking_system.unstake_nft("user1", "nft1")
        staking_system.calculate_rewards("user1")
    except ValueError as e:
        print(f"Error: {e}")
```
