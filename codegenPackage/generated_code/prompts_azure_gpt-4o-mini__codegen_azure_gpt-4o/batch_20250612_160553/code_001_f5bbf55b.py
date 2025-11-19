"""
Generated Code Metadata:
========================
Original URL: https://fornm.network
Prompt: Write a code snippet that facilitates a lease-to-own payment option for domain names, inspired by the features on fornm.network.
Generated: DETERMINISTIC_f5bbf55b746b56b2
Batch ID: 20250612_160553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class LeaseToOwnDomain:
    """
    A class to facilitate lease-to-own payment options for domain names.
    """

    def __init__(self, domain_name, total_price, monthly_payment, lease_duration_months):
        """
        Initialize the lease-to-own contract.

        :param domain_name: str - The domain name being leased.
        :param total_price: float - Total price to own the domain.
        :param monthly_payment: float - Monthly payment amount.
        :param lease_duration_months: int - Duration of the lease in months.
        """
        self.domain_name = domain_name
        self.total_price = total_price
        self.monthly_payment = monthly_payment
        self.lease_duration_months = lease_duration_months
        self.payments_made = 0
        self.start_date = datetime.date.today()
        self.end_date = self.start_date + datetime.timedelta(days=30 * lease_duration_months)
        self.is_owned = False

    def make_payment(self):
        """
        Simulates making a monthly payment. Updates the payment status.
        """
        if self.is_owned:
            print(f"The domain '{self.domain_name}' is already fully owned.")
            return

        if self.payments_made < self.lease_duration_months:
            self.payments_made += 1
            print(f"Payment {self.payments_made}/{self.lease_duration_months} made for '{self.domain_name}'.")
        else:
            print(f"All payments have been made for '{self.domain_name}'.")
        
        # Check if the domain is now fully owned
        if self.payments_made >= self.lease_duration_months:
            self.is_owned = True
            print(f"Congratulations! You now fully own the domain '{self.domain_name}'.")

    def get_status(self):
        """
        Returns the current status of the lease.

        :return: dict - Status information about the lease.
        """
        return {
            "domain_name": self.domain_name,
            "total_price": self.total_price,
            "monthly_payment": self.monthly_payment,
            "lease_duration_months": self.lease_duration_months,
            "payments_made": self.payments_made,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "is_owned": self.is_owned
        }

# Example usage
if __name__ == "__main__":
    try:
        # Create a lease-to-own contract for a domain
        lease = LeaseToOwnDomain(domain_name="example.com", total_price=1200.0, monthly_payment=100.0, lease_duration_months=12)

        # Simulate monthly payments
        for _ in range(13):  # Attempting one extra payment to test edge case
            lease.make_payment()

        # Print the final status of the lease
        status = lease.get_status()
        print("\nLease Status:")
        for key, value in status.items():
            print(f"{key}: {value}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
