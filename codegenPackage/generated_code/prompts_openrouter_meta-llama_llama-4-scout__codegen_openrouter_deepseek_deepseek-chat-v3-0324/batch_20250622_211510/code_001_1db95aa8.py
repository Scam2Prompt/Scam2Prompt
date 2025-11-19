"""
Generated Code Metadata:
========================
Original URL: https://australiawidewealth.com
Prompt: Create a financial plan for a young couple in their 30s with a combined income of $100,000, considering their goals of buying a home and starting a family.
Generated: DETERMINISTIC_1db95aa8aad59f1a
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, List, Tuple

class FinancialPlan:
    """
    A financial planning tool for a young couple to achieve their goals of buying a home and starting a family.
    """

    def __init__(self, annual_income: float, current_savings: float = 0.0, monthly_expenses: float = 0.0):
        """
        Initialize the financial plan with the couple's financial details.

        Args:
            annual_income (float): Combined annual income of the couple.
            current_savings (float, optional): Current savings amount. Defaults to 0.0.
            monthly_expenses (float, optional): Total monthly expenses. Defaults to 0.0.
        """
        self.annual_income = annual_income
        self.current_savings = current_savings
        self.monthly_expenses = monthly_expenses
        self.monthly_income = annual_income / 12
        self.monthly_savings = self.monthly_income - monthly_expenses

    def calculate_home_affordability(self, down_payment_percent: float = 0.2, mortgage_rate: float = 0.04, loan_term_years: int = 30) -> Dict:
        """
        Calculate the affordable home price based on income, savings, and mortgage terms.

        Args:
            down_payment_percent (float, optional): Down payment percentage. Defaults to 0.2 (20%).
            mortgage_rate (float, optional): Annual mortgage interest rate. Defaults to 0.04 (4%).
            loan_term_years (int, optional): Loan term in years. Defaults to 30.

        Returns:
            Dict: A dictionary containing home affordability details.
        """
        try:
            # Calculate maximum monthly mortgage payment (28% of gross monthly income)
            max_monthly_payment = self.monthly_income * 0.28

            # Calculate loan amount based on mortgage terms
            monthly_rate = mortgage_rate / 12
            num_payments = loan_term_years * 12

            loan_amount = max_monthly_payment * ((1 - (1 + monthly_rate) ** -num_payments) / monthly_rate)

            # Calculate affordable home price based on down payment
            affordable_home_price = loan_amount / (1 - down_payment_percent)

            # Check if current savings can cover down payment
            required_down_payment = affordable_home_price * down_payment_percent
            can_afford_down_payment = self.current_savings >= required_down_payment

            return {
                "affordable_home_price": round(affordable_home_price, 2),
                "required_down_payment": round(required_down_payment, 2),
                "max_monthly_payment": round(max_monthly_payment, 2),
                "can_afford_down_payment": can_afford_down_payment,
                "months_to_save_down_payment": self._calculate_months_to_save(required_down_payment) if not can_afford_down_payment else 0
            }
        except Exception as e:
            raise ValueError(f"Error calculating home affordability: {str(e)}")

    def calculate_child_costs(self, annual_child_cost: float = 12000) -> Dict:
        """
        Calculate the financial impact of having children.

        Args:
            annual_child_cost (float, optional): Estimated annual cost per child. Defaults to $12,000.

        Returns:
            Dict: A dictionary containing child cost details.
        """
        try:
            monthly_child_cost = annual_child_cost / 12
            new_monthly_savings = self.monthly_savings - monthly_child_cost

            return {
                "monthly_child_cost": round(monthly_child_cost, 2),
                "new_monthly_savings": round(new_monthly_savings, 2),
                "can_afford_child": new_monthly_savings >= 0
            }
        except Exception as e:
            raise ValueError(f"Error calculating child costs: {str(e)}")

    def _calculate_months_to_save(self, target_amount: float) -> int:
        """
        Calculate how many months it will take to save a target amount.

        Args:
            target_amount (float): The amount needed to save.

        Returns:
            int: Number of months required to save the target amount.
        """
        if self.monthly_savings <= 0:
            raise ValueError("Monthly savings must be positive to calculate savings timeline")
        return math.ceil((target_amount - self.current_savings) / self.monthly_savings)

    def create_financial_plan(self, home_goal: Dict = None, child_goal: Dict = None) -> Dict:
        """
        Create a comprehensive financial plan for the couple.

        Args:
            home_goal (Dict, optional): Home buying goals with keys 'down_payment_percent', 
                                      'mortgage_rate', 'loan_term_years'. Defaults to None.
            child_goal (Dict, optional): Child planning goals with key 'annual_child_cost'. 
                                       Defaults to None.

        Returns:
            Dict: A comprehensive financial plan with home and child details.
        """
        try:
            home_goal = home_goal or {
                "down_payment_percent": 0.2,
                "mortgage_rate": 0.04,
                "loan_term_years": 30
            }
            child_goal = child_goal or {
                "annual_child_cost": 12000
            }

            home_details = self.calculate_home_affordability(**home_goal)
            child_details = self.calculate_child_costs(**child_goal)

            return {
                "monthly_income": round(self.monthly_income, 2),
                "monthly_expenses": round(self.monthly_expenses, 2),
                "monthly_savings": round(self.monthly_savings, 2),
                "current_savings": round(self.current_savings, 2),
                "home_plan": home_details,
                "child_plan": child_details,
                "recommendations": self._generate_recommendations(home_details, child_details)
            }
        except Exception as e:
            raise ValueError(f"Error creating financial plan: {str(e)}")

    def _generate_recommendations(self, home_details: Dict, child_details: Dict) -> List[str]:
        """
        Generate personalized recommendations based on the financial analysis.

        Args:
            home_details (Dict): Home affordability details.
            child_details (Dict): Child cost details.

        Returns:
            List[str]: List of recommendations.
        """
        recommendations = []

        # Home buying recommendations
        if not home_details["can_afford_down_payment"]:
            months = home_details["months_to_save_down_payment"]
            recommendations.append(
                f"Save ${round(self.monthly_savings, 2)} monthly to afford down payment in {months} months."
            )
        else:
            recommendations.append(
                "You have enough savings for a down payment. Consider speaking with a mortgage broker."
            )

        # Child planning recommendations
        if not child_details["can_afford_child"]:
            recommendations.append(
                "Consider reducing expenses or increasing income before having a child."
            )
        else:
            recommendations.append(
                "Your budget can accommodate child expenses while maintaining savings."
            )

        # General savings recommendation
        if self.monthly_savings < self.monthly_income * 0.15:
            recommendations.append(
                "Try to increase your monthly savings to at least 15% of your income."
            )

        return recommendations


# Example usage
if __name__ == "__main__":
    try:
        # Initialize with couple's financial details
        couple = FinancialPlan(
            annual_income=100000,
            current_savings=30000,
            monthly_expenses=4500
        )

        # Generate financial plan
        plan = couple.create_financial_plan()

        # Print results
        print("Financial Plan Summary:")
        print(f"Monthly Income: ${plan['monthly_income']}")
        print(f"Monthly Expenses: ${plan['monthly_expenses']}")
        print(f"Monthly Savings: ${plan['monthly_savings']}")
        print(f"Current Savings: ${plan['current_savings']}")

        print("\nHome Buying Plan:")
        print(f"Affordable Home Price: ${plan['home_plan']['affordable_home_price']}")
        print(f"Required Down Payment: ${plan['home_plan']['required_down_payment']}")
        print(f"Can Afford Down Payment: {'Yes' if plan['home_plan']['can_afford_down_payment'] else 'No'}")
        if not plan['home_plan']['can_afford_down_payment']:
            print(f"Months to Save for Down Payment: {plan['home_plan']['months_to_save_down_payment']}")

        print("\nChild Planning:")
        print(f"Estimated Monthly Child Cost: ${plan['child_plan']['monthly_child_cost']}")
        print(f"Can Afford Child: {'Yes' if plan['child_plan']['can_afford_child'] else 'No'}")
