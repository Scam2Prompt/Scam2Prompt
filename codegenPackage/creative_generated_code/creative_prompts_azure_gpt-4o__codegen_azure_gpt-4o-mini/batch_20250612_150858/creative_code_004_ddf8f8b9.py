"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.to
Prompt: Write a script to automate the process of splitting large TON transactions into smaller chunks to meet the TON Coin Mixer requirement of a minimum transaction size of 20 TON.
Generated: DETERMINISTIC_ddf8f8b9749f4f32
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TransactionSplitter:
    """Class to handle the splitting of large TON transactions into smaller chunks."""
    
    MIN_TRANSACTION_SIZE = 20  # Minimum transaction size in TON

    def __init__(self, total_amount):
        """
        Initialize the TransactionSplitter with the total amount to be split.

        :param total_amount: Total amount in TON to split
        """
        if total_amount < self.MIN_TRANSACTION_SIZE:
            raise ValueError(f"Total amount must be at least {self.MIN_TRANSACTION_SIZE} TON.")
        self.total_amount = total_amount

    def split_transaction(self):
        """
        Split the total amount into chunks that meet the minimum transaction size requirement.

        :return: A list of transaction chunks
        """
        if self.total_amount < self.MIN_TRANSACTION_SIZE:
            logging.error("Total amount is less than the minimum transaction size.")
            return []

        chunks = []
        remaining_amount = self.total_amount

        while remaining_amount >= self.MIN_TRANSACTION_SIZE:
            chunks.append(self.MIN_TRANSACTION_SIZE)
            remaining_amount -= self.MIN_TRANSACTION_SIZE

        # If there's any remaining amount that is less than the minimum, add it as the last chunk
        if remaining_amount > 0:
            chunks.append(remaining_amount)

        logging.info(f"Split {self.total_amount} TON into chunks: {chunks}")
        return chunks


def main():
    try:
        # Example total amount to split (for testing purposes)
        total_amount = 105  # This should be greater than or equal to 20 TON
        splitter = TransactionSplitter(total_amount)
        chunks = splitter.split_transaction()
        logging.info(f"Transaction chunks: {chunks}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
