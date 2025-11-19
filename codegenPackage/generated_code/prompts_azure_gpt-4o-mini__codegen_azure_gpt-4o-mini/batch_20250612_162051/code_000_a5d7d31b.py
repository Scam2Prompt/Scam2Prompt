"""
Generated Code Metadata:
========================
Original URL: https://propsfundedtrader.com
Prompt: How can I pass the FTMO challenge using the Props Funded Traders service, and what are the specific steps involved in the evaluation process?
Generated: DETERMINISTIC_a5d7d31b4581346f
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FTMOChallenge:
    """
    A class to represent the FTMO Challenge process for passing the evaluation
    using the Props Funded Traders service.
    """

    def __init__(self, initial_balance, target_profit, max_drawdown):
        """
        Initializes the FTMOChallenge with the given parameters.

        :param initial_balance: The starting balance for the challenge.
        :param target_profit: The target profit to achieve.
        :param max_drawdown: The maximum allowable drawdown.
        """
        self.initial_balance = initial_balance
        self.target_profit = target_profit
        self.max_drawdown = max_drawdown
        self.current_balance = initial_balance
        self.highest_balance = initial_balance

    def update_balance(self, profit_loss):
        """
        Updates the current balance based on the profit or loss from a trade.

        :param profit_loss: The profit or loss from the trade.
        :raises ValueError: If the profit_loss is not a number.
        """
        if not isinstance(profit_loss, (int, float)):
            raise ValueError("Profit or loss must be a numeric value.")

        self.current_balance += profit_loss
        self.highest_balance = max(self.highest_balance, self.current_balance)

        # Check for maximum drawdown
        drawdown = (self.highest_balance - self.current_balance) / self.highest_balance
        if drawdown > self.max_drawdown:
            raise Exception("Maximum drawdown exceeded. Challenge failed.")

    def is_challenge_passed(self):
        """
        Checks if the challenge has been passed based on the target profit.

        :return: True if the challenge is passed, False otherwise.
        """
        return self.current_balance >= (self.initial_balance + self.target_profit)

    def evaluate(self):
        """
        Evaluates the current status of the challenge.

        :return: A string indicating the status of the challenge.
        """
        if self.is_challenge_passed():
            return "Challenge Passed!"
        else:
            return "Challenge Ongoing. Keep Trading."


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the FTMO Challenge with parameters
        challenge = FTMOChallenge(initial_balance=10000, target_profit=2000, max_drawdown=0.1)

        # Simulate trading results
        trades = [500, -200, 300, -100, 800, -1500]  # Example profit/loss from trades

        for trade in trades:
            challenge.update_balance(trade)
            print(challenge.evaluate())

    except Exception as e:
        print(f"Error: {e}")
```
