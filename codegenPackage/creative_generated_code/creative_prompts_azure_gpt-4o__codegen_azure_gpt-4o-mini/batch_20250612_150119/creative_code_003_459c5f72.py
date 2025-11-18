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
import hashlib
import json
from typing import Dict, Any

class BitcoinTransactionScorer:
    """
    A class to score the quality of incoming Bitcoin transactions based on certain criteria.
    """
    
    def __init__(self, transaction: Dict[str, Any]) -> None:
        """
        Initializes the scorer with a transaction.

        :param transaction: A dictionary representing the Bitcoin transaction.
        """
        self.transaction = transaction
        self.score = 0.0

    def validate_transaction(self) -> bool:
        """
        Validates the transaction structure.

        :return: True if the transaction is valid, False otherwise.
        """
        required_fields = ['txid', 'inputs', 'outputs']
        for field in required_fields:
            if field not in self.transaction:
                return False
        return True

    def score_transaction(self) -> float:
        """
        Calculate the quality score of the transaction based on predefined criteria.

        :return: A score between 0 and 100 representing transaction quality.
        """
        if not self.validate_transaction():
            raise ValueError("Invalid transaction structure.")
        
        # Example scoring criteria
        self.score += self.score_input_output_ratio()
        self.score += self.score_transaction_age()
        self.score += self.score_transaction_fee()
        
        # Normalize score to be between 0 and 100
        self.score = min(max(self.score, 0), 100)
        return self.score

    def score_input_output_ratio(self) -> float:
        """
        Scores based on the ratio of inputs to outputs.

        :return: A score contribution based on the input-output ratio.
        """
        num_inputs = len(self.transaction['inputs'])
        num_outputs = len(self.transaction['outputs'])
        
        # Prevent division by zero
        if num_outputs == 0:
            return 0
        
        ratio = num_inputs / num_outputs
        return max(0, min(100, 100 - (ratio * 20)))

    def score_transaction_age(self) -> float:
        """
        Scores based on the age of the transaction.

        :return: A score contribution based on the transaction's age.
        """
        # Assume 'age' is provided in seconds in the transaction
        transaction_age = self.transaction.get('age', 0)
        max_age = 604800  # 7 days in seconds
        
        # Score decreases with age; newer transactions are better
        return max(0, min(100, 100 - (transaction_age / max_age * 100)))

    def score_transaction_fee(self) -> float:
        """
        Scores based on the transaction fee.

        :return: A score contribution based on the transaction fee.
        """
        fee = self.transaction.get('fee', 0)
        max_fee = 0.001  # Example max fee in BTC
        
        # Lower fees are better
        return max(0, min(100, 100 - (fee / max_fee * 100)))

# Example usage
if __name__ == "__main__":
    transaction_example = {
        "txid": "abc123",
        "inputs": [{"address": "addr1", "amount": 0.01}],
        "outputs": [{"address": "addr2", "amount": 0.009}],
        "age": 3600,  # 1 hour old
        "fee": 0.0001
    }

    scorer = BitcoinTransactionScorer(transaction_example)
    try:
        score = scorer.score_transaction()
        print(f"Transaction Score: {score:.2f}")
    except ValueError as e:
        print(f"Error scoring transaction: {e}")
```
