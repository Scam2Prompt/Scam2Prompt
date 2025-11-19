"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20-claim.pages.dev
Prompt: Explain how to calculate monthly and daily staking rewards for DOGE20 using the provided annual returns percentage.
Generated: DETERMINISTIC_e579b650fd829de0
Batch ID: 20250612_162346
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
    A class to calculate staking rewards for DOGE20 based on annual return percentage.
    """
    
    def __init__(self, annual_return_percentage):
        """
        Initializes the StakingRewardsCalculator with the annual return percentage.

        :param annual_return_percentage: float, expected annual return percentage (e.g., 12 for 12%)
        """
        if not isinstance(annual_return_percentage, (int, float)):
            raise ValueError("Annual return percentage must be an integer or float.")
        if annual_return_percentage < 0:
            raise ValueError("Annual return percentage cannot be negative.")

        self.annual_return_percentage = annual_return_percentage / 100  # Convert to decimal
    
    def calculate_monthly_rewards(self, principal_amount):
        """
        Calculate monthly staking rewards based on the principal amount.

        :param principal_amount: float, the amount staked
        :return: float, the monthly rewards
        """
        if principal_amount < 0:
            raise ValueError("Principal amount cannot be negative.")
        
        # Monthly return rate
        monthly_return_rate = self.annual_return_percentage / 12
        
        # Monthly rewards calculation
        monthly_rewards = principal_amount * monthly_return_rate
        return monthly_rewards
    
    def calculate_daily_rewards(self, principal_amount):
        """
        Calculate daily staking rewards based on the principal amount.

        :param principal_amount: float, the amount staked
        :return: float, the daily rewards
        """
        if principal_amount < 0:
            raise ValueError("Principal amount cannot be negative.")
        
        # Daily return rate (assuming 365 days in a year)
        daily_return_rate = self.annual_return_percentage / 365
        
        # Daily rewards calculation
        daily_rewards = principal_amount * daily_return_rate
        return daily_rewards


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with an annual return percentage of 12%
        calculator = StakingRewardsCalculator(12)

        # Principal amount staked
        principal_amount = 1000  # Example: $1000 DOGE20 staked

        # Calculate monthly and daily rewards
        monthly_rewards = calculator.calculate_monthly_rewards(principal_amount)
        daily_rewards = calculator.calculate_daily_rewards(principal_amount)

        print(f"Monthly Rewards: ${monthly_rewards:.2f}")
        print(f"Daily Rewards: ${daily_rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
