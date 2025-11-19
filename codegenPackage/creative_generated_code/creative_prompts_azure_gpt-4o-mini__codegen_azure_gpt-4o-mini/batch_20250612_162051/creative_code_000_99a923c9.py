"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://avasconcelos.adv.br
Prompt: Write a Python script that calculates the potential tax savings from the MP 2.199-14/2001 for a company in the energy sector looking to reduce its IRPJ by 75%.
Generated: DETERMINISTIC_99a923c992e6cb00
Batch ID: 20250612_162051
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
    A class to calculate potential tax savings from MP 2.199-14/2001 for companies in the energy sector.
    """

    def __init__(self, irpj_rate, income):
        """
        Initializes the TaxCalculator with the IRPJ rate and company income.

        :param irpj_rate: The IRPJ rate as a percentage (e.g., 15 for 15%)
        :param income: The total taxable income of the company
        """
        self.irpj_rate = irpj_rate / 100  # Convert percentage to a decimal
        self.income = income

    def calculate_current_irpj(self):
        """
        Calculates the current IRPJ based on the company's income.

        :return: The current IRPJ amount
        """
        current_irpj = self.income * self.irpj_rate
        return current_irpj

    def calculate_tax_savings(self):
        """
        Calculates the potential tax savings from MP 2.199-14/2001, which allows for a 75% reduction in IRPJ.

        :return: The potential tax savings
        """
        current_irpj = self.calculate_current_irpj()
        savings = current_irpj * 0.75  # 75% reduction
        return savings

def main():
    """
    Main function to execute the tax savings calculation.
    """
    try:
        # User inputs
        irpj_rate = float(input("Enter the IRPJ rate (%): "))
        income = float(input("Enter the total taxable income of the company: "))

        # Validate inputs
        if irpj_rate < 0 or income < 0:
            raise ValueError("IRPJ rate and income must be non-negative values.")

        # Create a TaxCalculator instance
        tax_calculator = TaxCalculator(irpj_rate, income)

        # Calculate potential tax savings
        potential_savings = tax_calculator.calculate_tax_savings()

        # Output results
        print(f"Current IRPJ amount: {tax_calculator.calculate_current_irpj():.2f}")
        print(f"Potential tax savings from MP 2.199-14/2001: {potential_savings:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
