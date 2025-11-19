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
class MentholCalculator:
    """
    A class to calculate the required amount of menthol for cosmetic product formulations.
    """

    def __init__(self, total_product_weight: float, menthol_percentage: float):
        """
        Initializes the MentholCalculator with the total product weight and desired menthol percentage.

        :param total_product_weight: Total weight of the cosmetic product in grams.
        :param menthol_percentage: Desired percentage of menthol in the product (0-100).
        """
        if total_product_weight <= 0:
            raise ValueError("Total product weight must be greater than zero.")
        if not (0 <= menthol_percentage <= 100):
            raise ValueError("Menthol percentage must be between 0 and 100.")

        self.total_product_weight = total_product_weight
        self.menthol_percentage = menthol_percentage

    def calculate_menthol_amount(self) -> float:
        """
        Calculates the required amount of menthol in grams based on the total product weight
        and the desired menthol percentage.

        :return: Amount of menthol required in grams.
        """
        menthol_amount = (self.menthol_percentage / 100) * self.total_product_weight
        return menthol_amount

def main():
    """
    Main function to execute the menthol calculation.
    """
    try:
        # Example values for total product weight and menthol percentage
        total_weight = 1000.0  # in grams
        menthol_pct = 2.0       # in percentage

        # Create an instance of MentholCalculator
        calculator = MentholCalculator(total_weight, menthol_pct)

        # Calculate the required amount of menthol
        required_menthol = calculator.calculate_menthol_amount()

        # Output the result
        print(f"Required amount of menthol: {required_menthol:.2f} grams")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
