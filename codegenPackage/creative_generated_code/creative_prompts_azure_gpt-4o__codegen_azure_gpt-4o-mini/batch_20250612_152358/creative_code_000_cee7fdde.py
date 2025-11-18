"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hulashxcore.org
Prompt: Write Python code to simulate an investment plan calculator based on the "RTZ.y algorithm" described on hulashxcore.org, including parameters like deposit amount, plan duration, and percentage returns.
Generated: DETERMINISTIC_cee7fddeb09d4bcc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlanCalculator:
    """
    A class to simulate an investment plan calculator using the RTZ.y algorithm.
    
    Attributes:
        deposit_amount (float): The initial amount to invest.
        plan_duration (int): The duration of the investment plan in years.
        percentage_return (float): The annual return percentage.
    """

    def __init__(self, deposit_amount: float, plan_duration: int, percentage_return: float):
        """
        Initializes the investment plan calculator with the given parameters.
        
        Args:
            deposit_amount (float): The initial investment amount.
            plan_duration (int): The duration of the investment in years.
            percentage_return (float): The annual return percentage.
        
        Raises:
            ValueError: If any of the parameters are negative or zero.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        if plan_duration <= 0:
            raise ValueError("Plan duration must be greater than zero.")
        if percentage_return < 0:
            raise ValueError("Percentage return cannot be negative.")

        self.deposit_amount = deposit_amount
        self.plan_duration = plan_duration
        self.percentage_return = percentage_return

    def calculate_total_return(self) -> float:
        """
        Calculate the total return on investment at the end of the plan duration.
        
        Returns:
            float: Total amount after investment period.
        """
        total_return = self.deposit_amount * (1 + self.percentage_return / 100) ** self.plan_duration
        return total_return

    def calculate_profit(self) -> float:
        """
        Calculate the profit made from the investment.
        
        Returns:
            float: Profit from the investment.
        """
        total_return = self.calculate_total_return()
        profit = total_return - self.deposit_amount
        return profit

    def display_investment_summary(self):
        """
        Display a summary of the investment plan including initial deposit,
        total return, and profit earned.
        """
        try:
            total_return = self.calculate_total_return()
            profit = self.calculate_profit()
            print(f"Investment Summary:")
            print(f"Initial Deposit Amount: ${self.deposit_amount:,.2f}")
            print(f"Total Return after {self.plan_duration} years: ${total_return:,.2f}")
            print(f"Profit Earned: ${profit:,.2f}")
        except Exception as e:
            print(f"An error occurred while calculating the investment summary: {e}")

if __name__ == "__main__":
    try:
        # Example usage of the InvestmentPlanCalculator
        deposit = float(input("Enter the deposit amount: "))
        duration = int(input("Enter the plan duration (in years): "))
        return_percentage = float(input("Enter the annual return percentage: "))

        investment_plan = InvestmentPlanCalculator(deposit, duration, return_percentage)
        investment_plan.display_investment_summary()
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
