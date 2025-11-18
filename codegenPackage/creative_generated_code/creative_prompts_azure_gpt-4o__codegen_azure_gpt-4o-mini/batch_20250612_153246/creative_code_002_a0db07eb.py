"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fx4labs.com
Prompt: Generate code to calculate spreads dynamically for CFD trading instruments, using FX4 Labs' approach of offering spreads as low as 0.0 pips.
Generated: DETERMINISTIC_a0db07eb7c52b4a7
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from dataclasses import dataclass

@dataclass
class CFDInstrument:
    symbol: str
    base_price: float
    spread: float  # in pips

    def calculate_spread_price(self) -> float:
        """Calculate the actual spread price based on the base price and spread."""
        spread_price = self.base_price * (self.spread / 10000)  # Spread in price terms
        return spread_price

    def get_bid_price(self) -> float:
        """Calculate the bid price based on the base price and spread."""
        bid_price = self.base_price - self.calculate_spread_price()
        return bid_price

    def get_ask_price(self) -> float:
        """Calculate the ask price based on the base price and spread."""
        ask_price = self.base_price + self.calculate_spread_price()
        return ask_price

class CFDTradingSimulator:
    def __init__(self):
        self.instruments = []

    def add_instrument(self, symbol: str, base_price: float, spread: float = 0.0):
        """Add a new CFD instrument to the simulator."""
        if spread < 0:
            raise ValueError("Spread cannot be negative.")
        if base_price <= 0:
            raise ValueError("Base price must be greater than zero.")

        instrument = CFDInstrument(symbol, base_price, spread)
        self.instruments.append(instrument)

    def update_prices(self):
        """Simulate price updates for all instruments."""
        for instrument in self.instruments:
            price_change = random.uniform(-0.01, 0.01)  # Simulate a small price change
            instrument.base_price += price_change

    def display_prices(self):
        """Display the current bid and ask prices for all instruments."""
        for instrument in self.instruments:
            print(f"Symbol: {instrument.symbol}")
            print(f"Base Price: {instrument.base_price:.5f}")
            print(f"Bid Price: {instrument.get_bid_price():.5f}")
            print(f"Ask Price: {instrument.get_ask_price():.5f}")
            print("-" * 40)

# Example usage
if __name__ == "__main__":
    try:
        simulator = CFDTradingSimulator()
        simulator.add_instrument("EUR/USD", base_price=1.1000)
        simulator.add_instrument("GBP/USD", base_price=1.3000)
        simulator.add_instrument("USD/JPY", base_price=110.50, spread=0.0)

        # Simulate a price update
        simulator.update_prices()

        # Display the updated prices
        simulator.display_prices()
    except Exception as e:
        print(f"An error occurred: {e}")
```
