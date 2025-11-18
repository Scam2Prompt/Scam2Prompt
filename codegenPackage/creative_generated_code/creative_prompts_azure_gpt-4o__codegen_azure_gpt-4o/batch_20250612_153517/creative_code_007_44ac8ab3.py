"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holddao.web.app
Prompt: Generate a script to track and display real-time TPS (transactions per second) data from the Tensor platform.
Generated: DETERMINISTIC_44ac8ab3aea39342
Batch ID: 20250612_153517
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
from collections import deque

# Constants
WINDOW_SIZE_SECONDS = 10  # Time window to calculate TPS
DISPLAY_INTERVAL_SECONDS = 1  # Interval at which TPS is displayed

# Thread-safe deque to store transaction timestamps
transaction_timestamps = deque()
lock = threading.Lock()

def simulate_transactions():
    """
    Simulates transactions being processed in real-time.
    This function generates random transactions at random intervals.
    """
    while True:
        # Simulate a transaction by adding the current timestamp to the deque
        with lock:
            transaction_timestamps.append(time.time())
        # Sleep for a random interval between 0.01 and 0.1 seconds
        time.sleep(random.uniform(0.01, 0.1))

def calculate_tps():
    """
    Calculates and displays the current Transactions Per Second (TPS)
    based on the timestamps stored in the deque within the defined time window.
    """
    while True:
        with lock:
            # Get the current time
            now = time.time()
            # Remove transactions outside the time window
            while transaction_timestamps and transaction_timestamps[0] < now - WINDOW_SIZE_SECONDS:
                transaction_timestamps.popleft()
            # Calculate TPS
            tps = len(transaction_timestamps) / WINDOW_SIZE_SECONDS

        # Display TPS
        print(f"Current TPS: {tps:.2f}")

        # Sleep for the display interval
        time.sleep(DISPLAY_INTERVAL_SECONDS)

def main():
    """
    Main function to start the transaction simulation and TPS calculation threads.
    """
    try:
        # Start transaction simulation in a separate thread
        transaction_thread = threading.Thread(target=simulate_transactions, daemon=True)
        transaction_thread.start()

        # Start TPS calculation and display in the main thread
        calculate_tps()
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()
```
