"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://armourersandbrasiers.co.uk
Prompt: Develop a program to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust, including metrics for educational outcomes and research advancements.
Generated: DETERMINISTIC_95363ddc294af343
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict

class GrantReport:
    """
    Class to generate reports on the impact of grants given by the Armourers & Brasiers' Gauntlet Trust.
    """

    def __init__(self, data: List[Dict]):
        """
        Initializes the GrantReport with grant data.

        :param data: A list of dictionaries containing grant information.
        """
        self.data = pd.DataFrame(data)
        self.validate_data()

    def validate_data(self):
        """
        Validate the input data to ensure it contains the necessary fields.
        Raises ValueError if validation fails.
        """
        required_columns = ['grant_id', 'amount', 'educational_outcome', 'research_advanced', 'year']
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f'Missing columns in data: {", ".join(missing_columns)}')

    def generate_summary(self) -> pd.DataFrame:
        """
        Generate a summary report of grants.

        :return: A DataFrame summarizing total amount, educational outcomes, and research advancements.
        """
        summary = self.data.groupby('year').agg({
            'amount': 'sum',
            'educational_outcome': 'mean',
            'research_advanced': 'mean'
        }).reset_index()
        summary.columns = ['Year', 'Total Amount', 'Average Educational Outcome', 'Average Research Advancement']
        return summary

    def save_report(self, summary: pd.DataFrame, filename: str):
        """
        Save the summary report to a CSV file.

        :param summary: The summary DataFrame to save.
        :param filename: The name of the file to save the report.
        """
        try:
            summary.to_csv(filename, index=False)
            print(f'Report saved to {filename}')
        except Exception as e:
            print(f'Error saving report: {e}')

    def plot_report(self, summary: pd.DataFrame):
        """
        Plot the summary report metrics.

        :param summary: The summary DataFrame containing the report data.
        """
        try:
            summary.plot(x='Year', kind='bar', figsize=(10, 6), title='Grant Impact Report')
            plt.xlabel('Year')
            plt.ylabel('Amount / Outcome')
            plt.legend(['Total Amount', 'Avg Educational Outcome', 'Avg Research Advancement'])
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f'Error plotting report: {e}')

# Example usage:
if __name__ == "__main__":
    # Sample data for demonstration
    sample_data = [
        {'grant_id': 1, 'amount': 10000, 'educational_outcome': 0.8, 'research_advanced': 0.9, 'year': 2021},
        {'grant_id': 2, 'amount': 15000, 'educational_outcome': 0.7, 'research_advanced': 0.85, 'year': 2021},
        {'grant_id': 3, 'amount': 20000, 'educational_outcome': 0.9, 'research_advanced': 0.95, 'year': 2022},
        {'grant_id': 4, 'amount': 18000, 'educational_outcome': 0.75, 'research_advanced': 0.8, 'year': 2022},
    ]

    try:
        report = GrantReport(sample_data)
        summary = report.generate_summary()
        report.save_report(summary, 'grant_report.csv')
        report.plot_report(summary)
    except Exception as e:
        print(f'Error generating report: {e}')
```
