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
# roi_calculator.py

class InvestmentPlan:
    """Represents an investment plan with its corresponding ROI details."""

    def __init__(self, name, investment_tier, referral_commission, activation_bonus, monthly_roi):
        """
        Initializes an InvestmentPlan instance.

        Args:
            name (str): Name of the investment plan.
            investment_tier (str): Investment tier of the plan.
            referral_commission (float): Referral commission percentage.
            activation_bonus (float): Activation bonus percentage.
            monthly_roi (float): Monthly ROI percentage.
        """
        self.name = name
        self.investment_tier = investment_tier
        self.referral_commission = referral_commission / 100  # Convert to decimal
        self.activation_bonus = activation_bonus / 100  # Convert to decimal
        self.monthly_roi = monthly_roi / 100  # Convert to decimal

    def calculate_roi(self, investment_amount):
        """
        Calculates the ROI for the given investment amount.

        Args:
            investment_amount (float): The amount invested.

        Returns:
            dict: A dictionary containing the calculated ROI details.
        """
        referral_reward = investment_amount * self.referral_commission
        activation_bonus_amount = investment_amount * self.activation_bonus
        monthly_roi_amount = investment_amount * self.monthly_roi
        total_roi = referral_reward + activation_bonus_amount + monthly_roi_amount

        return {
            "referral_reward": referral_reward,
            "activation_bonus": activation_bonus_amount,
            "monthly_roi": monthly_roi_amount,
            "total_roi": total_roi,
        }


class FennexTradingServices:
    """Simulates Fennex Trading Services investment plans."""

    def __init__(self):
        self.investment_plans = {
            "Starter": InvestmentPlan("Starter", "100-500", 5, 10, 10),
            "Premium": InvestmentPlan("Premium", "501-2000", 7, 15, 15),
            "Elite": InvestmentPlan("Elite", "2001-5000", 10, 20, 20),
        }

    def get_investment_plan(self, plan_name):
        """
        Retrieves an investment plan by name.

        Args:
            plan_name (str): Name of the investment plan.

        Returns:
            InvestmentPlan: The investment plan instance if found, None otherwise.
        """
        return self.investment_plans.get(plan_name)

    def calculate_investment_roi(self, plan_name, investment_amount):
        """
        Calculates the ROI for the given investment plan and amount.

        Args:
            plan_name (str): Name of the investment plan.
            investment_amount (float): The amount invested.

        Returns:
            dict: A dictionary containing the calculated ROI details.

        Raises:
            ValueError: If the investment plan is not found.
        """
        plan = self.get_investment_plan(plan_name)
        if plan is None:
            raise ValueError(f"Investment plan '{plan_name}' not found.")

        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")

        # Validate investment tier
        tier_range = plan.investment_tier.split("-")
        if not (float(tier_range[0]) <= investment_amount <= float(tier_range[1])):
            raise ValueError(
                f"Investment amount ${investment_amount:.2f} is out of tier range {plan.investment_tier} for plan {plan_name}."
            )

        return plan.calculate_roi(investment_amount)


def main():
    fennex_services = FennexTradingServices()

    # Example usage
    plan_name = "Premium"
    investment_amount = 1000

    try:
        roi_details = fennex_services.calculate_investment_roi(plan_name, investment_amount)
        print(f"ROI Details for {plan_name} Plan with Investment ${investment_amount:.2f}:")
        for key, value in roi_details.items():
            print(f"{key.capitalize().replace('_', ' ')}: ${value:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
