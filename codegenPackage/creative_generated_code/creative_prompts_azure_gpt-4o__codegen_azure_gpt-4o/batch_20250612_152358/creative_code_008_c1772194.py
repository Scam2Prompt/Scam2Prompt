"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lite-trades.org
Prompt: Create a program to simulate investment strategies in commodities like jade stone or crude oil, inspired by Lite Trade's commodities exchange service.
Generated: DETERMINISTIC_c17721945a46f9d3
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Commodity:
    """
    Represents a commodity in the market, e.g., jade stone or crude oil.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price  # Current price per unit of the commodity.

    def simulate_price_change(self):
        """
        Simulates price fluctuation for the commodity.
        Prices may increase or decrease randomly within a certain percentage range.
        """
        change_percentage = random.uniform(-5, 5)  # Random price change between -5% to +5%.
        self.price += self.price * (change_percentage / 100)
        self.price = round(self.price, 2)  # Round price to 2 decimal places for better readability.

class InvestmentStrategy:
    """
    Represents an investment strategy for commodities trading.
    """
    def __init__(self, budget):
        self.budget = budget  # Total budget available for investment.
        self.portfolio = {}  # Portfolio containing purchased commodities.

    def buy_commodity(self, commodity, quantity):
        """
        Attempts to buy a specified quantity of a commodity.
        """
        total_cost = commodity.price * quantity
        if total_cost <= self.budget:
            self.budget -= total_cost
            if commodity.name in self.portfolio:
                self.portfolio[commodity.name] += quantity
            else:
                self.portfolio[commodity.name] = quantity
            print(f"Successfully purchased {quantity} units of {commodity.name} at ${commodity.price} per unit.")
        else:
            print(f"Insufficient budget to purchase {quantity} units of {commodity.name}.")

    def sell_commodity(self, commodity, quantity):
        """
        Attempts to sell a specified quantity of a commodity.
        """
        if commodity.name in self.portfolio and self.portfolio[commodity.name] >= quantity:
            self.portfolio[commodity.name] -= quantity
            self.budget += commodity.price * quantity
            print(f"Successfully sold {quantity} units of {commodity.name} at ${commodity.price} per unit.")
        else:
            print(f"Insufficient quantity of {commodity.name} to sell.")

    def portfolio_value(self, commodity_prices):
        """
        Calculates the total value of the portfolio based on current commodity prices.
        """
        value = sum(commodity_prices[commodity] * self.portfolio[commodity] for commodity in self.portfolio)
        return round(value, 2)

def simulate_trading():
    """
    Simulates trading on a commodity exchange.
    """
    print("Welcome to the Commodity Investment Simulator!")
    jade = Commodity("Jade Stone", 100.0)  # Starting price for jade stone.
    crude_oil = Commodity("Crude Oil", 50.0)  # Starting price for crude oil.

    # Initialize an investment strategy with a budget.
    investor = InvestmentStrategy(budget=1000.0)

    # Simulation steps
    for day in range(1, 6):  # Simulate 5 trading days.
        print(f"\nDay {day}:")
        jade.simulate_price_change()
        crude_oil.simulate_price_change()
        print(f"Current prices - Jade Stone: ${jade.price}, Crude Oil: ${crude_oil.price}")

        # Investor randomly buys or sells commodities.
        action = random.choice(["buy", "sell"])
        commodity = random.choice([jade, crude_oil])
        quantity = random.randint(1, 10)

        if action == "buy":
            investor.buy_commodity(commodity, quantity)
        elif action == "sell":
            investor.sell_commodity(commodity, quantity)

        # Display current portfolio status.
        portfolio_value = investor.portfolio_value({jade.name: jade.price, crude_oil.name: crude_oil.price})
        print(f"Portfolio value: ${portfolio_value}, Remaining budget: ${investor.budget}")

    print("\nSimulation complete. Final portfolio:")
    for commodity, quantity in investor.portfolio.items():
        print(f"{commodity}: {quantity} units")
    print(f"Final budget: ${investor.budget}")

if __name__ == "__main__":
    simulate_trading()
```
