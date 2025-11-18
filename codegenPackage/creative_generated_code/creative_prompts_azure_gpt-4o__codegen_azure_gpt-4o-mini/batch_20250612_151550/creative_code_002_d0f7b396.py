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
class InvestmentPlan:
    """
    A class to represent an investment plan.

    Attributes:
    -----------
    tier: str
        The tier of the investment plan (e.g., 'Basic', 'Premium', 'VIP').
    investment_amount: float
        The amount invested in the plan.
    referral_commission: float
        The commission earned from referrals.
    activation_bonus: float
        The bonus received upon activation.
    """

    def __init__(self, tier: str, investment_amount: float, referral_commission: float = 0.0, activation_bonus: float = 0.0):
        """
        Initializes the InvestmentPlan with the specified tier, investment amount,
        referral commission, and activation bonus.

        Parameters:
        -----------
        tier : str
            The investment tier.
        investment_amount : float
            The amount invested.
        referral_commission : float
            The commission from referrals.
        activation_bonus : float
            The bonus from activation.
        """
        self.tier = tier
        self.investment_amount = investment_amount
        self.referral_commission = referral_commission
        self.activation_bonus = activation_bonus

    def calculate_roi(self) -> float:
        """
        Calculates the Return on Investment (ROI) for the investment plan.

        Returns:
        --------
        float
            The calculated ROI as a percentage.
        """
        try:
            # Ensure investment amount is not zero to avoid division by zero
            if self.investment_amount <= 0:
                raise ValueError("Investment amount must be greater than zero.")

            total_earnings = self.referral_commission + self.activation_bonus
            roi = (total_earnings / self.investment_amount) * 100
            return roi
        except Exception as e:
            print(f"Error calculating ROI: {e}")
            return None


def main():
    """
    Main function to create investment plans and calculate their ROIs.
    """
    # Example investment plans
    plans = [
        InvestmentPlan(tier='Basic', investment_amount=1000, referral_commission=100, activation_bonus=50),
        InvestmentPlan(tier='Premium', investment_amount=5000, referral_commission=300, activation_bonus=200),
        InvestmentPlan(tier='VIP', investment_amount=10000, referral_commission=700, activation_bonus=500)
    ]

    # Calculate and print ROI for each investment plan
    for plan in plans:
        roi = plan.calculate_roi()
        if roi is not None:
            print(f"ROI for {plan.tier} tier: {roi:.2f}%")

if __name__ == "__main__":
    main()
```
