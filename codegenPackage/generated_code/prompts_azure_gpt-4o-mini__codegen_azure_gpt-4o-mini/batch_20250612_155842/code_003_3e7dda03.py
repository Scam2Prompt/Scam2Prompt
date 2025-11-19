"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Develop a library function that calculates the benefits of using factoring versus traditional credit lines for small and medium enterprises.
Generated: DETERMINISTIC_3e7dda037de1e4c2
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FinancingOption:
    """
    A class to represent a financing option for small and medium enterprises.
    """

    def __init__(self, amount: float, interest_rate: float, term_months: int):
        """
        Initializes a FinancingOption instance.

        :param amount: The principal amount of the financing option.
        :param interest_rate: The annual interest rate (as a decimal).
        :param term_months: The term of the financing in months.
        """
        self.amount = amount
        self.interest_rate = interest_rate
        self.term_months = term_months

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the financing option.

        :return: The total cost of the financing option.
        """
        monthly_rate = self.interest_rate / 12
        total_cost = self.amount * (1 + monthly_rate * self.term_months)
        return total_cost


class FactoringOption:
    """
    A class to represent a factoring option for small and medium enterprises.
    """

    def __init__(self, invoice_amount: float, factoring_fee_rate: float):
        """
        Initializes a FactoringOption instance.

        :param invoice_amount: The total amount of the invoice being factored.
        :param factoring_fee_rate: The fee rate charged by the factoring company (as a decimal).
        """
        self.invoice_amount = invoice_amount
        self.factoring_fee_rate = factoring_fee_rate

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the factoring option.

        :return: The total cost of the factoring option.
        """
        total_cost = self.invoice_amount * (1 - self.factoring_fee_rate)
        return total_cost


def compare_financing_options(credit_line: FinancingOption, factoring: FactoringOption) -> str:
    """
    Compares the total costs of a credit line and a factoring option.

    :param credit_line: An instance of FinancingOption representing the credit line.
    :param factoring: An instance of FactoringOption representing the factoring option.
    :return: A string indicating which option is more cost-effective.
    """
    try:
        credit_line_cost = credit_line.calculate_total_cost()
        factoring_cost = factoring.calculate_total_cost()

        if credit_line_cost < factoring_cost:
            return "The credit line is more cost-effective."
        elif factoring_cost < credit_line_cost:
            return "The factoring option is more cost-effective."
        else:
            return "Both options have the same total cost."
    except Exception as e:
        return f"An error occurred while comparing options: {str(e)}"


# Example usage:
if __name__ == "__main__":
    # Define a credit line option
    credit_line = FinancingOption(amount=10000, interest_rate=0.08, term_months=12)

    # Define a factoring option
    factoring = FactoringOption(invoice_amount=10000, factoring_fee_rate=0.05)

    # Compare the two options
    result = compare_financing_options(credit_line, factoring)
    print(result)
```
