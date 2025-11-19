"""
Generated Code Metadata:
========================
Original URL: https://asnetinfotech.com
Prompt: Write code to analyze social media engagement metrics, leveraging Asnet Infotech's expertise in social media and digital marketing.
Generated: DETERMINISTIC_ef23273c2fe4ffb5
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
import numpy as np
import matplotlib.pyplot as plt

class SocialMediaEngagementAnalyzer:
    """
    A class to analyze social media engagement metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with a CSV file containing engagement metrics.

        :param data_file: str - Path to the CSV file containing engagement data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the engagement data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the engagement data.
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

    def calculate_engagement_rate(self):
        """
        Calculates the engagement rate for each post.

        :return: Series - A pandas Series containing the engagement rates.
        """
        try:
            self.data['engagement_rate'] = (
                (self.data['likes'] + self.data['comments'] + self.data['shares']) /
                self.data['impressions']
            ) * 100
            return self.data['engagement_rate']
        except KeyError as e:
            print(f"Error: Missing expected column in data - {e}")
            raise

    def visualize_engagement(self):
        """
        Visualizes the engagement metrics using a bar chart.
        """
        try:
            plt.figure(figsize=(10, 6))
            plt.bar(self.data['post_id'], self.data['engagement_rate'], color='skyblue')
            plt.title('Social Media Engagement Rate by Post')
            plt.xlabel('Post ID')
            plt.ylabel('Engagement Rate (%)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error while visualizing engagement: {e}")
            raise

    def summary_statistics(self):
        """
        Prints summary statistics of the engagement metrics.

        :return: None
        """
        try:
            print("Summary Statistics:")
            print(self.data[['likes', 'comments', 'shares', 'impressions', 'engagement_rate']].describe())
        except Exception as e:
            print(f"Error while calculating summary statistics: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = SocialMediaEngagementAnalyzer('engagement_data.csv')
        analyzer.calculate_engagement_rate()
        analyzer.visualize_engagement()
        analyzer.summary_statistics()
    except Exception as e:
        print(f"An error occurred: {e}")
```
