"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypton-exchange.com
Prompt: Write a program to monitor transaction speed and performance under peak loads, similar to Crypton Exchange's high-performance capabilities.
Generated: DETERMINISTIC_ccf2c9228b91f9a3
Batch ID: 20250612_151415
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
import threading
import logging
from queue import Queue

# Configure logging for better visibility of the performance monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Transaction:
    """A class to represent a transaction with a unique ID and processing time."""

    def __init__(self, transaction_id):
        self.transaction_id = transaction_id
        self.process_time = random.uniform(0.01, 0.1)  # Simulated processing time in seconds

class TransactionProcessor:
    """A class to simulate processing transactions and measuring performance."""

    def __init__(self, max_transactions):
        self.transaction_queue = Queue(maxsize=max_transactions)
        self.processed_count = 0
        self.start_time = time.time()

    def simulate_transaction(self):
        """Simulate a transaction and add it to the queue."""
        transaction_id = self.processed_count + 1
        transaction = Transaction(transaction_id)
        self.transaction_queue.put(transaction)
        logging.info(f"Transaction {transaction.transaction_id} added to the queue.")

    def process_transactions(self):
        """Process transactions from the queue."""
        while True:
            try:
                transaction = self.transaction_queue.get(timeout=1)  # Wait for a transaction to process
                
                # Simulating processing time
                time.sleep(transaction.process_time)
                self.processed_count += 1

                logging.info(f"Processed transaction {transaction.transaction_id} in {transaction.process_time:.2f} seconds.")
                self.transaction_queue.task_done()

            except Exception as e:
                logging.error(f"Error processing transaction: {str(e)}")
                break

    def monitor_performance(self):
        """Monitor the performance of transaction processing."""
        while self.processed_count < 100:  # Example: Monitor until 100 transactions processed
            elapsed_time = time.time() - self.start_time
            transactions_per_second = self.processed_count / elapsed_time if elapsed_time > 0 else 0
            logging.info(f"Transactions processed: {self.processed_count}, TPS: {transactions_per_second:.2f}")
            time.sleep(1)

def main():
    """Main function to control the transaction monitoring system."""
    MAX_TRANSACTIONS = 10
    transaction_processor = TransactionProcessor(max_transactions=MAX_TRANSACTIONS)

    # Starting transaction processing thread
    processing_thread = threading.Thread(target=transaction_processor.process_transactions)
    processing_thread.daemon = True  # This will allow the program to exit even if this thread is running
    processing_thread.start()

    # Simulating adding transactions at peak load
    try:
        for _ in range(100):  # Example: Add 100 transactions
            transaction_processor.simulate_transaction()
            time.sleep(random.uniform(0.01, 0.05))  # Simulate peak load with variable transaction arrival times
    except Exception as e:
        logging.error(f"Error in main execution: {str(e)}")

    # Start monitoring performance
    transaction_processor.monitor_performance()

if __name__ == "__main__":
    main()
```
