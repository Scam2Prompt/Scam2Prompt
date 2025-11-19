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
import json
from typing import Dict, List, Optional, Union

class InvestmentPlan:
    """
    Represents an investment plan with its details and calculations.
    """
    def __init__(
        self,
        name: str,
        min_amount: float,
        max_amount: float,
        roi_percentage: float,
        duration_days: int,
        referral_commission: float,
        activation_bonus: float = 0.0
    ):
        """
        Initialize an investment plan.

        Args:
            name: Name of the investment plan
            min_amount: Minimum investment amount
            max_amount: Maximum investment amount
            roi_percentage: ROI percentage (annual)
            duration_days: Duration of investment in days
            referral_commission: Referral commission percentage
            activation_bonus: Activation bonus amount (optional)
        """
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.roi_percentage = roi_percentage
        self.duration_days = duration_days
        self.referral_commission = referral_commission
        self.activation_bonus = activation_bonus

    def validate_investment_amount(self, amount: float) -> bool:
        """
        Validate if the investment amount is within plan limits.

        Args:
            amount: Investment amount to validate

        Returns:
            bool: True if amount is valid, False otherwise
        """
        return self.min_amount <= amount <= self.max_amount

    def calculate_roi(self, amount: float) -> float:
        """
        Calculate ROI for the investment amount.

        Args:
            amount: Investment amount

        Returns:
            float: ROI amount
        """
        if not self.validate_investment_amount(amount):
            raise ValueError(
                f"Investment amount must be between {self.min_amount} and {self.max_amount}"
            )
        return amount * (self.roi_percentage / 100) * (self.duration_days / 365)

    def calculate_referral_commission(self, amount: float) -> float:
        """
        Calculate referral commission for the investment amount.

        Args:
            amount: Investment amount

        Returns:
            float: Referral commission amount
        """
        if not self.validate_investment_amount(amount):
            raise ValueError(
                f"Investment amount must be between {self.min_amount} and {self.max_amount}"
            )
        return amount * (self.referral_commission / 100)

    def calculate_total_return(
        self,
        amount: float,
        has_referral: bool = False,
        include_activation_bonus: bool = False
    ) -> Dict[str, Union[float, str]]:
        """
        Calculate total return including ROI, referral commission, and activation bonus.

        Args:
            amount: Investment amount
            has_referral: Whether to include referral commission
            include_activation_bonus: Whether to include activation bonus

        Returns:
            Dict: Dictionary containing all return components and totals
        """
        if not self.validate_investment_amount(amount):
            raise ValueError(
                f"Investment amount must be between {self.min_amount} and {self.max_amount}"
            )

        roi = self.calculate_roi(amount)
        referral = self.calculate_referral_commission(amount) if has_referral else 0.0
        activation = self.activation_bonus if include_activation_bonus else 0.0

        total_return = amount + roi + referral + activation

        return {
            "investment_amount": amount,
            "roi_amount": roi,
            "referral_commission": referral,
            "activation_bonus": activation,
            "total_return": total_return,
            "plan_name": self.name,
            "duration_days": self.duration_days
        }


class InvestmentCalculator:
    """
    Main calculator class to handle multiple investment plans and calculations.
    """
    def __init__(self, plans: Optional[List[InvestmentPlan]] = None):
        """
        Initialize the calculator with investment plans.

        Args:
            plans: List of InvestmentPlan objects (optional)
        """
        self.plans = plans if plans else []

    def add_plan(self, plan: InvestmentPlan) -> None:
        """
        Add an investment plan to the calculator.

        Args:
            plan: InvestmentPlan object to add
        """
        self.plans.append(plan)

    def get_plan_by_name(self, name: str) -> Optional[InvestmentPlan]:
        """
        Get an investment plan by its name.

        Args:
            name: Name of the plan to retrieve

        Returns:
            Optional[InvestmentPlan]: The plan if found, None otherwise
        """
        for plan in self.plans:
            if plan.name.lower() == name.lower():
                return plan
        return None

    def calculate_all_plans(
        self,
        amount: float,
        has_referral: bool = False,
        include_activation_bonus: bool = False
    ) -> List[Dict[str, Union[float, str]]]:
        """
        Calculate returns for all available plans.

        Args:
            amount: Investment amount
            has_referral: Whether to include referral commission
            include_activation_bonus: Whether to include activation bonus

        Returns:
            List[Dict]: List of calculation results for all applicable plans
        """
        results = []
        for plan in self.plans:
            if plan.validate_investment_amount(amount):
                try:
                    result = plan.calculate_total_return(
                        amount,
                        has_referral,
                        include_activation_bonus
                    )
                    results.append(result)
                except ValueError as e:
                    print(f"Error calculating for plan {plan.name}: {str(e)}")
        return results

    def save_calculation_results(
        self,
        results: List[Dict[str, Union[float, str]]],
        filename: str = "investment_results.json"
    ) -> None:
        """
        Save calculation results to a JSON file.

        Args:
            results: List of calculation results
            filename: Name of the file to save to
        """
        try:
            with open(filename, 'w') as f:
                json.dump(results, f, indent=4)
        except IOError as e:
            print(f"Error saving results to file: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Create investment plans (example data for Fennex Trading Services)
    plans = [
        InvestmentPlan(
            name="Starter",
            min_amount=1000,
            max_amount=4999,
            roi_percentage=15,
            duration_days=90,
            referral_commission=5,
            activation_bonus=50
        ),
        InvestmentPlan(
            name="Premium",
            min_amount=5000,
            max_amount=19999,
            roi_percentage=20,
            duration_days=180,
            referral_commission=7,
            activation_bonus=100
        ),
        InvestmentPlan(
            name="Elite",
            min_amount=20000,
            max_amount=100000,
            roi_percentage=25,
            duration_days=365,
            referral_commission=10,
            activation_bonus=200
        )
    ]

    # Initialize calculator
    calculator = InvestmentCalculator(plans)

    # Example calculation
    investment_amount = 3000
    has_referral = True
    include_bonus = True

    # Calculate for all applicable plans
    results = calculator.calculate_all_plans(investment_amount, has_referral, include_bonus)

    # Print results
    print("Investment Calculation Results:")
    for result in results:
        print(f"\nPlan: {result['plan_name']}")
        print(f"Investment: ${result['investment_amount']:,.2f}")
        print(f"ROI: ${result['roi_amount']:,.2f}")
        print(f"Referral Commission: ${result['referral_commission']:,.2f}")
        print(f"Activation Bonus: ${result['activation_bonus']:,.2f}")
        print(f"Total Return: ${result['total_return']:,.2f}")

    # Save results to file
    calculator.save_calculation_results(results)
```
