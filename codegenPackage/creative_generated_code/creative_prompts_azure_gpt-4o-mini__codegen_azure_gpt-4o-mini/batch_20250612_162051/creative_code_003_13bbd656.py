"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Generate a sample trading plan that aims for a 10% return per month, considering the parameters set by Props Funded Traders for their funded accounts.
Generated: DETERMINISTIC_13bbd65696eb51ff
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Set up logging for better visibility into the execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TradingPlan:
    def __init__(self, initial_capital: float, target_return: float, risk_per_trade: float, max_drawdown: float):
        """
        Initialize the trading plan with the given parameters.

        :param initial_capital: The starting capital for trading.
        :param target_return: The desired percentage return per month (as a decimal).
        :param risk_per_trade: The percentage of capital risked on each trade (as a decimal).
        :param max_drawdown: The maximum acceptable drawdown percentage (as a decimal).
        """
        self.initial_capital = initial_capital
        self.target_return = target_return
        self.risk_per_trade = risk_per_trade
        self.max_drawdown = max_drawdown
        self.current_capital = initial_capital
        self.drawdown = 0

    def simulate_trade(self):
        """
        Simulates a trade outcome using a random profit/loss generator.
        The trade outcome is determined by win/loss probabilities and risk.

        :return: None
        """
        # Randomly determine if the trade is a win or a loss
        if random.random() < 0.55:  # 55% chance of winning
            trade_profit = self.current_capital * self.risk_per_trade * 1.5  # Win 150% of risked amount
            logging.info(f"Trade Win: Profit = {trade_profit:.2f}")
            self.current_capital += trade_profit
        else:
            trade_loss = self.current_capital * self.risk_per_trade  # Lose risked amount
            logging.info(f"Trade Loss: Loss = {trade_loss:.2f}")
            self.current_capital -= trade_loss

        self.update_drawdown()

    def update_drawdown(self):
        """
        Updates the current drawdown based on the current capital.

        :return: None
        """
        if self.current_capital < self.initial_capital:
            drawdown = (self.initial_capital - self.current_capital) / self.initial_capital
            self.drawdown = max(self.drawdown, drawdown)

    def check_plan_sustainability(self):
        """
        Checks if the trading plan is still sustainable based on drawdown.

        :return: bool indicating sustainability
        """
        return self.drawdown <= self.max_drawdown

    def run_monthly_simulation(self, num_trades: int):
        """
        Run a monthly simulation of trades.

        :param num_trades: The number of trades to simulate in a month.
        :return: None
        """
        for trade in range(num_trades):
            self.simulate_trade()
            if not self.check_plan_sustainability():
                logging.warning("Max drawdown exceeded! Consider revising the trading strategy.")
                break

    def calculate_return(self):
        """
        Calculate the return achieved after trading.

        :return: The percentage return achieved.
        """
        return (self.current_capital - self.initial_capital) / self.initial_capital

def main():
    try:
        # Parameters for the trading plan
        initial_capital = 10000.0  # Starting capital
        target_return = 0.10  # Target return of 10%
        risk_per_trade = 0.02  # Risking 2% of capital per trade
        max_drawdown = 0.20  # Maximum drawdown of 20%

        # Create a TradingPlan instance
        trading_plan = TradingPlan(initial_capital, target_return, risk_per_trade, max_drawdown)

        # Run the monthly trading simulation with a specified number of trades
        trading_plan.run_monthly_simulation(num_trades=20)  # Simulating 20 trades in a month

        # Calculate and log the return
        achieved_return = trading_plan.calculate_return()
        logging.info(f"Achieved Return: {achieved_return:.2%}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
