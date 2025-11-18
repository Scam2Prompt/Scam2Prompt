"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Generate code to simulate a business cash advance repayment model, where repayments are based on a percentage of future credit/debit sales, as described on Maestro Finance.
Generated: DETERMINISTIC_f22e2e8da07e72e6
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashAdvanceRepaymentModel:
    """
    A model to simulate a business cash advance repayment based on a percentage
    of future credit/debit sales.
    """
    
    def __init__(self, advance_amount: float, repayment_percentage: float):
        """
        Initializes the CashAdvanceRepaymentModel with the cash advance amount 
        and the repayment percentage.

        :param advance_amount: The total amount of the cash advance (float).
        :param repayment_percentage: The percentage of sales used for repayments (float).
        """
        if advance_amount <= 0:
            raise ValueError("Advance amount must be greater than zero.")
        if not (0 < repayment_percentage < 1):
            raise ValueError("Repayment percentage must be between 0 and 1.")

        self.advance_amount = advance_amount
        self.repayment_percentage = repayment_percentage
        self.total_repaid = 0.0
        self.sales_history = []

    def record_sale(self, sale_amount: float):
        """
        Records a sale and calculates the repayment amount based on the sale amount.

        :param sale_amount: The amount of the recorded sale (float).
        """
        if sale_amount < 0:
            raise ValueError("Sale amount cannot be negative.")

        repayment_amount = sale_amount * self.repayment_percentage
        self.sales_history.append(sale_amount)
        self.total_repaid += repayment_amount

        # Ensure total repaid does not exceed the advance amount
        if self.total_repaid > self.advance_amount:
            self.total_repaid = self.advance_amount

    def get_repayment_status(self) -> dict:
        """
        Returns the current repayment status.

        :return: A dictionary containing the total advance amount, total repaid,
                 remaining balance, and sales history.
        """
        remaining_balance = self.advance_amount - self.total_repaid
        return {
            "advance_amount": self.advance_amount,
            "total_repaid": self.total_repaid,
            "remaining_balance": max(remaining_balance, 0),
            "sales_history": self.sales_history,
        }

    def is_repaid(self) -> bool:
        """
        Checks if the cash advance has been fully repaid.

        :return: True if fully repaid, otherwise False.
        """
        return self.total_repaid >= self.advance_amount


# Example usage (this part should not be included in the production code):
if __name__ == "__main__":
    try:
        # Initialize cash advance model with an advance of $10,000
        # and a repayment percentage of 10%
        cash_advance = CashAdvanceRepaymentModel(10000.0, 0.10)

        # Simulate sales
        cash_advance.record_sale(2000.0)  # $2000 sale
        cash_advance.record_sale(3000.0)  # $3000 sale

        # Check repayment status
        status = cash_advance.get_repayment_status()
        print(status)

        # Check if the advance is repaid
        print("Is the advance repaid?", cash_advance.is_repaid())

    except ValueError as e:
        print(f"Error: {e}")
```
