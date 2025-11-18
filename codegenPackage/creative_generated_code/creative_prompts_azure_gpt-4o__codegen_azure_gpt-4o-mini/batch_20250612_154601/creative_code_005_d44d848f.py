"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opterisglobal.com
Prompt: Write code to simulate a crypto exchange transaction with low fees and deep liquidity, inspired by the features of Opteris Global's exchange platform.
Generated: DETERMINISTIC_d44d848ff3c08f2a
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from decimal import Decimal, getcontext

# Set the precision for Decimal operations
getcontext().prec = 10

class CryptoExchange:
    def __init__(self):
        # Initialize currency pairs and their respective prices
        self.order_book = {
            'BTC/USD': {
                'ask': Decimal('30000.00'),  # Current ask price
                'bid': Decimal('29900.00'),  # Current bid price
                'liquidity': Decimal('1000.0')  # Available liquidity
            },
            'ETH/USD': {
                'ask': Decimal('2000.00'),
                'bid': Decimal('1990.00'),
                'liquidity': Decimal('500.0')
            }
        }
        self.fee = Decimal('0.001')  # Transaction fee (0.1%)
    
    def execute_trade(self, currency_pair, trade_amount, trade_type):
        """
        Execute a trade on the exchange.

        :param currency_pair: str - The trading pair (e.g., 'BTC/USD')
        :param trade_amount: Decimal - The amount to trade
        :param trade_type: str - Type of trade ('buy' or 'sell')
        :raises ValueError: If the trade type is invalid or insufficient liquidity
        :return: str - Confirmation message
        """
        if currency_pair not in self.order_book:
            raise ValueError("Invalid currency pair.")
        
        order = self.order_book[currency_pair]

        if trade_type not in ['buy', 'sell']:
            raise ValueError("Invalid trade type. Use 'buy' or 'sell'.")

        if trade_type == 'buy':
            if trade_amount > order['liquidity']:
                raise ValueError("Insufficient liquidity for buy order.")
            total_cost = order['ask'] * trade_amount * (1 + self.fee)
            order['liquidity'] -= trade_amount
            return f"Bought {trade_amount} {currency_pair} at {order['ask']} per unit, total cost (including fee): {total_cost:.2f} USD."
        
        elif trade_type == 'sell':
            total_revenue = order['bid'] * trade_amount * (1 - self.fee)
            order['liquidity'] += trade_amount
            return f"Sold {trade_amount} {currency_pair} at {order['bid']} per unit, total revenue (after fee): {total_revenue:.2f} USD."

    def get_order_book(self):
        """
        Retrieve the current order book.

        :return: dict - The current state of the order book
        """
        return self.order_book

def main():
    # Instantiate the crypto exchange
    exchange = CryptoExchange()
    
    # Display the current order book
    print("Current Order Book:")
    print(exchange.get_order_book())

    # Example transaction
    try:
        print(exchange.execute_trade('BTC/USD', Decimal('0.1'), 'buy'))
        print(exchange.execute_trade('ETH/USD', Decimal('0.5'), 'sell'))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
