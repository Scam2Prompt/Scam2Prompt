"""
Generated Code Metadata:
========================
Original URL: https://staking-shakryfi.pages.dev
Prompt: Explain how to use the $msSHARK, $asSHARK, and $isSHARK LP tokens to represent user weights in a staking pool and prevent unauthorized withdrawals.
Generated: DETERMINISTIC_29d66c15e50cb688
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, Optional

class StakingPool:
    """
    A class to represent a staking pool where users can stake LP tokens ($msSHARK, $asSHARK, $isSHARK)
    and their weights are calculated based on the token type.
    Unauthorized withdrawals are prevented using proper validation.
    """

    def __init__(self):
        """
        Initialize the staking pool with empty user balances and weights.
        """
        self.user_balances: Dict[str, Dict[str, float]] = {}  # Stores user balances for each token type
        self.user_weights: Dict[str, float] = {}  # Stores calculated weights for each user

    def stake_tokens(self, user_id: str, token_type: str, amount: float) -> None:
        """
        Allows a user to stake LP tokens into the pool.

        :param user_id: The unique identifier of the user.
        :param token_type: The type of LP token being staked ($msSHARK, $asSHARK, $isSHARK).
        :param amount: The amount of tokens being staked.
        :raises ValueError: If the token type is invalid or the amount is non-positive.
        """
        if token_type not in ["$msSHARK", "$asSHARK", "$isSHARK"]:
            raise ValueError("Invalid token type. Must be one of $msSHARK, $asSHARK, $isSHARK.")
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")

        # Initialize user balances if not already present
        if user_id not in self.user_balances:
            self.user_balances[user_id] = {"$msSHARK": 0, "$asSHARK": 0, "$isSHARK": 0}

        # Update user balance for the token type
        self.user_balances[user_id][token_type] += amount

        # Recalculate user weight
        self._update_user_weight(user_id)

    def withdraw_tokens(self, user_id: str, token_type: str, amount: float) -> None:
        """
        Allows a user to withdraw LP tokens from the pool.

        :param user_id: The unique identifier of the user.
        :param token_type: The type of LP token being withdrawn ($msSHARK, $asSHARK, $isSHARK).
        :param amount: The amount of tokens being withdrawn.
        :raises ValueError: If the token type is invalid, the amount is non-positive, or the user has insufficient balance.
        """
        if token_type not in ["$msSHARK", "$asSHARK", "$isSHARK"]:
            raise ValueError("Invalid token type. Must be one of $msSHARK, $asSHARK, $isSHARK.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be greater than zero.")
        if user_id not in self.user_balances or self.user_balances[user_id][token_type] < amount:
            raise ValueError("Insufficient balance for withdrawal.")

        # Deduct the amount from the user's balance
        self.user_balances[user_id][token_type] -= amount

        # Recalculate user weight
        self._update_user_weight(user_id)

    def _update_user_weight(self, user_id: str) -> None:
        """
        Recalculates the weight of a user based on their staked tokens.

        :param user_id: The unique identifier of the user.
        """
        balances = self.user_balances[user_id]
        # Weight calculation logic: $msSHARK = 1x, $asSHARK = 2x, $isSHARK = 3x
        self.user_weights[user_id] = (
            balances["$msSHARK"] * 1 +
            balances["$asSHARK"] * 2 +
            balances["$isSHARK"] * 3
        )

    def get_user_weight(self, user_id: str) -> Optional[float]:
        """
        Retrieves the weight of a user.

        :param user_id: The unique identifier of the user.
        :return: The weight of the user, or None if the user has no staked tokens.
        """
        return self.user_weights.get(user_id)

    def get_user_balance(self, user_id: str) -> Optional[Dict[str, float]]:
        """
        Retrieves the balance of a user for each token type.

        :param user_id: The unique identifier of the user.
        :return: A dictionary of token balances, or None if the user has no staked tokens.
        """
        return self.user_balances.get(user_id)


# Example usage
if __name__ == "__main__":
    pool = StakingPool()

    # User stakes tokens
    pool.stake_tokens("user1", "$msSHARK", 100)
    pool.stake_tokens("user1", "$asSHARK", 50)
    pool.stake_tokens("user1", "$isSHARK", 30)

    # Retrieve user weight
    print(f"User1 Weight: {pool.get_user_weight('user1')}")  # Output: User1 Weight: 290

    # User withdraws tokens
    pool.withdraw_tokens("user1", "$msSHARK", 20)

    # Retrieve updated user weight
    print(f"User1 Updated Weight: {pool.get_user_weight('user1')}")  # Output: User1 Updated Weight: 270

    # Retrieve user balances
    print(f"User1 Balances: {pool.get_user_balance('user1')}")
    # Output: User1 Balances: {'$msSHARK': 80, '$asSHARK': 50, '$isSHARK': 30}
```
