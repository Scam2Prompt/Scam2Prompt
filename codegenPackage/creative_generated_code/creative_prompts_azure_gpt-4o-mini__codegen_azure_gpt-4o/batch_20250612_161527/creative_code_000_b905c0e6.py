"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdays.com
Prompt: Generate a code snippet for a financial application that structures lending transactions in both local and foreign currencies, similar to the services offered by Ramdays.
Generated: DETERMINISTIC_b905c0e6ea0a3bb6
Batch ID: 20250612_161527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Currency:
    """
    Represents a currency with a name and exchange rate to a base currency (e.g., USD).
    """
    def __init__(self, code: str, name: str, exchange_rate_to_base: float):
        """
        Initialize a currency.

        :param code: Currency code (e.g., 'USD', 'EUR').
        :param name: Full name of the currency (e.g., 'US Dollar').
        :param exchange_rate_to_base: Exchange rate to base currency (e.g., 'USD' = 1.0).
        """
        self.code = code
        self.name = name
        self.exchange_rate_to_base = exchange_rate_to_base

    def convert_to_base(self, amount: float) -> float:
        """
        Converts an amount in this currency to the base currency.

        :param amount: Amount in this currency.
        :return: Equivalent amount in the base currency.
        """
        return amount * self.exchange_rate_to_base


class LendingTransaction:
    """
    Represents a lending transaction in local or foreign currencies.
    """
    def __init__(self, transaction_id: str, borrower_name: str, amount: float, currency: Currency, interest_rate: float, duration_months: int):
        """
        Initialize a lending transaction.

        :param transaction_id: Unique transaction identifier.
        :param borrower_name: Name of the borrower.
        :param amount: Loan amount.
        :param currency: Loan currency.
        :param interest_rate: Annual interest rate (in percentage).
        :param duration_months: Duration of the loan in months.
        """
        self.transaction_id = transaction_id
        self.borrower_name = borrower_name
        self.amount = amount
        self.currency = currency
        self.interest_rate = interest_rate
        self.duration_months = duration_months
        self.creation_date = datetime.datetime.now()

    def calculate_total_repayment(self) -> float:
        """
        Calculate the total repayment amount including interest.

        :return: Total repayment amount in the loan's currency.
        """
        principal = self.amount
        annual_interest = principal * (self.interest_rate / 100)
        total_interest = annual_interest * (self.duration_months / 12)
        return principal + total_interest

    def get_summary(self) -> str:
        """
        Generate a summary of the transaction.

        :return: Summary string containing transaction details.
        """
        total_repayment = self.calculate_total_repayment()
        total_in_base_currency = self.currency.convert_to_base(total_repayment)
        summary = (
            f"Transaction ID: {self.transaction_id}\n"
            f"Borrower: {self.borrower_name}\n"
            f"Loan Amount: {self.amount} {self.currency.code} ({self.currency.name})\n"
            f"Interest Rate: {self.interest_rate}%\n"
            f"Duration: {self.duration_months} months\n"
            f"Total Repayment: {total_repayment:.2f} {self.currency.code}\n"
            f"Equivalent in Base Currency: {total_in_base_currency:.2f} USD\n"
            f"Transaction Date: {self.creation_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Define currencies
        usd = Currency(code="USD", name="US Dollar", exchange_rate_to_base=1.0)
        eur = Currency(code="EUR", name="Euro", exchange_rate_to_base=1.1)  # Example exchange rate

        # Create a lending transaction (foreign currency)
        transaction = LendingTransaction(
            transaction_id="TX12345",
            borrower_name="John Doe",
            amount=5000,
            currency=eur,
            interest_rate=5.0,
            duration_months=12
        )

        # Print transaction summary
        print(transaction.get_summary())

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
