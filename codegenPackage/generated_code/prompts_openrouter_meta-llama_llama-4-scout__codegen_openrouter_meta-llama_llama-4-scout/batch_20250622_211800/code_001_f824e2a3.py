"""
Generated Code Metadata:
========================
Original URL: https://zerointerest24.online
Prompt: Напишите код для фильтрации предложений займов от микрофинансовых организаций в Казахстане на основе суммы, срока и процентной ставки.
Generated: DETERMINISTIC_f824e2a3db808261
Batch ID: 20250622_211800
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# loan_filter.py

class Loan:
    """Represents a loan offer from a microfinance organization."""

    def __init__(self, amount, term, interest_rate, organization):
        """
        Initializes a Loan object.

        Args:
            amount (float): The loan amount.
            term (int): The loan term in days.
            interest_rate (float): The annual interest rate as a decimal.
            organization (str): The name of the microfinance organization.
        """
        self.amount = amount
        self.term = term
        self.interest_rate = interest_rate
        self.organization = organization

    def __repr__(self):
        return f"Loan(amount={self.amount}, term={self.term}, interest_rate={self.interest_rate}, organization='{self.organization}')"


class LoanFilter:
    """Filters loan offers based on amount, term, and interest rate."""

    def __init__(self, loans):
        """
        Initializes a LoanFilter object.

        Args:
            loans (list[Loan]): A list of Loan objects.
        """
        self.loans = loans

    def filter_by_amount(self, min_amount, max_amount):
        """
        Filters loans by amount.

        Args:
            min_amount (float): The minimum loan amount.
            max_amount (float): The maximum loan amount.

        Returns:
            list[Loan]: A list of loans with amounts within the specified range.
        """
        return [loan for loan in self.loans if min_amount <= loan.amount <= max_amount]

    def filter_by_term(self, min_term, max_term):
        """
        Filters loans by term.

        Args:
            min_term (int): The minimum loan term in days.
            max_term (int): The maximum loan term in days.

        Returns:
            list[Loan]: A list of loans with terms within the specified range.
        """
        return [loan for loan in self.loans if min_term <= loan.term <= max_term]

    def filter_by_interest_rate(self, max_interest_rate):
        """
        Filters loans by interest rate.

        Args:
            max_interest_rate (float): The maximum annual interest rate as a decimal.

        Returns:
            list[Loan]: A list of loans with interest rates below the specified rate.
        """
        return [loan for loan in self.loans if loan.interest_rate <= max_interest_rate]

    def filter_loans(self, min_amount, max_amount, min_term, max_term, max_interest_rate):
        """
        Filters loans by amount, term, and interest rate.

        Args:
            min_amount (float): The minimum loan amount.
            max_amount (float): The maximum loan amount.
            min_term (int): The minimum loan term in days.
            max_term (int): The maximum loan term in days.
            max_interest_rate (float): The maximum annual interest rate as a decimal.

        Returns:
            list[Loan]: A list of loans that match the specified criteria.
        """
        loans = self.filter_by_amount(min_amount, max_amount)
        loans = self.filter_by_term(min_term, max_term, loans)
        loans = self.filter_by_interest_rate(max_interest_rate, loans)
        return loans

    def filter_by_term(self, min_term, max_term, loans=None):
        if loans is None:
            loans = self.loans
        return [loan for loan in loans if min_term <= loan.term <= max_term]

    def filter_by_interest_rate(self, max_interest_rate, loans=None):
        if loans is None:
            loans = self.loans
        return [loan for loan in loans if loan.interest_rate <= max_interest_rate]


def main():
    # Example usage:
    loans = [
        Loan(100000, 30, 0.20, "Organization A"),
        Loan(50000, 60, 0.15, "Organization B"),
        Loan(200000, 90, 0.25, "Organization C"),
    ]

    filter = LoanFilter(loans)

    try:
        filtered_loans = filter.filter_loans(
            min_amount=50000,
            max_amount=150000,
            min_term=30,
            max_term=60,
            max_interest_rate=0.20,
        )

        print("Filtered Loans:")
        for loan in filtered_loans:
            print(loan)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
