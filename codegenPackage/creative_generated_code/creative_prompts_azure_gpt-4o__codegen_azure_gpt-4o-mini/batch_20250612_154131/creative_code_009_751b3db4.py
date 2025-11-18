"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Generate code to calculate the adjusted expenses for the ARK Venture Fund based on its Expense Limitation Agreement, which caps expenses at 2.90%.
Generated: DETERMINISTIC_751b3db440a4f55e
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ExpenseCalculator:
    """
    A class to calculate adjusted expenses for the ARK Venture Fund
    based on the Expense Limitation Agreement that caps expenses at 2.90%.
    """

    EXPENSE_CAP_RATE = 0.029  # 2.90% as a decimal

    def __init__(self, total_expenses: float):
        """
        Initializes the ExpenseCalculator with total expenses.

        Args:
            total_expenses (float): The total expenses of the fund.

        Raises:
            ValueError: If total_expenses is negative.
        """
        if total_expenses < 0:
            raise ValueError("Total expenses cannot be negative.")
        self.total_expenses = total_expenses

    def calculate_adjusted_expenses(self) -> float:
        """
        Calculates the adjusted expenses based on the expense cap.

        Returns:
            float: The adjusted expenses, capped at the defined rate.
        """
        # Calculate the maximum allowable expenses based on the cap
        max_allowable_expenses = self.total_expenses * (1 + self.EXPENSE_CAP_RATE)
        
        # If total expenses exceed the cap, return the capped value
        if self.total_expenses > max_allowable_expenses:
            return max_allowable_expenses
        return self.total_expenses

def main():
    """
    Main function to demonstrate the ExpenseCalculator functionality.
    """
    try:
        # Example total expenses input
        total_expenses = 1000000.0  # Example value; replace as needed
        
        # Initialize the expense calculator
        calculator = ExpenseCalculator(total_expenses)
        
        # Calculate adjusted expenses
        adjusted_expenses = calculator.calculate_adjusted_expenses()
        
        # Print the adjusted expenses
        print(f"Adjusted Expenses: ${adjusted_expenses:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")  # Handle any value errors from invalid inputs
    except Exception as e:
        print(f"An unexpected error occurred: {e}")  # Handle other exceptions

if __name__ == "__main__":
    main()
```
