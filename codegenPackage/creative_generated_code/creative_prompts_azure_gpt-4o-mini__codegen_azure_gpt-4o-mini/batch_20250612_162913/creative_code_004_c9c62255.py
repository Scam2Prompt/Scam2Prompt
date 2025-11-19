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
class ComplianceError(Exception):
    """Custom exception for compliance errors."""
    pass

def check_compliance(order_details, user_terms_acceptance):
    """
    Check if the order complies with Metro Wholesale's terms and conditions.

    Args:
        order_details (dict): A dictionary containing order information.
        user_terms_acceptance (bool): Whether the user has accepted the terms and conditions.

    Raises:
        ComplianceError: If the order does not comply with the terms.

    Returns:
        bool: True if the order is compliant, raises an exception otherwise.
    """
    # Check if user accepted terms and conditions
    if not user_terms_acceptance:
        raise ComplianceError("User has not accepted the terms and conditions.")

    # Validate order details
    if not isinstance(order_details, dict):
        raise ComplianceError("Order details must be provided as a dictionary.")

    required_fields = ['product_id', 'quantity', 'payment_info']
    
    # Check for missing required fields
    for field in required_fields:
        if field not in order_details:
            raise ComplianceError(f"Missing required order detail: {field}")

    # Example compliance checks (these would depend on actual business logic)
    if order_details['quantity'] <= 0:
        raise ComplianceError("Quantity must be greater than zero.")
    
    # Assuming a hypothetical function to check product availability
    if not check_product_availability(order_details['product_id'], order_details['quantity']):
        raise ComplianceError("Requested quantity not available for product.")

    # If all checks pass, the order is compliant
    return True

def check_product_availability(product_id, quantity):
    """
    Check if the product is available in the specified quantity.

    Args:
        product_id (str): The ID of the product to check.
        quantity (int): The quantity to check for availability.

    Returns:
        bool: True if the product is available, False otherwise.
    """
    # Simulate a product availability check (replace with actual logic)
    available_products = {
        'product_1': 100,
        'product_2': 0,
        'product_3': 50
    }
    
    return available_products.get(product_id, 0) >= quantity

# Example usage:
try:
    order = {
        'product_id': 'product_1',
        'quantity': 2,
        'payment_info': 'VISA **** **** **** 1234'
    }
    
    user_accepted_terms = True  # User has accepted terms
    
    if check_compliance(order, user_accepted_terms):
        print("Order is compliant and can be processed.")
except ComplianceError as e:
    print(f"Compliance error: {e}")
```
