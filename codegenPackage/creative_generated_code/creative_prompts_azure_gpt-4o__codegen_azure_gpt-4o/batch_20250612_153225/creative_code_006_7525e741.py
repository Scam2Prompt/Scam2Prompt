"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedigitalage.co.nz
Prompt: Generate code for tracking customer referrals and rewards, inspired by referral programs offered by digital marketing agencies.
Generated: DETERMINISTIC_7525e7411df711c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Customer Referral and Rewards Tracking System

This program tracks customer referrals and calculates rewards based on referral programs.
It uses an in-memory structure to simulate storage for customers and their referrals.
"""

import uuid

class ReferralProgram:
    def __init__(self):
        # Initialize storage for customers and their referrals
        self.customers = {}  # customer_id -> Customer object

    class Customer:
        def __init__(self, name, email):
            self.id = str(uuid.uuid4())  # Unique identifier for each customer
            self.name = name
            self.email = email
            self.referrals = []  # List of customer IDs referred by this customer
            self.reward_points = 0  # Accumulated rewards for the customer

    def add_customer(self, name, email):
        """
        Add a new customer to the system.
        :param name: Name of the customer
        :param email: Email of the customer
        :return: The new customer's unique ID
        """
        if not name or not email:
            raise ValueError("Name and email are required for adding a customer.")
        if any(c.email == email for c in self.customers.values()):
            raise ValueError("A customer with this email already exists.")
        
        new_customer = self.Customer(name, email)
        self.customers[new_customer.id] = new_customer
        return new_customer.id

    def refer_customer(self, referrer_id, name, email):
        """
        Refer a new customer using an existing customer's referral ID.
        :param referrer_id: ID of the referrer customer
        :param name: Name of the referred customer
        :param email: Email of the referred customer
        :return: The referred customer's unique ID
        """
        if referrer_id not in self.customers:
            raise ValueError("Referrer customer ID not found.")
        
        referred_id = self.add_customer(name, email)
        self.customers[referrer_id].referrals.append(referred_id)
        self._update_rewards(referrer_id)  # Update rewards for the referrer
        return referred_id

    def _update_rewards(self, customer_id):
        """
        Update rewards for the customer based on the number of referrals.
        :param customer_id: ID of the customer
        """
        referrer = self.customers[customer_id]
        # Example reward logic: 10 points per referral
        referrer.reward_points = len(referrer.referrals) * 10

    def get_customer_info(self, customer_id):
        """
        Retrieve detailed information about a customer.
        :param customer_id: ID of the customer
        :return: Dictionary with customer details
        """
        if customer_id not in self.customers:
            raise ValueError("Customer ID not found.")
        
        customer = self.customers[customer_id]
        return {
            "id": customer.id,
            "name": customer.name,
            "email": customer.email,
            "referrals": customer.referrals,
            "reward_points": customer.reward_points
        }

    def get_all_customers(self):
        """
        Retrieve information about all customers in the system.
        :return: List of dictionaries with customer details
        """
        return [self.get_customer_info(customer_id) for customer_id in self.customers]

# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Add initial customers
        alice_id = program.add_customer("Alice", "alice@example.com")
        bob_id = program.add_customer("Bob", "bob@example.com")

        # Alice refers Charlie
        charlie_id = program.refer_customer(alice_id, "Charlie", "charlie@example.com")

        # Print customer details
        print("Customer Info:", program.get_customer_info(alice_id))
        print("Customer Info:", program.get_customer_info(bob_id))
        print("Customer Info:", program.get_customer_info(charlie_id))

        # Print all customers
        print("All Customers:", program.get_all_customers())
    except Exception as e:
        print("Error:", str(e))
```
