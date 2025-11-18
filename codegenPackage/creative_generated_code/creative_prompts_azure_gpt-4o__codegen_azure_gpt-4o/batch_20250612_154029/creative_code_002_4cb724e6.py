"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://validatorrefix.co
Prompt: Provide code for staking and unstaking tokens on a synthetic platform, including options for NFT staking, as outlined on validatorrefix.co.
Generated: DETERMINISTIC_4cb724e6ff430650
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from typing import Dict

class SyntheticStakingPlatform:
    """
    Class to represent a synthetic token staking platform.
    Supports both token staking and NFT staking.
    """

    def __init__(self):
        # Initialize staking pools for tokens and NFTs
        self.token_staking_pool: Dict[str, Dict] = {}  # Maps user ID to staking details
        self.nft_staking_pool: Dict[str, Dict] = {}    # Maps NFT ID to staking details
    
    def stake_tokens(self, user_id: str, amount: float):
        """
        Allows a user to stake a specific amount of tokens.
        
        Parameters:
            user_id (str): Unique identifier for the user staking tokens.
            amount (float): Amount of tokens to stake.

        Raises:
            ValueError: If the amount is invalid or less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        current_time = time.time()
        if user_id not in self.token_staking_pool:
            self.token_staking_pool[user_id] = {
                "amount": amount,
                "start_time": current_time
            }
        else:
            self.token_staking_pool[user_id]["amount"] += amount
            self.token_staking_pool[user_id]["start_time"] = current_time

        print(f"User {user_id} staked {amount} tokens.")

    def unstake_tokens(self, user_id: str):
        """
        Allows a user to unstake all their tokens.
        
        Parameters:
            user_id (str): Unique identifier for the user unstaking tokens.

        Returns:
            float: Amount of tokens unstaked.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.token_staking_pool:
            raise KeyError(f"User {user_id} has no tokens staked.")

        staking_details = self.token_staking_pool.pop(user_id)
        print(f"User {user_id} unstaked {staking_details['amount']} tokens.")
        return staking_details["amount"]

    def stake_nft(self, nft_id: str, user_id: str):
        """
        Allows a user to stake an NFT.

        Parameters:
            nft_id (str): Unique identifier for the NFT being staked.
            user_id (str): Unique identifier for the user staking the NFT.

        Raises:
            ValueError: If the NFT is already staked.
        """
        if nft_id in self.nft_staking_pool:
            raise ValueError(f"NFT {nft_id} is already staked.")

        current_time = time.time()
        self.nft_staking_pool[nft_id] = {
            "user_id": user_id,
            "start_time": current_time
        }

        print(f"User {user_id} staked NFT {nft_id}.")

    def unstake_nft(self, nft_id: str):
        """
        Allows a user to unstake an NFT.

        Parameters:
            nft_id (str): Unique identifier for the NFT being unstaked.

        Returns:
            str: User ID of the owner who unstaked the NFT.

        Raises:
            KeyError: If the NFT is not currently staked.
        """
        if nft_id not in self.nft_staking_pool:
            raise KeyError(f"NFT {nft_id} is not currently staked.")

        staking_details = self.nft_staking_pool.pop(nft_id)
        print(f"NFT {nft_id} unstaked by user {staking_details['user_id']}.")
        return staking_details["user_id"]

    def get_token_staking_info(self, user_id: str):
        """
        Retrieves staking information for a user.

        Parameters:
            user_id (str): Unique identifier for the user.

        Returns:
            dict: Staking details (amount and start time).

        Raises:
            KeyError: If the user has no tokens staked.
        """
        if user_id not in self.token_staking_pool:
            raise KeyError(f"User {user_id} has no tokens staked.")

        return self.token_staking_pool[user_id]

    def get_nft_staking_info(self, nft_id: str):
        """
        Retrieves staking information for an NFT.

        Parameters:
            nft_id (str): Unique identifier for the NFT.

        Returns:
            dict: Staking details (user ID and start time).

        Raises:
            KeyError: If the NFT is not currently staked.
        """
        if nft_id not in self.nft_staking_pool:
            raise KeyError(f"NFT {nft_id} is not currently staked.")

        return self.nft_staking_pool[nft_id]


# Example usage (uncomment for testing):
# platform = SyntheticStakingPlatform()
# platform.stake_tokens("user123", 100)
# platform.unstake_tokens("user123")
# platform.stake_nft("nft456", "user123")
# platform.unstake_nft("nft456")
```
