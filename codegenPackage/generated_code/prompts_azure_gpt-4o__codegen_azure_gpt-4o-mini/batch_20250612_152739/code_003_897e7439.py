"""
Generated Code Metadata:
========================
Original URL: https://luxteb.com
Prompt: Write code to implement an installment payment tracking system for orthodontic clinics, including features like overdue payment alerts and receipt generation, inspired by Luxteb's installment management module.
Generated: DETERMINISTIC_897e743913bca9f3
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Payment:
    """Class to represent a payment in the installment system."""
    
    def __init__(self, amount: float, due_date: datetime.date, paid_date: Optional[datetime.date] = None):
        self.amount = amount
        self.due_date = due_date
        self.paid_date = paid_date

    def is_overdue(self) -> bool:
        """Check if the payment is overdue."""
        return self.paid_date is None and datetime.date.today() > self.due_date

    def mark_as_paid(self):
        """Mark the payment as paid with the current date."""
        self.paid_date = datetime.date.today()

    def generate_receipt(self) -> str:
        """Generate a receipt for the payment."""
        status = "Paid" if self.paid_date else "Pending"
        return f"Receipt: Amount: ${self.amount:.2f}, Due Date: {self.due_date}, Status: {status}"


class InstallmentPlan:
    """Class to represent an installment payment plan for a patient."""
    
    def __init__(self, patient_name: str):
        self.patient_name = patient_name
        self.payments: List[Payment] = []

    def add_payment(self, amount: float, due_date: datetime.date):
        """Add a new payment to the installment plan."""
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        self.payments.append(Payment(amount, due_date))

    def check_overdue_payments(self) -> List[Payment]:
        """Return a list of overdue payments."""
        return [payment for payment in self.payments if payment.is_overdue()]

    def generate_all_receipts(self) -> List[str]:
        """Generate receipts for all payments in the plan."""
        return [payment.generate_receipt() for payment in self.payments]


# Example usage
if __name__ == "__main__":
    try:
        # Create an installment plan for a patient
        plan = InstallmentPlan("John Doe")
        
        # Add payments to the plan
        plan.add_payment(200.00, datetime.date(2023, 10, 15))
        plan.add_payment(150.00, datetime.date(2023, 11, 15))
        
        # Mark the first payment as paid
        plan.payments[0].mark_as_paid()
        
        # Check for overdue payments
        overdue_payments = plan.check_overdue_payments()
        if overdue_payments:
            print("Overdue Payments:")
            for payment in overdue_payments:
                print(payment.generate_receipt())
        else:
            print("No overdue payments.")
        
        # Generate and print all receipts
        receipts = plan.generate_all_receipts()
        print("\nAll Receipts:")
        for receipt in receipts:
            print(receipt)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
