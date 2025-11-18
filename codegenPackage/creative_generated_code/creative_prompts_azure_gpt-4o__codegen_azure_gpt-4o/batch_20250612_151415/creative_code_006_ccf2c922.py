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
import statistics
from concurrent.futures import ThreadPoolExecutor

class TransactionMonitor:
    """
    A class to monitor transaction speed and performance under peak loads.
    """

    def __init__(self, peak_load_transactions=1000, max_threads=10):
        """
        Initialize the monitor with the given peak load and thread pool.
        
        :param peak_load_transactions: Number of transactions to simulate during peak load.
        :param max_threads: Number of threads to use for concurrency.
        """
        self.peak_load_transactions = peak_load_transactions
        self.max_threads = max_threads
        self.transaction_times = []

    def simulate_transaction(self):
        """
        Simulate a single transaction. In a real-world scenario, this would involve
        actual transaction processing logic.
        
        :return: The time taken to process the transaction in seconds.
        """
        try:
            # Simulate transaction processing time (random between 1ms to 100ms)
            processing_time = random.uniform(0.001, 0.1)
            time.sleep(processing_time)  # Simulate the delay
            return processing_time
        except Exception as e:
            print(f"Error during transaction simulation: {e}")
            return None

    def monitor_transactions(self):
        """
        Run peak load simulations and monitor transaction performance.
        
        :return: Summary of transaction performance metrics.
        """
        print(f"Starting monitoring of {self.peak_load_transactions} transactions...")
        start_time = time.time()

        # Use ThreadPoolExecutor for concurrent transaction simulation
        with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
            # Submit tasks and collect results
            results = list(executor.map(lambda _: self.simulate_transaction(), range(self.peak_load_transactions)))

        end_time = time.time()
        self.transaction_times = [r for r in results if r is not None]

        # Calculate performance metrics
        if self.transaction_times:
            avg_time = statistics.mean(self.transaction_times)
            max_time = max(self.transaction_times)
            min_time = min(self.transaction_times)
            total_time = end_time - start_time
            throughput = self.peak_load_transactions / total_time  # Transactions per second

            # Return summary
            return {
                "average_time": avg_time,
                "max_time": max_time,
                "min_time": min_time,
                "total_time": total_time,
                "throughput": throughput,
                "successful_transactions": len(self.transaction_times),
                "failed_transactions": self.peak_load_transactions - len(self.transaction_times)
            }
        else:
            return {
                "error": "No transactions successfully completed."
            }

if __name__ == "__main__":
    # Example usage of the TransactionMonitor
    peak_load_transactions = 1000  # Number of transactions to simulate
    max_threads = 20  # Number of threads to use for concurrency

    monitor = TransactionMonitor(peak_load_transactions, max_threads)
    performance_metrics = monitor.monitor_transactions()

    if "error" in performance_metrics:
        print(performance_metrics["error"])
    else:
        print("Transaction Performance Metrics:")
        print(f"Average Transaction Time: {performance_metrics['average_time']:.4f} seconds")
        print(f"Max Transaction Time: {performance_metrics['max_time']:.4f} seconds")
        print(f"Min Transaction Time: {performance_metrics['min_time']:.4f} seconds")
        print(f"Total Time for All Transactions: {performance_metrics['total_time']:.4f} seconds")
        print(f"Throughput: {performance_metrics['throughput']:.2f} transactions/second")
        print(f"Successful Transactions: {performance_metrics['successful_transactions']}")
        print(f"Failed Transactions: {performance_metrics['failed_transactions']}")
```
