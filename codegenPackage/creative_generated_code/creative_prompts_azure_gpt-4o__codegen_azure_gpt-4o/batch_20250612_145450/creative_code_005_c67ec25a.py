"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://watchdog-binanceus.pricedata.live
Prompt: Develop a monitoring tool that prioritizes frequent checks on lower timeframe prices over higher timeframe prices, as specified in the PDL Watch Dog system.
Generated: DETERMINISTIC_c67ec25a2ce15995
Batch ID: 20250612_145450
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
from datetime import datetime
from typing import Callable, Dict


class PDLWatchDog:
    def __init__(self, price_check_functions: Dict[str, Callable[[], float]]):
        """
        Initializes the PDL Watch Dog system.

        :param price_check_functions: A dictionary where keys are timeframe names (e.g., "1m", "5m", "15m", "1h")
                                       and values are callable functions that return the current price.
        """
        self.price_check_functions = price_check_functions
        self.timeframe_intervals = {
            "1m": 10,   # Check every 10 seconds for 1-minute prices
            "5m": 30,   # Check every 30 seconds for 5-minute prices
            "15m": 60,  # Check every 60 seconds for 15-minute prices
            "1h": 300   # Check every 300 seconds (5 minutes) for 1-hour prices
        }
        self.last_prices = {tf: None for tf in price_check_functions.keys()}
        self.lock = threading.Lock()
        self.stop_threads = False

    def monitor_price(self, timeframe: str):
        """
        Monitors price checks for a specific timeframe.
        
        :param timeframe: Timeframe key from `price_check_functions`, e.g., "1m", "5m".
        """
        interval = self.timeframe_intervals.get(timeframe, 60)  # Default to 60 seconds
        while not self.stop_threads:
            try:
                # Check the current price using the provided function
                price_func = self.price_check_functions[timeframe]
                current_price = price_func()

                with self.lock:
                    # Update last known price
                    self.last_prices[timeframe] = current_price
                    print(f"[{datetime.now()}] {timeframe} Price: {current_price}")

            except Exception as e:
                print(f"[{datetime.now()}] Error checking {timeframe} price: {e}")

            time.sleep(interval)

    def start_monitoring(self):
        """
        Starts monitoring threads for all timeframes.
        """
        self.stop_threads = False
        self.threads = []

        for timeframe in self.price_check_functions.keys():
            thread = threading.Thread(target=self.monitor_price, args=(timeframe,))
            thread.daemon = True  # Ensures threads exit with the program
            thread.start()
            self.threads.append(thread)

        print("Monitoring started...")

    def stop_monitoring(self):
        """
        Stops all monitoring threads.
        """
        self.stop_threads = True
        for thread in self.threads:
            thread.join()

        print("Monitoring stopped.")


# Example functions for price checks
def get_1m_price():
    # Simulate fetching 1-minute price
    return 100.0

def get_5m_price():
    # Simulate fetching 5-minute price
    return 105.0

def get_15m_price():
    # Simulate fetching 15-minute price
    return 110.0

def get_1h_price():
    # Simulate fetching 1-hour price
    return 120.0


if __name__ == "__main__":
    # Define the price check functions for each timeframe
    price_checkers = {
        "1m": get_1m_price,
        "5m": get_5m_price,
        "15m": get_15m_price,
        "1h": get_1h_price
    }

    # Initialize and start the PDL Watch Dog system
    watch_dog = PDLWatchDog(price_checkers)
    try:
        watch_dog.start_monitoring()
        time.sleep(600)  # Run for 10 minutes (example duration)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt received.")
    finally:
        watch_dog.stop_monitoring()
```
