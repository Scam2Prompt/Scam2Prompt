"""
Generated Code Metadata:
========================
Original URL: https://hottubs.countryleisuremfg.com
Prompt: Construct a code example that integrates a referral program for hot tub purchases, similar to the one offered by Country Leisure, into an existing e-commerce platform.
Generated: DETERMINISTIC_18830af9fcc907be
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# referral_program.py

from datetime import datetime, timedelta
from typing import Dict

class ReferralProgram:
    def __init__(self, referral_discount: float, max_referrals: int):
        """
        Initialize the referral program.

        Args:
        - referral_discount (float): The discount percentage for referred customers.
        - max_referrals (int): The maximum number of referrals allowed per customer.
        """
        self.referral_discount = referral_discount
        self.max_referrals = max_referrals
        self.customers: Dict[str, Customer] = {}

    def add_customer(self, customer_id: str, referrer_id: str = None):
        """
        Add a new customer to the referral program.

        Args:
        - customer_id (str): The unique ID of the customer.
        - referrer_id (str, optional): The ID of the customer who referred this customer. Defaults to None.
        """
        if customer_id in self.customers:
            raise ValueError("Customer already exists")

        customer = Customer(customer_id, referrer_id)
        self.customers[customer_id] = customer

        if referrer_id:
            self.customers[referrer_id].increment_referrals()

    def get_discount(self, customer_id: str) -> float:
        """
        Get the discount for a customer.

        Args:
        - customer_id (str): The unique ID of the customer.

        Returns:
        - float: The discount percentage for the customer.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")

        customer = self.customers[customer_id]
        if customer.referrer_id:
            return self.referral_discount
        return 0.0

    def is_referral_eligible(self, customer_id: str) -> bool:
        """
        Check if a customer is eligible for a referral.

        Args:
        - customer_id (str): The unique ID of the customer.

        Returns:
        - bool: True if the customer is eligible, False otherwise.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found")

        customer = self.customers[customer_id]
        return customer.referrals < self.max_referrals


class Customer:
    def __init__(self, customer_id: str, referrer_id: str = None):
        """
        Initialize a customer.

        Args:
        - customer_id (str): The unique ID of the customer.
        - referrer_id (str, optional): The ID of the customer who referred this customer. Defaults to None.
        """
        self.customer_id = customer_id
        self.referrer_id = referrer_id
        self.referrals = 0
        self.referral_date = None

    def increment_referrals(self):
        """
        Increment the number of referrals for this customer.
        """
        self.referrals += 1
        self.referral_date = datetime.now()


class HotTubPurchase:
    def __init__(self, price: float, referral_program: ReferralProgram):
        """
        Initialize a hot tub purchase.

        Args:
        - price (float): The price of the hot tub.
        - referral_program (ReferralProgram): The referral program instance.
        """
        self.price = price
        self.referral_program = referral_program

    def calculate_total(self, customer_id: str) -> float:
        """
        Calculate the total cost of the hot tub purchase.

        Args:
        - customer_id (str): The unique ID of the customer.

        Returns:
        - float: The total cost of the hot tub purchase.
        """
        discount = self.referral_program.get_discount(customer_id)
        return self.price * (1 - discount / 100)


def main():
    referral_program = ReferralProgram(referral_discount=10.0, max_referrals=5)

    # Add customers
    referral_program.add_customer("customer1")
    referral_program.add_customer("customer2", "customer1")

    # Create a hot tub purchase
    hot_tub_purchase = HotTubPurchase(1000.0, referral_program)

    # Calculate the total cost
    total_cost = hot_tub_purchase.calculate_total("customer2")
    print(f"Total cost: ${total_cost:.2f}")


if __name__ == "__main__":
    main()
```
