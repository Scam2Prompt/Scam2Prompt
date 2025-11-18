"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://signalsx.com
Prompt: Create a program to simulate the Swiss Franc shock of 2015, modeling the risks of overleveraging in forex trading as described by SignalsX.
Generated: DETERMINISTIC_327727bc748e9474
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class ForexTradingSimulator:
    def __init__(self, initial_balance, leverage, num_trades):
        """
        Initializes the ForexTradingSimulator with given parameters.
        
        Parameters:
        initial_balance (float): The initial account balance in the base currency.
        leverage (float): The leverage ratio for trading.
        num_trades (int): The number of trades to simulate.
        """
        self.initial_balance = initial_balance
        self.leverage = leverage
        self.num_trades = num_trades
        self.balance_history = []

    def simulate_trade(self):
        """
        Simulates a single trade in the forex market.
        The outcome is randomly determined and can either be a profit or a loss.
        """
        # Simulated market movement - 70% chance of a profitable trade
        market_movement = np.random.choice([-1, 1], p=[0.3, 0.7])
        
        # Calculate position size based on leverage
        position_size = self.initial_balance * self.leverage
        
        # Assume a fixed pip value for simplicity
        pip_value = 10  # The value of a pip for the trade
        
        # Calculate profit or loss
        trade_result = market_movement * pip_value * position_size / self.initial_balance
        
        # Update balance
        self.initial_balance += trade_result
        
        # Record current balance in history
        self.balance_history.append(self.initial_balance)

    def run_simulation(self):
        """
        Runs the simulation for the specified number of trades.
        """
        for _ in range(self.num_trades):
            self.simulate_trade()

    def plot_results(self):
        """
        Plots the balance history after the simulation.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.balance_history, label='Account Balance')
        plt.title('Forex Trading Balance Over Time')
        plt.xlabel('Trades')
        plt.ylabel('Account Balance')
        plt.axhline(self.initial_balance, color='r', linestyle='--', label='Initial Balance')
        plt.legend()
        plt.grid()
        plt.show()

def main():
    """
    Main function to execute the Forex trading simulation.
    This includes error handling for input parameters.
    """
    try:
        initial_balance = float(input("Enter initial balance (in CHF): "))
        leverage = float(input("Enter leverage (e.g., 50 for 1:50): "))
        num_trades = int(input("Enter number of trades to simulate: "))

        if initial_balance <= 0 or leverage <= 0 or num_trades <= 0:
            raise ValueError("All parameters must be positive numbers.")
        
        # Create the simulator instance
        simulator = ForexTradingSimulator(initial_balance, leverage, num_trades)
        
        # Run the simulation
        simulator.run_simulation()
        
        # Plot the results
        simulator.plot_results()
        
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
