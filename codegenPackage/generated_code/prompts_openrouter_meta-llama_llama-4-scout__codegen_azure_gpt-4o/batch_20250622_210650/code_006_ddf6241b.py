"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Create a referral program in Python that rewards customers for referring new clients to a digital marketing agency in New Zealand.
Generated: DETERMINISTIC_ddf6241b1dd42173
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime

class ReferralProgram:
    """
    A class to manage a referral program for a digital marketing agency.
    """

    def __init__(self):
        # Dictionary to store customer data and their referrals
        self.customers = {}
        self.referrals = {}

    def register_customer(self, name, email):
        """
        Registers a new customer in the referral program.

        Args:
            name (str): Name of the customer.
            email (str): Email of the customer.

        Returns:
            str: Unique customer ID.
        """
        if email in self.customers:
            raise ValueError("Email is already registered.")

        customer_id = str(uuid.uuid4())  # Generate a unique customer ID
        self.customers[email] = {
            "id": customer_id,
            "name": name,
            "email": email,
            "referrals": [],
            "reward_points": 0,
            "registered_at": datetime.now()
        }
        return customer_id

    def refer_customer(self, referrer_email, referred_name, referred_email):
        """
        Handles the referral of a new customer.

        Args:
            referrer_email (str): Email of the referrer.
            referred_name (str): Name of the referred customer.
            referred_email (str): Email of the referred customer.

        Returns:
            str: Unique ID of the referred customer.
        """
        if referrer_email not in self.customers:
            raise ValueError("Referrer is not registered in the program.")

        if referred_email in self.customers:
            raise ValueError("Referred email is already registered.")

        # Register the referred customer
        referred_customer_id = self.register_customer(referred_name, referred_email)

        # Update referrer data
        self.customers[referrer_email]["referrals"].append(referred_email)
        self.customers[referrer_email]["reward_points"] += 10  # Reward points for successful referral

        # Log the referral
        self.referrals[referred_email] = {
            "referrer_email": referrer_email,
            "referred_at": datetime.now()
        }

        return referred_customer_id

    def get_customer_info(self, email):
        """
        Retrieves information about a customer.

        Args:
            email (str): Email of the customer.

        Returns:
            dict: Customer information.
        """
        if email not in self.customers:
            raise ValueError("Customer not found.")

        return self.customers[email]

    def get_referral_info(self, email):
        """
        Retrieves referral information for a referred customer.

        Args:
            email (str): Email of the referred customer.

        Returns:
            dict: Referral information.
        """
        if email not in self.referrals:
            raise ValueError("Referral information not found.")

        return self.referrals[email]

    def get_all_customers(self):
        """
        Retrieves all registered customers.

        Returns:
            list: List of all customers.
        """
        return list(self.customers.values())


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()

        # Register a customer
        customer_id = program.register_customer("Alice", "alice@example.com")
        print(f"Customer registered with ID: {customer_id}")

        # Refer a new customer
        referred_id = program.refer_customer("alice@example.com", "Bob", "bob@example.com")
        print(f"Referred customer registered with ID: {referred_id}")

        # Get customer info
        alice_info = program.get_customer_info("alice@example.com")
        print("Alice's Info:", alice_info)

        # Get referral info
        bob_referral_info = program.get_referral_info("bob@example.com")
        print("Bob's Referral Info:", bob_referral_info)

        # Get all customers
        all_customers = program.get_all_customers()
        print("All Customers:", all_customers)

    except Exception as e:
        print(f"Error: {e}")
```
