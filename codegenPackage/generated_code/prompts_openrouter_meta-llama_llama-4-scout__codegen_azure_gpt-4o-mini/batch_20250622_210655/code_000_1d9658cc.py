"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Write a code snippet in Python to calculate the reduction of 75% of IRPJ tax for a company in the Northeast region of Brazil, considering the MP 2.199-14/2001 law."
Generated: DETERMINISTIC_1d9658cca7d41be2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TaxCalculator:
    """
    A class to calculate the IRPJ tax reduction for companies in the Northeast region of Brazil
    based on the MP 2.199-14/2001 law.
    """

    def __init__(self, gross_income: float):
        """
        Initializes the TaxCalculator with the company's gross income.

        :param gross_income: The gross income of the company.
        """
        if gross_income < 0:
            raise ValueError("Gross income must be a non-negative value.")
        self.gross_income = gross_income
        self.irpj_rate = 0.15  # Standard IRPJ tax rate (15%)

    def calculate_irpj(self) -> float:
        """
        Calculates the IRPJ tax based on the gross income.

        :return: The calculated IRPJ tax.
        """
        return self.gross_income * self.irpj_rate

    def calculate_reduction(self) -> float:
        """
        Calculates the IRPJ tax reduction for companies in the Northeast region.

        :return: The reduced IRPJ tax after applying the 75% reduction.
        """
        irpj_tax = self.calculate_irpj()
        reduction = irpj_tax * 0.75  # 75% reduction
        reduced_tax = irpj_tax - reduction
        return reduced_tax

    def get_tax_summary(self) -> dict:
        """
        Provides a summary of the tax calculation and reduction.

        :return: A dictionary containing the gross income, original IRPJ tax, and reduced IRPJ tax.
        """
        try:
            irpj_tax = self.calculate_irpj()
            reduced_tax = self.calculate_reduction()
            return {
                "Gross Income": self.gross_income,
                "Original IRPJ Tax": irpj_tax,
                "Reduced IRPJ Tax": reduced_tax
            }
        except Exception as e:
            return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    try:
        # Example gross income for a company in the Northeast region
        gross_income_example = 1000000.0  # 1 million BRL
        tax_calculator = TaxCalculator(gross_income_example)
        tax_summary = tax_calculator.get_tax_summary()
        print(tax_summary)
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
