"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staking-wisdomise.pages.dev
Prompt: Write a code snippet to calculate the rewards for staking WSDM based on a 365-day lock term with a 28.39% reward rate.
Generated: DETERMINISTIC_749768f0e527d160
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    """
    A class to calculate the rewards for staking WSDM based on a specified lock term
    and reward rate.
    """

    def __init__(self, principal: float, reward_rate: float = 0.2839, lock_days: int = 365):
        """
        Initializes the staking rewards calculator.

        :param principal: The amount staked (in WSDM).
        :param reward_rate: The annual reward rate (default is 28.39%).
        :param lock_days: The duration of the lock term in days (default is 365).
        """
        self.principal = principal
        self.reward_rate = reward_rate
        self.lock_days = lock_days

    def calculate_rewards(self) -> float:
        """
        Calculates the rewards for staking WSDM.

        :return: The total rewards earned after the lock term.
        """
        # Validate input parameters
        if self.principal < 0:
            raise ValueError("Principal amount must be a non-negative value.")
        if self.lock_days <= 0:
            raise ValueError("Lock term must be a positive integer.")
        
        # Calculate the rewards
        # Annual rewards calculation based on the lock term
        annual_rewards = self.principal * self.reward_rate
        daily_rewards = annual_rewards / 365
        total_rewards = daily_rewards * self.lock_days

        return total_rewards

def main():
    """
    Main function to execute the staking rewards calculation.
    """
    # Set initial parameters
    principal_amount = 1000.0  # Example: 1000 WSDM staked
    lock_term_days = 365       # 365-day lock term

    # Create the rewards calculator instance
    rewards_calculator = StakingRewardsCalculator(principal=principal_amount)

    try:
        # Calculate and display the rewards
        rewards = rewards_calculator.calculate_rewards()
        print(f"Total rewards for staking {principal_amount} WSDM over {lock_term_days} days: {rewards:.2f} WSDM")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
