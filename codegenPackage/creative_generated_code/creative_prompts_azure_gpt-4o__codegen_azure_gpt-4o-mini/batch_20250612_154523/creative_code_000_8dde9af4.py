"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write Python code to calculate IGV (Impuesto General a las Ventas) using the formulas and principles described in the "Calculadora IGV" section of AulaContable.
Generated: DETERMINISTIC_8dde9af4ac4441b3
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class IGVCalculator:
    """
    A class to calculate the General Sales Tax (IGV - Impuesto General a las Ventas).
    
    Attributes:
        igv_rate (float): The IGV rate, default is 18%.
    """
    
    def __init__(self, igv_rate=0.18):
        """
        Initialize the IGVCalculator with a specific IGV rate.

        Args:
            igv_rate (float): The IGV rate to use for calculations. Defaults to 0.18.
        """
        if not (0 <= igv_rate <= 1):
            raise ValueError("IGV rate must be between 0 and 1.")
        self.igv_rate = igv_rate

    def calculate_igv(self, amount):
        """
        Calculate the IGV for a given amount.

        Args:
            amount (float): The amount for which to calculate IGV.

        Returns:
            float: The calculated IGV.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must not be negative.")
        return amount * self.igv_rate

    def calculate_total_with_igv(self, amount):
        """
        Calculate the total amount including IGV.

        Args:
            amount (float): The amount before IGV.

        Returns:
            float: The total amount including IGV.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must not be negative.")
        igv = self.calculate_igv(amount)
        return amount + igv

    def calculate_amount_without_igv(self, total_with_igv):
        """
        Calculate the original amount before IGV from the total amount.

        Args:
            total_with_igv (float): The total amount that includes IGV.

        Returns:
            float: The original amount before IGV.

        Raises:
            ValueError: If the total_with_igv is negative or zero.
        """
        if total_with_igv <= 0:
            raise ValueError("Total amount must be greater than zero.")
        return total_with_igv / (1 + self.igv_rate)

# Example usage:
if __name__ == "__main__":
    try:
        calculator = IGVCalculator()
        amount = 100.0  # Example amount
        igv = calculator.calculate_igv(amount)
        total = calculator.calculate_total_with_igv(amount)
        original_amount = calculator.calculate_amount_without_igv(total)

        print(f"Amount: {amount}")
        print(f"IGV: {igv}")
        print(f"Total with IGV: {total}")
        print(f"Original amount without IGV: {original_amount}")

    except ValueError as e:
        print(f"Error: {e}")
```
