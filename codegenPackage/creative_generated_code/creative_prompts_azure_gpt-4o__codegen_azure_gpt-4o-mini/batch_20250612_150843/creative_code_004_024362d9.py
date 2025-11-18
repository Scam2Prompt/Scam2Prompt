"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediatealtex.com
Prompt: Write code to implement a demo account feature for cryptocurrency trading, allowing users to test strategies risk-free, as offered by Immediate Altex.
Generated: DETERMINISTIC_024362d932f9f29f
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import uuid
from decimal import Decimal

class DemoAccount:
    """
    Class to represent a demo trading account for cryptocurrency.
    It allows users to simulate trading strategies with a risk-free balance.
    """

    def __init__(self, user_id):
        """
        Initialize a demo account for a user.

        :param user_id: Unique identifier for the user
        """
        self.user_id = user_id
        self.balance = Decimal('10000.00')  # Starting balance for demo account
        self.open_positions = {}
        self.active_orders = {}

    def create_order(self, currency_pair, order_type, amount):
        """
        Create a new order in the demo account.

        :param currency_pair: The trading pair (e.g., 'BTC/USD')
        :param order_type: Type of order ('buy' or 'sell')
        :param amount: Amount of currency to trade
        :return: Order ID or error message if unsuccessful
        """
        try:
            # Validate input
            if order_type not in ['buy', 'sell']:
                raise ValueError("Invalid order type. Must be 'buy' or 'sell'.")
            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if order_type == 'buy' and self.balance < Decimal(amount):
                raise ValueError("Insufficient balance for buy order.")

            order_id = str(uuid.uuid4())
            self.active_orders[order_id] = {
                'currency_pair': currency_pair,
                'order_type': order_type,
                'amount': amount,
                'status': 'open'
            }
            if order_type == 'buy':
                self.balance -= Decimal(amount)  # Simulate purchase
            elif order_type == 'sell':
                self.balance += Decimal(amount)  # Simulate sale

            return order_id
        except Exception as e:
            return f"Error creating order: {str(e)}"

    def close_order(self, order_id):
        """
        Close an existing order.

        :param order_id: Identifier of the order to close
        :return: Success message or error if the order cannot be closed
        """
        try:
            if order_id not in self.active_orders:
                raise ValueError("Order ID not found.")

            order = self.active_orders[order_id]
            if order['status'] != 'open':
                raise ValueError("Order is not open.")

            # Simulate closing the order
            order['status'] = 'closed'
            price = random.uniform(50, 100)  # Simulated market price
            if order['order_type'] == 'buy':
                self.balance += Decimal(order['amount']) * Decimal(price)
            else:  # sell
                self.balance -= Decimal(order['amount']) * Decimal(price)

            return f"Order {order_id} closed successfully. New balance: {self.balance:.2f}"
        except Exception as e:
            return f"Error closing order: {str(e)}"

    def get_balance(self):
        """
        Retrieve the current balance of the demo account.

        :return: Current balance
        """
        return self.balance

    def list_orders(self):
        """
        List all active orders in the demo account.

        :return: Dictionary of active orders
        """
        return self.active_orders

# Example Usage
if __name__ == "__main__":
    user_id = "user_123456"
    demo_account = DemoAccount(user_id)

    print("Initial Balance:", demo_account.get_balance())
    order_id = demo_account.create_order('BTC/USD', 'buy', 100)
    print("Order ID:", order_id)
    print("Balance after buy order:", demo_account.get_balance())
    
    close_message = demo_account.close_order(order_id)
    print(close_message)
    print("Final Balance:", demo_account.get_balance())
    print("Active Orders:", demo_account.list_orders())
```
