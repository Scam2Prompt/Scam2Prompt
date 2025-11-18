"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polymarketscanner.com
Prompt: Write code to implement a "flush interval" mechanism for real-time polling data, inspired by Polymarket Scanner's system.
Generated: DETERMINISTIC_b110366ae11be06c
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time
from typing import Callable, List

class FlushIntervalManager:
    """
    FlushIntervalManager class manages a flush interval mechanism to process real-time polling data.
    Data is collected over a specified interval, and then flushed (processed) using a callback function.
    """
    def __init__(self, interval_seconds: int, flush_callback: Callable[[List[dict]], None]):
        """
        Initializes the FlushIntervalManager.

        Args:
            interval_seconds (int): The flush interval in seconds.
            flush_callback (Callable[[List[dict]], None]): A callback function to process the flushed data.
        """
        if interval_seconds <= 0:
            raise ValueError("interval_seconds must be greater than zero.")
        if not callable(flush_callback):
            raise ValueError("flush_callback must be callable.")

        self.interval_seconds = interval_seconds
        self.flush_callback = flush_callback
        self.data_buffer = []  # Buffer to store polling data
        self.lock = threading.Lock()  # Thread-safe lock
        self.running = False  # Flag to manage the flush thread
        self.flush_thread = None

    def start(self):
        """
        Starts the flush interval mechanism.
        """
        if self.running:
            raise RuntimeError("FlushIntervalManager is already running.")
        self.running = True
        self.flush_thread = threading.Thread(target=self._flush_loop, daemon=True)
        self.flush_thread.start()

    def stop(self):
        """
        Stops the flush interval mechanism.
        """
        self.running = False
        if self.flush_thread:
            self.flush_thread.join()

    def add_data(self, data: dict):
        """
        Adds new polling data to the buffer.

        Args:
            data (dict): The data to be added to the buffer.
        """
        if not isinstance(data, dict):
            raise ValueError("data must be a dictionary.")
        
        with self.lock:
            self.data_buffer.append(data)

    def _flush_loop(self):
        """
        Internal loop that flushes data at regular intervals.
        """
        while self.running:
            time.sleep(self.interval_seconds)
            self._flush_data()

    def _flush_data(self):
        """
        Flushes the data buffer and triggers the callback.
        """
        with self.lock:
            if self.data_buffer:
                # Pass the buffer to the callback and clear it
                try:
                    self.flush_callback(self.data_buffer)
                except Exception as e:
                    # Handle exceptions in the callback function
                    print(f"Error during flush callback: {e}")
                finally:
                    self.data_buffer = []


# Example usage
def example_flush_callback(data_batch: List[dict]):
    """
    Example callback function to handle flushed data.

    Args:
        data_batch (List[dict]): Batch of data flushed from the buffer.
    """
    print(f"Flushed {len(data_batch)} items: {data_batch}")

# Initialize the FlushIntervalManager with a 5-second interval
flush_manager = FlushIntervalManager(interval_seconds=5, flush_callback=example_flush_callback)

# Start the manager
flush_manager.start()

# Simulate polling data addition
try:
    for i in range(10):
        flush_manager.add_data({"id": i, "value": f"Data-{i}"})
        time.sleep(1)  # Simulate data poll every second
finally:
    # Stop the manager gracefully
    flush_manager.stop()
```
