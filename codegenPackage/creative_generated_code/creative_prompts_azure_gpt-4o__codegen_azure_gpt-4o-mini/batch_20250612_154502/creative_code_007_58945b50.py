"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Recommend libraries or APIs for visualizing performance metrics of submersible pumps, specifically the WQ series, in real-time.
Generated: DETERMINISTIC_58945b50b60c5514
Batch ID: 20250612_154502
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/api/pump_performance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import time

class PumpPerformanceVisualizer:
    """
    A class to visualize performance metrics of WQ series submersible pumps in real-time.
    """

    def __init__(self, api_url):
        """
        Initialize the PumpPerformanceVisualizer with the API URL.

        :param api_url: str - The URL of the API providing pump performance data.
        """
        self.api_url = api_url
        self.data = []

    def fetch_data(self):
        """
        Fetch the latest pump performance data from the API.

        :return: dict - A dictionary containing pump performance metrics.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return None

    def update_data(self):
        """
        Update the internal data store with the latest performance metrics.
        """
        new_data = self.fetch_data()
        if new_data:
            self.data.append(new_data)

    def visualize_data(self):
        """
        Visualize the gathered pump performance data using matplotlib.
        """
        if not self.data:
            print("No data available to visualize.")
            return

        # Convert data to DataFrame for easier handling
        df = pd.DataFrame(self.data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])  # Ensure the timestamp is in datetime format

        plt.figure(figsize=(12, 6))
        plt.plot(df['timestamp'], df['flow_rate'], label='Flow Rate (L/min)', color='blue')
        plt.plot(df['timestamp'], df['head'], label='Head (m)', color='orange')
        plt.xlabel('Time')
        plt.ylabel('Metrics')
        plt.title('Real-time Performance Metrics of WQ Series Submersible Pumps')
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run(self, interval=60):
        """
        Run the visualizer, fetching data at specified intervals.

        :param interval: int - Time in seconds between data fetches.
        """
        try:
            while True:
                self.update_data()
                self.visualize_data()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Visualization stopped by user.")

if __name__ == "__main__":
    API_URL = "http://example.com/api/pump_performance"  # Replace with actual API URL
    visualizer = PumpPerformanceVisualizer(API_URL)
    visualizer.run(interval=60)  # Fetch and visualize data every 60 seconds
```
