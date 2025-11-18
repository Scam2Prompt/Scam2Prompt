"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blueraygroup.com
Prompt: Provide a step-by-step guide to integrate door-to-door delivery functionality into a logistics management system, similar to the services offered by Blue Ray Logistic.
Generated: DETERMINISTIC_773682cf308c686a
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# logistics_management.py

class Delivery:
    """Represents a delivery in the logistics management system."""

    def __init__(self, order_id, delivery_address, recipient_name):
        """
        Initialize a new delivery.

        :param order_id: Unique identifier for the order.
        :param delivery_address: The address where the order should be delivered.
        :param recipient_name: Name of the person receiving the delivery.
        """
        self.order_id = order_id
        self.delivery_address = delivery_address
        self.recipient_name = recipient_name
        self.status = 'Pending'  # Status of the delivery

    def update_status(self, new_status):
        """
        Update the delivery status.

        :param new_status: New status of the delivery.
        """
        valid_statuses = ['Pending', 'In Transit', 'Delivered', 'Cancelled']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")


class LogisticsManagementSystem:
    """Manages the logistics operations including deliveries."""

    def __init__(self):
        """Initialize the logistics management system with empty deliveries."""
        self.deliveries = {}

    def add_delivery(self, order_id, delivery_address, recipient_name):
        """
        Add a new delivery to the system.

        :param order_id: Unique identifier for the order.
        :param delivery_address: The address for delivery.
        :param recipient_name: Name of the recipient.
        :raises ValueError: If the order_id already exists.
        """
        if order_id in self.deliveries:
            raise ValueError(f"Delivery with order_id {order_id} already exists.")
        
        new_delivery = Delivery(order_id, delivery_address, recipient_name)
        self.deliveries[order_id] = new_delivery

    def update_delivery_status(self, order_id, new_status):
        """
        Update the status of a delivery.

        :param order_id: Unique identifier for the order.
        :param new_status: New status to set for the delivery.
        :raises KeyError: If the order_id does not exist.
        """
        if order_id not in self.deliveries:
            raise KeyError(f"No delivery found with order_id {order_id}.")
        
        delivery = self.deliveries[order_id]
        delivery.update_status(new_status)

    def get_delivery_status(self, order_id):
        """
        Get the current status of a delivery.

        :param order_id: Unique identifier for the order.
        :return: The current status of the delivery.
        :raises KeyError: If the order_id does not exist.
        """
        if order_id not in self.deliveries:
            raise KeyError(f"No delivery found with order_id {order_id}.")
        
        return self.deliveries[order_id].status


# Example usage
if __name__ == "__main__":
    logistics_system = LogisticsManagementSystem()
    
    # Adding a new delivery
    try:
        logistics_system.add_delivery('ORD123', '123 Elm St, Springfield', 'John Doe')
        print("Delivery added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Updating delivery status
    try:
        logistics_system.update_delivery_status('ORD123', 'In Transit')
        print("Delivery status updated successfully.")
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")

    # Retrieving delivery status
    try:
        status = logistics_system.get_delivery_status('ORD123')
        print(f"Current delivery status: {status}")
    except KeyError as e:
        print(f"Error: {e}")
```
