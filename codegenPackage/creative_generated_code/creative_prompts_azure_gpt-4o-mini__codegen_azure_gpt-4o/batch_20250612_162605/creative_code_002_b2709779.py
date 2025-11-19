"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fixnode-engine.vercel.app
Prompt: Generate a function to handle token staking and unstaking issues with the Node Engine's protocol.
Generated: DETERMINISTIC_b2709779cb19e2b7
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class TokenStakingEngine:
    def __init__(self):
        """
        Initializes the staking engine with an empty staking pool.
        """
        self.staking_pool = {}  # Format: {user_id: {"tokens": int, "stake_timestamp": datetime}}

    def stake_tokens(self, user_id, token_amount):
        """
        Handles the staking of tokens by a user.

        Args:
            user_id (str): Unique identifier of the user.
            token_amount (int): The number of tokens the user wants to stake.

        Returns:
            str: Confirmation message upon successful staking.

        Raises:
            ValueError: If token_amount is not a positive integer.
        """
        if token_amount <= 0:
            raise ValueError("Token amount must be a positive value.")

        # Add or update the user's stake in the staking pool
        if user_id in self.staking_pool:
            self.staking_pool[user_id]["tokens"] += token_amount
        else:
            self.staking_pool[user_id] = {
                "tokens": token_amount,
                "stake_timestamp": datetime.datetime.now()
            }

        return f"Successfully staked {token_amount} tokens for user {user_id}."

    def unstake_tokens(self, user_id, token_amount):
        """
        Handles the unstaking of tokens by a user.

        Args:
            user_id (str): Unique identifier of the user.
            token_amount (int): The number of tokens the user wants to unstake.

        Returns:
            str: Confirmation message upon successful unstaking.

        Raises:
            ValueError: If token_amount is not a positive integer or exceeds the staked amount.
            KeyError: If the user has not staked any tokens.
        """
        if token_amount <= 0:
            raise ValueError("Token amount must be a positive value.")

        if user_id not in self.staking_pool:
            raise KeyError(f"User {user_id} has no tokens staked.")

        if self.staking_pool[user_id]["tokens"] < token_amount:
            raise ValueError("Cannot unstake more tokens than currently staked.")

        # Remove the tokens from the user's stake
        self.staking_pool[user_id]["tokens"] -= token_amount

        # If the user has no tokens left, remove them from the staking pool
        if self.staking_pool[user_id]["tokens"] == 0:
            del self.staking_pool[user_id]

        return f"Successfully unstaked {token_amount} tokens for user {user_id}."

    def get_stake_info(self, user_id):
        """
        Retrieves staking information for a specific user.

        Args:
            user_id (str): Unique identifier of the user.

        Returns:
            dict: A dictionary containing the number of staked tokens and the timestamp.

        Raises:
            KeyError: If the user has not staked any tokens.
        """
        if user_id not in self.staking_pool:
            raise KeyError(f"User {user_id} has no tokens staked.")

        return self.staking_pool[user_id]

    def get_total_staked_tokens(self):
        """
        Calculates the total number of tokens staked in the pool.

        Returns:
            int: Total tokens staked.
        """
        return sum(user_info["tokens"] for user_info in self.staking_pool.values())

# Example usage:
# engine = TokenStakingEngine()
# print(engine.stake_tokens("user1", 100))
# print(engine.unstake_tokens("user1", 50))
# print(engine.get_stake_info("user1"))
# print(engine.get_total_staked_tokens())
```
