"""
Generated Code Metadata:
========================
Original URL: https://starshot90.com
Prompt: Create a program that visualizes web analytics data to improve online business performance, as discussed in the "Web Analytics: Understanding and Utilizing Data" section of the Star Shot 90 website.
Generated: DETERMINISTIC_d06e327b226cb4a1
Batch ID: 20250612_154657
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
import seaborn as sns
import numpy as np

# Set the style for seaborn
sns.set(style="whitegrid")

class WebAnalyticsVisualizer:
    def __init__(self, data_file):
        """
        Initializes the WebAnalyticsVisualizer with the provided data file.

        :param data_file: Path to the CSV file containing web analytics data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads the web analytics data from a CSV file.

        :return: DataFrame containing the web analytics data.
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

    def visualize_page_views(self):
        """
        Visualizes the number of page views over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='date', y='page_views', marker='o')
            plt.title('Page Views Over Time')
            plt.xlabel('Date')
            plt.ylabel('Number of Page Views')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
        except Exception as e:
            print(f"An error occurred while visualizing page views: {e}")

    def visualize_conversion_rate(self):
        """
        Visualizes the conversion rate over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='date', y='conversion_rate', marker='o', color='orange')
            plt.title('Conversion Rate Over Time')
            plt.xlabel('Date')
            plt.ylabel('Conversion Rate (%)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
        except Exception as e:
            print(f"An error occurred while visualizing conversion rate: {e}")

    def visualize_bounce_rate(self):
        """
        Visualizes the bounce rate over time.
        """
        try:
            plt.figure(figsize=(12, 6))
            sns.lineplot(data=self.data, x='date', y='bounce_rate', marker='o', color='red')
            plt.title('Bounce Rate Over Time')
            plt.xlabel('Date')
            plt.ylabel('Bounce Rate (%)')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except KeyError as e:
            print(f"Error: Missing expected column in data: {e}")
        except Exception as e:
            print(f"An error occurred while visualizing bounce rate: {e}")

if __name__ == "__main__":
    # Example usage
    data_file_path = 'web_analytics_data.csv'  # Replace with your actual data file path
    visualizer = WebAnalyticsVisualizer(data_file_path)
    
    # Visualize different metrics
    visualizer.visualize_page_views()
    visualizer.visualize_conversion_rate()
    visualizer.visualize_bounce_rate()
```

Make sure to replace `'web_analytics_data.csv'` with the actual path to your web analytics data file. The CSV file should contain columns named `date`, `page_views`, `conversion_rate`, and `bounce_rate` for the visualizations to work correctly.
