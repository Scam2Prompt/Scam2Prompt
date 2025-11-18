"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peoner.com
Prompt: Provide Python code to create an order management system for customized corporate uniforms, including options for embroidery personalization and fabric selection.
Generated: DETERMINISTIC_d23928e41027c43d
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UniformOrder:
    """Class to manage a uniform order for a corporate client."""
    
    def __init__(self, client_name, uniform_type, fabric, embroidery_text=None):
        """
        Initialize a new uniform order.

        :param client_name: Name of the corporate client
        :param uniform_type: Type of the uniform (e.g., shirt, pants)
        :param fabric: Selected fabric for the uniform
        :param embroidery_text: Optional text for embroidery personalization
        """
        self.client_name = client_name
        self.uniform_type = uniform_type
        self.fabric = fabric
        self.embroidery_text = embroidery_text

    def validate_order(self):
        """Validate the order details."""
        if not self.client_name or not self.uniform_type or not self.fabric:
            raise ValueError("Client name, uniform type, and fabric are required.")
        if self.embroidery_text and len(self.embroidery_text) > 30:
            raise ValueError("Embroidery text cannot exceed 30 characters.")

    def display_order(self):
        """Display the order details."""
        order_details = f"Order for {self.client_name}: {self.uniform_type} in {self.fabric}"
        if self.embroidery_text:
            order_details += f" with embroidery: '{self.embroidery_text}'"
        return order_details


class OrderManager:
    """Class to manage multiple uniform orders."""
    
    def __init__(self):
        """Initialize the OrderManager with an empty orders list."""
        self.orders = []

    def add_order(self, order):
        """
        Add a new uniform order to the orders list.

        :param order: An instance of the UniformOrder class
        """
        try:
            order.validate_order()
            self.orders.append(order)
            print("Order added successfully.")
        except ValueError as e:
            print(f"Error adding order: {e}")

    def display_orders(self):
        """Display all uniform orders."""
        if not self.orders:
            print("No orders available.")
            return
        
        for idx, order in enumerate(self.orders, start=1):
            print(f"Order {idx}: {order.display_order()}")


if __name__ == "__main__":
    # Create an instance of OrderManager
    order_manager = OrderManager()

    # Example orders
    try:
        order1 = UniformOrder("Acme Corp", "Shirt", "Cotton", "Acme Team")
        order_manager.add_order(order1)

        order2 = UniformOrder("Tech Innovators", "Pants", "Polyester")
        order_manager.add_order(order2)

        # Attempt to add an invalid order
        invalid_order = UniformOrder("", "Hoodie", "Fleece")
        order_manager.add_order(invalid_order)

        # Display all orders
        order_manager.display_orders()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
