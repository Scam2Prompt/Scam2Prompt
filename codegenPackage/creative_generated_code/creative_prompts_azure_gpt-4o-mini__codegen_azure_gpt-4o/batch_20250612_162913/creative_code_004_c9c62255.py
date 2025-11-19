"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metrorrl.com
Prompt: Provide an example of a Python function that checks compliance with Metro Wholesale's terms and conditions before processing an order.
Generated: DETERMINISTIC_c9c622554e960b78
Batch ID: 20250612_162913
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def check_compliance_and_process_order(order_details):
    """
    Checks compliance with Metro Wholesale's terms and conditions before processing an order.

    Parameters:
        order_details (dict): A dictionary containing order information. Expected keys:
                             - 'customer_id' (str): The ID of the customer.
                             - 'email' (str): The customer's email address.
                             - 'items' (list): List of items in the order.
                             - 'total_amount' (float): The total order amount.

    Returns:
        str: A message indicating whether the order was processed or rejected due to non-compliance.
    """
    try:
        # Validate customer ID (must be alphanumeric and of length 6-12)
        customer_id = order_details.get('customer_id')
        if not customer_id or not re.match(r'^[a-zA-Z0-9]{6,12}$', customer_id):
            return "Order rejected: Invalid customer ID."
        
        # Validate email format
        email = order_details.get('email')
        if not email or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return "Order rejected: Invalid email address."
        
        # Validate items (must contain at least one item)
        items = order_details.get('items')
        if not items or not isinstance(items, list) or len(items) == 0:
            return "Order rejected: No items in the order."
        
        # Validate total amount (must be greater than zero)
        total_amount = order_details.get('total_amount')
        if not isinstance(total_amount, (int, float)) or total_amount <= 0:
            return "Order rejected: Invalid total amount."
        
        # Additional compliance checks could be added here
        
        # If all checks pass, process the order (simulated here)
        # In a real-world application, processing logic would be implemented.
        return "Order processed successfully."
    
    except Exception as e:
        # Handle unexpected errors gracefully
        return f"Order processing failed due to an unexpected error: {str(e)}"


# Example Usage:
order = {
    "customer_id": "CUST1234",
    "email": "customer@example.com",
    "items": ["item1", "item2"],
    "total_amount": 150.75
}

result = check_compliance_and_process_order(order)
print(result)  # Output: "Order processed successfully."
```
