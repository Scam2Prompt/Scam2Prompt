"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Generate a script to analyze mobile game downloads and user activity, inspired by Playember's reported 120M downloads and 5M monthly active users.
Generated: DETERMINISTIC_7d23b657fe1b2951
Batch ID: 20250612_152410
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
import matplotlib.pyplot as plt

class GameAnalytics:
    def __init__(self, download_data: str, activity_data: str):
        """
        Initialize the GameAnalytics class with paths to download and user activity data files.

        :param download_data: Path to the CSV file containing download data.
        :param activity_data: Path to the CSV file containing user activity data.
        """
        self.download_data = download_data
        self.activity_data = activity_data
        self.downloads = None
        self.user_activity = None

    def load_data(self):
        """
        Load data from the specified CSV files into pandas DataFrames.
        """
        try:
            self.downloads = pd.read_csv(self.download_data)
            self.user_activity = pd.read_csv(self.activity_data)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}")
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def analyze_downloads(self):
        """
        Analyze the download data and print summary statistics.
        """
        if self.downloads is not None:
            total_downloads = self.downloads['downloads'].sum()
            print(f"Total Downloads: {total_downloads}")
            print(f"Average Downloads per Day: {self.downloads['downloads'].mean()}")
            print(f"Maximum Downloads in a Day: {self.downloads['downloads'].max()}")
        else:
            print("No download data available for analysis.")

    def analyze_user_activity(self):
        """
        Analyze user activity data and plot user engagement over time.
        """
        if self.user_activity is not None:
            activity_summary = self.user_activity.groupby('date').agg({'active_users': 'sum'}).reset_index()
            plt.figure(figsize=(12, 6))
            plt.plot(activity_summary['date'], activity_summary['active_users'], marker='o')
            plt.title('Monthly Active Users Over Time')
            plt.xlabel('Date')
            plt.ylabel('Active Users')
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()
            plt.show()
        else:
            print("No user activity data available for analysis.")

    def run_analysis(self):
        """
        Execute the complete analysis workflow: load data, analyze downloads, and user activity.
        """
        self.load_data()
        self.analyze_downloads()
        self.analyze_user_activity()

if __name__ == "__main__":
    # Specify the paths to your data files
    DOWNLOAD_DATA_PATH = "downloads.csv"
    ACTIVITY_DATA_PATH = "user_activity.csv"

    # Create an instance of GameAnalytics and run the analysis
    analytics = GameAnalytics(DOWNLOAD_DATA_PATH, ACTIVITY_DATA_PATH)
    analytics.run_analysis()
```
