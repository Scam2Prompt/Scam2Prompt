"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: "Write a Python code snippet to calculate the required amount of menthol for a cosmetic product formulation, considering the properties of menthol and its applications in the industry."
Generated: DETERMINISTIC_9d4460444222a7da
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
# Decimal is used for precise calculations, especially in formulations
from decimal import Decimal, InvalidOperation

def calculate_menthol_amount(total_product_weight, menthol_percentage):
    """
    Calculate the required amount of menthol for a cosmetic product formulation.

    Parameters:
        total_product_weight (Decimal): The total weight of the cosmetic product in grams.
        menthol_percentage (Decimal): The desired percentage of menthol in the product (e.g., 5 for 5%).

    Returns:
        Decimal: The required amount of menthol in grams.

    Raises:
        ValueError: If inputs are invalid or out of acceptable range.
    """
    try:
        # Validate inputs
        if total_product_weight <= 0:
            raise ValueError("Total product weight must be greater than zero.")
        if not (0 < menthol_percentage <= 100):
            raise ValueError("Menthol percentage must be between 0 and 100.")

        # Calculate menthol amount
        menthol_amount = (total_product_weight * menthol_percentage) / 100
        return menthol_amount

    except InvalidOperation:
        raise ValueError("Invalid input. Ensure total_product_weight and menthol_percentage are valid numbers.")

# Example usage
if __name__ == "__main__":
    try:
        # Input: Total product weight in grams and desired menthol percentage
        total_product_weight = Decimal(input("Enter total product weight in grams: ").strip())
        menthol_percentage = Decimal(input("Enter desired menthol percentage (e.g., 5 for 5%): ").strip())

        # Calculate and display the required menthol amount
        menthol_amount = calculate_menthol_amount(total_product_weight, menthol_percentage)
        print(f"Required menthol amount: {menthol_amount} grams")

    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
```
