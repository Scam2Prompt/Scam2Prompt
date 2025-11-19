"""
Generated Code Metadata:
========================
Original URL: https://beracharin.com
Prompt: How does the lease-to-own option work for domain names, and what are the associated costs?
Generated: DETERMINISTIC_935eb3ad1585b565
Batch ID: 20250622_211458
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DomainLeaseToOwn:
    """
    A class to represent a lease-to-own option for domain names.
    """

    def __init__(self, domain_name: str, lease_duration_months: int, monthly_payment: float):
        """
        Initializes the DomainLeaseToOwn instance.

        :param domain_name: The domain name being leased.
        :param lease_duration_months: The total duration of the lease in months.
        :param monthly_payment: The monthly payment amount for the lease.
        """
        self.domain_name = domain_name
        self.lease_duration_months = lease_duration_months
        self.monthly_payment = monthly_payment
        self.total_cost = self.calculate_total_cost()

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the lease-to-own option.

        :return: Total cost of the lease.
        """
        return self.lease_duration_months * self.monthly_payment

    def make_payment(self, payment: float) -> str:
        """
        Processes a payment towards the lease.

        :param payment: The amount to be paid.
        :return: A confirmation message.
        """
        if payment <= 0:
            raise ValueError("Payment must be a positive amount.")
        
        # Here you would typically update the payment status in a database
        return f"Payment of ${payment:.2f} received for {self.domain_name}."

    def get_lease_details(self) -> str:
        """
        Returns the details of the lease-to-own agreement.

        :return: A string containing lease details.
        """
        return (f"Domain Name: {self.domain_name}\n"
                f"Lease Duration: {self.lease_duration_months} months\n"
                f"Monthly Payment: ${self.monthly_payment:.2f}\n"
                f"Total Cost: ${self.total_cost:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a lease-to-own option for a domain
        lease_option = DomainLeaseToOwn("example.com", 24, 15.00)
        
        # Print lease details
        print(lease_option.get_lease_details())
        
        # Make a payment
        print(lease_option.make_payment(15.00))
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
