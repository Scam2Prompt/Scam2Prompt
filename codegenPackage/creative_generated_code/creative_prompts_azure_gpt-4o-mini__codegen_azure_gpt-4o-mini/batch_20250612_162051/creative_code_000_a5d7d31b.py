"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: How can I pass the FTMO challenge using the Props Funded Traders service, and what are the specific steps involved in the evaluation process?
Generated: DETERMINISTIC_a5d7d31b4581346f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FTMOChallenge:
    """
    A class to represent the FTMO Challenge process for the Props Funded Traders service.
    """

    def __init__(self, initial_balance: float, target_profit: float, max_drawdown: float):
        """
        Initializes the FTMOChallenge with initial parameters.

        :param initial_balance: The starting balance for the trading challenge.
        :param target_profit: The profit target needed to pass the challenge.
        :param max_drawdown: The maximum allowable drawdown for the account.
        """
        self.initial_balance = initial_balance
        self.target_profit = target_profit
        self.max_drawdown = max_drawdown
        self.current_balance = initial_balance
        self.highest_balance = initial_balance
        self.trades = []

    def record_trade(self, profit_loss: float):
        """
        Records a trade's profit or loss and updates balances accordingly.

        :param profit_loss: The profit or loss from the trade.
        """
        if not isinstance(profit_loss, (int, float)):
            raise ValueError("Profit/loss must be a numerical value.")
        
        self.current_balance += profit_loss
        self.trades.append(profit_loss)
        self.highest_balance = max(self.highest_balance, self.current_balance)

        # Check for maximum drawdown
        drawdown = self.highest_balance - self.current_balance
        if drawdown > self.max_drawdown:
            raise Exception("Maximum drawdown exceeded. Challenge failed.")

    def is_challenge_passed(self) -> bool:
        """
        Checks if the challenge has been passed based on current balance.

        :return: True if the challenge is passed, otherwise False.
        """
        return self.current_balance >= (self.initial_balance + self.target_profit)

    def challenge_summary(self) -> dict:
        """
        Provides a summary of the challenge results.

        :return: A dictionary containing the initial balance, current balance,
                 total profit, and challenge status.
        """
        total_profit = self.current_balance - self.initial_balance
        return {
            "Initial Balance": self.initial_balance,
            "Current Balance": self.current_balance,
            "Total Profit": total_profit,
            "Challenge Passed": self.is_challenge_passed(),
            "Max Drawdown": self.max_drawdown,
        }


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the FTMO Challenge with given parameters
        ftmo_challenge = FTMOChallenge(initial_balance=10000, target_profit=2000, max_drawdown=1500)

        # Simulate trades
        ftmo_challenge.record_trade(profit_loss=500)  # Trade 1: +500
        ftmo_challenge.record_trade(profit_loss=-200)  # Trade 2: -200
        ftmo_challenge.record_trade(profit_loss=800)  # Trade 3: +800
        ftmo_challenge.record_trade(profit_loss=-300)  # Trade 4: -300

        # Check if the challenge is passed and print summary
        print(ftmo_challenge.challenge_summary())

    except Exception as e:
        print(f"An error occurred: {e}")
```
