"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fornm.network
Prompt: Write a code snippet that facilitates a lease-to-own payment option for domain names, inspired by the features on fornm.network.
Generated: DETERMINISTIC_f5bbf55b746b56b2
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LeaseToOwnDomain:
    """
    A class to facilitate lease-to-own payment options for domain names.
    Inspired by features offered by fornm.network.
    """

    def __init__(self, domain_name, total_price, monthly_payment, lease_start_date=None):
        """
        Initialize the lease-to-own contract.

        :param domain_name: str - The name of the domain being leased.
        :param total_price: float - The total price of the domain.
        :param monthly_payment: float - The monthly payment amount.
        :param lease_start_date: datetime.date - The start date of the lease. Defaults to today.
        """
        self.domain_name = domain_name
        self.total_price = total_price
        self.monthly_payment = monthly_payment
        self.lease_start_date = lease_start_date or datetime.date.today()
        self.payments_made = 0
        self.balance_remaining = total_price
        self.is_lease_completed = False

    def make_payment(self):
        """
        Processes a monthly payment towards the lease.

        :raises ValueError: If the lease is already completed.
        """
        if self.is_lease_completed:
            raise ValueError(f"The lease for domain '{self.domain_name}' is already completed.")

        self.payments_made += 1
        self.balance_remaining -= self.monthly_payment

        # Check if lease is completed
        if self.balance_remaining <= 0:
            self.balance_remaining = 0
            self.is_lease_completed = True

        return {
            "domain_name": self.domain_name,
            "payments_made": self.payments_made,
            "balance_remaining": self.balance_remaining,
            "is_lease_completed": self.is_lease_completed
        }

    def get_lease_status(self):
        """
        Retrieves the current lease status.

        :return: dict - Lease status including payments made and balance remaining.
        """
        return {
            "domain_name": self.domain_name,
            "total_price": self.total_price,
            "monthly_payment": self.monthly_payment,
            "lease_start_date": self.lease_start_date,
            "payments_made": self.payments_made,
            "balance_remaining": self.balance_remaining,
            "is_lease_completed": self.is_lease_completed
        }


# Example Usage
if __name__ == "__main__":
    # Create a lease-to-own contract for a domain
    lease = LeaseToOwnDomain(domain_name="example.com", total_price=1200.0, monthly_payment=100.0)

    print("Initial Lease Status:")
    print(lease.get_lease_status())

    # Simulating monthly payments
    for month in range(13):  # Attempting 13 payments
        try:
            payment_status = lease.make_payment()
            print(f"Month {month + 1}: Payment Successful")
            print(payment_status)
        except ValueError as e:
            print(f"Month {month + 1}: {e}")
            break

    print("Final Lease Status:")
    print(lease.get_lease_status())
```

This code snippet demonstrates a lease-to-own implementation for domain names, including error handling, documentation, and production-ready practices.
