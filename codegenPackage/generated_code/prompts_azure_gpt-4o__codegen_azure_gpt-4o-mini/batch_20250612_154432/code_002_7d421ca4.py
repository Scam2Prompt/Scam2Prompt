"""
Generated Code Metadata:
========================
Original URL: https://3rdandtaylor.com
Prompt: Generate a Python script to audit and identify leaks in a revenue generation pipeline, following the "full-funnel approach to growth" methodology described by 3rd & Taylor.
Generated: DETERMINISTIC_7d421ca478e5016e
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
import numpy as np

class RevenuePipelineAuditor:
    """
    A class to audit and identify leaks in a revenue generation pipeline
    following the full-funnel approach to growth.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the auditor with the provided data.

        :param data: A pandas DataFrame containing the revenue pipeline data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the input data for necessary columns and data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['stage', 'count', 'conversion_rate']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not np.issubdtype(self.data['count'].dtype, np.number):
            raise ValueError("Column 'count' must be numeric.")
        if not np.issubdtype(self.data['conversion_rate'].dtype, np.number):
            raise ValueError("Column 'conversion_rate' must be numeric.")

    def calculate_leaks(self):
        """
        Calculates the leaks in the revenue pipeline by analyzing the conversion rates
        between stages.

        :return: A DataFrame with stages and their respective leak percentages.
        """
        self.validate_data()
        
        # Calculate expected counts based on conversion rates
        self.data['expected_count'] = self.data['count'].shift(1) * self.data['conversion_rate'].shift(1)
        self.data['leak'] = self.data['expected_count'] - self.data['count']
        self.data['leak_percentage'] = (self.data['leak'] / self.data['expected_count'].replace(0, np.nan)) * 100

        # Filter out the first stage as it has no previous stage to compare
        return self.data.dropna(subset=['leak_percentage'])

    def generate_report(self):
        """
        Generates a report of the leaks in the revenue pipeline.

        :return: A summary DataFrame of leaks.
        """
        leaks = self.calculate_leaks()
        report = leaks[['stage', 'leak', 'leak_percentage']]
        return report

def main():
    """
    Main function to execute the revenue pipeline audit.
    """
    # Sample data for demonstration purposes
    data = {
        'stage': ['Awareness', 'Interest', 'Decision', 'Action'],
        'count': [1000, 800, 400, 200],
        'conversion_rate': [0.8, 0.5, 0.5, 0.5]
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    try:
        auditor = RevenuePipelineAuditor(df)
        report = auditor.generate_report()
        print("Revenue Pipeline Leak Report:")
        print(report)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
