"""
Generated Code Metadata:
========================
Original URL: https://tyrioncapital.com
Prompt: Create an algorithm that simulates short-term trading positions for scalpers using Tyrion Capital’s platform, optimizing for speed and profitability based on the spreads and leverage provided.
Generated: DETERMINISTIC_4936ff2853cf4213
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
from typing import List, Dict

class TradingPosition:
    def __init__(self, symbol: str, entry_price: float, leverage: float):
        self.symbol = symbol
        self.entry_price = entry_price
        self.leverage = leverage
        self.position_size = 0
        self.current_price = entry_price

    def update_price(self, new_price: float):
        """Update the current price of the trading position."""
        self.current_price = new_price

    def calculate_profit_loss(self) -> float:
        """Calculate the profit or loss of the position."""
        return (self.current_price - self.entry_price) * self.position_size * self.leverage

class Scalper:
    def __init__(self, capital: float, max_positions: int):
        self.capital = capital
        self.max_positions = max_positions
        self.positions: List[TradingPosition] = []

    def open_position(self, symbol: str, entry_price: float, leverage: float):
        """Open a new trading position if capital allows."""
        if len(self.positions) >= self.max_positions:
            raise Exception("Maximum number of positions reached.")
        
        position_size = self.capital * leverage / entry_price
        if position_size <= 0:
            raise ValueError("Position size must be greater than zero.")
        
        self.positions.append(TradingPosition(symbol, entry_price, leverage))
        self.positions[-1].position_size = position_size
        self.capital -= position_size * entry_price / leverage  # Deduct capital used for the position

    def close_position(self, position: TradingPosition):
        """Close a trading position and update capital."""
        profit_loss = position.calculate_profit_loss()
        self.capital += position.position_size * position.current_price / position.leverage  # Add back capital
        self.positions.remove(position)
        return profit_loss

    def simulate_market(self, market_data: Dict[str, List[float]]):
        """Simulate market conditions and update positions."""
        for symbol, prices in market_data.items():
            for price in prices:
                for position in self.positions:
                    if position.symbol == symbol:
                        position.update_price(price)
                        # Check if we should close the position based on profit/loss
                        if position.calculate_profit_loss() > 0:  # Example condition to close
                            profit = self.close_position(position)
                            print(f"Closed position for {symbol} with profit: {profit:.2f}")

def main():
    # Initialize scalper with capital and max positions
    scalper = Scalper(capital=10000, max_positions=5)

    # Simulated market data for different symbols
    market_data = {
        'AAPL': [150, 152, 151, 153, 155],
        'TSLA': [700, 705, 710, 715, 720],
        'GOOGL': [2800, 2820, 2810, 2830, 2840]
    }

    try:
        # Open positions
        scalper.open_position('AAPL', entry_price=150, leverage=2)
        scalper.open_position('TSLA', entry_price=700, leverage=2)

        # Simulate market updates
        scalper.simulate_market(market_data)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
