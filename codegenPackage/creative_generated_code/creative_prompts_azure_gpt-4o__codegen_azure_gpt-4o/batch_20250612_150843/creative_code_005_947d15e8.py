"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoin-lifestyle-pro.com
Prompt: Develop a Python program that demonstrates how to implement demo trading functionality, allowing users to practice cryptocurrency trading with virtual funds before transitioning to live trading.
Generated: DETERMINISTIC_947d15e8afc49b8b
Batch ID: 20250612_150843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random


class DemoTradingPlatform:
    """
    A class to simulate cryptocurrency demo trading functionality with virtual funds.
    """

    def __init__(self):
        """
        Initializes the demo trading platform with a virtual account balance
        and a list of available cryptocurrencies.
        """
        self.virtual_balance = 10000.00  # Virtual funds ($10,000)
        self.portfolio = {}  # User's cryptocurrency portfolio
        self.prices = {"BTC": 50000.00, "ETH": 3000.00, "DOGE": 0.25}  # Mock prices

    def display_balance(self):
        """
        Displays the user's virtual account balance and portfolio holdings.
        """
        print(f"Virtual Balance: ${self.virtual_balance:.2f}")
        if self.portfolio:
            print("Portfolio Holdings:")
            for crypto, amount in self.portfolio.items():
                print(f"  {crypto}: {amount:.6f}")
        else:
            print("Portfolio is empty.")

    def get_current_price(self, cryptocurrency):
        """
        Returns the current price of the specified cryptocurrency.
        Simulates real-time price fluctuations.
        """
        if cryptocurrency in self.prices:
            # Simulate price fluctuation
            self.prices[cryptocurrency] *= random.uniform(0.98, 1.02)
            return round(self.prices[cryptocurrency], 2)
        else:
            raise ValueError(f"Cryptocurrency '{cryptocurrency}' not supported.")

    def buy_crypto(self, cryptocurrency, amount):
        """
        Allows the user to buy cryptocurrency with virtual funds.
        :param cryptocurrency: The cryptocurrency to buy (e.g., 'BTC', 'ETH').
        :param amount: The amount of virtual funds to invest.
        """
        try:
            price = self.get_current_price(cryptocurrency)
            quantity = amount / price

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")
            if amount > self.virtual_balance:
                raise ValueError("Insufficient virtual balance.")

            self.virtual_balance -= amount
            self.portfolio[cryptocurrency] = self.portfolio.get(cryptocurrency, 0) + quantity
            print(f"Bought {quantity:.6f} {cryptocurrency} at ${price:.2f} per unit.")
        except ValueError as e:
            print(f"Error: {e}")

    def sell_crypto(self, cryptocurrency, quantity):
        """
        Allows the user to sell cryptocurrency for virtual funds.
        :param cryptocurrency: The cryptocurrency to sell (e.g., 'BTC', 'ETH').
        :param quantity: The quantity of cryptocurrency to sell.
        """
        try:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero.")
            if cryptocurrency not in self.portfolio or self.portfolio[cryptocurrency] < quantity:
                raise ValueError("Insufficient cryptocurrency in portfolio.")

            price = self.get_current_price(cryptocurrency)
            earnings = quantity * price

            self.virtual_balance += earnings
            self.portfolio[cryptocurrency] -= quantity

            if self.portfolio[cryptocurrency] == 0:
                del self.portfolio[cryptocurrency]  # Remove empty holdings

            print(f"Sold {quantity:.6f} {cryptocurrency} at ${price:.2f} per unit.")
        except ValueError as e:
            print(f"Error: {e}")

    def run_demo(self):
        """
        Main method to simulate demo trading functionality.
        Provides a simple menu for the user to interact with.
        """
        print("Welcome to the Cryptocurrency Demo Trading Platform!")
        while True:
            print("\nMenu:")
            print("1. View Balance and Portfolio")
            print("2. Buy Cryptocurrency")
            print("3. Sell Cryptocurrency")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_balance()
            elif choice == "2":
                crypto = input("Enter the cryptocurrency to buy (e.g., 'BTC', 'ETH'): ").upper()
                try:
                    amount = float(input("Enter the amount in virtual funds to invest: "))
                    self.buy_crypto(crypto, amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == "3":
                crypto = input("Enter the cryptocurrency to sell (e.g., 'BTC', 'ETH'): ").upper()
                try:
                    quantity = float(input("Enter the quantity to sell: "))
                    self.sell_crypto(crypto, quantity)
                except ValueError:
                    print("Invalid input. Please enter a valid quantity.")
            elif choice == "4":
                print("Thank you for using the demo trading platform. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # Entry point of the program
    platform = DemoTradingPlatform()
    platform.run_demo()
```
