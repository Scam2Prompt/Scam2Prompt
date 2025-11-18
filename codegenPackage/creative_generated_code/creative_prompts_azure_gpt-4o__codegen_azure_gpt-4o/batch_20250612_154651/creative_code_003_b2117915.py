"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qiananjs.com
Prompt: Create a program to simulate trading scenarios for crude oil and copper using FXCG's off-market commodity trading options and MT4 platform features.
Generated: DETERMINISTIC_b21179158ed4cf3c
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CommodityTradingSimulator:
    """
    A class to simulate trading scenarios for crude oil and copper using FXCG's off-market
    commodity trading options and MT4 platform features.
    """

    def __init__(self):
        """
        Initializes the simulator with trading parameters and market data.
        """
        self.commodities = {
            "Crude Oil": {"price": 80.0},  # Starting price in USD per barrel
            "Copper": {"price": 4.0}  # Starting price in USD per pound
        }
        self.trade_history = []

    def simulate_trade(self, commodity, trade_type, trade_amount):
        """
        Simulates a trade for the specified commodity.

        Args:
            commodity (str): Name of the commodity ("Crude Oil" or "Copper").
            trade_type (str): Type of trade ("BUY" or "SELL").
            trade_amount (float): Amount of commodity to trade.

        Returns:
            dict: Details of the executed trade.
        """
        if commodity not in self.commodities:
            raise ValueError(f"Unsupported commodity: {commodity}")

        if trade_type not in ["BUY", "SELL"]:
            raise ValueError(f"Unsupported trade type: {trade_type}")

        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")

        # Simulate price fluctuation
        market_price = self.commodities[commodity]["price"]
        price_fluctuation = random.uniform(-0.05 * market_price, 0.05 * market_price)  # +/- 5% fluctuation
        new_price = round(market_price + price_fluctuation, 2)
        self.commodities[commodity]["price"] = new_price

        # Record trade details
        trade = {
            "commodity": commodity,
            "type": trade_type,
            "amount": trade_amount,
            "price_at_trade": new_price
        }
        self.trade_history.append(trade)

        return trade

    def get_market_data(self):
        """
        Returns the current market data for all commodities.

        Returns:
            dict: Current market prices of commodities.
        """
        return {commodity: data["price"] for commodity, data in self.commodities.items()}

    def get_trade_history(self):
        """
        Returns the history of executed trades.

        Returns:
            list: List of trade records.
        """
        return self.trade_history


def main():
    """
    Main function to demonstrate trading scenarios.
    """
    try:
        # Initialize the trading simulator
        simulator = CommodityTradingSimulator()

        # Display initial market data
        print("Initial Market Data:")
        print(simulator.get_market_data())

        # Simulate a BUY trade for Crude Oil
        trade_1 = simulator.simulate_trade("Crude Oil", "BUY", 100)
        print("\nExecuted Trade 1:")
        print(trade_1)

        # Simulate a SELL trade for Copper
        trade_2 = simulator.simulate_trade("Copper", "SELL", 50)
        print("\nExecuted Trade 2:")
        print(trade_2)

        # Display updated market data
        print("\nUpdated Market Data:")
        print(simulator.get_market_data())

        # Display trade history
        print("\nTrade History:")
        print(simulator.get_trade_history())

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
