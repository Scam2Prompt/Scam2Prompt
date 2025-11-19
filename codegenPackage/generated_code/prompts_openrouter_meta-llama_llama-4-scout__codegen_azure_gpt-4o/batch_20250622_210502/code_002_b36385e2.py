"""
Generated Code Metadata:
========================
Original URL: https://vantardxyz.web.app
Prompt: Generate code to calculate the surge tax for redeeming VTARD tokens based on the provided surge pricing model.
Generated: DETERMINISTIC_b36385e265f5e9c8
Batch ID: 20250622_210502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# surge_tax_calculator.py

class SurgeTaxCalculator:
    """
    A class to calculate surge tax for redeeming VTARD tokens based on a surge pricing model.
    """

    def __init__(self, base_tax_rate: float, surge_threshold: float, surge_multiplier: float):
        """
        Initialize the SurgeTaxCalculator with the base tax rate, surge threshold, and surge multiplier.

        :param base_tax_rate: The base tax rate (percentage) applied to all transactions.
        :param surge_threshold: The threshold value above which surge pricing is applied.
        :param surge_multiplier: The multiplier applied to the base tax rate during surge pricing.
        """
        if base_tax_rate < 0 or surge_threshold < 0 or surge_multiplier < 1:
            raise ValueError("Invalid input values. Ensure base_tax_rate >= 0, surge_threshold >= 0, and surge_multiplier >= 1.")
        
        self.base_tax_rate = base_tax_rate
        self.surge_threshold = surge_threshold
        self.surge_multiplier = surge_multiplier

    def calculate_tax(self, token_value: float) -> float:
        """
        Calculate the surge tax for redeeming VTARD tokens.

        :param token_value: The value of the tokens being redeemed.
        :return: The calculated tax amount.
        """
        if token_value < 0:
            raise ValueError("Token value must be non-negative.")

        # Determine if surge pricing applies
        if token_value > self.surge_threshold:
            # Apply surge pricing
            tax_rate = self.base_tax_rate * self.surge_multiplier
        else:
            # Apply base tax rate
            tax_rate = self.base_tax_rate

        # Calculate the tax amount
        tax_amount = token_value * (tax_rate / 100)
        return round(tax_amount, 2)  # Return the tax amount rounded to 2 decimal places


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with example values
        base_tax_rate = 5.0  # 5% base tax rate
        surge_threshold = 1000.0  # Surge pricing applies for token values above 1000
        surge_multiplier = 2.0  # Surge multiplier doubles the base tax rate

        calculator = SurgeTaxCalculator(base_tax_rate, surge_threshold, surge_multiplier)

        # Example token values
        token_values = [500, 1500, 2000]

        for value in token_values:
            tax = calculator.calculate_tax(value)
            print(f"Token Value: {value}, Tax Amount: {tax}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
