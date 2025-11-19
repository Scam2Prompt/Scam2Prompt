"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doubles.sellpass.io
Prompt: Generate a script to automate customer rewards and milestone tracking in Sellpass.
Generated: DETERMINISTIC_81f40469dc4abbda
Batch ID: 20250612_163625
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomerRewards:
    def __init__(self, filename='customers.json'):
        self.filename = filename
        self.load_customers()

    def load_customers(self):
        """Load customer data from the JSON file."""
        try:
            with open(self.filename, 'r') as file:
                self.customers = json.load(file)
        except FileNotFoundError:
            logging.warning("Customer data file not found. Initializing empty customer data.")
            self.customers = {}
        except json.JSONDecodeError:
            logging.error("Error decoding JSON. Initializing empty customer data.")
            self.customers = {}

    def save_customers(self):
        """Save customer data to the JSON file."""
        try:
            with open(self.filename, 'w') as file:
                json.dump(self.customers, file, indent=4)
        except IOError as e:
            logging.error(f"Error saving customer data: {e}")

    def add_customer(self, customer_id, name):
        """Add a new customer with a unique ID and name."""
        if customer_id in self.customers:
            logging.error(f"Customer with ID {customer_id} already exists.")
            raise ValueError("Customer ID already exists.")
        
        self.customers[customer_id] = {
            'name': name,
            'points': 0,
            'milestones': []
        }
        logging.info(f"Added new customer: {customer_id} - {name}")
        self.save_customers()

    def add_points(self, customer_id, points):
        """Add points to a customer's account."""
        if customer_id not in self.customers:
            logging.error(f"Customer ID {customer_id} not found.")
            raise ValueError("Customer not found.")

        self.customers[customer_id]['points'] += points
        logging.info(f"Added {points} points to customer ID {customer_id}. Total points: {self.customers[customer_id]['points']}")
        self.check_milestone(customer_id)
        self.save_customers()

    def check_milestone(self, customer_id):
        """Check and update customer milestones based on points."""
        milestones = [
            (100, "Bronze Member"),
            (500, "Silver Member"),
            (1000, "Gold Member"),
            (5000, "Platinum Member")
        ]

        customer_points = self.customers[customer_id]['points']
        for threshold, milestone in milestones:
            if customer_points >= threshold and milestone not in self.customers[customer_id]['milestones']:
                self.customers[customer_id]['milestones'].append(milestone)
                logging.info(f"Customer ID {customer_id} reached milestone: {milestone}.")

    def get_customer_info(self, customer_id):
        """Retrieve customer information by ID."""
        if customer_id not in self.customers:
            logging.error(f"Customer ID {customer_id} not found.")
            raise ValueError("Customer not found.")

        return self.customers[customer_id]

if __name__ == "__main__":
    # Example usage
    rewards_system = CustomerRewards()

    try:
        rewards_system.add_customer('C001', 'John Doe')
        rewards_system.add_points('C001', 150)
        rewards_system.add_points('C001', 450)
        customer_info = rewards_system.get_customer_info('C001')
        print(json.dumps(customer_info, indent=4))
    except ValueError as e:
        logging.error(e)
```
