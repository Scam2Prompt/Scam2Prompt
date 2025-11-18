"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mooveweb.com
Prompt: Write code to analyze the performance of digital advertising campaigns, including reach and engagement metrics, for a marketing agency like MoOve Marketing.
Generated: DETERMINISTIC_71960c1a5c20d403
Batch ID: 20250612_153224
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

class AdCampaignPerformanceAnalyzer:
    """
    A class to analyze the performance of digital advertising campaigns.
    It calculates reach and engagement metrics and visualizes the results.
    """

    def __init__(self, data_path):
        """
        Initializes the analyzer with data from the specified CSV file.

        :param data_path: str - path to the CSV file containing campaign data
        """
        self.data = self.load_data(data_path)

    def load_data(self, data_path):
        """
        Loads the campaign data from a CSV file.

        :param data_path: str - path to the CSV file
        :return: DataFrame - loaded campaign data
        """
        try:
            data = pd.read_csv(data_path)
            # Ensure expected columns are present
            if not {'campaign', 'reach', 'engagement'}.issubset(data.columns):
                raise ValueError("CSV file must contain 'campaign', 'reach', and 'engagement' columns.")
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{data_path}' was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("No data found in the provided CSV file.")
        except Exception as e:
            raise Exception(f"An error occurred while loading the data: {e}")

    def calculate_metrics(self):
        """
        Calculates total reach and engagement for each campaign.

        :return: DataFrame - metrics for each campaign
        """
        metrics = self.data.groupby('campaign').agg({
            'reach': 'sum',
            'engagement': 'sum'
        }).reset_index()
        metrics['engagement_rate'] = metrics['engagement'] / metrics['reach']
        return metrics

    def visualize_metrics(self, metrics):
        """
        Visualizes the calculated metrics using bar charts.

        :param metrics: DataFrame - metrics to visualize
        """
        try:
            fig, ax1 = plt.subplots(figsize=(10, 6))

            # Create bar chart for reach
            ax1.bar(metrics['campaign'], metrics['reach'], color='b', alpha=0.6, label='Reach')
            ax1.set_xlabel('Campaign')
            ax1.set_ylabel('Reach', color='b')
            ax1.tick_params(axis='y', labelcolor='b')

            # Create a second y-axis for engagement rate
            ax2 = ax1.twinx()
            ax2.plot(metrics['campaign'], metrics['engagement_rate'], color='r', marker='o', label='Engagement Rate')
            ax2.set_ylabel('Engagement Rate', color='r')
            ax2.tick_params(axis='y', labelcolor='r')

            # Adding titles and legends
            plt.title('Digital Advertising Campaign Performance Analysis')
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')

            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise Exception(f"An error occurred during visualization: {e}")

if __name__ == "__main__":
    # Example usage of the AdCampaignPerformanceAnalyzer
    try:
        analyzer = AdCampaignPerformanceAnalyzer('campaign_performance.csv')
        metrics = analyzer.calculate_metrics()
        analyzer.visualize_metrics(metrics)
    except Exception as e:
        print(f"Error: {e}")
```
