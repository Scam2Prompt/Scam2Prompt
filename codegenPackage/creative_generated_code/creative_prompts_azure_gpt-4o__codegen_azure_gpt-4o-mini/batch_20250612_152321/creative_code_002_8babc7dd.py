"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaxstartrust.com
Prompt: Generate code to calculate daily returns for Vaxstar Trust's investment plans (e.g., 2% daily for 5 days). Include functionality to handle referral bonuses.
Generated: DETERMINISTIC_8babc7dd792dc85f
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    Class to calculate daily returns for investment plans and handle referral bonuses.
    """

    def __init__(self, daily_rate: float, duration_days: int):
        """
        Initialize the investment plan with daily rate and duration.

        :param daily_rate: Daily return rate (as a percentage).
        :param duration_days: Number of days the investment is held.
        """
        self.daily_rate = daily_rate / 100  # Convert percentage to a decimal
        self.duration_days = duration_days

    def calculate_daily_returns(self, principal: float) -> float:
        """
        Calculate the total returns after a specified duration.

        :param principal: The initial amount invested.
        :return: Total returns after the investment duration.
        :raises ValueError: If principal is non-positive.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")

        total_returns = principal * ((1 + self.daily_rate) ** self.duration_days)
        return total_returns

    def calculate_referral_bonus(self, referral_count: int, bonus_per_referral: float) -> float:
        """
        Calculate total referral bonus based on the number of referrals.

        :param referral_count: Number of successful referrals.
        :param bonus_per_referral: Bonus amount per referral.
        :return: Total referral bonus.
        :raises ValueError: If referral_count or bonus_per_referral is negative.
        """
        if referral_count < 0 or bonus_per_referral < 0:
            raise ValueError("Referral count and bonus per referral must be non-negative.")

        total_bonus = referral_count * bonus_per_referral
        return total_bonus


def main():
    """
    Main function to demonstrate the investment returns and referral bonus calculation.
    """
    try:
        # Set up investment plan parameters
        daily_rate = 2.0  # 2% daily
        duration_days = 5  # for 5 days
        principal_amount = 1000.0  # initial investment amount
        referral_count = 3  # number of successful referrals
        bonus_per_referral = 50.0  # bonus amount for each referral

        # Create an investment plan instance
        investment_plan = InvestmentPlan(daily_rate, duration_days)

        # Calculate daily returns
        total_returns = investment_plan.calculate_daily_returns(principal_amount)
        print(f"Total returns after {duration_days} days: ${total_returns:.2f}")

        # Calculate referral bonus
        total_bonus = investment_plan.calculate_referral_bonus(referral_count, bonus_per_referral)
        print(f"Total referral bonus: ${total_bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
