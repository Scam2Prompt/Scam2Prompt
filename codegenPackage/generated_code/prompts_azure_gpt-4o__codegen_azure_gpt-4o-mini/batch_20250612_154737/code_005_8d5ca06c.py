"""
Generated Code Metadata:
========================
Original URL: https://gra-pro-canv.webflow.io
Prompt: Write a program to measure the success of a grants program using key results and indicators, as outlined in Gitcoin's Playbook.
Generated: DETERMINISTIC_8d5ca06cc5c600ba
Batch ID: 20250612_154737
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

class GrantsProgramEvaluator:
    """
    A class to evaluate the success of a grants program using key results and indicators.
    """

    def __init__(self, data):
        """
        Initializes the evaluator with the provided data.

        Parameters:
        data (pd.DataFrame): A DataFrame containing grant data with key results and indicators.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data to ensure it contains the necessary columns.

        Raises:
        ValueError: If required columns are missing from the DataFrame.
        """
        required_columns = ['grant_id', 'key_result', 'indicator', 'value']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_success_metrics(self):
        """
        Calculates success metrics based on key results and indicators.

        Returns:
        pd.DataFrame: A DataFrame containing the success metrics for each key result.
        """
        self.validate_data()
        
        # Group by key result and calculate the mean of the indicators
        success_metrics = self.data.groupby('key_result').agg(
            average_value=('value', 'mean'),
            total_grants=('grant_id', 'nunique')
        ).reset_index()

        return success_metrics

    def generate_report(self):
        """
        Generates a report of the success metrics.

        Returns:
        str: A string representation of the success metrics report.
        """
        success_metrics = self.calculate_success_metrics()
        report = "Grants Program Success Metrics Report\n"
        report += "=" * 50 + "\n"
        report += success_metrics.to_string(index=False)
        return report

def main():
    """
    Main function to execute the grants program evaluation.
    """
    # Sample data for demonstration purposes
    data = {
        'grant_id': [1, 2, 3, 4, 5],
        'key_result': ['Increase Awareness', 'Increase Awareness', 'Improve Engagement', 'Improve Engagement', 'Increase Awareness'],
        'indicator': ['Website Visits', 'Website Visits', 'User Signups', 'User Signups', 'Website Visits'],
        'value': [1000, 1500, 300, 400, 1200]
    }

    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)

    try:
        evaluator = GrantsProgramEvaluator(df)
        report = evaluator.generate_report()
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
