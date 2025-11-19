"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: "Write a Python script to analyze the effectiveness of digital marketing campaigns in Jordan, including metrics such as customer satisfaction rate, project completion rate, and sales increase percentage."
Generated: DETERMINISTIC_08e2907e1dd387f6
Batch ID: 20250622_212844
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# digital_marketing_analyzer.py

import pandas as pd

class DigitalMarketingAnalyzer:
    """
    Analyzes the effectiveness of digital marketing campaigns.

    Attributes:
        data (pd.DataFrame): A DataFrame containing campaign data.
    """

    def __init__(self, data):
        """
        Initializes the analyzer with campaign data.

        Args:
            data (pd.DataFrame): A DataFrame containing campaign data.
                Required columns: ['campaign_name', 'customer_satisfaction_rate', 
                                   'project_completion_rate', 'sales_increase_percentage']
        """
        required_columns = ['campaign_name', 'customer_satisfaction_rate', 
                            'project_completion_rate', 'sales_increase_percentage']
        if not all(col in data.columns for col in required_columns):
            raise ValueError("Data is missing required columns")
        self.data = data

    def calculate_average_customer_satisfaction(self):
        """
        Calculates the average customer satisfaction rate across all campaigns.

        Returns:
            float: The average customer satisfaction rate.
        """
        return self.data['customer_satisfaction_rate'].mean()

    def calculate_average_project_completion_rate(self):
        """
        Calculates the average project completion rate across all campaigns.

        Returns:
            float: The average project completion rate.
        """
        return self.data['project_completion_rate'].mean()

    def calculate_average_sales_increase(self):
        """
        Calculates the average sales increase percentage across all campaigns.

        Returns:
            float: The average sales increase percentage.
        """
        return self.data['sales_increase_percentage'].mean()

    def get_campaign_performance(self, campaign_name):
        """
        Retrieves the performance metrics for a specific campaign.

        Args:
            campaign_name (str): The name of the campaign.

        Returns:
            dict: A dictionary containing the campaign's performance metrics.
                Keys: ['customer_satisfaction_rate', 'project_completion_rate', 
                       'sales_increase_percentage']
        """
        campaign_data = self.data[self.data['campaign_name'] == campaign_name]
        if campaign_data.empty:
            raise ValueError("Campaign not found")
        return campaign_data.to_dict(orient='records')[0]

    def save_results_to_csv(self, results, filename):
        """
        Saves the analysis results to a CSV file.

        Args:
            results (list): A list of dictionaries containing the analysis results.
            filename (str): The name of the output CSV file.
        """
        pd.DataFrame(results).to_csv(filename, index=False)


def main():
    # Example usage
    data = pd.DataFrame({
        'campaign_name': ['Campaign 1', 'Campaign 2', 'Campaign 3'],
        'customer_satisfaction_rate': [0.8, 0.7, 0.9],
        'project_completion_rate': [0.9, 0.8, 0.95],
        'sales_increase_percentage': [10, 15, 8]
    })

    analyzer = DigitalMarketingAnalyzer(data)

    average_customer_satisfaction = analyzer.calculate_average_customer_satisfaction()
    average_project_completion_rate = analyzer.calculate_average_project_completion_rate()
    average_sales_increase = analyzer.calculate_average_sales_increase()

    print(f"Average Customer Satisfaction Rate: {average_customer_satisfaction:.2f}")
    print(f"Average Project Completion Rate: {average_project_completion_rate:.2f}")
    print(f"Average Sales Increase Percentage: {average_sales_increase:.2f}")

    campaign_performance = analyzer.get_campaign_performance('Campaign 1')
    print("Campaign 1 Performance:")
    print(campaign_performance)

    results = [
        {
            'metric': 'Average Customer Satisfaction Rate',
            'value': average_customer_satisfaction
        },
        {
            'metric': 'Average Project Completion Rate',
            'value': average_project_completion_rate
        },
        {
            'metric': 'Average Sales Increase Percentage',
            'value': average_sales_increase
        }
    ]

    analyzer.save_results_to_csv(results, 'analysis_results.csv')


if __name__ == "__main__":
    main()
```
