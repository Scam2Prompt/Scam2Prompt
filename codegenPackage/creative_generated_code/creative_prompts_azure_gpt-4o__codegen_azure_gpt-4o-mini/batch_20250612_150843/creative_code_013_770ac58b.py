"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theimmediateavage-360.com
Prompt: Create a Python program to simulate Immediate Avage 360's profit calculation based on trading parameters, stake size, and risk management strategies.
Generated: DETERMINISTIC_770ac58b1dd8ae64
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

class TradingSimulator:
    """
    A class to simulate profit calculation for Immediate Avage 360's trading system.
    """

    def __init__(self, stake_size, risk_per_trade, win_rate):
        """
        Initializes the trading simulator with given parameters.
        
        :param stake_size: The amount of money staked on each trade.
        :param risk_per_trade: The maximum percentage of the stake that can be risked on a single trade.
        :param win_rate: The probability of winning a trade (between 0 and 1).
        """
        self.stake_size = stake_size
        self.risk_per_trade = risk_per_trade
        self.win_rate = win_rate

    def calculate_profit(self, number_of_trades):
        """
        Simulates a series of trades and calculates the profit.
        
        :param number_of_trades: The total number of trades to simulate.
        :return: The total profit after the specified number of trades.
        """
        total_profit = 0
        
        for trade in range(number_of_trades):
            outcome = self.simulate_trade()
            total_profit += outcome
        
        return total_profit

    def simulate_trade(self):
        """
        Simulates a single trade and returns the profit or loss for that trade.
        
        :return: Profit if the trade is won, otherwise loss.
        """
        if random.random() <= self.win_rate:
            # Trade won
            profit = self.stake_size * (1 - self.risk_per_trade)
            return profit
        else:
            # Trade lost
            loss = self.stake_size * self.risk_per_trade
            return -loss

def main():
    """
    Main function to run the trading simulator.
    """
    try:
        # Define parameters for the trading simulation
        stake_size = float(input("Enter the stake size per trade: "))
        risk_per_trade = float(input("Enter the risk per trade (as a percentage, e.g., 0.05 for 5%): "))
        win_rate = float(input("Enter the win rate (between 0 and 1): "))
        number_of_trades = int(input("Enter the number of trades to simulate: "))

        # Validate input values
        if not (0 < risk_per_trade < 1):
            raise ValueError("Risk per trade must be between 0 and 1.")
        if not (0 <= win_rate <= 1):
            raise ValueError("Win rate must be between 0 and 1.")
        if number_of_trades <= 0:
            raise ValueError("Number of trades must be a positive integer.")

        # Create a TradingSimulator instance and calculate profit
        simulator = TradingSimulator(stake_size, risk_per_trade, win_rate)
        total_profit = simulator.calculate_profit(number_of_trades)

        # Display the results
        print(f"Total profit after {number_of_trades} trades: ${total_profit:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
