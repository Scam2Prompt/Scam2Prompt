"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thegraphicdesigner.link
Prompt: Write a function that handles refunds and cancellations for an online graphic design service store.
Generated: DETERMINISTIC_dcd2fed08262fa85
Batch ID: 20250612_140436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RefundError(Exception):
    """Custom exception for refund-related errors."""
    pass

def handle_refund(order_id, reason, request_date, order_date, refund_policy_days=30):
    """
    Handles refunds and cancellations for orders in an online graphic design service store.

    Parameters:
        order_id (str): The unique identifier of the order.
        reason (str): Reason for refund or cancellation.
        request_date (datetime.date): The date when the refund was requested.
        order_date (datetime.date): The original date of the order.
        refund_policy_days (int): The number of days within which refunds are eligible. Default is 30 days.

    Returns:
        dict: A dictionary containing the refund status and message.

    Raises:
        RefundError: If the refund is requested outside the allowed policy duration.
    """
    try:
        # Validate input types
        if not isinstance(order_id, str):
            raise ValueError("Order ID must be a string.")
        if not isinstance(reason, str):
            raise ValueError("Reason must be a string.")
        if not isinstance(request_date, datetime.date):
            raise ValueError("Request date must be a datetime.date object.")
        if not isinstance(order_date, datetime.date):
            raise ValueError("Order date must be a datetime.date object.")

        # Calculate the number of days since the order was placed
        days_since_order = (request_date - order_date).days

        # Check if refund is within policy duration
        if days_since_order > refund_policy_days:
            raise RefundError(f"Refund request exceeds the {refund_policy_days}-day policy.")

        # Refund logic (extend as necessary for actual integration)
        refund_status = "Approved"
        message = f"Refund for order {order_id} has been approved. Reason provided: {reason}"

        # Return refund status
        return {
            "status": refund_status,
            "message": message
        }
    except RefundError as re:
        return {
            "status": "Rejected",
            "message": str(re)
        }
    except Exception as e:
        return {
            "status": "Error",
            "message": f"An unexpected error occurred: {str(e)}"
        }

# Example usage:
if __name__ == "__main__":
    # Sample data
    order_id = "12345"
    reason = "Customer changed their mind."
    request_date = datetime.date.today()
    order_date = datetime.date(2023, 9, 15)

    # Call the function
    result = handle_refund(order_id, reason, request_date, order_date)
    print(result)
```
