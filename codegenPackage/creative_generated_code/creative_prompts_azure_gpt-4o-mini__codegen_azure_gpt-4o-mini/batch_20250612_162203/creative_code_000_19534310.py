"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Generate a code snippet for an accounting application that integrates tax calculation features based on the latest tax guide provided by Lund & Kieck.
Generated: DETERMINISTIC_195343100b1ec1f8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TaxCalculator:
    """
    A class to calculate tax based on the latest tax guide provided by Lund & Kieck.
    """

    def __init__(self, income: float, tax_rate: float):
        """
        Initializes the TaxCalculator with income and tax rate.
        
        :param income: Total income for which tax needs to be calculated
        :param tax_rate: Applicable tax rate as a percentage (e.g., 20 for 20%)
        """
        self.income = income
        self.tax_rate = tax_rate / 100  # Convert percentage to decimal

    def calculate_tax(self) -> float:
        """
        Calculate the total tax based on income and tax rate.
        
        :return: The calculated tax amount
        :raises ValueError: If income is negative or tax rate is not between 0 and 100
        """
        if self.income < 0:
            raise ValueError("Income cannot be negative.")
        if not (0 <= self.tax_rate * 100 <= 100):
            raise ValueError("Tax rate must be between 0 and 100.")

        tax = self.income * self.tax_rate
        return tax

    def get_tax_summary(self) -> dict:
        """
        Generate a summary of the tax calculation.
        
        :return: A dictionary with income, tax rate, and calculated tax
        """
        try:
            tax = self.calculate_tax()
            return {
                "income": self.income,
                "tax_rate": self.tax_rate * 100,  # Convert back to percentage for display
                "calculated_tax": tax
            }
        except ValueError as e:
            # Log the error (in production, consider using logging framework)
            print(f"Error calculating tax: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    try:
        income = 50000  # Example income
        tax_rate = 20   # Example tax rate in percentage
        
        tax_calculator = TaxCalculator(income, tax_rate)
        tax_summary = tax_calculator.get_tax_summary()
        
        print("Tax Summary:", tax_summary)
    except Exception as e:
        print(f"An error occurred: {e}")
```
