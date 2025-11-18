"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Develop a program to manage customer orders for personalized promotional items, incorporating customization options like DTF printing and vinyl textile designs.
Generated: DETERMINISTIC_f5bcbc010a77c73c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from typing import List, Dict, Optional

class Order:
    """
    Represents a customer order for personalized promotional items.
    """

    def __init__(self, customer_name: str, item: str, customization_options: Dict[str, str]):
        self.order_id: str = str(uuid.uuid4())  # Unique identifier for the order
        self.customer_name: str = customer_name
        self.item: str = item
        self.customization_options: Dict[str, str] = customization_options

    def __str__(self) -> str:
        return f"Order ID: {self.order_id}, Customer: {self.customer_name}, Item: {self.item}, Customizations: {self.customization_options}"

class OrderManager:
    """
    Manages customer orders for personalized promotional items.
    """

    def __init__(self):
        self.orders: List[Order] = []

    def create_order(self, customer_name: str, item: str, customization_options: Dict[str, str]) -> Order:
        """
        Creates an order and adds it to the order list.

        Args:
            customer_name (str): Name of the customer placing the order.
            item (str): Name of the item being ordered.
            customization_options (Dict[str, str]): Customization options for the order.

        Returns:
            Order: The created order.
        """
        if not customer_name or not item:
            raise ValueError("Customer name and item must be provided.")
        
        order = Order(customer_name, item, customization_options)
        self.orders.append(order)
        return order

    def get_order(self, order_id: str) -> Optional[Order]:
        """
        Retrieves an order by its ID.

        Args:
            order_id (str): The ID of the order to retrieve.

        Returns:
            Optional[Order]: The order if found, else None.
        """
        for order in self.orders:
            if order.order_id == order_id:
                return order
        return None

    def list_orders(self) -> List[str]:
        """
        Lists all orders in string format.

        Returns:
            List[str]: A list of all orders as strings.
        """
        return [str(order) for order in self.orders]

def main():
    """
    Main function to demonstrate order management.
    """
    order_manager = OrderManager()

    try:
        # Create a sample order
        customization_options = {
            "Printing Method": "DTF",
            "Design Type": "Vinyl Textile"
        }
        order = order_manager.create_order("John Doe", "Custom T-Shirt", customization_options)
        print(f"Order Created: {order}")

        # List all orders
        print("\nCurrent Orders:")
        for order_str in order_manager.list_orders():
            print(order_str)

        # Retrieve a specific order
        retrieved_order = order_manager.get_order(order.order_id)
        if retrieved_order:
            print(f"\nRetrieved Order: {retrieved_order}")
        else:
            print("Order not found.")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
