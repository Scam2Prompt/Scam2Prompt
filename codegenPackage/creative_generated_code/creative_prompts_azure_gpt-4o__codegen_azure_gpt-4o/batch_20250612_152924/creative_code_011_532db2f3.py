"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftimus.com
Prompt: Create a Python script to manage orders for Himalayan salt licks and animal-shaped salt lamps, including options for bulk purchasing and custom packaging.
Generated: DETERMINISTIC_532db2f3f6978980
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid


class OrderManager:
    """
    A class to manage orders for Himalayan salt products.
    Supports bulk purchasing and custom packaging options.
    """

    def __init__(self):
        # Dictionary to store orders with unique IDs
        self.orders = {}

    def create_order(self, customer_name, product_type, quantity, bulk_purchase=False, custom_packaging=False):
        """
        Create a new order with the provided details.
        
        Parameters:
            customer_name (str): Name of the customer placing the order.
            product_type (str): Type of product ('salt lick' or 'salt lamp').
            quantity (int): Number of items ordered.
            bulk_purchase (bool): True if bulk purchase discount applies, default is False.
            custom_packaging (bool): True if custom packaging is required, default is False.
        
        Returns:
            str: Unique order ID.
        """
        # Validate inputs
        if product_type not in ['salt lick', 'salt lamp']:
            raise ValueError("Invalid product type. Must be 'salt lick' or 'salt lamp'.")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        # Generate a unique order ID
        order_id = str(uuid.uuid4())
        
        # Create an order dictionary
        order = {
            "customer_name": customer_name,
            "product_type": product_type,
            "quantity": quantity,
            "bulk_purchase": bulk_purchase,
            "custom_packaging": custom_packaging
        }
        
        # Save the order in the orders dictionary
        self.orders[order_id] = order
        
        return order_id

    def get_order(self, order_id):
        """
        Retrieve an order by its ID.
        
        Parameters:
            order_id (str): Unique ID of the order.
        
        Returns:
            dict: Order details or None if not found.
        """
        return self.orders.get(order_id)

    def update_order(self, order_id, **kwargs):
        """
        Update an existing order with new details.

        Parameters:
            order_id (str): Unique ID of the order.
            kwargs (dict): Attributes to update (e.g., quantity, product_type, bulk_purchase, custom_packaging).
        
        Returns:
            bool: True if the order was updated successfully, False otherwise.
        """
        order = self.orders.get(order_id)
        
        if not order:
            return False
        
        # Update the order with provided attributes
        for key, value in kwargs.items():
            if key in order:
                order[key] = value
        return True

    def delete_order(self, order_id):
        """
        Delete an order by its ID.

        Parameters:
            order_id (str): Unique ID of the order.
        
        Returns:
            bool: True if the order was deleted successfully, False otherwise.
        """
        if order_id in self.orders:
            del self.orders[order_id]
            return True
        return False

    def list_orders(self):
        """
        List all orders.

        Returns:
            dict: Dictionary of all orders with their IDs and details.
        """
        return self.orders


# Example usage
if __name__ == "__main__":
    try:
        manager = OrderManager()

        # Create orders
        order1_id = manager.create_order(
            customer_name="Alice",
            product_type="salt lick",
            quantity=5,
            bulk_purchase=True,
            custom_packaging=False
        )
        order2_id = manager.create_order(
            customer_name="Bob",
            product_type="salt lamp",
            quantity=2,
            bulk_purchase=False,
            custom_packaging=True
        )

        # List all orders
        print("All Orders:")
        print(manager.list_orders())

        # Retrieve an order
        print("\nRetrieve Order:")
        print(manager.get_order(order1_id))

        # Update an order
        manager.update_order(order1_id, quantity=10, custom_packaging=True)
        print("\nUpdated Order:")
        print(manager.get_order(order1_id))

        # Delete an order
        manager.delete_order(order2_id)
        print("\nAll Orders After Deletion:")
        print(manager.list_orders())
    except Exception as e:
        print(f"Error: {e}")
```
