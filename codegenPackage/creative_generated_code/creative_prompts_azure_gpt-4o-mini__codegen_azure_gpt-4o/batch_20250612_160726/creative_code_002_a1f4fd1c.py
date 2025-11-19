"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symibyotic.fi
Prompt: What are the best practices for creating a lease-to-own payment model for domain names, inspired by the offerings on symibyotic.fi?
Generated: DETERMINISTIC_a1f4fd1c0cb6483c
Batch ID: 20250612_160726
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation of a simple lease-to-own payment model for domain names. The code follows best practices, is well-documented, and includes error handling.

```python
import datetime
from typing import Optional


class DomainLeaseToOwn:
    """
    A class to represent a lease-to-own payment model for domain names.
    """

    def __init__(self, domain_name: str, total_price: float, lease_duration_months: int):
        """
        Initialize the lease-to-own model.

        :param domain_name: The domain name being leased.
        :param total_price: The total price of the domain in dollars.
        :param lease_duration_months: The duration of the lease in months.
        """
        if total_price <= 0:
            raise ValueError("Total price must be a positive number.")
        if lease_duration_months <= 0:
            raise ValueError("Lease duration must be a positive number.")

        self.domain_name = domain_name
        self.total_price = total_price
        self.lease_duration_months = lease_duration_months
        self.monthly_payment = round(total_price / lease_duration_months, 2)
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=lease_duration_months * 30)
        self.payments_made = 0
        self.is_fully_paid = False

    def make_payment(self, amount: float) -> Optional[str]:
        """
        Make a monthly payment toward the total domain cost.

        :param amount: The payment amount in dollars.
        :return: A message indicating the payment status.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")

        if self.is_fully_paid:
            return "Domain is already fully paid. Ownership has been transferred."

        if amount < self.monthly_payment:
            return (
                f"Payment insufficient. Monthly payment amount is ${self.monthly_payment:.2f}. "
                f"You paid ${amount:.2f}."
            )

        self.payments_made += 1
        remaining_payments = self.lease_duration_months - self.payments_made

        if remaining_payments <= 0:
            self.is_fully_paid = True
            return f"Congratulations! You have fully paid for the domain '{self.domain_name}'. Ownership has been transferred."
        else:
            return (
                f"Payment successful. {remaining_payments} payment(s) remaining "
                f"for the domain '{self.domain_name}'."
            )

    def get_lease_status(self) -> dict:
        """
        Get the current status of the lease.

        :return: A dictionary containing lease status information.
        """
        return {
            "domain_name": self.domain_name,
            "total_price": self.total_price,
            "monthly_payment": self.monthly_payment,
            "lease_duration_months": self.lease_duration_months,
            "payments_made": self.payments_made,
            "is_fully_paid": self.is_fully_paid,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    def __str__(self) -> str:
        """
        Provide a string representation of the lease-to-own details.

        :return: A formatted string with lease details.
        """
        return (
            f"Domain: {self.domain_name}\n"
            f"Total Price: ${self.total_price:.2f}\n"
            f"Monthly Payment: ${self.monthly_payment:.2f}\n"
            f"Lease Duration: {self.lease_duration_months} months\n"
            f"Payments Made: {self.payments_made}\n"
            f"Fully Paid: {'Yes' if self.is_fully_paid else 'No'}\n"
            f"Start Date: {self.start_date}\n"
            f"End Date: {self.end_date}\n"
        )


# Example usage
if __name__ == "__main__":
    try:
        # Initialize a lease-to-own agreement
        lease = DomainLeaseToOwn(domain_name="example.com", total_price=1200.0, lease_duration_months=12)

        print(lease)

        # Make payments
        print(lease.make_payment(100))  # Insufficient payment
        print(lease.make_payment(100))  # Insufficient payment again
        print(lease.make_payment(200))  # Correct payment
        print(lease.get_lease_status())  # Print current lease status

    except ValueError as e:
        print(f"Error: {e}")
```

This code models a lease-to-own payment system for domain names, where customers can pay monthly installments. It includes error handling for invalid inputs and provides detailed status information about the lease.
