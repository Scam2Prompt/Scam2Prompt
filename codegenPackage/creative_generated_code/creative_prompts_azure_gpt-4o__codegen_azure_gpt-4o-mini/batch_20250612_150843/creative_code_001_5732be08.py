"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-evrixedge.com
Prompt: Generate code to simulate trading using Evrix Edge's demo account feature, allowing users to test strategies with virtual funds before live trading.
Generated: DETERMINISTIC_5732be08d49a0d32
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
import time

class TradingAccount:
    """Class to represent a trading account for simulation."""
    
    def __init__(self, initial_balance=10000):
        """
        Initialize the trading account with a starting balance.
        
        :param initial_balance: Initial virtual funds for the demo account.
        """
        self.balance = initial_balance
        self.positions = {}
        
    def buy(self, symbol, amount):
        """
        Simulate buying a stock.
        
        :param symbol: The symbol of the stock to buy.
        :param amount: The amount of stock to buy.
        :raises ValueError: If the transaction exceeds available balance.
        """
        price = self.get_stock_price(symbol)
        total_cost = price * amount
        if total_cost > self.balance:
            raise ValueError("Insufficient balance to complete the transaction.")
        
        self.balance -= total_cost
        self.positions[symbol] = self.positions.get(symbol, 0) + amount
        print(f"Bought {amount} shares of {symbol} at ${price:.2f} each.")
        
    def sell(self, symbol, amount):
        """
        Simulate selling a stock.
        
        :param symbol: The symbol of the stock to sell.
        :param amount: The amount of stock to sell.
        :raises ValueError: If the user does not own enough shares.
        """
        if symbol not in self.positions or self.positions[symbol] < amount:
            raise ValueError("Not enough shares to sell.")
        
        price = self.get_stock_price(symbol)
        self.balance += price * amount
        self.positions[symbol] -= amount
        print(f"Sold {amount} shares of {symbol} at ${price:.2f} each.")
        
    def get_stock_price(self, symbol):
        """
        Simulate fetching the current stock price.
        
        :param symbol: The symbol of the stock to get the price for.
        :return: A simulated stock price (random float).
        """
        return round(random.uniform(50, 150), 2)  # Simulated stock price between $50 and $150

    def check_balance(self):
        """Return the current balance of the account."""
        return self.balance

    def check_positions(self):
        """Return the current positions in the account."""
        return self.positions


def main():
    """Main function to simulate trading."""
    account = TradingAccount()  # Create a demo trading account
    print("Welcome to Evrix Edge Demo Trading!")
    
    while True:
        print("\nCurrent Balance: ${:.2f}".format(account.check_balance()))
        print("Current Positions:", account.check_positions())
        
        action = input("Would you like to (b)uy, (s)ell, or (q)uit? ").lower()
        
        if action == 'b':
            symbol = input("Enter stock symbol to buy: ").upper()
            amount = int(input("Enter amount to buy: "))
            try:
                account.buy(symbol, amount)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif action == 's':
            symbol = input("Enter stock symbol to sell: ").upper()
            amount = int(input("Enter amount to sell: "))
            try:
                account.sell(symbol, amount)
            except ValueError as e:
                print(f"Error: {e}")
                
        elif action == 'q':
            print("Thank you for using Evrix Edge Demo Trading. Goodbye!")
            break
            
        else:
            print("Invalid action. Please choose 'b', 's', or 'q'.")

if __name__ == "__main__":
    main()
```
