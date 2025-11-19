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
class ARKVentureFund:
    """
    Calculates adjusted expenses for the ARK Venture Fund based on its Expense Limitation Agreement.
    """

    def __init__(self, expense_ratio: float, expense_limitation: float = 0.029):
        """
        Initializes the ARKVentureFund with an expense ratio and expense limitation.

        Args:
        - expense_ratio (float): The expense ratio of the fund.
        - expense_limitation (float, optional): The expense limitation. Defaults to 0.029 (2.90%).
        """
        self.expense_ratio = expense_ratio
        self.expense_limitation = expense_limitation

    def calculate_adjusted_expenses(self, fund_assets: float) -> float:
        """
        Calculates the adjusted expenses for the ARK Venture Fund.

        Args:
        - fund_assets (float): The total assets of the fund.

        Returns:
        - float: The adjusted expenses.

        Raises:
        - ValueError: If fund_assets or expense_ratio is negative.
        - TypeError: If fund_assets or expense_ratio is not a number.
        """
        if not isinstance(fund_assets, (int, float)) or not isinstance(self.expense_ratio, (int, float)):
            raise TypeError("Fund assets and expense ratio must be numbers.")
        if fund_assets < 0 or self.expense_ratio < 0:
            raise ValueError("Fund assets and expense ratio cannot be negative.")

        # Calculate the maximum allowable expenses based on the expense limitation
        max_allowable_expenses = fund_assets * self.expense_limitation

        # Calculate the adjusted expenses, which is the minimum of the actual expenses and the maximum allowable expenses
        adjusted_expenses = min(fund_assets * self.expense_ratio, max_allowable_expenses)

        return adjusted_expenses


def main():
    try:
        # Example usage
        fund = ARKVentureFund(expense_ratio=0.03)  # 3.00% expense ratio
        fund_assets = 1000000  # $1,000,000 in fund assets
        adjusted_expenses = fund.calculate_adjusted_expenses(fund_assets)
        print(f"Adjusted expenses: ${adjusted_expenses:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
