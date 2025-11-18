"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://3rdandtaylor.com
Prompt: Create a Python script to calculate marketing-sourced revenue and track performance metrics, inspired by the case studies shared on the 3rd & Taylor website.
Generated: DETERMINISTIC_8ec1384a2542c8f5
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class MarketingPerformanceTracker:
    def __init__(self, data_file):
        """
        Initializes the MarketingPerformanceTracker with data from a CSV file.

        :param data_file: str - Path to the CSV file containing marketing data.
        """
        try:
            self.data = pd.read_csv(data_file)
            self.validate_data()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {data_file} not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("Data file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the data: {e}")

    def validate_data(self):
        """
        Validates the data to ensure required columns are present.
        """
        required_columns = ['source', 'revenue', 'date', 'campaign']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_marketing_sourced_revenue(self):
        """
        Calculates total revenue sourced from marketing campaigns.

        :return: float - Total marketing-sourced revenue.
        """
        try:
            marketing_revenue = self.data['revenue'][self.data['source'] == 'marketing'].sum()
            return marketing_revenue
        except Exception as e:
            raise Exception(f"An error occurred while calculating marketing sourced revenue: {e}")

    def track_performance_metrics(self):
        """
        Tracks performance metrics for marketing campaigns.

        :return: DataFrame - A DataFrame containing campaign performance metrics.
        """
        try:
            metrics = self.data.groupby('campaign').agg(
                total_revenue=pd.NamedAgg(column='revenue', aggfunc='sum'),
                total_count=pd.NamedAgg(column='revenue', aggfunc='count')
            ).reset_index()
            return metrics
        except Exception as e:
            raise Exception(f"An error occurred while tracking performance metrics: {e}")

if __name__ == '__main__':
    # Example usage
    try:
        tracker = MarketingPerformanceTracker('marketing_data.csv')
        total_revenue = tracker.calculate_marketing_sourced_revenue()
        print(f"Total Marketing-Sourced Revenue: ${total_revenue:.2f}")
        
        performance_metrics = tracker.track_performance_metrics()
        print("Campaign Performance Metrics:")
        print(performance_metrics)
    except Exception as e:
        print(f"Error: {e}")
```
