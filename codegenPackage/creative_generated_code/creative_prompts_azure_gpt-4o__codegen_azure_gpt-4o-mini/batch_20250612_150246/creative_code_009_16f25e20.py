"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kings-tradefx.com
Prompt: Write code to generate weekly profit reports for forex investments, incorporating features like instant withdrawal and reinvestment options, as KINGSTRADE FX provides.
Generated: DETERMINISTIC_16f25e2058bd913d
Batch ID: 20250612_150246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging

# Configure logging for debugging and monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ForexInvestment:
    """Class to manage Forex investments and generate weekly profit reports."""

    def __init__(self, initial_investment):
        """Initialize the ForexInvestment with an initial amount."""
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        self.investment = initial_investment
        self.profit_history = []
        self.withdrawals = []

    def simulate_profit(self):
        """Simulate profit calculation. In a real scenario, this would be replaced by actual market data."""
        # Example logic for simulating profit (could be replaced with real data)
        profit = self.investment * (0.05 * (0.5 - random.random()))  # Random profit within +/- 5%
        self.profit_history.append(profit)
        self.investment += profit
        logging.info(f"Profit for the week: {profit:.2f}. Total investment: {self.investment:.2f}.")

    def generate_weekly_report(self):
        """Generate and return a weekly profit report."""
        report_date = datetime.datetime.now()
        total_profit = sum(self.profit_history)
        report = {
            'date': report_date.strftime('%Y-%m-%d'),
            'total_profit': total_profit,
            'current_investment': self.investment,
            'withdrawals': self.withdrawals
        }
        logging.info(f"Weekly Report: {report}")
        return report

    def withdraw(self, amount):
        """Withdraw a specified amount from the investment."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.investment:
            raise ValueError("Withdrawal amount exceeds current investment.")
        
        self.investment -= amount
        self.withdrawals.append(amount)
        logging.info(f"Withdrawn: {amount:.2f}. Remaining investment: {self.investment:.2f}.")

    def reinvest(self, amount):
        """Reinvest a specified amount back into the investment."""
        if amount <= 0:
            raise ValueError("Reinvestment amount must be greater than zero.")
        
        self.investment += amount
        logging.info(f"Reinvested: {amount:.2f}. New investment total: {self.investment:.2f}.")

# Example usage
if __name__ == "__main__":
    try:
        initial_investment = 1000.00  # Initial investment amount
        forex_account = ForexInvestment(initial_investment)
        
        # Simulate weekly profit for 4 weeks
        for week in range(4):
            forex_account.simulate_profit()

        # Generate weekly report
        report = forex_account.generate_weekly_report()
        
        # Perform withdrawal and reinvestment
        forex_account.withdraw(200)
        forex_account.reinvest(100)

    except ValueError as e:
        logging.error(f"Error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
```
