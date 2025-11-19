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
# Import required libraries
import pandas as pd
from datetime import datetime

class DigitalMarketingReport:
    def __init__(self, campaign_name, start_date, end_date):
        """
        Initialize a digital marketing report.

        Args:
            campaign_name (str): Name of the digital marketing campaign.
            start_date (str): Start date of the campaign in 'YYYY-MM-DD' format.
            end_date (str): End date of the campaign in 'YYYY-MM-DD' format.
        """
        self.campaign_name = campaign_name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = datetime.strptime(end_date, '%Y-%m-%d')
        self.metrics = {
            'customer_satisfaction_rate': [],
            'project_completion_rate': [],
            'sales_increase_percentage': []
        }

    def add_metric(self, metric_name, value):
        """
        Add a metric value to the report.

        Args:
            metric_name (str): Name of the metric.
            value (float): Value of the metric.

        Raises:
            ValueError: If the metric name is not recognized.
        """
        if metric_name in self.metrics:
            self.metrics[metric_name].append(value)
        else:
            raise ValueError(f"Invalid metric name: {metric_name}")

    def calculate_average(self, metric_name):
        """
        Calculate the average value of a metric.

        Args:
            metric_name (str): Name of the metric.

        Returns:
            float: Average value of the metric.

        Raises:
            ValueError: If the metric name is not recognized or if no values are available.
        """
        if metric_name in self.metrics:
            values = self.metrics[metric_name]
            if values:
                return sum(values) / len(values)
            else:
                raise ValueError(f"No values available for metric: {metric_name}")
        else:
            raise ValueError(f"Invalid metric name: {metric_name}")

    def generate_report(self):
        """
        Generate a data analysis report.

        Returns:
            dict: A dictionary containing the report data.
        """
        report = {
            'campaign_name': self.campaign_name,
            'start_date': self.start_date.strftime('%Y-%m-%d'),
            'end_date': self.end_date.strftime('%Y-%m-%d'),
            'metrics': {}
        }

        for metric_name in self.metrics:
            try:
                average_value = self.calculate_average(metric_name)
                report['metrics'][metric_name] = average_value
            except ValueError as e:
                print(f"Error calculating {metric_name}: {e}")

        return report

    def to_dataframe(self):
        """
        Convert the report to a Pandas DataFrame.

        Returns:
            pd.DataFrame: A DataFrame containing the report data.
        """
        report = self.generate_report()
        data = {
            'Metric': list(report['metrics'].keys()),
            'Value': list(report['metrics'].values())
        }
        return pd.DataFrame(data)

def main():
    # Create a digital marketing report
    report = DigitalMarketingReport('Jordan Campaign', '2022-01-01', '2022-12-31')

    # Add metric values
    report.add_metric('customer_satisfaction_rate', 85.0)
    report.add_metric('customer_satisfaction_rate', 90.0)
    report.add_metric('project_completion_rate', 95.0)
    report.add_metric('project_completion_rate', 92.0)
    report.add_metric('sales_increase_percentage', 20.0)
    report.add_metric('sales_increase_percentage', 25.0)

    # Generate and print the report
    report_data = report.generate_report()
    print("Data Analysis Report:")
    print(f"Campaign Name: {report_data['campaign_name']}")
    print(f"Start Date: {report_data['start_date']}")
    print(f"End Date: {report_data['end_date']}")
    print("Metrics:")
    for metric_name, value in report_data['metrics'].items():
        print(f"{metric_name.capitalize().replace('_', ' ')}: {value:.2f}")

    # Convert to DataFrame and print
    df = report.to_dataframe()
    print("\nReport as DataFrame:")
    print(df)

if __name__ == "__main__":
    main()
```
