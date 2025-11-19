"""
Generated Code Metadata:
========================
Original URL: https://aptoslive.com
Prompt: "Write a case study on how Aptos ONE POS improved customer engagement for The North Face, including specific features and benefits."
Generated: DETERMINISTIC_531c2626d00adefb
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Aptos ONE POS Case Study: The North Face

class AptosONEPOS:
    def __init__(self, store_name):
        """
        Initialize Aptos ONE POS for a specific store.

        Args:
            store_name (str): Name of the store.
        """
        self.store_name = store_name
        self.customer_data = {}

    def customer_lookup(self, customer_id):
        """
        Retrieve customer data by ID.

        Args:
            customer_id (int): Unique customer ID.

        Returns:
            dict: Customer data if found, otherwise None.
        """
        try:
            return self.customer_data[customer_id]
        except KeyError:
            print(f"Customer {customer_id} not found.")
            return None

    def add_customer(self, customer_id, name, email):
        """
        Add a new customer to the database.

        Args:
            customer_id (int): Unique customer ID.
            name (str): Customer name.
            email (str): Customer email.

        Returns:
            bool: True if customer added successfully, otherwise False.
        """
        if customer_id in self.customer_data:
            print(f"Customer {customer_id} already exists.")
            return False
        self.customer_data[customer_id] = {"name": name, "email": email}
        return True

    def engage_customer(self, customer_id):
        """
        Engage with a customer through personalized offers.

        Args:
            customer_id (int): Unique customer ID.

        Returns:
            str: Personalized offer message if customer found, otherwise None.
        """
        customer = self.customer_lookup(customer_id)
        if customer:
            name = customer["name"]
            offer = f"Hi {name}, welcome back to {self.store_name}! Enjoy 10% off your next purchase."
            return offer
        return None


class TheNorthFace:
    def __init__(self):
        """
        Initialize The North Face store with Aptos ONE POS.
        """
        self.pos = AptosONEPOS("The North Face")

    def run_campaign(self):
        """
        Run a customer engagement campaign.

        Returns:
            None
        """
        # Add customers
        self.pos.add_customer(1, "John Doe", "john.doe@example.com")
        self.pos.add_customer(2, "Jane Smith", "jane.smith@example.com")

        # Engage with customers
        offer1 = self.pos.engage_customer(1)
        offer2 = self.pos.engage_customer(2)

        # Print results
        print(offer1)
        print(offer2)


if __name__ == "__main__":
    try:
        north_face = TheNorthFace()
        north_face.run_campaign()
    except Exception as e:
        print(f"An error occurred: {e}")
```
