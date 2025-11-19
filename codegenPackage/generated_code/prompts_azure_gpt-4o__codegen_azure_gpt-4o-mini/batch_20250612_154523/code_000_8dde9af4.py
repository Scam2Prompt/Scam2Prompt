"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Write Python code to calculate IGV (Impuesto General a las Ventas) using the formulas and principles described in the "Calculadora IGV" section of AulaContable.
Generated: DETERMINISTIC_8dde9af4ac4441b3
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IGVCalculator:
    """
    A class to calculate the IGV (Impuesto General a las Ventas) based on the provided amount.
    The IGV rate is typically 18% in Peru.
    """

    IGV_RATE = 0.18  # IGV rate of 18%

    @staticmethod
    def calculate_igv(amount: float) -> float:
        """
        Calculate the IGV for a given amount.

        Parameters:
        amount (float): The amount to calculate IGV for.

        Returns:
        float: The calculated IGV.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        
        igv = amount * IGVCalculator.IGV_RATE
        return round(igv, 2)

    @staticmethod
    def calculate_total_with_igv(amount: float) -> float:
        """
        Calculate the total amount including IGV.

        Parameters:
        amount (float): The amount to calculate total with IGV for.

        Returns:
        float: The total amount including IGV.

        Raises:
        ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        
        total_with_igv = amount + IGVCalculator.calculate_igv(amount)
        return round(total_with_igv, 2)

    @staticmethod
    def calculate_amount_excluding_igv(total_with_igv: float) -> float:
        """
        Calculate the original amount before IGV was added.

        Parameters:
        total_with_igv (float): The total amount including IGV.

        Returns:
        float: The original amount excluding IGV.

        Raises:
        ValueError: If the total_with_igv is negative or zero.
        """
        if total_with_igv <= 0:
            raise ValueError("Total amount must be positive.")
        
        amount_excluding_igv = total_with_igv / (1 + IGVCalculator.IGV_RATE)
        return round(amount_excluding_igv, 2)

# Example usage
if __name__ == "__main__":
    try:
        amount = 100.00  # Example amount
        igv = IGVCalculator.calculate_igv(amount)
        total = IGVCalculator.calculate_total_with_igv(amount)
        original_amount = IGVCalculator.calculate_amount_excluding_igv(total)

        print(f"Amount: {amount}")
        print(f"Calculated IGV: {igv}")
        print(f"Total with IGV: {total}")
        print(f"Original amount excluding IGV: {original_amount}")

    except ValueError as e:
        print(f"Error: {e}")
```
