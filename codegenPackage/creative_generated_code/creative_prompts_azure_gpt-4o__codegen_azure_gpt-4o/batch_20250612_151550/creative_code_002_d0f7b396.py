"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fennextradingservices.com
Prompt: Develop a script to calculate ROI (Return on Investment) for different investment plans, including referral commissions and activation bonuses, based on the investment tiers provided by Fennex Trading Services.
Generated: DETERMINISTIC_d0f7b3960153e790
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
    -----------
    tier_name : str
        Name of the investment tier (e.g., "Basic", "Premium", etc.).
    investment_amount : float
        The initial amount invested.
    roi_percentage : float
        ROI percentage for the tier (e.g., 10% as 10.0).
    referral_commission_percentage : float
        Referral commission percentage for the tier (e.g., 5% as 5.0).
    activation_bonus : float
        Fixed activation bonus for the tier.
    """

    def __init__(self, tier_name, investment_amount, roi_percentage, referral_commission_percentage, activation_bonus):
        self.tier_name = tier_name
        self.investment_amount = investment_amount
        self.roi_percentage = roi_percentage
        self.referral_commission_percentage = referral_commission_percentage
        self.activation_bonus = activation_bonus

    def calculate_roi(self):
        """
        Calculate the ROI (Return on Investment) based on the tier's percentage.

        Returns:
        --------
        float : ROI value
        """
        return (self.investment_amount * self.roi_percentage) / 100

    def calculate_referral_commission(self):
        """
        Calculate the referral commission based on the tier's percentage.

        Returns:
        --------
        float : Referral commission amount
        """
        return (self.investment_amount * self.referral_commission_percentage) / 100

    def calculate_total_earnings(self):
        """
        Calculate the total earnings including ROI, referral commission, and activation bonus.

        Returns:
        --------
        float : Total earnings
        """
        roi = self.calculate_roi()
        referral_commission = self.calculate_referral_commission()
        return roi + referral_commission + self.activation_bonus


def main():
    """
    Main function to accept user input and calculate ROI for different investment plans.
    """
    try:
        # Define example investment tiers
        investment_plans = [
            InvestmentPlan("Basic", 1000, 10.0, 5.0, 50),
            InvestmentPlan("Premium", 5000, 15.0, 7.0, 100),
            InvestmentPlan("Elite", 10000, 20.0, 10.0, 200)
        ]

        print("Fennex Trading Services - Investment Plans ROI Calculator")
        print("----------------------------------------------------------")

        for plan in investment_plans:
            print(f"Tier: {plan.tier_name}")
            print(f"Investment Amount: ${plan.investment_amount}")
            print(f"ROI Percentage: {plan.roi_percentage}%")
            print(f"Referral Commission Percentage: {plan.referral_commission_percentage}%")
            print(f"Activation Bonus: ${plan.activation_bonus}")
            print(f"Calculated ROI: ${plan.calculate_roi():.2f}")
            print(f"Referral Commission: ${plan.calculate_referral_commission():.2f}")
            print(f"Total Earnings: ${plan.calculate_total_earnings():.2f}")
            print("----------------------------------------------------------")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
