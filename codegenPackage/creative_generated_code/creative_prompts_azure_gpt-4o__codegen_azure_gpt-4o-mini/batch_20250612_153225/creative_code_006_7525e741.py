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
class Customer:
    """Class representing a customer in the referral program."""
    
    def __init__(self, customer_id, name):
        """Initialize a new customer with an ID and name."""
        self.customer_id = customer_id
        self.name = name
        self.referrals = []  # List to store referred customers
        self.rewards = 0  # Rewards earned by the customer

    def refer(self, referred_customer):
        """
        Add a referred customer to the customer's referral list.
        
        Args:
            referred_customer (Customer): The customer being referred.
        """
        if isinstance(referred_customer, Customer):
            self.referrals.append(referred_customer)
            self.update_rewards()
        else:
            raise ValueError("Referred customer must be an instance of Customer.")

    def update_rewards(self):
        """Update rewards based on the number of referrals."""
        # Assuming a reward of 10 for each successful referral
        self.rewards = len(self.referrals) * 10

    def __str__(self):
        """String representation of the customer."""
        return f"Customer({self.customer_id}, {self.name}, Referrals: {len(self.referrals)}, Rewards: {self.rewards})"


class ReferralProgram:
    """Class to manage the referral program."""
    
    def __init__(self):
        """Initialize the referral program."""
        self.customers = {}  # Dictionary to store customers by ID

    def add_customer(self, customer):
        """
        Add a customer to the referral program.
        
        Args:
            customer (Customer): The customer to add.
        """
        if not isinstance(customer, Customer):
            raise ValueError("Customer must be an instance of Customer.")
        
        if customer.customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        
        self.customers[customer.customer_id] = customer

    def refer_customer(self, referrer_id, referred_customer):
        """
        Process the referral of a new customer by an existing customer.
        
        Args:
            referrer_id (str): The ID of the referrer.
            referred_customer (Customer): The customer being referred.
        """
        if referrer_id not in self.customers:
            raise ValueError("Referrer not found.")
        
        self.customers[referrer_id].refer(referred_customer)
        self.add_customer(referred_customer)

    def get_customer_info(self, customer_id):
        """
        Get information about a customer.
        
        Args:
            customer_id (str): The ID of the customer.
        
        Returns:
            str: Information about the customer.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        
        return str(self.customers[customer_id])


# Example usage
if __name__ == "__main__":
    try:
        program = ReferralProgram()
        
        # Create customers
        customer1 = Customer("C001", "Alice")
        customer2 = Customer("C002", "Bob")
        
        # Add customers to the program
        program.add_customer(customer1)
        program.add_customer(customer2)

        # Refer a new customer
        customer3 = Customer("C003", "Charlie")
        program.refer_customer("C001", customer3)  # Alice refers Charlie
        
        # Print customer information
        print(program.get_customer_info("C001"))
        print(program.get_customer_info("C002"))
        print(program.get_customer_info("C003"))

    except ValueError as e:
        print(f"Error: {e}")
```
