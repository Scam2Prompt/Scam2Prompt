"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longtradegroup.com
Prompt: Create a script to simulate the profit accumulation over 100 days for an investment in the LongTradeGroup USD Plan, factoring in daily payouts and allowing additional investments.
Generated: DETERMINISTIC_0c3c6e7eca6e0c52
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

class LongTradeGroupInvestment:
    """
    A class to simulate profit accumulation over 100 days for the LongTradeGroup USD Plan.
    """
    def __init__(self, initial_investment, daily_rate):
        """
        Initialize the investment object.
        
        :param initial_investment: The initial amount invested (float).
        :param daily_rate: The fixed daily payout rate as a percentage (e.g., 1.5 for 1.5% daily).
        """
        self.balance = initial_investment
        self.daily_rate = daily_rate / 100  # Convert percentage to decimal
        self.history = []  # To track daily balance and transactions

    def add_investment(self, amount, day):
        """
        Add additional investment to the current balance.
        
        :param amount: The amount to add to the balance (float).
        :param day: The day of the additional investment (int).
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        self.balance += amount
        self.history.append({"day": day, "action": "additional_investment", "amount": amount})

    def simulate(self, days=100):
        """
        Simulate the profit accumulation for a given number of days.
        
        :param days: The number of days to simulate (default: 100).
        :return: The final balance after simulation.
        """
        for day in range(1, days + 1):
            # Calculate daily payout
            daily_payout = self.balance * self.daily_rate
            # Add daily payout to the balance
            self.balance += daily_payout
            # Record daily payout in history
            self.history.append({"day": day, "action": "daily_payout", "amount": daily_payout})
            
            # Simulate random additional investment for demonstration (optional)
            if random.random() < 0.1:  # 10% chance of additional investment on any day
                additional_investment = random.uniform(10, 100)  # Random amount between $10 and $100
                self.add_investment(additional_investment, day)
        
        return self.balance

    def get_history(self):
        """
        Get the transaction history.
        
        :return: A list of all transactions and payouts.
        """
        return self.history


# Main script
if __name__ == "__main__":
    try:
        # Initialize the investment with an initial amount and a daily payout rate
        initial_investment = 1000.0  # Initial investment in USD
        daily_rate = 1.5  # Daily payout rate in percentage
        investment = LongTradeGroupInvestment(initial_investment, daily_rate)
        
        # Simulate profit accumulation for 100 days
        final_balance = investment.simulate(days=100)
        
        # Print final balance and transaction history
        print(f"Final Balance after 100 days: ${final_balance:.2f}")
        print("\nTransaction History:")
        for entry in investment.get_history():
            print(f"Day {entry['day']}: {entry['action']} of ${entry['amount']:.2f}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
