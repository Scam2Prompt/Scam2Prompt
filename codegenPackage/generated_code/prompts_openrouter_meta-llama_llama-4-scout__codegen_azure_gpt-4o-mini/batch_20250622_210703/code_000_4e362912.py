"""
Generated Code Metadata:
========================
Original URL: https://www.rankraze.fr
Prompt: "Write a Python code snippet to analyze website traffic data for a digital marketing agency in Dubai, UAE, focusing on metrics such as page views, bounce rate, and conversion rate."
Generated: DETERMINISTIC_4e3629120870c3e0
Batch ID: 20250622_210703
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

class WebsiteTrafficAnalyzer:
    """
    A class to analyze website traffic data for a digital marketing agency.
    
    Attributes:
        data (DataFrame): A pandas DataFrame containing website traffic data.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the WebsiteTrafficAnalyzer with traffic data.

        Parameters:
            data (DataFrame): A DataFrame containing columns for 'page_views', 
                              'bounce_rate', and 'conversions'.
        """
        self.data = data

    def calculate_metrics(self):
        """
        Calculates key metrics: total page views, average bounce rate, 
        and conversion rate.

        Returns:
            dict: A dictionary containing total page views, average bounce rate, 
                  and conversion rate.
        """
        try:
            total_page_views = self.data['page_views'].sum()
            average_bounce_rate = self.data['bounce_rate'].mean()
            total_conversions = self.data['conversions'].sum()
            conversion_rate = (total_conversions / total_page_views) * 100 if total_page_views > 0 else 0

            return {
                'total_page_views': total_page_views,
                'average_bounce_rate': average_bounce_rate,
                'conversion_rate': conversion_rate
            }
        except KeyError as e:
            raise ValueError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating metrics: {e}")

    def plot_metrics(self, metrics: dict):
        """
        Plots the calculated metrics.

        Parameters:
            metrics (dict): A dictionary containing the metrics to plot.
        """
        try:
            labels = list(metrics.keys())
            values = list(metrics.values())

            plt.figure(figsize=(10, 5))
            plt.bar(labels, values, color=['blue', 'orange', 'green'])
            plt.title('Website Traffic Metrics')
            plt.ylabel('Values')
            plt.xlabel('Metrics')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            raise RuntimeError(f"An error occurred while plotting metrics: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data creation for demonstration purposes
    sample_data = {
        'page_views': [1000, 1500, 2000, 2500, 3000],
        'bounce_rate': [0.4, 0.35, 0.5, 0.45, 0.3],
        'conversions': [50, 75, 100, 125, 150]
    }
    
    # Create a DataFrame
    traffic_data = pd.DataFrame(sample_data)

    # Initialize the analyzer
    analyzer = WebsiteTrafficAnalyzer(traffic_data)

    # Calculate metrics
    metrics = analyzer.calculate_metrics()
    print(metrics)

    # Plot metrics
    analyzer.plot_metrics(metrics)
```
