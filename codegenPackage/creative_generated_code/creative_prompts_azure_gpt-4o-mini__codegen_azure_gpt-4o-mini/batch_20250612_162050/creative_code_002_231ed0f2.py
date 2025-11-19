"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Write a script to analyze the success metrics of a digital marketing campaign similar to those offered by Tara Media Works.
Generated: DETERMINISTIC_231ed0f2723bc898
Batch ID: 20250612_162050
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

class CampaignAnalyzer:
    """
    A class to analyze the success metrics of a digital marketing campaign.
    """

    def __init__(self, data_file):
        """
        Initializes the CampaignAnalyzer with the given data file.

        :param data_file: str, path to the CSV data file containing campaign metrics
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads data from the CSV file and performs basic validation.

        :return: DataFrame containing the campaign data
        """
        try:
            data = pd.read_csv(self.data_file)
            if not all(column in data.columns for column in ['impressions', 'clicks', 'conversions']):
                raise ValueError("Data must contain 'impressions', 'clicks', and 'conversions' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_metrics(self):
        """
        Calculates key performance metrics for the campaign.

        :return: dict, a dictionary containing calculated metrics
        """
        total_impressions = self.data['impressions'].sum()
        total_clicks = self.data['clicks'].sum()
        total_conversions = self.data['conversions'].sum()

        # Calculate rates
        click_through_rate = (total_clicks / total_impressions) * 100 if total_impressions else 0
        conversion_rate = (total_conversions / total_clicks) * 100 if total_clicks else 0

        metrics = {
            'Total Impressions': total_impressions,
            'Total Clicks': total_clicks,
            'Total Conversions': total_conversions,
            'Click Through Rate (%)': click_through_rate,
            'Conversion Rate (%)': conversion_rate
        }

        return metrics

    def plot_metrics(self, metrics):
        """
        Plots the key performance metrics of the campaign.

        :param metrics: dict, the metrics to plot
        """
        plt.figure(figsize=(10, 5))

        # Plotting Click Through Rate and Conversion Rate
        plt.bar(metrics.keys(), metrics.values(), color=['blue', 'green', 'red', 'orange', 'purple'])
        plt.title('Digital Marketing Campaign Metrics')
        plt.ylabel('Counts and Rates')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def run_analysis(self):
        """
        Runs the complete analysis process: loading data, calculating metrics, and plotting results.
        """
        try:
            metrics = self.calculate_metrics()
            self.plot_metrics(metrics)
        except Exception as e:
            print(f"Analysis error: {e}")


if __name__ == '__main__':
    # Path to the CSV file containing campaign data
    data_file_path = 'campaign_data.csv'
    analyzer = CampaignAnalyzer(data_file_path)
    analyzer.run_analysis()
```
