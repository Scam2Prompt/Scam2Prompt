"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tensxair.web.app
Prompt: Implement a script to track and display real-time TPS (transactions per second) data for Tensor's NFT marketplace.
Generated: DETERMINISTIC_be1639bd79746a57
Batch ID: 20250612_150557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
import random  # Mock data source for demonstration
from collections import deque

class TPSMonitor:
    """
    A class to monitor and display Transactions Per Second (TPS) in real-time.
    """

    def __init__(self, window_size=60):
        """
        Initialize the TPSMonitor.

        :param window_size: The time window (in seconds) over which TPS is calculated.
        """
        self.window_size = window_size  # Sliding window size in seconds
        self.transactions = deque()  # Stores timestamps of transactions
        self.lock = threading.Lock()  # Thread-safe lock for data consistency

    def record_transaction(self):
        """
        Record the occurrence of a transaction at the current time.
        """
        with self.lock:
            current_time = time.time()
            self.transactions.append(current_time)

            # Remove transactions outside the sliding window
            while self.transactions and self.transactions[0] < current_time - self.window_size:
                self.transactions.popleft()

    def get_tps(self):
        """
        Calculate the current Transactions Per Second (TPS).

        :return: The current TPS value.
        """
        with self.lock:
            current_time = time.time()
            
            # Remove old transactions outside the sliding window
            while self.transactions and self.transactions[0] < current_time - self.window_size:
                self.transactions.popleft()

            # TPS is the count of transactions in the current window divided by the window size
            return len(self.transactions) / self.window_size if self.transactions else 0

    def start_real_time_display(self, interval=1):
        """
        Continuously display the TPS at regular intervals.

        :param interval: Time interval (in seconds) between TPS updates.
        """
        def display_loop():
            while True:
                tps = self.get_tps()
                print(f"Current TPS: {tps:.2f}")
                time.sleep(interval)

        display_thread = threading.Thread(target=display_loop, daemon=True)
        display_thread.start()


# Mock integration for demonstration
if __name__ == "__main__":
    monitor = TPSMonitor(window_size=60)

    # Start real-time TPS display
    monitor.start_real_time_display(interval=2)

    # Simulate incoming transactions
    try:
        while True:
            # Simulate random transaction bursts
            transaction_count = random.randint(1, 5)
            for _ in range(transaction_count):
                monitor.record_transaction()
            time.sleep(random.uniform(0.1, 0.5))  # Random delay between bursts
    except KeyboardInterrupt:
        print("\nStopped TPS monitoring.")
```
