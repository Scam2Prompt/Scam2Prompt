"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: Write a Python script that calculates the potential tax savings from the MP 2.199-14/2001 for a company in the energy sector looking to reduce its IRPJ by 75%.
Generated: DETERMINISTIC_99a923c992e6cb00
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_savings_calculator.py

class TaxSavingsCalculator:
    """
    A class to calculate potential tax savings from the MP 2.199-14/2001
    for companies in the energy sector looking to reduce their IRPJ by 75%.
    """

    def __init__(self, irpj_rate: float, taxable_income: float):
        """
        Initializes the TaxSavingsCalculator with the IRPJ rate and taxable income.

        :param irpj_rate: The current IRPJ rate as a decimal (e.g., 0.15 for 15%).
        :param taxable_income: The taxable income of the company.
        """
        if not (0 <= irpj_rate <= 1):
            raise ValueError("IRPJ rate must be between 0 and 1.")
        if taxable_income < 0:
            raise ValueError("Taxable income must be a non-negative value.")

        self.irpj_rate = irpj_rate
        self.taxable_income = taxable_income

    def calculate_irpj(self) -> float:
        """
        Calculates the current IRPJ based on the taxable income.

        :return: The current IRPJ amount.
        """
        return self.taxable_income * self.irpj_rate

    def calculate_tax_savings(self) -> float:
        """
        Calculates the potential tax savings from the MP 2.199-14/2001.

        :return: The amount of tax savings.
        """
        current_irpj = self.calculate_irpj()
        tax_savings = current_irpj * 0.75  # 75% reduction
        return tax_savings

    def display_results(self):
        """
        Displays the current IRPJ and potential tax savings.
        """
        try:
            current_irpj = self.calculate_irpj()
            tax_savings = self.calculate_tax_savings()
            print(f"Current IRPJ: {current_irpj:.2f}")
            print(f"Potential Tax Savings: {tax_savings:.2f}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    try:
        # Define the IRPJ rate and taxable income
        irpj_rate = 0.15  # 15%
        taxable_income = 1000000  # Example taxable income

        # Create an instance of the TaxSavingsCalculator
        calculator = TaxSavingsCalculator(irpj_rate, taxable_income)

        # Display the results
        calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
