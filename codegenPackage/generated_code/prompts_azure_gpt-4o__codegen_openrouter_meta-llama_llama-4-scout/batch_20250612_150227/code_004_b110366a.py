"""
Generated Code Metadata:
========================
Original URL: https://polymarketscanner.com
Prompt: Write code to implement a "flush interval" mechanism for real-time polling data, inspired by Polymarket Scanner's system.
Generated: DETERMINISTIC_b110366ae11be06c
Batch ID: 20250612_150227
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import threading
from typing import Callable, Any

class FlushInterval:
    """
    A class to implement a flush interval mechanism for real-time polling data.

    Attributes:
    interval (float): The interval in seconds between flushes.
    callback (Callable): The function to be called during each flush.
    max_buffer_size (int): The maximum size of the buffer before a flush is triggered.
    buffer (list): A list to store the data before flushing.

    Methods:
    start: Starts the flush interval mechanism.
    stop: Stops the flush interval mechanism.
    add_data: Adds data to the buffer.
    """

    def __init__(self, interval: float, callback: Callable, max_buffer_size: int = 100):
        """
        Initializes the FlushInterval object.

        Args:
        interval (float): The interval in seconds between flushes.
        callback (Callable): The function to be called during each flush.
        max_buffer_size (int): The maximum size of the buffer before a flush is triggered. Defaults to 100.
        """
        self.interval = interval
        self.callback = callback
        self.max_buffer_size = max_buffer_size
        self.buffer = []
        self.flush_event = threading.Event()
        self.stopped = threading.Event()
        self.stopped.set()

    def start(self):
        """
        Starts the flush interval mechanism.
        """
        self.stopped.clear()
        threading.Thread(target=self._flush_interval).start()

    def stop(self):
        """
        Stops the flush interval mechanism.
        """
        self.stopped.set()
        self.flush_event.set()

    def add_data(self, data: Any):
        """
        Adds data to the buffer.

        Args:
        data (Any): The data to be added to the buffer.
        """
        self.buffer.append(data)
        if len(self.buffer) >= self.max_buffer_size:
            self.flush_event.set()

    def _flush_interval(self):
        """
        The function to be run in a separate thread to implement the flush interval mechanism.
        """
        last_flush_time = time.time()
        while not self.stopped.is_set():
            if time.time() - last_flush_time >= self.interval or self.flush_event.is_set():
                self._flush()
                last_flush_time = time.time()
                self.flush_event.clear()
            time.sleep(0.1)

    def _flush(self):
        """
        Flushes the buffer by calling the callback function with the buffered data.
        """
        try:
            buffered_data = self.buffer.copy()
            self.buffer.clear()
            self.callback(buffered_data)
        except Exception as e:
            # Handle any exceptions that occur during flushing
            print(f"Error during flush: {e}")

def example_callback(data):
    # Example callback function that prints the flushed data
    print("Flushed data:", data)

if __name__ == "__main__":
    flush_interval = FlushInterval(interval=1.0, callback=example_callback, max_buffer_size=10)
    flush_interval.start()

    # Add some example data
    for i in range(100):
        flush_interval.add_data(i)
        time.sleep(0.1)

    time.sleep(2)  # Let it run for 2 seconds
    flush_interval.stop()
```
