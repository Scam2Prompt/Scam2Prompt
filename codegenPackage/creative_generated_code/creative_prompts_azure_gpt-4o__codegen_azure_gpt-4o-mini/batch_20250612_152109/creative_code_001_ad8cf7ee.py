"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-io.web.app
Prompt: Generate code to calculate staking rewards for $SCOTTY tokens based on the lock period multiplier described in the Scotty AI staking system.
Generated: DETERMINISTIC_ad8cf7eef93f0a40
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ScottyStaking:
    """
    A class to calculate staking rewards for SCOTTY tokens based on the lock period multiplier.
    """

    def __init__(self, base_reward_rate: float):
        """
        Initializes the ScottyStaking class with a base reward rate.

        Args:
            base_reward_rate (float): The base reward rate per token per time period.
        """
        if base_reward_rate <= 0:
            raise ValueError("Base reward rate must be a positive number.")
        self.base_reward_rate = base_reward_rate

    def calculate_rewards(self, amount: float, lock_period: int) -> float:
        """
        Calculates the staking rewards based on the amount of tokens, the lock period, and the corresponding multiplier.

        Args:
            amount (float): The amount of SCOTTY tokens staked.
            lock_period (int): The lock period in days (e.g., 30, 60, 90).
        
        Returns:
            float: The total rewards calculated for the staking period.
        
        Raises:
            ValueError: If the amount is non-positive or the lock period is not valid.
        """
        if amount <= 0:
            raise ValueError("Amount of tokens must be a positive number.")
        if lock_period not in {30, 60, 90}:
            raise ValueError("Lock period must be one of the following values: 30, 60, or 90 days.")

        # Define lock period multipliers
        multipliers = {
            30: 1.1,  # 10% bonus for 30 days
            60: 1.25, # 25% bonus for 60 days
            90: 1.5   # 50% bonus for 90 days
        }

        # Calculate rewards
        multiplier = multipliers[lock_period]
        rewards = amount * self.base_reward_rate * multiplier

        return rewards


def main():
    """
    Main function to demonstrate the staking reward calculation.
    """
    try:
        # Example base reward rate (e.g., tokens earned per token staked per day)
        base_reward_rate = 0.05  # Example: 5% reward rate
        staking = ScottyStaking(base_reward_rate)

        # Example inputs
        amount = 1000  # Amount of SCOTTY tokens
        lock_period = 60  # Lock period in days

        # Calculate and display the rewards
        rewards = staking.calculate_rewards(amount, lock_period)
        print(f"Total rewards for staking {amount} SCOTTY tokens for {lock_period} days: {rewards:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
