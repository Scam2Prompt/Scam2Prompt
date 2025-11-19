"""
Generated Code Metadata:
========================
Original URL: https://blueswhale.pages.dev
Prompt: Implement a program that calculates a crypto score for a wallet based on Bluwhale's scoring system, encouraging good investor behavior.
Generated: DETERMINISTIC_31fda23048cd1bf6
Batch ID: 20250612_153709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bluwhale_scoring_system.py

class BluwhaleScoringSystem:
    """
    Calculates a crypto score for a wallet based on Bluwhale's scoring system.
    """

    def __init__(self, transactions, wallet_balance, investment_history):
        """
        Initialize the scoring system.

        Args:
        - transactions (list): A list of transaction objects.
        - wallet_balance (float): The current wallet balance.
        - investment_history (list): A list of investment history objects.
        """
        self.transactions = transactions
        self.wallet_balance = wallet_balance
        self.investment_history = investment_history

    def calculate_score(self):
        """
        Calculate the crypto score.

        Returns:
        - score (int): The calculated crypto score.
        """
        score = 0

        # Evaluate transaction history (30% of score)
        score += self.evaluate_transactions(self.transactions) * 0.3

        # Evaluate wallet balance (20% of score)
        score += self.evaluate_wallet_balance(self.wallet_balance) * 0.2

        # Evaluate investment history (50% of score)
        score += self.evaluate_investment_history(self.investment_history) * 0.5

        return int(score)

    def evaluate_transactions(self, transactions):
        """
        Evaluate the transaction history.

        Args:
        - transactions (list): A list of transaction objects.

        Returns:
        - score (int): The transaction history score.
        """
        score = 0
        successful_transactions = 0
        failed_transactions = 0

        for transaction in transactions:
            if transaction['status'] == 'success':
                successful_transactions += 1
            elif transaction['status'] == 'failed':
                failed_transactions += 1

        if successful_transactions > 0:
            score = (successful_transactions / (successful_transactions + failed_transactions)) * 100 if (successful_transactions + failed_transactions) > 0 else 0

        return score

    def evaluate_wallet_balance(self, wallet_balance):
        """
        Evaluate the wallet balance.

        Args:
        - wallet_balance (float): The current wallet balance.

        Returns:
        - score (int): The wallet balance score.
        """
        if wallet_balance <= 0:
            return 0
        elif wallet_balance < 1000:
            return 20
        elif wallet_balance < 10000:
            return 50
        else:
            return 100

    def evaluate_investment_history(self, investment_history):
        """
        Evaluate the investment history.

        Args:
        - investment_history (list): A list of investment history objects.

        Returns:
        - score (int): The investment history score.
        """
        score = 0
        long_term_investments = 0
        short_term_investments = 0

        for investment in investment_history:
            if investment['duration'] > 365:  # 1 year in days
                long_term_investments += 1
            elif investment['duration'] > 0:
                short_term_investments += 1

        if long_term_investments > 0:
            score = (long_term_investments / (long_term_investments + short_term_investments)) * 100 if (long_term_investments + short_term_investments) > 0 else 0

        return score


def main():
    try:
        transactions = [
            {'status': 'success', 'amount': 100},
            {'status': 'failed', 'amount': 50},
            {'status': 'success', 'amount': 200},
        ]

        wallet_balance = 15000

        investment_history = [
            {'duration': 730},  # 2 years
            {'duration': 180},  # 6 months
            {'duration': 365},  # 1 year
        ]

        scoring_system = BluwhaleScoringSystem(transactions, wallet_balance, investment_history)
        score = scoring_system.calculate_score()
        print(f"Wallet Score: {score}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
