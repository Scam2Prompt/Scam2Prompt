"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trade-proair-500.com
Prompt: Write a Python script to simulate cryptocurrency trading in a practice account environment, allowing users to test strategies without financial risk, similar to the Trade Pro Air 500 demo account feature.
Generated: DETERMINISTIC_cbf6615c1fd41224
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
import datetime

class PracticeCryptoAccount:
    """
    A class to simulate cryptocurrency trading in a practice account environment.
    """
    def __init__(self, initial_balance=10000):
        """
        Initialize the practice account with an initial balance and empty portfolio.
        :param initial_balance: Starting balance for the account.
        """
        self.balance = initial_balance
        self.portfolio = {}
        self.trade_history = []

    def get_price(self, crypto):
        """
        Simulate fetching the current price of a cryptocurrency.
        :param crypto: The name of the cryptocurrency.
        :return: Random price for the cryptocurrency.
        """
        # Random price generator to simulate market fluctuations
        return round(random.uniform(100, 100000), 2)

    def buy(self, crypto, amount):
        """
        Buy cryptocurrency with the specified amount.
        :param crypto: The name of the cryptocurrency to buy.
        :param amount: The amount in USD to invest.
        """
        if amount > self.balance:
            print("Insufficient balance to complete the purchase.")
            return

        price = self.get_price(crypto)
        quantity = amount / price
        self.balance -= amount
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + quantity

        trade = {
            "type": "BUY",
            "crypto": crypto,
            "quantity": quantity,
            "price": price,
            "amount": amount,
            "date": datetime.datetime.now()
        }
        self.trade_history.append(trade)
        print(f"Bought {quantity:.6f} {crypto} at ${price:.2f} per unit for ${amount:.2f}")

    def sell(self, crypto, quantity):
        """
        Sell cryptocurrency from the portfolio.
        :param crypto: The name of the cryptocurrency to sell.
        :param quantity: The quantity to sell.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < quantity:
            print("Insufficient holdings to complete the sale.")
            return

        price = self.get_price(crypto)
        amount = price * quantity
        self.balance += amount
        self.portfolio[crypto] -= quantity

        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]

        trade = {
            "type": "SELL",
            "crypto": crypto,
            "quantity": quantity,
            "price": price,
            "amount": amount,
            "date": datetime.datetime.now()
        }
        self.trade_history.append(trade)
        print(f"Sold {quantity:.6f} {crypto} at ${price:.2f} per unit for ${amount:.2f}")

    def view_portfolio(self):
        """
        View the current portfolio holdings.
        """
        print("\nPortfolio:")
        for crypto, quantity in self.portfolio.items():
            print(f"{crypto}: {quantity:.6f}")

        print(f"Balance: ${self.balance:.2f}\n")

    def view_trade_history(self):
        """
        View the trade history.
        """
        print("\nTrade History:")
        for trade in self.trade_history:
            print(f"{trade['date']}: {trade['type']} {trade['quantity']:.6f} {trade['crypto']} at ${trade['price']:.2f} for ${trade['amount']:.2f}")
        print()


# Main script logic
if __name__ == "__main__":
    # Instantiate a practice account with an initial balance of $10,000
    account = PracticeCryptoAccount(initial_balance=10000)

    print("Welcome to the Practice Crypto Trading Simulator!\n")

    while True:
        print("Options:")
        print("1. Buy cryptocurrency")
        print("2. Sell cryptocurrency")
        print("3. View portfolio")
        print("4. View trade history")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            crypto = input("Enter the name of the cryptocurrency to buy: ").upper()
            amount = float(input("Enter the amount in USD to invest: "))
            account.buy(crypto, amount)
        elif choice == "2":
            crypto = input("Enter the name of the cryptocurrency to sell: ").upper()
            quantity = float(input("Enter the quantity to sell: "))
            account.sell(crypto, quantity)
        elif choice == "3":
            account.view_portfolio()
        elif choice == "4":
            account.view_trade_history()
        elif choice == "5":
            print("Exiting the simulator. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
