"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pozymedia.com
Prompt: Create a Python program to analyze social media campaign performance metrics for an event, leveraging Pozy Media's expertise in digital outreach and marketing.
Generated: DETERMINISTIC_9e2de2925f641531
Batch ID: 20250612_152924
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

class CampaignPerformanceAnalyzer:
    """
    A class to analyze social media campaign performance metrics for an event.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: str, path to the CSV file containing campaign metrics
        """
        self.data_file = data_file
        self.df = self.load_data()
        self.validate_data()

    def load_data(self):
        """
        Loads the campaign metrics data from a CSV file.

        :return: DataFrame containing the campaign metrics
        """
        try:
            df = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return df
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def validate_data(self):
        """
        Validates the loaded data to ensure it contains required columns.
        """
        required_columns = ['Date', 'Impressions', 'Clicks', 'Engagements', 'Conversions']
        for column in required_columns:
            if column not in self.df.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_metrics(self):
        """
        Calculates key performance metrics.

        :return: dict containing total and average metrics
        """
        total_impressions = self.df['Impressions'].sum()
        total_clicks = self.df['Clicks'].sum()
        total_engagements = self.df['Engagements'].sum()
        total_conversions = self.df['Conversions'].sum()

        metrics = {
            'Total Impressions': total_impressions,
            'Total Clicks': total_clicks,
            'Total Engagements': total_engagements,
            'Total Conversions': total_conversions,
            'CTR (%)': (total_clicks / total_impressions) * 100 if total_impressions > 0 else 0,
            'Engagement Rate (%)': (total_engagements / total_impressions) * 100 if total_impressions > 0 else 0,
            'Conversion Rate (%)': (total_conversions / total_clicks) * 100 if total_clicks > 0 else 0,
        }
        return metrics

    def plot_metrics(self, metrics):
        """
        Plots the key performance metrics for visual analysis.

        :param metrics: dict containing calculated metrics
        """
        categories = list(metrics.keys())
        values = list(metrics.values())

        plt.figure(figsize=(10, 6))
        plt.bar(categories, values, color='blue')
        plt.title('Social Media Campaign Performance Metrics')
        plt.xlabel('Metrics')
        plt.ylabel('Values')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.grid(axis='y')
        plt.show()

    def analyze(self):
        """
        Analyzes the campaign performance and displays the results.
        """
        metrics = self.calculate_metrics()
        for metric, value in metrics.items():
            print(f"{metric}: {value:.2f}")
        self.plot_metrics(metrics)


if __name__ == "__main__":
    # Path to the CSV file containing campaign data
    data_path = 'campaign_data.csv'
    analyzer = CampaignPerformanceAnalyzer(data_path)
    analyzer.analyze()
```
