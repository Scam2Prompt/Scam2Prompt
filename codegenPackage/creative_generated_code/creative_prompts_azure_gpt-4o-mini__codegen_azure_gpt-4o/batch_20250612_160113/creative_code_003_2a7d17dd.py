"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtuals-lite.pages.dev
Prompt: Provide an example of how to stake $VIRTUAL tokens to earn rewards within the Virtuals ecosystem.
Generated: DETERMINISTIC_2a7d17dd42ccab6b
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import json

class VirtualTokenStaking:
    """
    A class representing the staking of $VIRTUAL tokens to earn rewards.
    """

    def __init__(self):
        # Initialize staking pool
        self.stakes = {}  # Stores the user stakes, format: {user_id: {"amount": float, "timestamp": int}}
        self.reward_rate = 0.05  # Reward rate per second (5% annualized returns converted to seconds)

    def stake_tokens(self, user_id, amount):
        """
        Allows a user to stake $VIRTUAL tokens.
        :param user_id: Unique identifier for the user (string).
        :param amount: Amount of tokens to stake (float).
        """
        if not isinstance(user_id, str) or not isinstance(amount, (int, float)):
            raise ValueError("Invalid input: 'user_id' must be a string and 'amount' must be a number.")

        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")

        # If user already has a stake, calculate and add existing rewards before staking more
        if user_id in self.stakes:
            self._update_rewards(user_id)

        # Record the stake
        self.stakes[user_id] = {
            "amount": self.stakes.get(user_id, {}).get("amount", 0) + amount,
            "timestamp": int(time.time())
        }

    def _update_rewards(self, user_id):
        """
        Updates the rewards for a user based on their staking duration.
        :param user_id: Unique identifier for the user (string).
        """
        if user_id not in self.stakes:
            raise ValueError(f"User with ID '{user_id}' has no stake.")

        stake = self.stakes[user_id]
        current_time = int(time.time())
        staking_duration = current_time - stake["timestamp"]

        # Calculate rewards based on staking duration
        rewards = stake["amount"] * self.reward_rate * staking_duration
        stake["amount"] += rewards  # Add rewards to the user's stake
        stake["timestamp"] = current_time  # Refresh timestamp

    def withdraw_stake(self, user_id):
        """
        Allows a user to withdraw their stake along with earned rewards.
        :param user_id: Unique identifier for the user (string).
        :return: Withdrawn amount (float).
        """
        if user_id not in self.stakes:
            raise ValueError(f"User with ID '{user_id}' has no stake.")

        # Update rewards before withdrawal
        self._update_rewards(user_id)

        # Withdraw the stake
        withdrawable_amount = self.stakes[user_id]["amount"]
        del self.stakes[user_id]  # Remove user from the staking pool
        return withdrawable_amount

    def get_user_stake(self, user_id):
        """
        Retrieves the current stake amount and earned rewards for a user.
        :param user_id: Unique identifier for the user (string).
        :return: Dictionary with stake amount and timestamp.
        """
        if user_id not in self.stakes:
            raise ValueError(f"User with ID '{user_id}' has no stake.")

        # Update rewards before reporting the stake
        self._update_rewards(user_id)

        return self.stakes[user_id]

# Example Usage
if __name__ == "__main__":
    staking = VirtualTokenStaking()

    try:
        # User stakes tokens
        staking.stake_tokens("user123", 100)
        print("User stake after staking 100 tokens:", staking.get_user_stake("user123"))

        # Simulate staking duration
        time.sleep(2)  # Wait for 2 seconds to earn rewards

        # User checks stake and rewards
        print("User stake after 2 seconds:", staking.get_user_stake("user123"))

        # User withdraws their stake
        withdrawn_amount = staking.withdraw_stake("user123")
        print("User has withdrawn:", withdrawn_amount)

    except ValueError as e:
        print("Error:", e)

    # Save stakes for debugging or persistence
    print("All stakes data:", json.dumps(staking.stakes, indent=4))
```
