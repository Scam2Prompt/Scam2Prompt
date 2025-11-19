"""
Generated Code Metadata:
========================
Original URL: https://pepe-unchaineds.pages.dev
Prompt: Generate code to calculate double staking rewards for $PEPU tokens based on the tokenomics described on Pepe Unchained's Layer 2 blockchain.
Generated: DETERMINISTIC_3e682ec86947e601
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PepuStaking:
    """
    A class to calculate double staking rewards for $PEPU tokens based on the tokenomics of Pepe Unchained's Layer 2 blockchain.
    """

    def __init__(self, base_reward_rate: float, bonus_multiplier: float):
        """
        Initializes the PepuStaking class with the base reward rate and bonus multiplier.

        :param base_reward_rate: The base reward rate for staking in percentage (e.g., 0.05 for 5%).
        :param bonus_multiplier: The multiplier for double staking rewards (e.g., 2.0 for double rewards).
        """
        if base_reward_rate < 0 or bonus_multiplier < 1:
            raise ValueError("Base reward rate must be non-negative and bonus multiplier must be at least 1.")
        
        self.base_reward_rate = base_reward_rate
        self.bonus_multiplier = bonus_multiplier

    def calculate_rewards(self, staked_amount: float, staking_duration: int) -> float:
        """
        Calculates the total staking rewards based on the staked amount and duration.

        :param staked_amount: The amount of $PEPU tokens staked.
        :param staking_duration: The duration of staking in days.
        :return: The total rewards earned.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if staking_duration < 0:
            raise ValueError("Staking duration must be non-negative.")

        # Calculate base rewards
        base_rewards = staked_amount * (self.base_reward_rate / 100) * staking_duration

        # Calculate double rewards
        total_rewards = base_rewards * self.bonus_multiplier

        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the staking calculator with a base reward rate of 5% and a double rewards multiplier
        staking_calculator = PepuStaking(base_reward_rate=5.0, bonus_multiplier=2.0)

        # Define the amount staked and the duration of staking
        staked_amount = 1000.0  # Amount of $PEPU tokens
        staking_duration = 30    # Duration in days

        # Calculate the rewards
        rewards = staking_calculator.calculate_rewards(staked_amount, staking_duration)

        # Output the results
        print(f"Total rewards for staking {staked_amount} $PEPU for {staking_duration} days: {rewards:.2f} $PEPU")
    
    except ValueError as e:
        print(f"Error: {e}")
```
