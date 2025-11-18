"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Build a function to handle transaction delays and hard resets for blockchain operations, inspired by the "TXN Delay" and "Hard Reset" features on the ICO Protocol site.
Generated: DETERMINISTIC_11dbc6581db976c5
Batch ID: 20250612_153809
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class BlockchainTransactionError(Exception):
    """Custom exception for handling blockchain transaction errors."""
    pass

class BlockchainTransactionHandler:
    def __init__(self, transaction_timeout=30):
        """
        Initializes the transaction handler with a specified timeout.
        
        :param transaction_timeout: Maximum time in seconds to wait for a transaction to complete.
        """
        self.transaction_timeout = transaction_timeout

    def simulate_transaction(self):
        """
        Simulates a blockchain transaction process, randomly succeeding or failing.
        
        :raises BlockchainTransactionError: If the transaction fails.
        """
        if random.choice([True, False]):
            raise BlockchainTransactionError("Transaction failed due to network issue.")

    def handle_transaction_delay(self):
        """
        Handles transaction delays by attempting to process the transaction within the specified timeout.
        
        :raises BlockchainTransactionError: If the transaction fails after the timeout.
        """
        start_time = time.time()
        while True:
            try:
                self.simulate_transaction()
                print("Transaction completed successfully.")
                return
            except BlockchainTransactionError as e:
                current_time = time.time()
                if current_time - start_time > self.transaction_timeout:
                    print("Transaction timed out.")
                    raise
                print(f"Error occurred: {e}. Retrying...")
                time.sleep(2)  # Wait before retrying

    def hard_reset(self):
        """
        Performs a hard reset action, which can be called to reset the transaction handler state.
        This is a placeholder for resetting state in a real implementation.
        """
        print("Performing hard reset...")
        # Logic to reset state can be implemented here
        time.sleep(1)  # Simulating reset time
        print("Hard reset completed.")

if __name__ == "__main__":
    handler = BlockchainTransactionHandler(transaction_timeout=10)
    try:
        handler.handle_transaction_delay()
    except BlockchainTransactionError:
        handler.hard_reset()
```
