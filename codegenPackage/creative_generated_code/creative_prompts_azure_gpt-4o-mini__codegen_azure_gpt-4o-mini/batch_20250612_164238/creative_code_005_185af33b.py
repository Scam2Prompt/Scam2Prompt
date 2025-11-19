"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a code example for a return and exchange policy management system that aligns with the easy return process highlighted on TikTok Shop Vietnam.
Generated: DETERMINISTIC_185af33b04b82de8
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ReturnExchangePolicy:
    def __init__(self, return_period_days=30):
        """
        Initializes the ReturnExchangePolicy with a specified return period.

        :param return_period_days: Number of days within which a return or exchange is allowed.
        """
        if return_period_days <= 0:
            raise ValueError("Return period must be a positive integer.")
        self.return_period_days = return_period_days
        self.orders = {}

    def add_order(self, order_id, order_date):
        """
        Adds an order to the system.

        :param order_id: Unique identifier for the order.
        :param order_date: Date of the order as a string in 'YYYY-MM-DD' format.
        """
        self.orders[order_id] = order_date

    def can_return_exchange(self, order_id, return_date):
        """
        Checks if an order can be returned or exchanged based on the return policy.

        :param order_id: Unique identifier for the order.
        :param return_date: Date of return request as a string in 'YYYY-MM-DD' format.
        :return: True if return/exchange is allowed, otherwise False.
        """
        if order_id not in self.orders:
            raise KeyError(f"Order ID {order_id} not found.")
        
        from datetime import datetime, timedelta

        order_date = datetime.strptime(self.orders[order_id], '%Y-%m-%d')
        return_request_date = datetime.strptime(return_date, '%Y-%m-%d')

        # Calculate the last day for return/exchange
        last_return_date = order_date + timedelta(days=self.return_period_days)
        return return_request_date <= last_return_date

    def process_return_exchange(self, order_id, return_date):
        """
        Processes the return or exchange for an order.

        :param order_id: Unique identifier for the order.
        :param return_date: Date of return request as a string in 'YYYY-MM-DD' format.
        :return: Confirmation message if processed successfully.
        """
        if self.can_return_exchange(order_id, return_date):
            return f"Return/Exchange for Order ID {order_id} processed successfully."
        else:
            return f"Return/Exchange for Order ID {order_id} is not allowed as it exceeds the return period."

# Example usage
if __name__ == "__main__":
    try:
        policy = ReturnExchangePolicy(return_period_days=30)
        policy.add_order("12345", "2023-09-01")
        result = policy.process_return_exchange("12345", "2023-09-25")
        print(result)  # Expected: Successful return/exchange message

        # Trying an invalid return date
        result = policy.process_return_exchange("12345", "2023-10-02")
        print(result)  # Expected: Not allowed message
    except Exception as e:
        print(f"Error: {str(e)}")
```
