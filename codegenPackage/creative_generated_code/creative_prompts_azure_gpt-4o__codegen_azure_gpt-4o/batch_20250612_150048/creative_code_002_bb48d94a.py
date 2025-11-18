"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inditexcapitalsoftware.com
Prompt: Create a script that simulates a cryptocurrency trading platform with customizable autonomy and assistance levels, inspired by the features of the Inditex Capital app.
Generated: DETERMINISTIC_bb48d94ad5310b38
Batch ID: 20250612_150048
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
from datetime import datetime

class CryptoTradingPlatform:
    """
    Simulates a cryptocurrency trading platform with customizable autonomy and assistance levels.
    """

    def __init__(self):
        self.portfolio = {}
        self.balance = 10000.0  # Starting balance in USD
        self.assistance_levels = ["manual", "guided", "autonomous"]  # Trading modes
        self.current_mode = "manual"
        self.market_data = {
            "BTC": {"price": 50000.0, "volatility": 0.05},
            "ETH": {"price": 4000.0, "volatility": 0.08},
            "DOGE": {"price": 0.30, "volatility": 0.15},
        }

    def set_mode(self, mode: str):
        """
        Sets the trading mode to one of the predefined levels.
        :param mode: Mode to switch to ("manual", "guided", "autonomous").
        """
        if mode in self.assistance_levels:
            self.current_mode = mode
            print(f"Trading mode set to: {mode}")
        else:
            raise ValueError("Invalid mode. Choose from 'manual', 'guided', or 'autonomous'.")

    def display_portfolio(self):
        """
        Displays the user's current portfolio.
        """
        print("\n=== Portfolio ===")
        for asset, quantity in self.portfolio.items():
            price = self.market_data[asset]["price"]
            value = price * quantity
            print(f"{asset}: {quantity} units (${value:.2f})")
        print(f"Balance: ${self.balance:.2f}")
        print("=================\n")

    def simulate_market(self):
        """
        Simulates market data fluctuations based on volatility.
        """
        for asset, data in self.market_data.items():
            # Simulate price fluctuation
            fluctuation = random.uniform(-data["volatility"], data["volatility"])
            new_price = max(data["price"] * (1 + fluctuation), 0.01)  # Ensure price doesn't fall below $0.01
            self.market_data[asset]["price"] = round(new_price, 2)

    def manual_trade(self):
        """
        Manual trading mode: allows the user to buy or sell specific assets.
        """
        print("\n=== Manual Trading ===")
        asset = input("Enter the cryptocurrency symbol to trade (e.g., BTC): ").upper()
        if asset not in self.market_data:
            print("Invalid cryptocurrency symbol.")
            return

        action = input("Enter 'buy' or 'sell': ").lower()
        if action not in ["buy", "sell"]:
            print("Invalid action. Choose 'buy' or 'sell'.")
            return

        quantity = float(input("Enter the quantity: "))
        price = self.market_data[asset]["price"]

        if action == "buy":
            cost = quantity * price
            if self.balance >= cost:
                self.balance -= cost
                self.portfolio[asset] = self.portfolio.get(asset, 0) + quantity
                print(f"Purchased {quantity} {asset} for ${cost:.2f}.")
            else:
                print("Insufficient balance.")

        elif action == "sell":
            if self.portfolio.get(asset, 0) >= quantity:
                self.portfolio[asset] -= quantity
                self.balance += quantity * price
                print(f"Sold {quantity} {asset} for ${quantity * price:.2f}.")
            else:
                print("Insufficient holdings.")

        self.display_portfolio()

    def guided_trade(self):
        """
        Guided trading mode: recommends a trade based on market trends.
        """
        print("\n=== Guided Trading ===")
        asset = random.choice(list(self.market_data.keys()))
        price = self.market_data[asset]["price"]
        print(f"Recommendation: Consider buying {asset}. Current price: ${price:.2f}.")
        decision = input("Would you like to proceed? (yes/no): ").lower()

        if decision == "yes":
            quantity = float(input(f"Enter quantity of {asset} to buy: "))
            cost = quantity * price
            if self.balance >= cost:
                self.balance -= cost
                self.portfolio[asset] = self.portfolio.get(asset, 0) + quantity
                print(f"Purchased {quantity} {asset} for ${cost:.2f}.")
            else:
                print("Insufficient balance.")
        else:
            print("No trade executed.")

        self.display_portfolio()

    def autonomous_trade(self):
        """
        Autonomous trading mode: executes random trades automatically.
        """
        print("\n=== Autonomous Trading ===")
        asset = random.choice(list(self.market_data.keys()))
        action = random.choice(["buy", "sell"])
        quantity = random.uniform(0.1, 5.0)  # Random quantity between 0.1 and 5 units
        price = self.market_data[asset]["price"]

        if action == "buy":
            cost = quantity * price
            if self.balance >= cost:
                self.balance -= cost
                self.portfolio[asset] = self.portfolio.get(asset, 0) + quantity
                print(f"Automatically purchased {quantity:.2f} {asset} for ${cost:.2f}.")
            else:
                print("Autonomous trade skipped due to insufficient balance.")
        elif action == "sell":
            if self.portfolio.get(asset, 0) >= quantity:
                self.portfolio[asset] -= quantity
                self.balance += quantity * price
                print(f"Automatically sold {quantity:.2f} {asset} for ${quantity * price:.2f}.")
            else:
                print("Autonomous trade skipped due to insufficient holdings.")

        self.display_portfolio()

    def run(self):
        """
        Main function to run the platform.
        """
        print("Welcome to the Cryptocurrency Trading Platform!")
        while True:
            self.simulate_market()
            print("\n=== Main Menu ===")
            print("1. Set trading mode")
            print("2. Display portfolio")
            print("3. Trade (current mode)")
            print("4. Exit")
            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    mode = input("Enter trading mode ('manual', 'guided', 'autonomous'): ").lower()
                    self.set_mode(mode)
                elif choice == "2":
                    self.display_portfolio()
                elif choice == "3":
                    if self.current_mode == "manual":
                        self.manual_trade()
                    elif self.current_mode == "guided":
                        self.guided_trade()
                    elif self.current_mode == "autonomous":
                        self.autonomous_trade()
                elif choice == "4":
                    print("Exiting the platform. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    platform = CryptoTradingPlatform()
    platform.run()
```
