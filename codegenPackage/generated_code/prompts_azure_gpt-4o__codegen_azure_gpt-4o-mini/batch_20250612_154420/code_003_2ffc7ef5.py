"""
Generated Code Metadata:
========================
Original URL: https://stuff-artgobblers.com
Prompt: Create a script to analyze social media engagement metrics, inspired by the social media marketing strategies discussed by ACE Digital Marketing Agency.
Generated: DETERMINISTIC_2ffc7ef59957b350
Batch ID: 20250612_154420
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

    def analyze_engagement(self):
        """
        Analyzes engagement metrics and generates summary statistics.

        :return: DataFrame - A DataFrame containing summary statistics.
        """
        try:
            summary = self.data.describe()
            print("Engagement analysis completed.")
            return summary
        except Exception as e:
            print(f"Error during analysis: {e}")
            raise

    def plot_engagement(self):
        """
        Plots engagement metrics over time.

        :return: None
        """
        try:
            plt.figure(figsize=(10, 6))
            for column in self.data.columns[1:]:  # Assuming the first column is 'Date'
                plt.plot(self.data['Date'], self.data[column], label=column)
            plt.title('Social Media Engagement Metrics Over Time')
            plt.xlabel('Date')
            plt.ylabel('Engagement Metrics')
            plt.xticks(rotation=45)
            plt.legend()
            plt.tight_layout()
            plt.show()
            print("Engagement plot generated.")
        except Exception as e:
            print(f"Error during plotting: {e}")
            raise

if __name__ == "__main__":
    # Example usage
    try:
        analyzer = SocialMediaEngagementAnalyzer('engagement_data.csv')
        summary_stats = analyzer.analyze_engagement()
        print(summary_stats)
        analyzer.plot_engagement()
    except Exception as e:
        print(f"An error occurred: {e}")
```
