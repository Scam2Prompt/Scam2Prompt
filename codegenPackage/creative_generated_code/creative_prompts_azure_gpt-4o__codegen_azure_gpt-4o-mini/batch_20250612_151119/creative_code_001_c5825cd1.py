"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bitkub.jp
Prompt: Generate code to calculate cryptocurrency tax obligations in Thailand based on the guidelines discussed on the Bitkub Japan website.
Generated: DETERMINISTIC_c5825cd1f3a4cacc
Batch ID: 20250612_151119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

class CryptoTaxCalculator:
    def __init__(self, income: float, expenses: float, capital_gains: float):
        """
        Initializes the CryptoTaxCalculator with income, expenses, and capital gains.

        :param income: Total income from cryptocurrency transactions
        :param expenses: Total expenses related to cryptocurrency transactions
        :param capital_gains: Total capital gains from cryptocurrency investments
        """
        self.income = income
        self.expenses = expenses
        self.capital_gains = capital_gains

    def calculate_net_income(self) -> float:
        """
        Calculates net income by subtracting expenses from income.

        :return: Net income
        """
        return self.income - self.expenses

    def calculate_taxable_income(self) -> float:
        """
        Calculates taxable income by adding net income to capital gains.

        :return: Taxable income
        """
        net_income = self.calculate_net_income()
        return net_income + self.capital_gains

    def calculate_tax_obligation(self) -> float:
        """
        Calculates the total tax obligation based on taxable income.

        :return: Tax obligation
        """
        taxable_income = self.calculate_taxable_income()
        tax_rate = self.get_tax_rate(taxable_income)
        return taxable_income * tax_rate

    @staticmethod
    def get_tax_rate(taxable_income: float) -> float:
        """
        Determines the tax rate based on Taxable income according to Thai tax brackets.

        :param taxable_income: The taxable income to assess the tax rate
        :return: Corresponding tax rate
        """
        if taxable_income <= 300000:
            return 0.0
        elif taxable_income <= 500000:
            return 0.15
        elif taxable_income <= 750000:
            return 0.20
        elif taxable_income <= 1000000:
            return 0.25
        else:
            return 0.30

def main():
    """
    Main function to execute the tax calculation based on user input.
    """
    try:
        income = float(input("Enter your total income from cryptocurrency transactions: "))
        expenses = float(input("Enter your total expenses related to cryptocurrency transactions: "))
        capital_gains = float(input("Enter your total capital gains from cryptocurrency investments: "))

        tax_calculator = CryptoTaxCalculator(income, expenses, capital_gains)
        tax_obligation = tax_calculator.calculate_tax_obligation()

        print(f"Your total tax obligation is: {tax_obligation:.2f} THB")

    except ValueError as e:
        print("Invalid input. Please enter numeric values.", str(e))
    except Exception as e:
        print("An error occurred while calculating tax obligations.", str(e))

if __name__ == "__main__":
    main()
```
