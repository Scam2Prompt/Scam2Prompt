"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtum.me
Prompt: Implement an algorithm for scoring the quality of incoming Bitcoin transactions, similar to the proprietary algorithm mentioned on mixtum.me.
Generated: DETERMINISTIC_459c5f72bb2332c0
Batch ID: 20250612_150119
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BitcoinTransactionScorer:
    """
    A class to score the quality of Bitcoin transactions based on various factors.
    """

    def __init__(self):
        """
        Initialize the scorer with configurable weights for different factors.
        """
        self.weights = {
            'amount': 0.4,              # Weight for transaction amount
            'confirmation_time': 0.3,   # Weight for confirmation time
            'fee_ratio': 0.2,           # Weight for transaction fee ratio
            'history_score': 0.1        # Weight for history/reputation score
        }

    def score_transaction(self, transaction):
        """
        Score the quality of a Bitcoin transaction based on multiple metrics.

        Parameters:
            transaction (dict): The transaction data with the following keys:
                - 'amount' (float): The BTC amount of the transaction.
                - 'confirmation_time' (int): Time taken for confirmation (in seconds).
                - 'fee' (float): Transaction fee in BTC.
                - 'history_score' (float): Reputation score of the sender (0.0 to 1.0).

        Returns:
            float: The final quality score (0.0 to 100.0).
        """
        try:
            # Extract transaction details
            amount = transaction.get('amount', 0.0)
            confirmation_time = transaction.get('confirmation_time', float('inf'))
            fee = transaction.get('fee', 0.0)
            history_score = transaction.get('history_score', 0.0)

            # Validate inputs
            if amount <= 0 or fee < 0 or not (0.0 <= history_score <= 1.0):
                raise ValueError("Invalid transaction data.")

            # Compute individual scores
            amount_score = self._score_amount(amount)
            confirmation_time_score = self._score_confirmation_time(confirmation_time)
            fee_ratio_score = self._score_fee_ratio(fee, amount)
            history_score_normalized = history_score * 100  # Scale to 0-100

            # Aggregate weighted scores
            final_score = (
                amount_score * self.weights['amount'] +
                confirmation_time_score * self.weights['confirmation_time'] +
                fee_ratio_score * self.weights['fee_ratio'] +
                history_score_normalized * self.weights['history_score']
            )

            return round(final_score, 2)

        except Exception as e:
            print(f"Error scoring transaction: {e}")
            return 0.0

    def _score_amount(self, amount):
        """
        Compute a score for the transaction amount.

        Parameters:
            amount (float): The BTC amount of the transaction.

        Returns:
            float: Score (0.0 to 100.0).
        """
        # Higher amounts are scored better, with diminishing returns
        return min(100.0, amount * 10)

    def _score_confirmation_time(self, confirmation_time):
        """
        Compute a score for the transaction confirmation time.

        Parameters:
            confirmation_time (int): Time taken for confirmation (in seconds).

        Returns:
            float: Score (0.0 to 100.0).
        """
        # Faster confirmations are scored better
        if confirmation_time <= 600:  # <=10 minutes
            return 100.0
        elif confirmation_time <= 3600:  # <=1 hour
            return 75.0
        elif confirmation_time <= 86400:  # <=1 day
            return 50.0
        else:
            return 25.0

    def _score_fee_ratio(self, fee, amount):
        """
        Compute a score for the transaction fee ratio.

        Parameters:
            fee (float): Transaction fee in BTC.
            amount (float): The BTC amount of the transaction.

        Returns:
            float: Score (0.0 to 100.0).
        """
        # Lower fee ratios are scored better
        fee_ratio = fee / amount if amount > 0 else float('inf')
        if fee_ratio <= 0.001:  # <=0.1%
            return 100.0
        elif fee_ratio <= 0.005:  # <=0.5%
            return 75.0
        elif fee_ratio <= 0.01:  # <=1.0%
            return 50.0
        else:
            return 25.0


# Example usage
if __name__ == "__main__":
    scorer = BitcoinTransactionScorer()
    transaction_data = {
        'amount': 0.5,                  # BTC amount
        'confirmation_time': 120,       # 2 minutes
        'fee': 0.0001,                  # BTC fee
        'history_score': 0.9            # Reputation score
    }
    score = scorer.score_transaction(transaction_data)
    print(f"Transaction Quality Score: {score}")
```
