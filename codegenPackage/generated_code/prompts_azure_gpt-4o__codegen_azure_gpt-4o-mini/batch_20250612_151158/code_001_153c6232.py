"""
Generated Code Metadata:
========================
Original URL: https://appwienerclaim.pages.dev
Prompt: Generate code to implement a staking mechanism for $WAI tokens, ensuring rewards calculation based on the provided APY of 177%.
Generated: DETERMINISTIC_153c6232f3812370
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingContract:
    """
    A simple staking contract for $WAI tokens that calculates rewards based on an Annual Percentage Yield (APY).
    """

    def __init__(self, apy: float):
        """
        Initializes the staking contract with the given APY.

        :param apy: Annual Percentage Yield (APY) as a percentage (e.g., 177 for 177%)
        """
        if apy < 0:
            raise ValueError("APY must be a non-negative value.")
        self.apy = apy / 100  # Convert APY to a decimal
        self.stakers = {}  # Dictionary to hold staker balances and timestamps

    def stake(self, user: str, amount: float):
        """
        Allows a user to stake a certain amount of $WAI tokens.

        :param user: The address of the user staking tokens.
        :param amount: The amount of $WAI tokens to stake.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        
        if user in self.stakers:
            self.stakers[user]['balance'] += amount
        else:
            self.stakers[user] = {'balance': amount, 'timestamp': self.current_time()}

    def unstake(self, user: str):
        """
        Allows a user to unstake their tokens and receive rewards.

        :param user: The address of the user unstaking tokens.
        :return: The total amount of $WAI tokens including rewards.
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")
        
        staked_amount = self.stakers[user]['balance']
        rewards = self.calculate_rewards(user)
        total_amount = staked_amount + rewards
        
        # Remove user from stakers after unstaking
        del self.stakers[user]
        return total_amount

    def calculate_rewards(self, user: str) -> float:
        """
        Calculates the rewards for a user based on the time staked and the APY.

        :param user: The address of the user for whom to calculate rewards.
        :return: The calculated rewards.
        """
        if user not in self.stakers:
            raise ValueError("User has no staked tokens.")
        
        staked_info = self.stakers[user]
        staked_amount = staked_info['balance']
        staking_duration = self.current_time() - staked_info['timestamp']
        
        # Calculate rewards based on APY and duration in years
        rewards = staked_amount * self.apy * (staking_duration / (365 * 24 * 60 * 60))
        return rewards

    @staticmethod
    def current_time() -> float:
        """
        Returns the current time in seconds since the epoch.

        :return: Current time in seconds.
        """
        import time
        return time.time()


# Example usage
if __name__ == "__main__":
    try:
        staking_contract = StakingContract(apy=177)
        staking_contract.stake(user="user1", amount=1000)
        print("Rewards for user1:", staking_contract.calculate_rewards("user1"))
        total_amount = staking_contract.unstake("user1")
        print("Total amount returned to user1:", total_amount)
    except ValueError as e:
        print(f"Error: {e}")
```
