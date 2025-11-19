"""
Generated Code Metadata:
========================
Original URL: https://arkventure.net
Prompt: Generate code to calculate the adjusted expenses for the ARK Venture Fund based on its Expense Limitation Agreement, which caps expenses at 2.90%.
Generated: DETERMINISTIC_751b3db440a4f55e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ExpenseCalculator:
    """
    A class to calculate adjusted expenses for the ARK Venture Fund based on the Expense Limitation Agreement.
    """

    def __init__(self, total_expenses: float):
        """
        Initializes the ExpenseCalculator with the total expenses.

        :param total_expenses: Total expenses incurred by the fund.
        """
        if total_expenses < 0:
            raise ValueError("Total expenses cannot be negative.")
        self.total_expenses = total_expenses
        self.expense_limit_percentage = 2.90 / 100  # Convert percentage to decimal

    def calculate_adjusted_expenses(self) -> float:
        """
        Calculates the adjusted expenses based on the expense limitation agreement.

        :return: Adjusted expenses capped at the expense limit.
        """
        # Calculate the maximum allowable expenses based on the limit
        max_allowable_expenses = self.total_expenses * self.expense_limit_percentage
        
        # Return the lesser of total expenses or the maximum allowable expenses
        adjusted_expenses = min(self.total_expenses, max_allowable_expenses)
        
        return adjusted_expenses

def main():
    """
    Main function to execute the expense calculation.
    """
    try:
        # Example total expenses for the ARK Venture Fund
        total_expenses = float(input("Enter the total expenses for the ARK Venture Fund: "))
        
        # Create an instance of ExpenseCalculator
        calculator = ExpenseCalculator(total_expenses)
        
        # Calculate and display the adjusted expenses
        adjusted_expenses = calculator.calculate_adjusted_expenses()
        print(f"Adjusted Expenses: ${adjusted_expenses:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
