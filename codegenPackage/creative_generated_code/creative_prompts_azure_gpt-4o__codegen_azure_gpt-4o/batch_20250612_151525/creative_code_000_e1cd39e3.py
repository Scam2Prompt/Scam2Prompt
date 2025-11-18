"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Write Python code to calculate a personalized asset allocation strategy based on a user's financial goals, as described in the Ahmeti Wealth Management process. Include risk-reward balancing in the calculation.
Generated: DETERMINISTIC_e1cd39e3d9d001c8
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to track errors and information
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class AssetAllocation:
    """
    A class to calculate personalized asset allocation based on financial goals
    and risk-reward preferences (Ahmeti Wealth Management process).
    """

    def __init__(self, age, income, savings, risk_tolerance, financial_goal_years):
        """
        Initializes the AssetAllocation object with user-specific parameters.

        Args:
            age (int): Age of the user.
            income (float): Annual income of the user.
            savings (float): Total savings of the user.
            risk_tolerance (str): User's risk tolerance ("low", "medium", "high").
            financial_goal_years (int): Years to achieve the financial goal.
        """
        self.age = age
        self.income = income
        self.savings = savings
        self.risk_tolerance = risk_tolerance.lower()
        self.financial_goal_years = financial_goal_years

    def calculate_allocation(self):
        """
        Calculate asset allocation strategy based on inputs.

        Returns:
            dict: A dictionary with allocation percentages for stocks, bonds, and cash.
        """
        try:
            # Base allocation percentages
            base_stock_allocation = max(0, 100 - self.age) / 1.5
            base_bond_allocation = min(100, self.age) / 2.0
            base_cash_allocation = 10

            # Adjustments based on risk tolerance
            if self.risk_tolerance == "low":
                stock_allocation = base_stock_allocation * 0.7
                bond_allocation = base_bond_allocation * 1.3
                cash_allocation = base_cash_allocation * 1.5
            elif self.risk_tolerance == "medium":
                stock_allocation = base_stock_allocation * 1.0
                bond_allocation = base_bond_allocation * 1.0
                cash_allocation = base_cash_allocation * 1.0
            elif self.risk_tolerance == "high":
                stock_allocation = base_stock_allocation * 1.3
                bond_allocation = base_bond_allocation * 0.7
                cash_allocation = base_cash_allocation * 0.5
            else:
                raise ValueError(f"Invalid risk tolerance: {self.risk_tolerance}")

            # Adjustments based on financial goal timeline
            if self.financial_goal_years < 5:
                # Shift focus to safer investments for short-term goals
                stock_allocation *= 0.8
                bond_allocation *= 1.2
                cash_allocation *= 1.5
            elif self.financial_goal_years > 20:
                # Higher risk-reward strategy for long-term goals
                stock_allocation *= 1.2
                bond_allocation *= 0.8

            # Normalize allocations to ensure total is 100%
            total_allocation = stock_allocation + bond_allocation + cash_allocation
            stock_allocation = (stock_allocation / total_allocation) * 100
            bond_allocation = (bond_allocation / total_allocation) * 100
            cash_allocation = (cash_allocation / total_allocation) * 100

            return {
                "Stocks (%)": round(stock_allocation, 2),
                "Bonds (%)": round(bond_allocation, 2),
                "Cash (%)": round(cash_allocation, 2),
            }

        except Exception as e:
            logging.error(f"Error during allocation calculation: {e}")
            return {
                "Stocks (%)": 0,
                "Bonds (%)": 0,
                "Cash (%)": 0,
            }


if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        user_age = int(input("Enter your age: "))
        user_income = float(input("Enter your annual income: "))
        user_savings = float(input("Enter your total savings: "))
        user_risk_tolerance = input("Enter your risk tolerance (low/medium/high): ")
        user_financial_goal_years = int(input("Enter the number of years to achieve your financial goal: "))

        # Create AssetAllocation instance
        asset_allocation = AssetAllocation(
            age=user_age,
            income=user_income,
            savings=user_savings,
            risk_tolerance=user_risk_tolerance,
            financial_goal_years=user_financial_goal_years,
        )

        # Calculate and display allocation
        allocation = asset_allocation.calculate_allocation()
        logging.info("Personalized Asset Allocation Strategy:")
        for asset, percentage in allocation.items():
            print(f"{asset}: {percentage}%")

    except ValueError as ve:
        logging.error(f"Invalid input: {ve}")
    except Exception as ex:
        logging.error(f"An unexpected error occurred: {ex}")
```
