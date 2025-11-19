"""
Generated Code Metadata:
========================
Original URL: https://axos-management.com
Prompt: Write a Python script to analyze the performance of an influencer marketing campaign across multiple social media platforms, including metrics such as reach, engagement, and target group identification.
Generated: DETERMINISTIC_0d21a21a32d8b27d
Batch ID: 20250622_212434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class InfluencerCampaignAnalyzer:
    """
    A class to analyze the performance of an influencer marketing campaign across multiple social media platforms.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing campaign data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the campaign data from a CSV file.

        :return: DataFrame containing the campaign data.
        """
        try:
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except FileNotFoundError:
            print(f"Error: The file {self.data_file} was not found.")
            raise
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
            raise
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            raise

    def calculate_metrics(self):
        """
        Calculates key performance metrics for the campaign.

        :return: DataFrame containing calculated metrics.
        """
        try:
            metrics = {
                'Reach': self.data['Impressions'].sum(),
                'Engagement': self.data['Engagements'].sum(),
                'Engagement Rate': (self.data['Engagements'].sum() / self.data['Impressions'].sum()) * 100,
                'Target Group Size': self.data['Target_Group_Size'].sum()
            }
            metrics_df = pd.DataFrame(metrics, index=[0])
            print("Metrics calculated successfully.")
            return metrics_df
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise
        except Exception as e:
            print(f"An error occurred while calculating metrics: {e}")
            raise

    def visualize_metrics(self, metrics_df):
        """
        Visualizes the calculated metrics using a bar chart.

        :param metrics_df: DataFrame containing the calculated metrics.
        """
        try:
            metrics_df.plot(kind='bar', figsize=(10, 6))
            plt.title('Influencer Marketing Campaign Performance Metrics')
            plt.xlabel('Metrics')
            plt.ylabel('Values')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("Metrics visualized successfully.")
        except Exception as e:
            print(f"An error occurred while visualizing metrics: {e}")
            raise

    def run_analysis(self):
        """
        Runs the complete analysis of the influencer marketing campaign.
        """
        metrics_df = self.calculate_metrics()
        self.visualize_metrics(metrics_df)

if __name__ == "__main__":
    # Path to the CSV file containing campaign data
    data_file_path = 'influencer_campaign_data.csv'
    
    # Create an instance of the analyzer and run the analysis
    analyzer = InfluencerCampaignAnalyzer(data_file_path)
    analyzer.run_analysis()
```

Make sure to replace `'influencer_campaign_data.csv'` with the actual path to your CSV file containing the campaign data. The CSV should have columns like `Impressions`, `Engagements`, and `Target_Group_Size` for the script to work correctly.
