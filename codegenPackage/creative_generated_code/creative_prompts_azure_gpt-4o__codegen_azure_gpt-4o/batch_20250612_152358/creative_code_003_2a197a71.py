"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://largeoptions.org
Prompt: Write a program to calculate the total earnings for an investor on largeoptions.org, factoring in daily profits, referral commissions, and investment durations.
Generated: DETERMINISTIC_2a197a71b1272af9
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class InvestorEarningsCalculator:
    """
    A class to calculate the total earnings for an investor on largeoptions.org.
    This includes daily profits, referral commissions, and investment durations.
    """

    def __init__(self, daily_profit_rate, referral_commission_rate):
        """
        Initialize the calculator with profit rates.

        :param daily_profit_rate: Daily profit percentage (e.g., 0.05 for 5%)
        :param referral_commission_rate: Referral commission percentage (e.g., 0.10 for 10%)
        """
        self.daily_profit_rate = daily_profit_rate
        self.referral_commission_rate = referral_commission_rate

    def calculate_daily_profit(self, principal_amount, days):
        """
        Calculate the daily profit based on investment duration.

        :param principal_amount: The amount of money invested.
        :param days: Number of days the investment has been active.
        :return: Total earnings from daily profits.
        """
        try:
            return principal_amount * self.daily_profit_rate * days
        except Exception as e:
            print(f"Error calculating daily profit: {e}")
            return 0

    def calculate_referral_commission(self, referral_earnings):
        """
        Calculate the referral commissions earned.

        :param referral_earnings: Total earnings through referrals.
        :return: Total referral commission.
        """
        try:
            return referral_earnings * self.referral_commission_rate
        except Exception as e:
            print(f"Error calculating referral commission: {e}")
            return 0

    def calculate_total_earnings(self, principal_amount, investment_start_date, referral_earnings):
        """
        Calculate the total earnings for the investor.

        :param principal_amount: The amount of money invested.
        :param investment_start_date: The start date of the investment (datetime object).
        :param referral_earnings: Total earnings through referrals.
        :return: Total earnings combining daily profits and referral commissions.
        """
        try:
            # Calculate the number of days the investment has been active
            current_date = datetime.datetime.now()
            days_active = (current_date - investment_start_date).days

            # Ensure days_active is non-negative
            if days_active < 0:
                raise ValueError("Investment start date cannot be in the future.")

            # Calculate earnings components
            daily_profit = self.calculate_daily_profit(principal_amount, days_active)
            referral_commission = self.calculate_referral_commission(referral_earnings)

            # Total earnings
            return daily_profit + referral_commission
        except Exception as e:
            print(f"Error calculating total earnings: {e}")
            return 0


# Example usage:
if __name__ == "__main__":
    # Investment details
    principal = 2000  # $2000 invested
    start_date = datetime.datetime(2023, 1, 1)  # Investment started on January 1, 2023
    referral_earnings = 300  # $300 earned through referrals

    # Define profit rates
    daily_profit_rate = 0.05  # 5% daily profit rate
    referral_commission_rate = 0.10  # 10% referral commission rate

    # Create calculator instance
    calculator = InvestorEarningsCalculator(daily_profit_rate, referral_commission_rate)

    # Calculate total earnings
    total_earnings = calculator.calculate_total_earnings(principal, start_date, referral_earnings)
    print(f"Total Earnings: ${total_earnings:.2f}")
```
