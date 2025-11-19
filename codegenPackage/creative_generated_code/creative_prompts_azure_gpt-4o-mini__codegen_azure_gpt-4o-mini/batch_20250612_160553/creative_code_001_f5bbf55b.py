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
class DomainLeaseToOwn:
    """
    A class to facilitate the lease-to-own payment option for domain names.
    """

    def __init__(self, domain_name, lease_price, lease_terms_months, purchase_price):
        """
        Initializes the DomainLeaseToOwn instance.

        :param domain_name: str: The domain name to be leased.
        :param lease_price: float: The monthly lease price.
        :param lease_terms_months: int: The number of months for the lease term.
        :param purchase_price: float: The total purchase price if leased is completed.
        """
        self.domain_name = domain_name
        self.lease_price = lease_price
        self.lease_terms_months = lease_terms_months
        self.purchase_price = purchase_price
        self.total_paid = 0.0
        self.is_owned = False

    def make_payment(self, amount):
        """
        Processes a payment towards the lease or purchase price.

        :param amount: float: The amount to be paid.
        :raises ValueError: If the payment amount is not positive or exceeds the remaining balance.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be positive.")
        
        # Calculate remaining balance
        remaining_balance = self.purchase_price - self.total_paid
        if amount > remaining_balance:
            raise ValueError("Payment amount exceeds the remaining balance.")

        # Process the payment
        self.total_paid += amount
        print(f"Payment of ${amount:.2f} made for {self.domain_name}. Total paid: ${self.total_paid:.2f}")

        # Check if the domain ownership is completed
        if self.total_paid >= self.purchase_price:
            self.is_owned = True
            print(f"Congratulations! You now own the domain {self.domain_name}.")

    def get_payment_schedule(self):
        """
        Generates the payment schedule for the lease term.

        :return: list of dicts: A list of payment details per month.
        """
        schedule = []
        for month in range(1, self.lease_terms_months + 1):
            schedule.append({
                'month': month,
                'amount': self.lease_price,
                'total_paid_until_now': min(month * self.lease_price, self.purchase_price)
            })
        return schedule

    def remaining_balance(self):
        """
        Returns the remaining balance for the purchase after lease payments.

        :return: float: The remaining balance.
        """
        return max(0, self.purchase_price - self.total_paid)

    def __str__(self):
        """
        Returns a string representation of the domain lease-to-own instance.
        """
        return (f"Domain: {self.domain_name}, "
                f"Lease Price: ${self.lease_price:.2f}/month, "
                f"Total Paid: ${self.total_paid:.2f}, "
                f"Owned: {'Yes' if self.is_owned else 'No'}")

# Example usage:
if __name__ == "__main__":
    try:
        domain = DomainLeaseToOwn("example.com", 20.0, 12, 500.0)
        print(domain)

        # Simulate monthly payments
        for month in range(1, 13):
            domain.make_payment(domain.lease_price)

        # Final purchase payment
        domain.make_payment(domain.remaining_balance())
        print(domain)

    except ValueError as e:
        print(f"Error: {e}")
```
