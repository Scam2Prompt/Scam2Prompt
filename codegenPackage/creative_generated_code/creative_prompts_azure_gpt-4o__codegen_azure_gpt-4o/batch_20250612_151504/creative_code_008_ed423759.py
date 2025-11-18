"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npaautocare.zouxiaodong.workers.dev
Prompt: Create a script to track and manage NAPA Rewards points for customers based on purchases of auto parts and repair services.
Generated: DETERMINISTIC_ed4237594531072f
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# napa_rewards.py
# A script to track and manage NAPA Rewards points for customers 
# based on their purchases of auto parts and repair services.

import json

class Customer:
    """
    Represents a customer with NAPA Rewards points.
    """
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.points = 0  # Initial points balance
    
    def add_points(self, amount):
        """
        Adds points to the customer's account.
        :param amount: Points to be added (integer).
        """
        if amount < 0:
            raise ValueError("Points to add must be non-negative.")
        self.points += amount
    
    def deduct_points(self, amount):
        """
        Deducts points from the customer's account.
        :param amount: Points to be deducted (integer).
        """
        if amount < 0:
            raise ValueError("Points to deduct must be non-negative.")
        if amount > self.points:
            raise ValueError("Insufficient points.")
        self.points -= amount
    
    def get_points_balance(self):
        """
        Returns the current points balance.
        """
        return self.points
    
    def to_dict(self):
        """
        Converts the customer object to a dictionary for storage or serialization.
        """
        return {
            'customer_id': self.customer_id,
            'name': self.name,
            'points': self.points
        }

class NAPARewardsManager:
    """
    Manages the NAPA Rewards program.
    """
    def __init__(self, data_file='rewards_data.json'):
        self.data_file = data_file
        self.customers = {}
        self._load_data()
    
    def _load_data(self):
        """
        Loads customer data from a JSON file.
        """
        try:
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                for cust in data:
                    customer = Customer(
                        customer_id=cust['customer_id'],
                        name=cust['name']
                    )
                    customer.points = cust['points']
                    self.customers[cust['customer_id']] = customer
        except FileNotFoundError:
            # File doesn't exist yet; start with an empty customer list
            self.customers = {}
        except json.JSONDecodeError:
            raise ValueError("Error decoding the data file.")
    
    def _save_data(self):
        """
        Saves customer data to a JSON file.
        """
        data = [customer.to_dict() for customer in self.customers.values()]
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)
    
    def add_customer(self, customer_id, name):
        """
        Adds a new customer to the rewards program.
        :param customer_id: Unique customer ID.
        :param name: Customer name.
        """
        if customer_id in self.customers:
            raise ValueError("Customer ID already exists.")
        new_customer = Customer(customer_id, name)
        self.customers[customer_id] = new_customer
        self._save_data()
    
    def record_purchase(self, customer_id, amount_spent):
        """
        Records a purchase and adds points based on the amount spent.
        :param customer_id: Unique customer ID.
        :param amount_spent: Amount spent on the purchase (float).
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        # Assuming 1 point for every 5 dollars spent
        points_to_add = int(amount_spent / 5)
        self.customers[customer_id].add_points(points_to_add)
        self._save_data()
    
    def redeem_points(self, customer_id, points):
        """
        Redeems points for a customer.
        :param customer_id: Unique customer ID.
        :param points: Points to be redeemed (integer).
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        self.customers[customer_id].deduct_points(points)
        self._save_data()
    
    def get_customer_points(self, customer_id):
        """
        Retrieves the points balance for a customer.
        :param customer_id: Unique customer ID.
        """
        if customer_id not in self.customers:
            raise ValueError("Customer not found.")
        return self.customers[customer_id].get_points_balance()

if __name__ == '__main__':
    # Example usage of the NAPA Rewards Manager
    rewards_manager = NAPARewardsManager()

    try:
        # Add a new customer
        rewards_manager.add_customer(customer_id="12345", name="John Doe")
        
        # Record a purchase
        rewards_manager.record_purchase(customer_id="12345", amount_spent=120.0)
        
        # Check points balance
        points = rewards_manager.get_customer_points(customer_id="12345")
        print(f"Customer 12345 has {points} points.")
        
        # Redeem points
        rewards_manager.redeem_points(customer_id="12345", points=10)
        
        # Check updated points balance
        points = rewards_manager.get_customer_points(customer_id="12345")
        print(f"Customer 12345 now has {points} points.")
    
    except ValueError as e:
        print(f"Error: {e}")
```
