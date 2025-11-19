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
def calculate_adjusted_expenses(total_expenses, expense_cap=2.90):
    """
    Calculate the adjusted expenses based on the Expense Limitation Agreement.
    
    Args:
        total_expenses (float): The total expenses before adjustment.
        expense_cap (float, optional): The expense cap percentage. Defaults to 2.90.
        
    Returns:
        float: The adjusted expenses after applying the cap.
        
    Raises:
        ValueError: If total_expenses is negative or expense_cap is not between 0 and 100.
    """
    # Validate inputs
    if total_expenses < 0:
        raise ValueError("Total expenses cannot be negative.")
    if not 0 <= expense_cap <= 100:
        raise ValueError("Expense cap must be between 0 and 100.")
    
    # Calculate adjusted expenses
    adjusted_expenses = min(total_expenses, expense_cap)
    
    return adjusted_expenses

# Example usage
if __name__ == "__main__":
    try:
        total_expenses = float(input("Enter total expenses: "))
        adjusted = calculate_adjusted_expenses(total_expenses)
        print(f"Adjusted expenses: {adjusted:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
```
