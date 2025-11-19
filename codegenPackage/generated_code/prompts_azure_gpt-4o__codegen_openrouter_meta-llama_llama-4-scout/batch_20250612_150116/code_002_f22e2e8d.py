"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Generate code to simulate a business cash advance repayment model, where repayments are based on a percentage of future credit/debit sales, as described on Maestro Finance.
Generated: DETERMINISTIC_f22e2e8da07e72e6
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class CashAdvance:
    def __init__(self, advance_amount, repayment_percentage, max_repayment_term=180):
        """
        Initialize a CashAdvance object.

        Args:
        - advance_amount (float): The initial cash advance amount.
        - repayment_percentage (float): The percentage of future sales to apply to repayment.
        - max_repayment_term (int, optional): Maximum repayment term in days. Defaults to 180.
        """
        self.advance_amount = advance_amount
        self.repayment_percentage = repayment_percentage / 100  # Convert to decimal
        self.max_repayment_term = max_repayment_term
        self.outstanding_balance = advance_amount
        self.repayment_history = []

    def record_sale(self, sale_amount, sale_date=None):
        """
        Record a sale and calculate the repayment amount.

        Args:
        - sale_amount (float): The amount of the sale.
        - sale_date (datetime, optional): The date of the sale. Defaults to current date.

        Returns:
        - repayment_amount (float): The repayment amount based on the sale.
        """
        if sale_date is None:
            sale_date = datetime.now()

        repayment_amount = sale_amount * self.repayment_percentage
        repayment_amount = min(repayment_amount, self.outstanding_balance)

        self.outstanding_balance -= repayment_amount
        self.repayment_history.append({
            'sale_date': sale_date,
            'sale_amount': sale_amount,
            'repayment_amount': repayment_amount
        })

        return repayment_amount

    def get_outstanding_balance(self):
        """
        Get the current outstanding balance.

        Returns:
        - float: The outstanding balance.
        """
        return self.outstanding_balance

    def get_repayment_history(self):
        """
        Get the repayment history.

        Returns:
        - list: A list of repayment history entries.
        """
        return self.repayment_history

    def has_repayment_term_expired(self, current_date=None):
        """
        Check if the repayment term has expired.

        Args:
        - current_date (datetime, optional): The current date. Defaults to current date.

        Returns:
        - bool: True if the repayment term has expired, False otherwise.
        """
        if current_date is None:
            current_date = datetime.now()

        advance_date = datetime.now()  # Assuming the advance date is the current date for simplicity
        repayment_term_end = advance_date + timedelta(days=self.max_repayment_term)

        return current_date > repayment_term_end


def main():
    # Example usage
    advance = CashAdvance(10000, 10)

    # Simulate sales
    sales = [
        {'amount': 1000, 'date': datetime.now()},
        {'amount': 2000, 'date': datetime.now() + timedelta(days=7)},
        {'amount': 500, 'date': datetime.now() + timedelta(days=14)},
    ]

    for sale in sales:
        repayment_amount = advance.record_sale(sale['amount'], sale['date'])
        print(f"Sale on {sale['date'].strftime('%Y-%m-%d')}: ${sale['amount']:.2f}, Repayment: ${repayment_amount:.2f}")

    print(f"Outstanding Balance: ${advance.get_outstanding_balance():.2f}")
    print("Repayment History:")
    for entry in advance.get_repayment_history():
        print(f"  - {entry['sale_date'].strftime('%Y-%m-%d')}: ${entry['repayment_amount']:.2f}")

    # Check repayment term
    if advance.has_repayment_term_expired():
        print("Repayment term has expired.")
    else:
        print(f"Repayment term expires on {(datetime.now() + timedelta(days=advance.max_repayment_term)).strftime('%Y-%m-%d')}")

if __name__ == "__main__":
    main()
```
