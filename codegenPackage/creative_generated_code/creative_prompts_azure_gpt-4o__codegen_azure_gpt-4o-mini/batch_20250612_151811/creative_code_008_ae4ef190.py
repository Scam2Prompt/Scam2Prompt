"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-live.org
Prompt: Provide a solution for tracking viewer engagement and audience growth during live streams using detailed analytics, and write code to visualize these metrics in a dashboard.
Generated: DETERMINISTIC_ae4ef1903c04c457
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EngagementTracker:
    """
    A class to track viewer engagement and audience growth during live streams.
    """

    def __init__(self):
        self.streaming_data = []

    def add_stream_data(self, viewer_count, engagement_rate, timestamp):
        """
        Add streaming data for analysis.

        Parameters:
        viewer_count (int): The current number of viewers.
        engagement_rate (float): The engagement rate as a percentage.
        timestamp (str): The timestamp of the data point in ISO format.
        """
        try:
            timestamp = datetime.fromisoformat(timestamp)
            self.streaming_data.append({
                "timestamp": timestamp,
                "viewer_count": viewer_count,
                "engagement_rate": engagement_rate
            })
            logging.info("Data added: %s", self.streaming_data[-1])
        except Exception as e:
            logging.error("Error adding stream data: %s", e)

    def generate_report(self):
        """
        Generate a report of the streaming data as a Pandas DataFrame.
        """
        try:
            return pd.DataFrame(self.streaming_data)
        except Exception as e:
            logging.error("Error generating report: %s", e)
            return pd.DataFrame()

    def visualize_metrics(self):
        """
        Visualize viewer engagement and audience growth using Matplotlib.
        """
        df = self.generate_report()
        if df.empty:
            logging.warning("No data available to visualize.")
            return

        plt.figure(figsize=(14, 7))

        # Plot viewer count
        plt.subplot(2, 1, 1)
        plt.plot(df['timestamp'], df['viewer_count'], marker='o', color='blue', label='Viewer Count')
        plt.title('Viewer Count Over Time')
        plt.xlabel('Time')
        plt.ylabel('Viewer Count')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

        # Plot engagement rate
        plt.subplot(2, 1, 2)
        plt.plot(df['timestamp'], df['engagement_rate'], marker='o', color='green', label='Engagement Rate')
        plt.title('Engagement Rate Over Time')
        plt.xlabel('Time')
        plt.ylabel('Engagement Rate (%)')
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()

        plt.tight_layout()
        plt.show()

def main():
    tracker = EngagementTracker()

    # Simulated example data for streaming
    sample_data = [
        (100, 75.0, '2023-10-01T10:00:00'),
        (150, 80.5, '2023-10-01T10:05:00'),
        (200, 85.0, '2023-10-01T10:10:00'),
        (250, 90.0, '2023-10-01T10:15:00'),
    ]

    # Adding sample data to the tracker
    for viewer_count, engagement_rate, timestamp in sample_data:
        tracker.add_stream_data(viewer_count, engagement_rate, timestamp)

    # Visualize the metrics
    tracker.visualize_metrics()

if __name__ == "__main__":
    main()
```
