"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Create a data analysis report template for tracking the performance of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_7c5438641dd817fb
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
import matplotlib.pyplot as plt

class DigitalMarketingReport:
    """
    A class to generate a data analysis report for tracking the performance of digital marketing campaigns.
    """

    def __init__(self, data):
        """
        Initializes the DigitalMarketingReport with the provided data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing campaign performance data.
        """
        self.data = data

    def calculate_metrics(self):
        """
        Calculates key performance metrics from the campaign data.

        Returns:
        dict: A dictionary containing calculated metrics.
        """
        try:
            metrics = {
                'customer_satisfaction_rate': self.data['customer_satisfaction'].mean(),
                'project_completion_rate': self.data['project_completion'].mean(),
                'sales_increase_percentage': self.data['sales_increase'].mean()
            }
            return metrics
        except KeyError as e:
            raise KeyError(f"Missing expected column in data: {e}")
        except Exception as e:
            raise Exception(f"An error occurred while calculating metrics: {e}")

    def generate_report(self):
        """
        Generates a report of the calculated metrics and visualizes the data.

        Returns:
        None
        """
        try:
            metrics = self.calculate_metrics()
            print("Digital Marketing Campaign Performance Report")
            print("==============================================")
            for metric, value in metrics.items():
                print(f"{metric.replace('_', ' ').title()}: {value:.2f}")

            # Visualization
            self.visualize_metrics(metrics)
        except Exception as e:
            print(f"Error generating report: {e}")

    def visualize_metrics(self, metrics):
        """
        Visualizes the calculated metrics using a bar chart.

        Parameters:
        metrics (dict): A dictionary containing calculated metrics.

        Returns:
        None
        """
        try:
            plt.bar(metrics.keys(), metrics.values(), color=['blue', 'orange', 'green'])
            plt.title('Digital Marketing Campaign Performance Metrics')
            plt.ylabel('Percentage')
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error visualizing metrics: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration purposes
    data = {
        'customer_satisfaction': [85, 90, 78, 92, 88],
        'project_completion': [95, 100, 90, 85, 98],
        'sales_increase': [10, 15, 5, 20, 12]
    }
    
    # Create a DataFrame
    df = pd.DataFrame(data)

    # Initialize the report
    report = DigitalMarketingReport(df)

    # Generate the report
    report.generate_report()
```
