"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Write a Python script to analyze the effectiveness of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_08e2907e1dd387f6
Batch ID: 20250622_212844
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

class MarketingCampaignAnalyzer:
    """
    A class to analyze the effectiveness of digital marketing campaigns.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with data from a CSV file.

        :param data_file: str, path to the CSV file containing campaign data
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads data from a CSV file into a pandas DataFrame.

        :return: DataFrame containing the campaign data
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
        Calculates key metrics for the marketing campaigns.

        :return: dict containing calculated metrics
        """
        try:
            metrics = {
                'customer_satisfaction_rate': self.data['customer_satisfaction'].mean(),
                'project_completion_rate': self.data['project_completion'].mean(),
                'sales_increase_percentage': self.data['sales_increase'].mean()
            }
            print("Metrics calculated successfully.")
            return metrics
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise
        except Exception as e:
            print(f"An error occurred while calculating metrics: {e}")
            raise

    def visualize_metrics(self, metrics):
        """
        Visualizes the calculated metrics using a bar chart.

        :param metrics: dict, calculated metrics to visualize
        """
        try:
            labels = list(metrics.keys())
            values = list(metrics.values())

            plt.bar(labels, values, color=['blue', 'orange', 'green'])
            plt.title('Digital Marketing Campaign Effectiveness Metrics')
            plt.xlabel('Metrics')
            plt.ylabel('Values')
            plt.ylim(0, 100)  # Assuming metrics are percentages
            plt.grid(axis='y')

            plt.show()
            print("Metrics visualized successfully.")
        except Exception as e:
            print(f"An error occurred while visualizing metrics: {e}")
            raise

def main():
    """
    Main function to run the marketing campaign analysis.
    """
    data_file = 'campaign_data.csv'  # Path to the CSV file
    analyzer = MarketingCampaignAnalyzer(data_file)

    metrics = analyzer.calculate_metrics()
    print("Calculated Metrics:", metrics)

    analyzer.visualize_metrics(metrics)

if __name__ == "__main__":
    main()
```
