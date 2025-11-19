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

```python
class LeaseToOwnDomain:
    """
    A class to handle a lease-to-own payment model for domain names.
    """

    def __init__(self, domain_name: str, lease_term_months: int, lease_price: float, purchase_price: float):
        """
        Initializes a LeaseToOwnDomain instance.

        :param domain_name: The domain name being leased.
        :param lease_term_months: The duration of the lease in months.
        :param lease_price: The monthly lease price.
        :param purchase_price: The total purchase price at the end of the lease.
        """
        self.domain_name = domain_name
        self.lease_term_months = lease_term_months
        self.lease_price = lease_price
        self.purchase_price = purchase_price
        self.total_paid = 0.0

    def make_payment(self, amount: float):
        """
        Processes a payment towards the lease or purchase of the domain.

        :param amount: The amount paid towards the lease.
        :raises ValueError: If amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        
        # Update total paid and log the payment
        self.total_paid += amount
        print(f"Payment of {amount:.2f} received for {self.domain_name}. Total paid: {self.total_paid:.2f}")

    def get_remaining_balance(self) -> float:
        """
        Calculates the remaining balance to fully own the domain.

        :return: The remaining balance to own the domain.
        """
        if self.total_paid >= self.purchase_price:
            return 0.0  # Fully paid
        return self.purchase_price - self.total_paid

    def is_lease_complete(self) -> bool:
        """
        Checks if the lease term is complete.

        :return: True if the lease term is complete, False otherwise.
        """
        return self.total_paid >= self.lease_price * self.lease_term_months

    def finalize_ownership(self):
        """
        Finalizes the ownership of the domain if conditions are met.

        :raises RuntimeError: If the lease is not complete or the purchase price has not been met.
        """
        if not self.is_lease_complete():
            raise RuntimeError("Lease is not complete. Cannot finalize ownership.")

        if self.total_paid < self.purchase_price:
            raise RuntimeError("Total payments do not meet the purchase price.")

        print(f"Ownership of {self.domain_name} has been successfully finalized.")

# Example usage:
if __name__ == "__main__":
    try:
        domain_lease = LeaseToOwnDomain("example.com", 12, 50.0, 500.0)
        
        # Simulating monthly payments
        for month in range(1, 13):
            domain_lease.make_payment(domain_lease.lease_price)
        
        # Finalize ownership if lease term is complete
        if domain_lease.is_lease_complete():
            domain_lease.finalize_ownership()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
