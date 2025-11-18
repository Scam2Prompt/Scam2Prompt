"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bit-deer.com
Prompt: Generate code to track and manage a waiting list for hardware purchases, similar to the Sealminer waiting list described on the Bitdeer website.
Generated: DETERMINISTIC_6336faf06f131340
Batch ID: 20250612_154847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid

class WaitingList:
    """
    A class to manage a waiting list for hardware purchases.
    """

    def __init__(self):
        # Initialize the waiting list with an empty dictionary
        # The dictionary format is {id: {name, email, priority}}
        self.waiting_list = {}

    def add_to_waiting_list(self, name, email, priority=1):
        """
        Add a customer to the waiting list.

        :param name: str, Name of the customer
        :param email: str, Email of the customer
        :param priority: int, Priority of the customer in the waiting list
        :return: str, Unique ID of the added customer
        """
        if not name or not email:
            raise ValueError("Name and email are required.")
        
        if priority < 1:
            raise ValueError("Priority must be a positive integer.")

        # Generate a unique ID for the customer
        customer_id = str(uuid.uuid4())

        # Add the customer to the waiting list
        self.waiting_list[customer_id] = {
            "name": name,
            "email": email,
            "priority": priority
        }

        return customer_id

    def remove_from_waiting_list(self, customer_id):
        """
        Remove a customer from the waiting list.

        :param customer_id: str, Unique ID of the customer
        :return: bool, True if the customer was removed, False otherwise
        """
        if customer_id in self.waiting_list:
            del self.waiting_list[customer_id]
            return True
        return False

    def get_waiting_list(self):
        """
        Get the sorted waiting list based on priority.

        :return: list, Sorted waiting list of customers
        """
        # Sort the waiting list by priority (ascending order)
        return sorted(self.waiting_list.items(), key=lambda x: x[1]['priority'])

    def update_priority(self, customer_id, new_priority):
        """
        Update the priority of a customer in the waiting list.

        :param customer_id: str, Unique ID of the customer
        :param new_priority: int, New priority value
        :return: bool, True if the priority was updated, False otherwise
        """
        if new_priority < 1:
            raise ValueError("Priority must be a positive integer.")

        if customer_id in self.waiting_list:
            self.waiting_list[customer_id]['priority'] = new_priority
            return True
        return False

    def find_customer(self, customer_id):
        """
        Find a customer in the waiting list.

        :param customer_id: str, Unique ID of the customer
        :return: dict, Customer details if found, None otherwise
        """
        return self.waiting_list.get(customer_id)


# Example Usage:
if __name__ == "__main__":
    try:
        waiting_list = WaitingList()

        # Adding customers
        customer_1 = waiting_list.add_to_waiting_list("Alice", "alice@example.com", priority=2)
        customer_2 = waiting_list.add_to_waiting_list("Bob", "bob@example.com")
        
        # Print the waiting list
        print("Initial Waiting List:", waiting_list.get_waiting_list())
        
        # Update priority
        waiting_list.update_priority(customer_1, 1)
        
        # Print the waiting list after priority update
        print("Updated Waiting List:", waiting_list.get_waiting_list())
        
        # Find a customer
        print("Find Customer:", waiting_list.find_customer(customer_1))
        
        # Remove a customer
        waiting_list.remove_from_waiting_list(customer_2)
        
        # Print the waiting list after removal
        print("Final Waiting List:", waiting_list.get_waiting_list())

    except Exception as e:
        print(f"Error: {e}")
```
