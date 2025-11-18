"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dashboard.smartglobalwealthfx.com
Prompt: Provide a Python implementation for tracking and displaying real-time trade data, including last trade price, 24-hour price change, and 24-hour volume, as seen on the SmartglobalwealthFx dashboard.
Generated: DETERMINISTIC_d72e1dd24b0a223c
Batch ID: 20250612_150030
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
import random
from collections import deque
from datetime import datetime

class TradeDataTracker:
    """
    A class to track and display real-time trade data.
    """

    def __init__(self):
        """
        Initializes the tracker with default values.
        """
        self.last_trade_price = None
        self.price_changes = deque(maxlen=1440)  # Stores minute-wise price changes
        self.trade_volumes = deque(maxlen=1440)  # Stores minute-wise trade volumes
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def update_trade_data(self, price, volume):
        """
        Updates the trade data with a new trade's price and volume.

        :param price: The price of the last trade
        :param volume: The volume of the last trade
        """
        with self.lock:
            current_time = datetime.utcnow()
            if self.last_trade_price is not None:
                # Calculate price change as a percentage
                price_change = ((price - self.last_trade_price) / self.last_trade_price) * 100
                self.price_changes.append((current_time, price_change))
            else:
                # First trade, no price change
                self.price_changes.append((current_time, 0))

            # Update the trade volume
            self.trade_volumes.append((current_time, volume))
            self.last_trade_price = price

    def get_24_hour_summary(self):
        """
        Calculates the 24-hour price change and volume summary.

        :return: A dictionary containing the last trade price, 24-hour price change, and 24-hour volume
        """
        with self.lock:
            now = datetime.utcnow()
            # Filter 24-hour data
            valid_price_changes = [
                change for timestamp, change in self.price_changes if (now - timestamp).seconds <= 86400
            ]
            valid_volumes = [
                volume for timestamp, volume in self.trade_volumes if (now - timestamp).seconds <= 86400
            ]

            # Calculate 24-hour summary
            total_price_change = sum(valid_price_changes)
            total_volume = sum(valid_volumes)

        return {
            "last_trade_price": self.last_trade_price,
            "24_hour_price_change": total_price_change,
            "24_hour_volume": total_volume
        }

    def display_summary(self):
        """
        Displays the latest 24-hour trade summary.
        """
        summary = self.get_24_hour_summary()
        print("------------------------------")
        print("Last Trade Price: ${:.2f}".format(summary["last_trade_price"] or 0))
        print("24-Hour Price Change: {:.2f}%".format(summary["24_hour_price_change"] or 0))
        print("24-Hour Volume: {:.2f}".format(summary["24_hour_volume"] or 0))
        print("------------------------------")


# Mock Data Generator for Simulating Real-Time Trades
def mock_trade_data_generator(tracker):
    """
    Simulates real-time trade data updates.

    :param tracker: The TradeDataTracker instance to update
    """
    while True:
        # Generate random trade data
        price = random.uniform(50.0, 150.0)  # Random price between $50 and $150
        volume = random.uniform(1.0, 10.0)   # Random volume between 1 and 10 units

        tracker.update_trade_data(price, volume)
        time.sleep(1)  # Simulate a trade every second


# Main Function
def main():
    """
    The main function to run the tracker.
    """
    tracker = TradeDataTracker()

    # Start the mock data generator in a separate thread
    generator_thread = threading.Thread(target=mock_trade_data_generator, args=(tracker,))
    generator_thread.daemon = True
    generator_thread.start()

    try:
        while True:
            # Display the summary every 10 seconds
            tracker.display_summary()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nTerminating the tracker.")


if __name__ == "__main__":
    main()
```
