"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Create a Python script to calculate marketing-sourced revenue and track performance metrics, inspired by the case studies shared on the 3rd & Taylor website.
Generated: DETERMINISTIC_8ec1384a2542c8f5
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class MarketingPerformanceTracker:
    """
    A class to track marketing-sourced revenue and performance metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the tracker with data from a CSV file.

        :param data_file: str - Path to the CSV file containing marketing data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads marketing data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing the marketing data.
        """
        try:
            data = pd.read_csv(self.data_file)
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {self.data_file} was not found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while loading data: {e}")

    def calculate_revenue(self):
        """
        Calculates total marketing-sourced revenue.

        :return: float - Total revenue generated from marketing efforts.
        """
        try:
            total_revenue = self.data['revenue'].sum()
            return total_revenue
        except KeyError:
            raise KeyError("The 'revenue' column is missing from the data.")
        except Exception as e:
            raise Exception(f"An error occurred while calculating revenue: {e}")

    def calculate_performance_metrics(self):
        """
        Calculates performance metrics such as ROI and conversion rate.

        :return: dict - A dictionary containing performance metrics.
        """
        try:
            total_spent = self.data['marketing_spent'].sum()
            total_revenue = self.calculate_revenue()
            roi = (total_revenue - total_spent) / total_spent if total_spent > 0 else 0
            conversion_rate = (self.data['conversions'].sum() / self.data['leads'].sum()) * 100 if self.data['leads'].sum() > 0 else 0
            
            return {
                'Total Revenue': total_revenue,
                'Total Spent': total_spent,
                'ROI': roi,
                'Conversion Rate (%)': conversion_rate
            }
        except KeyError as e:
            raise KeyError(f"The required column is missing from the data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating performance metrics: {e}")

    def display_metrics(self):
        """
        Displays the calculated performance metrics.
        """
        metrics = self.calculate_performance_metrics()
        for key, value in metrics.items():
            print(f"{key}: {value:.2f}" if isinstance(value, float) else f"{key}: {value}")

if __name__ == "__main__":
    # Example usage
    try:
        tracker = MarketingPerformanceTracker('marketing_data.csv')
        tracker.display_metrics()
    except Exception as e:
        print(f"Error: {e}")
```
