"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://syrupps.pages.dev
Prompt: Explain the process of staking SYRUP and how it contributes to earning protocol rewards.
Generated: DETERMINISTIC_e2096fc6e517c2d8
Batch ID: 20250612_160044
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Staking SYRUP Token Example

This script demonstrates how to stake SYRUP tokens in a hypothetical staking contract.
It includes error handling, comments explaining each step, and follows best practices.
"""

class StakingContract:
    def __init__(self):
        """Initialize the staking contract with an empty stakers dictionary."""
        self.stakers = {}
        self.total_staked = 0.0
        self.reward_rate = 0.05  # Example reward rate (5%)

    def stake(self, user, amount):
        """
        Allow a user to stake an amount of SYRUP tokens.
        
        Args:
            user (str): The username of the user staking tokens.
            amount (float): The amount of SYRUP tokens to stake.

        Raises:
            ValueError: If the amount is zero or negative.
            KeyError: If the user is already staking.
        """
        if amount <= 0:
            raise ValueError("Amount to stake must be positive")

        if user in self.stakers:
            raise KeyError("User is already staking tokens")

        # Add the user and their staked amount to the stakers dictionary
        self.stakers[user] = amount
        self.total_staked += amount
        print(f"{user} successfully staked {amount} SYRUP.")

    def calculate_rewards(self, user):
        """
        Calculate the rewards for a user based on their staked amount.

        Args:
            user (str): The username of the user for whom to calculate rewards.
        
        Returns:
            float: The total rewards earned by the user.

        Raises:
            KeyError: If the user is not found in the stakers list.
        """
        if user not in self.stakers:
            raise KeyError("User not found in stakers")

        staked_amount = self.stakers[user]
        rewards = staked_amount * self.reward_rate
        return rewards

    def withdraw(self, user):
        """
        Allow a user to withdraw their staked SYRUP tokens along with earned rewards.
        
        Args:
            user (str): The username of the user withdrawing tokens.

        Returns:
            float: The total amount withdrawn (staked amount + rewards).

        Raises:
            KeyError: If the user is not found in the stakers list.
        """
        if user not in self.stakers:
            raise KeyError("User not found in stakers")

        staked_amount = self.stakers.pop(user)  # Remove user from stakers
        rewards = self.calculate_rewards(user)
        total_withdrawal = staked_amount + rewards
        self.total_staked -= staked_amount
        print(f"{user} successfully withdrew {total_withdrawal} SYRUP.")
        return total_withdrawal


# Example usage
if __name__ == "__main__":
    staking_contract = StakingContract()

    # User staking
    try:
        staking_contract.stake("Alice", 100.0)
        staking_contract.stake("Bob", 150.0)
        
        # Calculate rewards for Alice
        alice_rewards = staking_contract.calculate_rewards("Alice")
        print(f"Alice's rewards: {alice_rewards} SYRUP")

        # Withdraw for Alice
        staking_contract.withdraw("Alice")
        
        # Attempt to withdraw again to demonstrate error handling
        staking_contract.withdraw("Alice")
        
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
```
