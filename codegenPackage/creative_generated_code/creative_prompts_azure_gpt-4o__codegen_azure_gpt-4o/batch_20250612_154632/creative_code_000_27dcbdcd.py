"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aphatradespro.com
Prompt: Write Python code to simulate a "Grid Trading Bot" with adjustable parameters for minimum and maximum investment amounts, as described on Aphatradespro's website.
Generated: DETERMINISTIC_27dcbdcd90fa7844
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

class GridTradingBot:
    """
    A simple grid trading bot that simulates buying and selling within specified price ranges.
    """

    def __init__(self, min_investment: float, max_investment: float, grid_size: int):
        """
        Initialize the trading bot with investment parameters and grid size.

        :param min_investment: Minimum investment amount (float).
        :param max_investment: Maximum investment amount (float).
        :param grid_size: Number of grid levels (int).
        """
        if min_investment <= 0 or max_investment <= 0 or grid_size <= 0:
            raise ValueError("All parameters must be positive values.")
        if min_investment >= max_investment:
            raise ValueError("min_investment must be less than max_investment.")
        
        self.min_investment = min_investment
        self.max_investment = max_investment
        self.grid_size = grid_size
        self.grid = self._generate_grid()
        self.positions = []  # Keeps track of active positions

    def _generate_grid(self):
        """
        Generate price levels for the grid based on the min and max investment.

        :return: List of grid levels (prices).
        """
        step_size = (self.max_investment - self.min_investment) / self.grid_size
        return [self.min_investment + i * step_size for i in range(self.grid_size + 1)]

    def buy(self, price: float):
        """
        Simulate a buy action.

        :param price: The price at which to buy.
        """
        if price < self.min_investment or price > self.max_investment:
            raise ValueError("Price is out of trading range.")
        self.positions.append(price)
        logging.info(f"Buy executed at price: {price}")

    def sell(self, price: float):
        """
        Simulate a sell action.

        :param price: The price at which to sell.
        """
        if price in self.positions:
            self.positions.remove(price)
            logging.info(f"Sell executed at price: {price}")
        else:
            logging.warning(f"No matching buy position found for price: {price}")

    def simulate_market(self, prices: list):
        """
        Simulate market movements and execute trades based on the grid.

        :param prices: List of prices representing market movements.
        """
        for price in prices:
            if price <= self.grid[0]:  # Simulate buying at the lowest grid level
                self.buy(price)
            elif price >= self.grid[-1]:  # Simulate selling at the highest grid level
                self.sell(price)

    def status(self):
        """
        Print the bot's current status, including active positions and grid levels.
        """
        logging.info(f"Active positions: {self.positions}")
        logging.info(f"Grid levels: {self.grid}")


if __name__ == "__main__":
    # Configure logging for the bot
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    try:
        # Example usage
        bot = GridTradingBot(min_investment=100.0, max_investment=500.0, grid_size=5)
        bot.simulate_market([90, 150, 300, 500, 550])
        bot.status()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
