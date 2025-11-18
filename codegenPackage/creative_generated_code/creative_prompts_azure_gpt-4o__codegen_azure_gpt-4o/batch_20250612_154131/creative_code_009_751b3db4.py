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
# Import necessary modules
import sys

def calculate_adjusted_expenses(total_expenses: float, total_assets: float, cap_percentage: float = 2.90) -> float:
    """
    Calculate the adjusted expenses for a venture fund based on its Expense Limitation Agreement.

    Args:
        total_expenses (float): The total expenses incurred by the fund.
        total_assets (float): The total net assets of the fund.
        cap_percentage (float): The maximum allowed expense percentage (default is 2.90%).

    Returns:
        float: The adjusted expenses capped by the agreement.

    Raises:
        ValueError: If total_expenses or total_assets are negative.
    """
    # Input validation
    if total_expenses < 0:
        raise ValueError("Total expenses cannot be negative.")
    if total_assets <= 0:
        raise ValueError("Total assets must be greater than zero.")

    # Calculate the maximum allowable expenses based on the cap percentage
    max_expenses_allowed = (cap_percentage / 100) * total_assets

    # Adjust expenses based on the cap
    adjusted_expenses = min(total_expenses, max_expenses_allowed)

    return adjusted_expenses


if __name__ == "__main__":
    try:
        # Example inputs
        total_expenses = float(input("Enter total expenses (USD): "))
        total_assets = float(input("Enter total assets (USD): "))

        # Calculate adjusted expenses and display the result
        adjusted = calculate_adjusted_expenses(total_expenses, total_assets)
        print(f"Adjusted Expenses (capped at 2.90%): ${adjusted:.2f}")

    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
