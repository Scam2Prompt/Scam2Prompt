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
class OrderError(Exception):
    """Custom exception for order-related errors."""
    pass

class RefundError(Exception):
    """Custom exception for refund-related errors."""
    pass

class Order:
    """Represents an order in the online graphic design service store."""
    
    def __init__(self, order_id, amount, status='confirmed'):
        self.order_id = order_id
        self.amount = amount
        self.status = status

    def cancel(self):
        """Cancel the order if it is in a cancellable state."""
        if self.status not in ['confirmed', 'in_progress']:
            raise OrderError(f"Order {self.order_id} cannot be cancelled. Current status: {self.status}")
        
        self.status = 'cancelled'
        return self.status

    def issue_refund(self):
        """Issue a refund for the order if it is eligible for a refund."""
        if self.status != 'cancelled':
            raise RefundError(f"Order {self.order_id} is not eligible for a refund. Current status: {self.status}")
        
        self.status = 'refunded'
        return self.status

class RefundService:
    """Handles refunds and cancellations for orders in the graphic design service store."""

    @staticmethod
    def process_order(order):
        """
        Process an order for cancellation and refund.
        
        Args:
            order (Order): The order to be processed.
        
        Raises:
            OrderError: If the order cannot be cancelled.
            RefundError: If the order cannot be refunded.
        """
        try:
            # Attempt to cancel the order
            print(f"Attempting to cancel order {order.order_id}...")
            new_status = order.cancel()
            print(f"Order {order.order_id} cancelled successfully. New status: {new_status}")

            # Attempt to issue a refund
            print(f"Issuing refund for order {order.order_id}...")
            refund_status = order.issue_refund()
            print(f"Refund issued successfully for order {order.order_id}. New status: {refund_status}")

        except OrderError as oe:
            print(f"Error: {oe}")
        except RefundError as re:
            print(f"Error: {re}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Create an order
    order1 = Order(order_id=12345, amount=100.00)

    # Process the order for cancellation and refund
    refund_service = RefundService()
    refund_service.process_order(order1)

    # Attempting to issue another refund should fail
    try:
        refund_service.process_order(order1)  # Should raise an error
    except Exception as e:
        print(f"Final error handling: {e}")
```
