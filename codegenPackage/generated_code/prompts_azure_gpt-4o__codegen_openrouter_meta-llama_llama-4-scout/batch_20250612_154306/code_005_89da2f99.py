"""
Generated Code Metadata:
========================
Original URL: https://pipelinefinanceconseil.com
Prompt: Develop a tool to simulate quarterly withdrawals for the "Epargne Revenus" formula, ensuring compliance with the withdrawal conditions outlined on pipelinefinanceconseil.com.
Generated: DETERMINISTIC_89da2f994b6ec1cc
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Epargne Revenus Simulator

Simulates quarterly withdrawals for the "Epargne Revenus" formula,
ensuring compliance with the withdrawal conditions.

Author: [Your Name]
Date: [Today's Date]
"""

import datetime

class EpargneRevenusSimulator:
    def __init__(self, initial_capital, quarterly_withdrawal, 
                 withdrawal_percentage, years):
        """
        Initializes the simulator.

        Args:
            initial_capital (float): Initial capital amount.
            quarterly_withdrawal (float): Quarterly withdrawal amount.
            withdrawal_percentage (float): Percentage of capital for withdrawal.
            years (int): Number of years to simulate.
        """
        self.initial_capital = initial_capital
        self.quarterly_withdrawal = quarterly_withdrawal
        self.withdrawal_percentage = withdrawal_percentage / 100
        self.years = years
        self.current_capital = initial_capital
        self.withdrawal_history = []

    def simulate_quarterly_withdrawals(self):
        """
        Simulates quarterly withdrawals for the specified number of years.

        Returns:
            list: List of withdrawal history.
        """
        for year in range(self.years):
            for quarter in range(4):
                if self.can_withdraw():
                    self.withdraw()
                self.record_withdrawal()

        return self.withdrawal_history

    def can_withdraw(self):
        """
        Checks if a withdrawal is allowed based on the withdrawal conditions.

        Returns:
            bool: True if withdrawal is allowed, False otherwise.
        """
        # Assuming the conditions are:
        # 1. The current capital is greater than 0.
        # 2. The quarterly withdrawal does not exceed the allowed percentage of the current capital.
        return (self.current_capital > 0 and 
                self.quarterly_withdrawal <= self.current_capital * self.withdrawal_percentage)

    def withdraw(self):
        """
        Performs a quarterly withdrawal.
        """
        self.current_capital -= self.quarterly_withdrawal

    def record_withdrawal(self):
        """
        Records the current withdrawal.
        """
        self.withdrawal_history.append({
            'date': datetime.datetime.now() + datetime.timedelta(days=(self.years * 365) + (len(self.withdrawal_history) * 91)),
            'withdrawal_amount': self.quarterly_withdrawal,
            'current_capital': self.current_capital
        })

def main():
    try:
        simulator = EpargneRevenusSimulator(
            initial_capital=100000,
            quarterly_withdrawal=5000,
            withdrawal_percentage=2,
            years=10
        )

        withdrawal_history = simulator.simulate_quarterly_withdrawals()

        for withdrawal in withdrawal_history:
            print(f"Date: {withdrawal['date']}, Withdrawal Amount: {withdrawal['withdrawal_amount']}, Current Capital: {withdrawal['current_capital']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
