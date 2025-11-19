"""
Generated Code Metadata:
========================
Original URL: https://synthr-mvp.pages.dev
Prompt: Generate a function that calculates the C-ratio based on collateral and debt balances in the SYNTHR ecosystem.
Generated: DETERMINISTIC_8deb1628c5ebe555
Batch ID: 20250612_161201
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SynthrCalculator:
    """
    A class to calculate the C-ratio in the SYNTHR ecosystem based on collateral and debt balances.
    """

    def __init__(self, collateral: float, debt: float):
        """
        Initializes the SynthrCalculator with collateral and debt balances.

        :param collateral: The amount of collateral.
        :param debt: The amount of debt.
        """
        self.collateral = collateral
        self.debt = debt

    def calculate_c_ratio(self) -> float:
        """
        Calculates the C-ratio.

        The C-ratio is defined as the ratio of collateral to debt.

        :return: The C-ratio as a float.
        :raises ValueError: If the debt is zero, as this would lead to division by zero.
        """
        if self.debt == 0:
            raise ValueError("Debt cannot be zero when calculating C-ratio.")

        c_ratio = self.collateral / self.debt
        return c_ratio

# Example usage
if __name__ == "__main__":
    try:
        collateral_amount = 1000.0  # Example collateral amount
        debt_amount = 500.0          # Example debt amount

        calculator = SynthrCalculator(collateral_amount, debt_amount)
        c_ratio = calculator.calculate_c_ratio()
        print(f"The C-ratio is: {c_ratio:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
