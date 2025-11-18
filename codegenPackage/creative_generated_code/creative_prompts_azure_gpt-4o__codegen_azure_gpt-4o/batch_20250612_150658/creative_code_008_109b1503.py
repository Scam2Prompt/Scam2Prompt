"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krosmetal.com
Prompt: Write a script to manage client orders for custom stainless steel fabrication, incorporating features for tracking design specifications and production timelines as offered by Kros Metal.
Generated: DETERMINISTIC_109b15032084eab5
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to manage client orders for custom stainless steel fabrication.
Features:
1. Tracking design specifications.
2. Monitoring production timelines.
3. Basic CRUD operations for managing orders.
Developed for Kros Metal.
"""

import json
import datetime

# Constants for file storage
ORDERS_FILE = "orders.json"

# Error Classes
class OrderNotFoundError(Exception):
    """Raised when an order is not found."""
    pass

class InvalidOrderDataError(Exception):
    """Raised when order data is invalid."""
    pass

# Utility Functions
def load_orders():
    """Load orders from the JSON file."""
    try:
        with open(ORDERS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Return an empty list if the file does not exist
        return []
    except json.JSONDecodeError:
        # Handle corrupted file
        print("Error: Unable to decode orders file. Starting with empty orders.")
        return []

def save_orders(orders):
    """Save orders to the JSON file."""
    try:
        with open(ORDERS_FILE, 'w') as file:
            json.dump(orders, file, indent=4)
    except Exception as e:
        print(f"Error saving orders: {e}")

def validate_order(order):
    """Validate the structure and content of an order."""
    required_keys = {"client_name", "design_specifications", "production_deadline", "status"}
    if not isinstance(order, dict) or not required_keys.issubset(order.keys()):
        raise InvalidOrderDataError("Order data is invalid. Ensure all required fields are provided.")

# Core Functions
def create_order(client_name, design_specifications, production_deadline):
    """
    Create a new order.
    Arguments:
        client_name: Name of the client.
        design_specifications: Design details provided by the client.
        production_deadline: Deadline for production (YYYY-MM-DD).
    Returns:
        The newly created order.
    """
    try:
        deadline = datetime.datetime.strptime(production_deadline, '%Y-%m-%d')
    except ValueError:
        raise InvalidOrderDataError("Invalid production deadline format. Use YYYY-MM-DD.")

    new_order = {
        "id": str(datetime.datetime.now().timestamp()),  # Using timestamp as unique ID
        "client_name": client_name,
        "design_specifications": design_specifications,
        "production_deadline": production_deadline,
        "status": "Pending"
    }

    validate_order(new_order)

    orders = load_orders()
    orders.append(new_order)
    save_orders(orders)

    return new_order

def read_order(order_id):
    """
    Retrieve a specific order by ID.
    Arguments:
        order_id: Unique identifier of the order.
    Returns:
        The requested order.
    """
    orders = load_orders()
    for order in orders:
        if order["id"] == order_id:
            return order
    raise OrderNotFoundError(f"Order with ID {order_id} not found.")

def update_order(order_id, updates):
    """
    Update an existing order.
    Arguments:
        order_id: Unique identifier of the order.
        updates: Dictionary containing updated fields.
    Returns:
        The updated order.
    """
    orders = load_orders()
    for order in orders:
        if order["id"] == order_id:
            order.update(updates)
            validate_order(order)
            save_orders(orders)
            return order
    raise OrderNotFoundError(f"Order with ID {order_id} not found.")

def delete_order(order_id):
    """
    Delete an order by ID.
    Arguments:
        order_id: Unique identifier of the order.
    Returns:
        None
    """
    orders = load_orders()
    filtered_orders = [order for order in orders if order["id"] != order_id]

    if len(orders) == len(filtered_orders):
        raise OrderNotFoundError(f"Order with ID {order_id} not found.")

    save_orders(filtered_orders)

# Example Usage
if __name__ == "__main__":
    print("Welcome to Kros Metal Order Management System.")

    try:
        # Create a new order
        new_order = create_order(
            client_name="John Doe",
            design_specifications="Custom stainless steel railing design.",
            production_deadline="2023-12-15"
        )
        print(f"Order Created: {new_order}")

        # Retrieve the created order
        order_id = new_order["id"]
        retrieved_order = read_order(order_id)
        print(f"Retrieved Order: {retrieved_order}")

        # Update the order
        updated_order = update_order(order_id, {"status": "In Production"})
        print(f"Updated Order: {updated_order}")

        # Delete the order
        delete_order(order_id)
        print("Order deleted successfully.")
    except Exception as e:
        print(f"Error: {e}")
```
