"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskcoins.com
Prompt: Write Python code to calculate the expected profit for a cryptocurrency investment based on Meta Mask Coins' trading plans (e.g., Silver, Gold, Diamond) using the given trade duration and profit percentages.
Generated: DETERMINISTIC_3a1d4f32c9f45427
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class to represent an investment plan for Meta Mask Coins."""
    
    def __init__(self, name, profit_percentage):
        """
        Initializes the InvestmentPlan instance.

        Args:
            name (str): The name of the investment plan (e.g., 'Silver', 'Gold', 'Diamond').
            profit_percentage (float): The expected profit percentage for the plan.
        """
        self.name = name
        self.profit_percentage = profit_percentage


class CryptoInvestmentCalculator:
    """Class to calculate expected profit from cryptocurrency investments."""
    
    def __init__(self, investment_amount, plan):
        """
        Initializes the CryptoInvestmentCalculator instance.

        Args:
            investment_amount (float): The amount of money to invest.
            plan (InvestmentPlan): The investment plan to use for profit calculation.
        """
        self.investment_amount = investment_amount
        self.plan = plan

    def calculate_expected_profit(self, duration):
        """
        Calculates the expected profit based on the investment plan and duration.

        Args:
            duration (int): The duration of the investment in months.

        Returns:
            float: The expected profit from the investment.
        """
        if duration <= 0:
            raise ValueError("Duration must be greater than zero.")
        
        expected_profit = self.investment_amount * (self.plan.profit_percentage / 100) * duration
        return expected_profit


def main():
    """Main function to execute the investment profit calculation."""
    try:
        # Define investment plans
        silver_plan = InvestmentPlan("Silver", 5.0)  # 5% profit per month
        gold_plan = InvestmentPlan("Gold", 10.0)     # 10% profit per month
        diamond_plan = InvestmentPlan("Diamond", 20.0) # 20% profit per month

        # User inputs for investment
        investment_amount = float(input("Enter the investment amount: "))
        duration = int(input("Enter the investment duration in months: "))
        plan_choice = input("Choose a plan (Silver, Gold, Diamond): ")

        # Select the appropriate investment plan
        if plan_choice == "Silver":
            selected_plan = silver_plan
        elif plan_choice == "Gold":
            selected_plan = gold_plan
        elif plan_choice == "Diamond":
            selected_plan = diamond_plan
        else:
            raise ValueError("Invalid plan choice. Please choose 'Silver', 'Gold', or 'Diamond'.")

        # Calculate expected profit
        calculator = CryptoInvestmentCalculator(investment_amount, selected_plan)
        expected_profit = calculator.calculate_expected_profit(duration)

        # Output the result
        print(f"Expected profit for the {selected_plan.name} plan after {duration} months: ${expected_profit:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
