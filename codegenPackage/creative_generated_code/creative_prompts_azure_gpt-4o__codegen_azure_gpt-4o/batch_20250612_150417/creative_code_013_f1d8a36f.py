"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://megapromining.live
Prompt: Develop a forex trading simulation tool that allows users to experiment with trading popular currencies like USD, GBP, AUD, BTC, and EUR, as described on Megapromining.live.
Generated: DETERMINISTIC_f1d8a36fe601d6f6
Batch ID: 20250612_150417
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

class ForexTradingSimulator:
    """
    A Forex Trading Simulation tool for experimenting with trading 
    popular currencies (USD, GBP, AUD, BTC, EUR).
    """

    def __init__(self):
        # Initialize available currencies
        self.currencies = ["USD", "GBP", "AUD", "BTC", "EUR"]
        # Initialize exchange rates (randomized for simulation)
        self.exchange_rates = self._generate_exchange_rates()
        # Initialize user's portfolio
        self.portfolio = {currency: 1000.0 for currency in self.currencies}  # Starting amount for each currency
    
    def _generate_exchange_rates(self):
        """
        Generate random exchange rates between 0.5 and 2.0 for the currencies.
        """
        rates = {}
        for currency in self.currencies:
            rates[currency] = round(random.uniform(0.5, 2.0), 2)
        return rates

    def display_exchange_rates(self):
        """
        Display current exchange rates.
        """
        print("\nCurrent Exchange Rates:")
        for currency, rate in self.exchange_rates.items():
            print(f"  1 {currency} = {rate} USD")

    def display_portfolio(self):
        """
        Display the user's portfolio.
        """
        print("\nYour Portfolio:")
        for currency, amount in self.portfolio.items():
            print(f"  {currency}: {amount:.2f}")

    def trade_currency(self, from_currency, to_currency, amount):
        """
        Perform a trade between two currencies.

        :param from_currency: Currency to trade from
        :param to_currency: Currency to trade to
        :param amount: Amount to trade
        """
        try:
            # Validate currency and amount
            if from_currency not in self.currencies or to_currency not in self.currencies:
                raise ValueError("Invalid currency selected.")
            if amount <= 0:
                raise ValueError("Trade amount must be positive.")
            if self.portfolio[from_currency] < amount:
                raise ValueError("Insufficient funds in the source currency.")

            # Calculate the equivalent amount in the target currency
            exchange_rate = self.exchange_rates[to_currency] / self.exchange_rates[from_currency]
            converted_amount = amount * exchange_rate

            # Perform the trade
            self.portfolio[from_currency] -= amount
            self.portfolio[to_currency] += converted_amount

            print(f"\nSuccessfully traded {amount:.2f} {from_currency} to {converted_amount:.2f} {to_currency}.")
        except ValueError as e:
            print(f"\nError: {e}")

    def update_exchange_rates(self):
        """
        Simulate changes in exchange rates.
        """
        self.exchange_rates = self._generate_exchange_rates()
        print("\nExchange rates updated.")

def main():
    """
    Main function to run the forex trading simulation.
    """
    simulator = ForexTradingSimulator()
    print("Welcome to the Forex Trading Simulator!")

    while True:
        print("\nMenu:")
        print("  1. Display Exchange Rates")
        print("  2. Display Portfolio")
        print("  3. Trade Currency")
        print("  4. Update Exchange Rates")
        print("  5. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                simulator.display_exchange_rates()
            elif choice == 2:
                simulator.display_portfolio()
            elif choice == 3:
                from_currency = input("Enter the source currency: ").upper()
                to_currency = input("Enter the target currency: ").upper()
                amount = float(input(f"Enter the amount of {from_currency} to trade: "))
                simulator.trade_currency(from_currency, to_currency, amount)
            elif choice == 4:
                simulator.update_exchange_rates()
            elif choice == 5:
                print("\nThank you for using the Forex Trading Simulator. Goodbye!")
                break
            else:
                print("\nInvalid choice. Please select a valid option.")
        except ValueError:
            print("\nInvalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
```
