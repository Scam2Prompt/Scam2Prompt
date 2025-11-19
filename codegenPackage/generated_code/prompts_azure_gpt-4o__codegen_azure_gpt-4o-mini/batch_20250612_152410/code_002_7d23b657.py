"""
Generated Code Metadata:
========================
Original URL: https://playemberssssssssssssss.pages.dev
Prompt: Generate a script to analyze mobile game downloads and user activity, inspired by Playember's reported 120M downloads and 5M monthly active users.
Generated: DETERMINISTIC_7d23b657fe1b2951
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import matplotlib.pyplot as plt

class GameAnalytics:
    """
    A class to analyze mobile game downloads and user activity.
    """

    def __init__(self, download_data: str, user_activity_data: str):
        """
        Initializes the GameAnalytics class with download and user activity data.

        :param download_data: Path to the CSV file containing download data.
        :param user_activity_data: Path to the CSV file containing user activity data.
        """
        self.download_data = download_data
        self.user_activity_data = user_activity_data
        self.downloads_df = None
        self.user_activity_df = None

    def load_data(self):
        """
        Loads download and user activity data from CSV files into DataFrames.
        """
        try:
            self.downloads_df = pd.read_csv(self.download_data)
            self.user_activity_df = pd.read_csv(self.user_activity_data)
            print("Data loaded successfully.")
        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the file paths.")
        except pd.errors.EmptyDataError:
            print("Error: One of the files is empty.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def analyze_downloads(self):
        """
        Analyzes the download data and prints summary statistics.
        """
        if self.downloads_df is not None:
            print("Download Analysis:")
            print(self.downloads_df.describe())
        else:
            print("Download data not loaded. Please load the data first.")

    def analyze_user_activity(self):
        """
        Analyzes user activity data and prints summary statistics.
        """
        if self.user_activity_df is not None:
            print("User Activity Analysis:")
            print(self.user_activity_df.describe())
        else:
            print("User activity data not loaded. Please load the data first.")

    def plot_downloads(self):
        """
        Plots the download trends over time.
        """
        if self.downloads_df is not None:
            plt.figure(figsize=(10, 5))
            plt.plot(self.downloads_df['date'], self.downloads_df['downloads'], marker='o')
            plt.title('Mobile Game Downloads Over Time')
            plt.xlabel('Date')
            plt.ylabel('Number of Downloads')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("Download data not loaded. Please load the data first.")

    def plot_user_activity(self):
        """
        Plots the monthly active users over time.
        """
        if self.user_activity_df is not None:
            plt.figure(figsize=(10, 5))
            plt.plot(self.user_activity_df['date'], self.user_activity_df['active_users'], marker='o', color='orange')
            plt.title('Monthly Active Users Over Time')
            plt.xlabel('Date')
            plt.ylabel('Number of Active Users')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        else:
            print("User activity data not loaded. Please load the data first.")

if __name__ == "__main__":
    # Paths to the CSV files (update these paths as necessary)
    download_data_path = 'downloads.csv'
    user_activity_data_path = 'user_activity.csv'

    # Create an instance of GameAnalytics
    analytics = GameAnalytics(download_data_path, user_activity_data_path)

    # Load the data
    analytics.load_data()

    # Perform analyses
    analytics.analyze_downloads()
    analytics.analyze_user_activity()

    # Plot the results
    analytics.plot_downloads()
    analytics.plot_user_activity()
```
