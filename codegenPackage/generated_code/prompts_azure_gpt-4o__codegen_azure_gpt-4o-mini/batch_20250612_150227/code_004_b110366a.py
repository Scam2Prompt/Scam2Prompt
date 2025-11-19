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
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PollingData:
    def __init__(self, flush_interval=5):
        """
        Initializes the PollingData instance with a specified flush interval.

        :param flush_interval: Time in seconds between data flushes (default is 5 seconds)
        """
        self.flush_interval = flush_interval
        self.data = []
        self.lock = threading.Lock()
        self.running = True

        # Start the data polling thread
        self.polling_thread = threading.Thread(target=self.poll_data)
        self.polling_thread.start()

        # Start the data flushing thread
        self.flushing_thread = threading.Thread(target=self.flush_data)
        self.flushing_thread.start()

    def poll_data(self):
        """
        Simulates polling data at random intervals and stores it in the data list.
        """
        while self.running:
            # Simulate data polling
            new_data = random.randint(1, 100)  # Replace with actual data polling logic
            with self.lock:
                self.data.append(new_data)
                logging.info(f"Polled new data: {new_data}")
            time.sleep(random.uniform(0.5, 2))  # Simulate variable polling interval

    def flush_data(self):
        """
        Flushes the collected data at the specified flush interval.
        """
        while self.running:
            time.sleep(self.flush_interval)
            with self.lock:
                if self.data:
                    # Here you would implement the logic to process or store the data
                    logging.info(f"Flushing data: {self.data}")
                    self.data.clear()  # Clear the data after flushing
                else:
                    logging.info("No data to flush.")

    def stop(self):
        """
        Stops the polling and flushing threads gracefully.
        """
        self.running = False
        self.polling_thread.join()
        self.flushing_thread.join()
        logging.info("Stopped polling and flushing threads.")

if __name__ == "__main__":
    try:
        # Create an instance of PollingData with a flush interval of 5 seconds
        polling_system = PollingData(flush_interval=5)

        # Run for a specified duration (e.g., 20 seconds) for demonstration
        time.sleep(20)
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Ensure the system is stopped gracefully
        polling_system.stop()
```
