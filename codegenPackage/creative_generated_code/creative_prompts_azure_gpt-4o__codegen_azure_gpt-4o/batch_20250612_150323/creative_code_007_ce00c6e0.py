"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixbtc.online
Prompt: Write code to enforce the restriction that only the first transaction is counted for mixing, ignoring subsequent payments, as specified in the MixBTC mixer rules.
Generated: DETERMINISTIC_ce00c6e0bfd2f676
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading

class MixBTCMixer:
    """
    A class to enforce MixBTC mixer rules: only the first transaction is counted for mixing,
    ignoring any subsequent payments.
    """

    def __init__(self):
        """
        Initializes the mixer with transaction tracking.
        """
        self.lock = threading.Lock()
        self.first_transaction_processed = False  # Tracks if the first transaction has been processed

    def process_transaction(self, transaction_id, amount):
        """
        Processes a transaction if it is the first one; ignores subsequent payments.

        :param transaction_id: Unique identifier of the transaction
        :param amount: Amount in BTC for the transaction
        :return: str indicating success or ignored transaction
        """
        with self.lock:
            if not self.first_transaction_processed:
                # Process the first transaction
                self.first_transaction_processed = True
                # Simulate transaction processing logic here
                return f"Transaction {transaction_id} processed with amount {amount} BTC."
            else:
                # Ignore subsequent transactions
                return f"Transaction {transaction_id} ignored, only first transaction is allowed."

# Example usage:
if __name__ == "__main__":
    mixer = MixBTCMixer()

    # Simulate transactions
    print(mixer.process_transaction("tx001", 0.5))  # Should process
    print(mixer.process_transaction("tx002", 1.0))  # Should be ignored
    print(mixer.process_transaction("tx003", 0.3))  # Should be ignored
```
