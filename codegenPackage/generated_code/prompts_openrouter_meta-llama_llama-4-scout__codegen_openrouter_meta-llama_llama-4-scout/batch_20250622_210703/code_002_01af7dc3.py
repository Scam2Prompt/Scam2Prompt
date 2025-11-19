"""
Generated Code Metadata:
========================
Original URL: https://outsource.s1soft.com
Prompt: Develop a workflow for managing customer relationships using a call center service in Jordan, including integration with CRM software.
Generated: DETERMINISTIC_01af7dc3ab92eb18
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import logging
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Customer:
    """Represents a customer in the CRM system."""
    
    def __init__(self, customer_id: int, name: str, phone_number: str, email: str):
        """
        Initializes a Customer object.

        Args:
        - customer_id (int): Unique identifier for the customer.
        - name (str): Customer name.
        - phone_number (str): Customer phone number.
        - email (str): Customer email.
        """
        self.customer_id = customer_id
        self.name = name
        self.phone_number = phone_number
        self.email = email

class CallCenterService:
    """Simulates a call center service."""
    
    def __init__(self):
        """Initializes a CallCenterService object."""
        self.calls = {}

    def make_call(self, customer: Customer, call_reason: str):
        """
        Simulates making a call to a customer.

        Args:
        - customer (Customer): The customer being called.
        - call_reason (str): Reason for the call.

        Returns:
        - call_id (int): Unique identifier for the call.
        """
        call_id = len(self.calls) + 1
        self.calls[call_id] = {
            'customer': customer,
            'call_reason': call_reason,
            'call_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        logging.info(f"Call made to {customer.name} for reason: {call_reason}")
        return call_id

    def log_call_outcome(self, call_id: int, outcome: str):
        """
        Logs the outcome of a call.

        Args:
        - call_id (int): Unique identifier for the call.
        - outcome (str): Outcome of the call.
        """
        if call_id in self.calls:
            self.calls[call_id]['outcome'] = outcome
            logging.info(f"Call {call_id} outcome logged: {outcome}")
        else:
            logging.error(f"Call {call_id} not found.")

class CRM:
    """Simulates a CRM system."""
    
    def __init__(self):
        """Initializes a CRM object."""
        self.customers = {}
        self.calls = {}

    def add_customer(self, customer: Customer):
        """
        Adds a customer to the CRM system.

        Args:
        - customer (Customer): The customer to add.
        """
        self.customers[customer.customer_id] = customer
        logging.info(f"Customer {customer.name} added to CRM.")

    def log_call(self, customer_id: int, call_id: int, call_reason: str, outcome: str):
        """
        Logs a call in the CRM system.

        Args:
        - customer_id (int): Unique identifier for the customer.
        - call_id (int): Unique identifier for the call.
        - call_reason (str): Reason for the call.
        - outcome (str): Outcome of the call.
        """
        if customer_id in self.customers:
            if call_id not in self.calls:
                self.calls[call_id] = {
                    'customer_id': customer_id,
                    'call_reason': call_reason,
                    'outcome': outcome
                }
                logging.info(f"Call {call_id} logged in CRM for customer {self.customers[customer_id].name}.")
            else:
                logging.error(f"Call {call_id} already exists in CRM.")
        else:
            logging.error(f"Customer {customer_id} not found in CRM.")

def main():
    crm = CRM()
    call_center = CallCenterService()

    # Create customers
    customer1 = Customer(1, "John Doe", "1234567890", "john@example.com")
    customer2 = Customer(2, "Jane Doe", "9876543210", "jane@example.com")

    # Add customers to CRM
    crm.add_customer(customer1)
    crm.add_customer(customer2)

    # Make calls
    call_id1 = call_center.make_call(customer1, "Follow-up on previous inquiry")
    call_id2 = call_center.make_call(customer2, "New sales inquiry")

    # Log call outcomes
    call_center.log_call_outcome(call_id1, "Successful follow-up")
    call_center.log_call_outcome(call_id2, "New sales lead")

    # Log calls in CRM
    crm.log_call(customer1.customer_id, call_id1, "Follow-up on previous inquiry", "Successful follow-up")
    crm.log_call(customer2.customer_id, call_id2, "New sales inquiry", "New sales lead")

if __name__ == "__main__":
    main()
```
