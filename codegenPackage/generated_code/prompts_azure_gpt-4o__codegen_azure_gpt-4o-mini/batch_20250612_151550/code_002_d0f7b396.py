"""
Generated Code Metadata:
========================
Original URL: https://fennextradingservices.com
Prompt: Develop a script to calculate ROI (Return on Investment) for different investment plans, including referral commissions and activation bonuses, based on the investment tiers provided by Fennex Trading Services.
Generated: DETERMINISTIC_d0f7b3960153e790
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """
    A class to represent an investment plan and calculate its Return on Investment (ROI).
    """

    def __init__(self, investment_amount, referral_commission_rate, activation_bonus):
        """
        Initializes the InvestmentPlan with the given parameters.

        :param investment_amount: The amount invested.
        :param referral_commission_rate: The rate of referral commission as a decimal (e.g., 0.1 for 10%).
        :param activation_bonus: The activation bonus amount.
        """
        self.investment_amount = investment_amount
        self.referral_commission_rate = referral_commission_rate
        self.activation_bonus = activation_bonus

    def calculate_roi(self, total_return):
        """
        Calculates the Return on Investment (ROI).

        :param total_return: The total return from the investment.
        :return: The ROI as a percentage.
        """
        if self.investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        roi = ((total_return - self.investment_amount) / self.investment_amount) * 100
        return roi

    def calculate_total_earnings(self, total_return):
        """
        Calculates the total earnings including referral commissions and activation bonuses.

        :param total_return: The total return from the investment.
        :return: The total earnings.
        """
        if total_return < 0:
            raise ValueError("Total return must be non-negative.")
        
        referral_commission = total_return * self.referral_commission_rate
        total_earnings = total_return + referral_commission + self.activation_bonus
        return total_earnings


def main():
    """
    Main function to execute the investment plan calculations.
    """
    try:
        # Example investment plan parameters
        investment_amount = 1000  # Amount invested
        referral_commission_rate = 0.1  # 10% referral commission
        activation_bonus = 50  # Activation bonus

        # Create an instance of InvestmentPlan
        plan = InvestmentPlan(investment_amount, referral_commission_rate, activation_bonus)

        # Example total return from the investment
        total_return = 1500  # Total return from the investment

        # Calculate ROI
        roi = plan.calculate_roi(total_return)
        print(f"Return on Investment (ROI): {roi:.2f}%")

        # Calculate total earnings
        total_earnings = plan.calculate_total_earnings(total_return)
        print(f"Total Earnings: ${total_earnings:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
