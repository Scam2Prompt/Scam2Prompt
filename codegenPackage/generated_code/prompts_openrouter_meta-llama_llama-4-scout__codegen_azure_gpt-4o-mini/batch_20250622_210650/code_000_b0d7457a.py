"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Write a Python script to analyze social media engagement metrics for a digital marketing campaign, including website traffic, leads generated, and brand awareness."
Generated: DETERMINISTIC_b0d7457a8cc94d7c
Batch ID: 20250622_210650
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

class SocialMediaEngagementAnalyzer:
    """
    A class to analyze social media engagement metrics for a digital marketing campaign.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing engagement metrics.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the engagement metrics data from a CSV file.

        :return: DataFrame containing the engagement metrics.
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

    def analyze_metrics(self):
        """
        Analyzes the engagement metrics and generates reports.
        """
        try:
            # Calculate total website traffic, leads generated, and brand awareness
            total_traffic = self.data['website_traffic'].sum()
            total_leads = self.data['leads_generated'].sum()
            total_awareness = self.data['brand_awareness'].mean()

            print(f"Total Website Traffic: {total_traffic}")
            print(f"Total Leads Generated: {total_leads}")
            print(f"Average Brand Awareness: {total_awareness:.2f}")

            self.visualize_metrics(total_traffic, total_leads, total_awareness)

        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise
        except Exception as e:
            print(f"An error occurred during analysis: {e}")
            raise

    def visualize_metrics(self, traffic, leads, awareness):
        """
        Visualizes the engagement metrics using a bar chart.

        :param traffic: Total website traffic.
        :param leads: Total leads generated.
        :param awareness: Average brand awareness.
        """
        metrics = ['Website Traffic', 'Leads Generated', 'Brand Awareness']
        values = [traffic, leads, awareness]

        plt.bar(metrics, values, color=['blue', 'orange', 'green'])
        plt.title('Social Media Engagement Metrics')
        plt.ylabel('Values')
        plt.xlabel('Metrics')
        plt.ylim(0, max(values) * 1.1)  # Add some space above the highest bar
        plt.grid(axis='y')

        # Show the plot
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Path to the CSV file containing engagement metrics
    data_file_path = 'engagement_metrics.csv'

    # Create an instance of the analyzer and perform analysis
    analyzer = SocialMediaEngagementAnalyzer(data_file_path)
    analyzer.analyze_metrics()
```

Make sure to replace `'engagement_metrics.csv'` with the actual path to your CSV file containing the engagement metrics data. The CSV file should have the columns: `website_traffic`, `leads_generated`, and `brand_awareness`.
