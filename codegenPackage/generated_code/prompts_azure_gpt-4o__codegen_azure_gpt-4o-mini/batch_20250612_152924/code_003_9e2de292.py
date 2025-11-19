"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Create a Python program to analyze social media campaign performance metrics for an event, leveraging Pozy Media's expertise in digital outreach and marketing.
Generated: DETERMINISTIC_9e2de2925f641531
Batch ID: 20250612_152924
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

class SocialMediaCampaignAnalyzer:
    """
    A class to analyze social media campaign performance metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the provided data file.

        :param data_file: Path to the CSV file containing campaign metrics.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the campaign data from a CSV file.

        :return: DataFrame containing the campaign metrics.
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
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
            raise

    def analyze_metrics(self):
        """
        Analyzes the campaign metrics and generates summary statistics.
        
        :return: A dictionary containing summary statistics.
        """
        try:
            summary = {
                'total_impressions': self.data['impressions'].sum(),
                'total_engagements': self.data['engagements'].sum(),
                'average_engagement_rate': (self.data['engagements'].sum() / self.data['impressions'].sum()) * 100,
                'total_clicks': self.data['clicks'].sum(),
            }
            print("Metrics analyzed successfully.")
            return summary
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def visualize_metrics(self):
        """
        Visualizes the campaign performance metrics using bar charts.
        """
        try:
            metrics = self.analyze_metrics()
            labels = list(metrics.keys())
            values = list(metrics.values())

            plt.bar(labels, values, color='blue')
            plt.title('Social Media Campaign Performance Metrics')
            plt.xlabel('Metrics')
            plt.ylabel('Values')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
            print("Metrics visualized successfully.")
        except Exception as e:
            print(f"Error during visualization: {e}")
            raise

if __name__ == "__main__":
    # Path to the CSV file containing campaign metrics
    data_file_path = 'campaign_metrics.csv'
    
    # Create an instance of the analyzer
    analyzer = SocialMediaCampaignAnalyzer(data_file_path)
    
    # Analyze and visualize the metrics
    try:
        metrics_summary = analyzer.analyze_metrics()
        print("Metrics Summary:", metrics_summary)
        analyzer.visualize_metrics()
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
```
