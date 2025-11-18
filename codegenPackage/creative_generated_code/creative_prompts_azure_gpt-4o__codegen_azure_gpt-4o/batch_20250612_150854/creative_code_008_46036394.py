"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-peak.io
Prompt: Write code to detect pump-and-dump schemes in cryptocurrency markets, as highlighted by Immediate Peak.
Generated: DETERMINISTIC_4603639468b8994d
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PumpAndDumpDetector:
    """
    A class to detect pump-and-dump schemes in cryptocurrency markets.
    """

    def __init__(self, price_data: pd.DataFrame, volume_data: pd.DataFrame):
        """
        Initializes the detector with price and volume data.

        :param price_data: DataFrame with columns ['timestamp', 'price'].
        :param volume_data: DataFrame with columns ['timestamp', 'volume'].
        """
        self.price_data = price_data
        self.volume_data = volume_data

    def detect_anomalies(self, price_threshold=0.2, volume_threshold=2.0, time_window_minutes=15):
        """
        Detects potential pump-and-dump schemes based on rapid price increase followed by a steep drop.

        :param price_threshold: Percentage change (e.g., 0.2 for 20%).
        :param volume_threshold: Multiplicative increase in volume (e.g., 2.0 for 2x).
        :param time_window_minutes: Time window to examine (in minutes).
        :return: List of timestamps where pump-and-dump schemes are detected.
        """
        try:
            # Ensure the price and volume data are sorted by timestamp
            self.price_data.sort_values('timestamp', inplace=True)
            self.volume_data.sort_values('timestamp', inplace=True)

            detected_events = []

            # Merge price and volume data on timestamp for analysis
            data = pd.merge(self.price_data, self.volume_data, on='timestamp')

            # Iterate through the data to detect pump-and-dump patterns
            for i in range(len(data) - 1):
                current_time = data.iloc[i]['timestamp']
                current_price = data.iloc[i]['price']
                current_volume = data.iloc[i]['volume']

                # Define the time window for analysis
                end_time = current_time + timedelta(minutes=time_window_minutes)
                subset = data[(data['timestamp'] > current_time) & (data['timestamp'] <= end_time)]

                if not subset.empty:
                    # Check for price spike and volume increase
                    price_change = (subset['price'].max() - current_price) / current_price
                    volume_change = subset['volume'].max() / current_volume

                    # Check for price drop after spike
                    price_drop = (current_price - subset['price'].min()) / current_price

                    if price_change > price_threshold and volume_change > volume_threshold and price_drop > price_threshold:
                        logging.info(f"Pump-and-dump detected at {current_time}")
                        detected_events.append(current_time)
            return detected_events

        except Exception as e:
            logging.error(f"Error detecting pump-and-dump schemes: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Sample data for testing
    price_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-10-01', periods=10, freq='T'),
        'price': [100, 105, 120, 150, 90, 85, 80, 75, 70, 65]
    })

    volume_data = pd.DataFrame({
        'timestamp': pd.date_range(start='2023-10-01', periods=10, freq='T'),
        'volume': [1000, 1200, 5000, 10000, 2000, 1500, 1400, 1300, 1200, 1100]
    })

    # Initialize the detector
    detector = PumpAndDumpDetector(price_data, volume_data)
    pump_and_dump_events = detector.detect_anomalies()

    # Output detected events
    print("Detected pump-and-dump events:", pump_and_dump_events)
```
