"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a code snippet that automates the selection and ordering process for PU golf grips based on the workflow provided by Longhui Golf.
Generated: DETERMINISTIC_39410fd824547958
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class GolfGripOrderAutomation:
    """
    A class to automate the selection and ordering process for PU golf grips.
    """

    def __init__(self):
        # Initialize available grips and inventory
        self.available_grips = {
            "Standard": {"price": 10.99, "stock": 100},
            "Midsize": {"price": 12.99, "stock": 50},
            "Oversize": {"price": 14.99, "stock": 30}
        }
        self.order = []

    def display_available_grips(self):
        """
        Display the available grips with their prices and stock.
        """
        print("Available PU Golf Grips:")
        for grip, details in self.available_grips.items():
            print(f"{grip}: ${details['price']} (Stock: {details['stock']})")

    def select_grip(self, grip_type, quantity):
        """
        Select a grip type and quantity to add to the order.

        :param grip_type: The type of grip to order (e.g., "Standard").
        :param quantity: The number of grips to order.
        :raises ValueError: If the grip type is invalid or stock is insufficient.
        """
        if grip_type not in self.available_grips:
            raise ValueError(f"Invalid grip type: {grip_type}")
        
        grip_details = self.available_grips[grip_type]
        if quantity > grip_details["stock"]:
            raise ValueError(f"Insufficient stock for {grip_type}. Available: {grip_details['stock']}")
        
        # Add to order and reduce stock
        self.order.append({"grip_type": grip_type, "quantity": quantity, "price": grip_details["price"]})
        grip_details["stock"] -= quantity
        print(f"Added {quantity} {grip_type} grip(s) to the order.")

    def calculate_total(self):
        """
        Calculate the total cost of the order.

        :return: The total cost as a float.
        """
        return sum(item["quantity"] * item["price"] for item in self.order)

    def finalize_order(self):
        """
        Finalize the order and display the summary.

        :return: A JSON string containing the order summary.
        """
        if not self.order:
            raise ValueError("No items in the order to finalize.")
        
        total_cost = self.calculate_total()
        order_summary = {
            "order": self.order,
            "total_cost": total_cost
        }
        print("Order Summary:")
        print(json.dumps(order_summary, indent=4))
        return json.dumps(order_summary)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the automation system
        golf_grip_order = GolfGripOrderAutomation()
        
        # Display available grips
        golf_grip_order.display_available_grips()
        
        # Select grips
        golf_grip_order.select_grip("Standard", 2)
        golf_grip_order.select_grip("Midsize", 1)
        
        # Finalize and display the order
        golf_grip_order.finalize_order()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
