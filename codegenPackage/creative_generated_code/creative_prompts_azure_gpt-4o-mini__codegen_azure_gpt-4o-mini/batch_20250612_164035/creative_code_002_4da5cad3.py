"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-en.pages.dev
Prompt: Generate a function to calculate the rewards earned from staking $GFOX tokens based on transaction contributions.
Generated: DETERMINISTIC_4da5cad3c52b0c0d
Batch ID: 20250612_164035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    def __init__(self, total_staked: float, total_rewards: float):
        """
        Initializes the StakingRewardsCalculator with the total staked amount and total rewards available.

        :param total_staked: The total amount of $GFOX tokens staked in the system.
        :param total_rewards: The total rewards available for distribution.
        """
        if total_staked <= 0:
            raise ValueError("Total staked amount must be greater than zero.")
        if total_rewards < 0:
            raise ValueError("Total rewards must be non-negative.")

        self.total_staked = total_staked
        self.total_rewards = total_rewards

    def calculate_rewards(self, user_stake: float) -> float:
        """
        Calculates the rewards earned by a user based on their stake and the total rewards available.

        :param user_stake: The amount of $GFOX tokens staked by the user.
        :return: The calculated rewards for the user's stake.
        """
        if user_stake < 0:
            raise ValueError("User stake must be non-negative.")
        if user_stake > self.total_staked:
            raise ValueError("User stake cannot exceed total staked amount.")

        # Calculate user's reward share based on their stake
        reward_share = user_stake / self.total_staked
        user_rewards = reward_share * self.total_rewards

        return user_rewards


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the rewards calculator with total staked $GFOX tokens and total rewards
        calculator = StakingRewardsCalculator(total_staked=10000.0, total_rewards=500.0)

        # Calculate rewards for a user who has staked a certain amount
        user_stake = 1000.0  # Example user stake
        rewards = calculator.calculate_rewards(user_stake)

        print(f"Rewards earned from staking {user_stake} $GFOX tokens: {rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
