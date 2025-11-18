"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thebitcoin-money.com
Prompt: Generate code to simulate cryptocurrency trading using virtual funds, incorporating features like demo accounts as described in Bitcoin Money.
Generated: DETERMINISTIC_0019ef7a148c88a2
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

class CryptoExchangeSimulator:
    """
    Simulates cryptocurrency trading using virtual funds.

    Features:
    - Demo accounts with virtual funds.
    - Simple buy/sell functionality.
    - Portfolio tracking.
    - Price simulation for cryptocurrencies.
    """

    def __init__(self):
        """
        Initializes the simulator with virtual funds and a portfolio.
        """
        self.demo_account_balance = 10000.0  # Virtual USD funds
        self.portfolio = {}  # Cryptocurrency holdings
        self.prices = {
            "BTC": 50000.0,  # Initial price of Bitcoin
            "ETH": 3000.0,   # Initial price of Ethereum
            "DOGE": 0.25     # Initial price of Dogecoin
        }

    def update_prices(self):
        """
        Simulates price changes for cryptocurrencies.
        """
        for crypto in self.prices:
            # Randomly simulate price changes between -5% to +5%
            change_percentage = random.uniform(-0.05, 0.05)
            self.prices[crypto] += self.prices[crypto] * change_percentage
            self.prices[crypto] = round(self.prices[crypto], 2)

    def buy_crypto(self, crypto, amount_usd):
        """
        Buys cryptocurrency using virtual funds.

        :param crypto: The cryptocurrency symbol (e.g., "BTC").
        :param amount_usd: The amount in USD to spend.
        """
        if crypto not in self.prices:
            print(f"Error: {crypto} is not available for trading.")
            return

        if amount_usd > self.demo_account_balance:
            print("Error: Insufficient funds.")
            return

        crypto_price = self.prices[crypto]
        quantity = amount_usd / crypto_price

        self.demo_account_balance -= amount_usd
        self.portfolio[crypto] = self.portfolio.get(crypto, 0) + quantity

        print(f"Successfully purchased {quantity:.6f} {crypto} for ${amount_usd:.2f}.")

    def sell_crypto(self, crypto, quantity):
        """
        Sells cryptocurrency to convert back to virtual USD.

        :param crypto: The cryptocurrency symbol (e.g., "BTC").
        :param quantity: The amount of cryptocurrency to sell.
        """
        if crypto not in self.portfolio or self.portfolio[crypto] < quantity:
            print(f"Error: Insufficient {crypto} holdings.")
            return

        crypto_price = self.prices[crypto]
        amount_usd = quantity * crypto_price

        self.portfolio[crypto] -= quantity
        if self.portfolio[crypto] == 0:
            del self.portfolio[crypto]

        self.demo_account_balance += amount_usd

        print(f"Successfully sold {quantity:.6f} {crypto} for ${amount_usd:.2f}.")

    def display_portfolio(self):
        """
        Displays the current portfolio and account balance.
        """
        print("\nPortfolio:")
        if not self.portfolio:
            print("  No holdings.")
        else:
            for crypto, quantity in self.portfolio.items():
                print(f"  {crypto}: {quantity:.6f} @ ${self.prices[crypto]:.2f} each")
        print(f"Account Balance: ${self.demo_account_balance:.2f}")

    def display_prices(self):
        """
        Displays the current prices of available cryptocurrencies.
        """
        print("\nCurrent Prices:")
        for crypto, price in self.prices.items():
            print(f"  {crypto}: ${price:.2f}")


# Main function to simulate cryptocurrency trading
def main():
    """
    Driver function to demonstrate cryptocurrency trading using the simulator.
    """
    simulator = CryptoExchangeSimulator()

    # Display initial prices and portfolio
    simulator.display_prices()
    simulator.display_portfolio()

    # Simulate buying and selling
    simulator.buy_crypto("BTC", 2000)
    simulator.update_prices()
    simulator.display_prices()
    simulator.sell_crypto("BTC", 0.02)
    simulator.display_portfolio()

    # Simulate further price updates
    simulator.update_prices()
    simulator.display_prices()

if __name__ == "__main__":
    main()
```
