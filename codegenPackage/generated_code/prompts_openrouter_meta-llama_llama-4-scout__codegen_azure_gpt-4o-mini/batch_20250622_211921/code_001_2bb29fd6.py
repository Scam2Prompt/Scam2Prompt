"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: "Write a Python script to calculate the Impuesto General a las Ventas (IGV) for a given amount in Peru, considering the current tax rates and regulations."
Generated: DETERMINISTIC_2bb29fd6749975db
Batch ID: 20250622_211921
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# igv_calculator.py

class IGVCalculator:
    """
    A class to calculate the Impuesto General a las Ventas (IGV) in Peru.
    The current IGV rate is set to 18%.
    """

    IGV_RATE = 0.18  # Current IGV rate in Peru

    @staticmethod
    def calculate_igv(amount):
        """
        Calculate the IGV for a given amount.

        Parameters:
        amount (float): The amount to calculate IGV for.

        Returns:
        float: The calculated IGV.

        Raises:
        ValueError: If the amount is negative or not a number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount must be a number.")
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        return amount * IGVCalculator.IGV_RATE

    @staticmethod
    def calculate_total_with_igv(amount):
        """
        Calculate the total amount including IGV.

        Parameters:
        amount (float): The amount to calculate total with IGV for.

        Returns:
        float: The total amount including IGV.

        Raises:
        ValueError: If the amount is negative or not a number.
        """
        igv = IGVCalculator.calculate_igv(amount)
        return amount + igv


def main():
    """
    Main function to execute the IGV calculation.
    It prompts the user for an amount and displays the IGV and total amount.
    """
    try:
        amount = float(input("Enter the amount (in PEN): "))
        igv = IGVCalculator.calculate_igv(amount)
        total = IGVCalculator.calculate_total_with_igv(amount)

        print(f"IGV (18%): {igv:.2f} PEN")
        print(f"Total amount including IGV: {total:.2f} PEN")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
