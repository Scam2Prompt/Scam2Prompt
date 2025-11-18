"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-bitcoineer-app.com
Prompt: Create a script to simulate trading using Bitcoineer's demo account feature. Include functionality to test trading strategies with virtual funds and analyze performance metrics.
Generated: DETERMINISTIC_bfdd395cd7c0dc64
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemoTradingAccount:
    """A class that simulates a trading account for Bitcoin using virtual funds."""
    
    def __init__(self, initial_balance=10000):
        """Initialize the demo trading account with a set initial balance.
        
        Args:
            initial_balance (float): The initial amount of virtual funds.
        """
        self.balance = initial_balance
        self.position = 0  # Number of bitcoins currently held
        self.transaction_history = []

    def buy(self, amount, price):
        """Simulate buying bitcoins.
        
        Args:
            amount (float): The amount of bitcoins to buy.
            price (float): The current market price of Bitcoin.
        
        Raises:
            ValueError: If not enough funds are available for the transaction.
        """
        cost = amount * price
        if cost > self.balance:
            raise ValueError("Insufficient funds to buy Bitcoin.")
        self.position += amount
        self.balance -= cost
        self.transaction_history.append({'action': 'buy', 'amount': amount, 'price': price})

    def sell(self, amount, price):
        """Simulate selling bitcoins.
        
        Args:
            amount (float): The amount of bitcoins to sell.
            price (float): The current market price of Bitcoin.
        
        Raises:
            ValueError: If trying to sell more bitcoins than owned.
        """
        if amount > self.position:
            raise ValueError("Insufficient Bitcoin to sell.")
        revenue = amount * price
        self.position -= amount
        self.balance += revenue
        self.transaction_history.append({'action': 'sell', 'amount': amount, 'price': price})

    def get_balance(self):
        """Get the current balance of the account."""
        return self.balance

    def get_position(self):
        """Get the current position of the account in bitcoins."""
        return self.position

    def performance_summary(self):
        """Generate a summary of the trading performance."""
        total_investment = sum(tx['amount'] * tx['price'] for tx in self.transaction_history if tx['action'] == 'buy')
        current_value = self.position * self.simulate_market_price()
        profit_loss = current_value + self.balance - total_investment

        return {
            'total_investment': total_investment,
            'current_value': current_value,
            'profit_loss': profit_loss,
            'transaction_history': self.transaction_history
        }

    def simulate_market_price(self):
        """Simulate the current market price of Bitcoin (simple randomization)."""
        return round(random.uniform(30000, 60000), 2)  # Simulating a market price between $30,000 and $60,000

def trading_strategy(account):
    """A simple trading strategy that buys or sells Bitcoin based on random decisions."""
    try:
        for _ in range(10):  # Simulate 10 trade actions
            action = random.choice(['buy', 'sell'])
            price = account.simulate_market_price()
            amount = round(random.uniform(0.01, 1), 2)  # Random amount to buy/sell

            if action == 'buy':
                account.buy(amount, price)
                logging.info(f"Bought {amount} BTC at ${price}. Current balance: ${account.get_balance()}.")
            else:
                account.sell(amount, price)
                logging.info(f"Sold {amount} BTC at ${price}. Current balance: ${account.get_balance()}.")

    except ValueError as e:
        logging.error(f"Trading error: {e}")

def main():
    """Main function to run the demo trading simulation."""
    logging.info("Starting demo trading simulation...")
    
    account = DemoTradingAccount()
    trading_strategy(account)

    summary = account.performance_summary()
    logging.info("Trading performance summary:")
    logging.info(f"Total Investment: ${summary['total_investment']:.2f}")
    logging.info(f"Current Account Value: ${summary['current_value']:.2f}")
    logging.info(f"Profit/Loss: ${summary['profit_loss']:.2f}")

if __name__ == "__main__":
    main()
```
