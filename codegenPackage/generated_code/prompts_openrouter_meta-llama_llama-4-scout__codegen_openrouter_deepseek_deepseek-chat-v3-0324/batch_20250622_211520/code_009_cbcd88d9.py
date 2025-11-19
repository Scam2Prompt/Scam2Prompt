"""
Generated Code Metadata:
========================
Original URL: https://ethn.cc
Prompt: Develop a script to analyze data from a gravel cycling computer, including GPS tracks, heart rate, and power output.
Generated: DETERMINISTIC_cbcd88d9fec4e4bb
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import pandas as pd
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
from geopy.distance import geodesic
import warnings

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

class GravelCyclingAnalyzer:
    """
    A class to analyze data from a gravel cycling computer.
    Supports GPS tracks, heart rate, and power output analysis.
    """

    def __init__(self, file_path):
        """
        Initialize the analyzer with data from a JSON file.

        Args:
            file_path (str): Path to the JSON file containing cycling data.
        """
        self.file_path = file_path
        self.data = self._load_data()
        self.df = self._process_data()

    def _load_data(self):
        """
        Load and validate the JSON data from the file.

        Returns:
            dict: Parsed JSON data.

        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file is not valid JSON.
        """
        try:
            with open(self.file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON file")

    def _process_data(self):
        """
        Process the raw JSON data into a pandas DataFrame.

        Returns:
            pd.DataFrame: Processed cycling data.
        """
        required_fields = ['timestamp', 'latitude', 'longitude', 'heart_rate', 'power']
        if not all(field in self.data for field in required_fields):
            raise ValueError("Missing required fields in the data")

        df = pd.DataFrame(self.data)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['time_diff'] = df['timestamp'].diff().dt.total_seconds().fillna(0)
        return df

    def calculate_distance(self):
        """
        Calculate the total distance traveled using GPS coordinates.

        Returns:
            float: Total distance in kilometers.
        """
        coords = list(zip(self.df['latitude'], self.df['longitude']))
        distance = 0.0
        for i in range(1, len(coords)):
            distance += geodesic(coords[i-1], coords[i]).kilometers
        return distance

    def average_heart_rate(self):
        """
        Calculate the average heart rate.

        Returns:
            float: Average heart rate in BPM.
        """
        return self.df['heart_rate'].mean()

    def average_power(self):
        """
        Calculate the average power output.

        Returns:
            float: Average power in watts.
        """
        return self.df['power'].mean()

    def normalized_power(self):
        """
        Calculate the normalized power (30-second rolling average).

        Returns:
            float: Normalized power in watts.
        """
        rolling_avg = self.df['power'].rolling(window=30, min_periods=1).mean()
        return np.sqrt(np.mean(rolling_avg**2))

    def plot_heart_rate(self):
        """
        Plot heart rate over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['timestamp'], self.df['heart_rate'], label='Heart Rate (BPM)', color='red')
        plt.xlabel('Time')
        plt.ylabel('Heart Rate (BPM)')
        plt.title('Heart Rate Over Time')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_power(self):
        """
        Plot power output over time.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.df['timestamp'], self.df['power'], label='Power (Watts)', color='blue')
        plt.xlabel('Time')
        plt.ylabel('Power (Watts)')
        plt.title('Power Output Over Time')
        plt.legend()
        plt.grid()
        plt.show()

    def plot_route(self):
        """
        Plot the GPS route on a simple map.
        """
        plt.figure(figsize=(10, 8))
        plt.plot(self.df['longitude'], self.df['latitude'], label='Route', color='green')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('GPS Route')
        plt.legend()
        plt.grid()
        plt.show()

    def generate_report(self):
        """
        Generate a summary report of the cycling session.

        Returns:
            dict: Summary statistics.
        """
        return {
            'total_distance_km': self.calculate_distance(),
            'average_heart_rate_bpm': self.average_heart_rate(),
            'average_power_watts': self.average_power(),
            'normalized_power_watts': self.normalized_power(),
            'duration_seconds': self.df['time_diff'].sum()
        }

# Example usage
if __name__ == "__main__":
    try:
        analyzer = GravelCyclingAnalyzer('cycling_data.json')
        print("Analysis Report:")
        report = analyzer.generate_report()
        for key, value in report.items():
            print(f"{key}: {value:.2f}")

        analyzer.plot_heart_rate()
        analyzer.plot_power()
        analyzer.plot_route()

    except Exception as e:
        print(f"Error: {e}")
```
