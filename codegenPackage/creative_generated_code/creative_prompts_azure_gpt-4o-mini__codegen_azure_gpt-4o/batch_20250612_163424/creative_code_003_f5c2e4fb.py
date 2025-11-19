"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lbicgroup.com
Prompt: Create a function that simulates order processing for fittings and accessories related to phase conductors and ground wires, inspired by Swamiji Transmission Pvt. Ltd.'s product offerings.
Generated: DETERMINISTIC_f5c2e4fbffa3c3e8
Batch ID: 20250612_163424
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime

class OrderProcessingError(Exception):
    """Custom exception for order processing errors."""
    pass

def process_order(customer_name, products):
    """
    Simulates the processing of an order for fittings and accessories 
    related to phase conductors and ground wires.

    Args:
        customer_name (str): Name of the customer placing the order.
        products (list): List of product dictionaries containing 'name', 'quantity', and 'price'.

    Returns:
        dict: A dictionary containing order details including order ID, customer name, 
              products, total amount, and order timestamp.

    Raises:
        OrderProcessingError: If input data is invalid or any processing error occurs.
    """
    try:
        # Validate input
        if not customer_name or not isinstance(customer_name, str):
            raise ValueError("Customer name must be a non-empty string.")
        
        if not products or not isinstance(products, list):
            raise ValueError("Products must be a list of dictionaries.")
        
        if not all(isinstance(product, dict) and 'name' in product and 'quantity' in product and 'price' in product for product in products):
            raise ValueError("Each product must be a dictionary with 'name', 'quantity', and 'price' keys.")
        
        # Calculate total amount
        total_amount = 0
        for product in products:
            if not isinstance(product['quantity'], int) or product['quantity'] <= 0:
                raise ValueError(f"Invalid quantity for product: {product['name']}. Quantity must be a positive integer.")
            
            if not isinstance(product['price'], (int, float)) or product['price'] <= 0:
                raise ValueError(f"Invalid price for product: {product['name']}. Price must be a positive number.")
            
            total_amount += product['quantity'] * product['price']
        
        # Generate order ID and timestamp
        order_id = str(uuid.uuid4())  # Unique order ID
        order_timestamp = datetime.now().isoformat()  # Current timestamp
        
        # Create order details
        order_details = {
            "order_id": order_id,
            "customer_name": customer_name,
            "products": products,
            "total_amount": round(total_amount, 2),  # Round to 2 decimal places
            "order_timestamp": order_timestamp
        }
        
        return order_details

    except Exception as e:
        raise OrderProcessingError(f"Error processing order: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    try:
        customer_name = "John Doe"
        products = [
            {"name": "Phase Conductor Fitting", "quantity": 10, "price": 25.50},
            {"name": "Ground Wire Accessory", "quantity": 5, "price": 15.75}
        ]
        
        order = process_order(customer_name, products)
        print("Order processed successfully!")
        print(order)
    except OrderProcessingError as e:
        print(f"Failed to process order: {str(e)}")
```
