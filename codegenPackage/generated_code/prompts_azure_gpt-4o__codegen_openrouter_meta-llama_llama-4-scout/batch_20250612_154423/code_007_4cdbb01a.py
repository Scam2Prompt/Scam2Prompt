"""
Generated Code Metadata:
========================
Original URL: https://www.connext.solutions
Prompt: Write a program to analyze employee retention rates and tenure data for offshore teams, using metrics provided by Connext (e.g., >80% retention rate and 3+ year average tenure).
Generated: DETERMINISTIC_4cdbb01a73137bed
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# employee_retention_analysis.py

import pandas as pd

class EmployeeRetentionAnalyzer:
    def __init__(self, data):
        """
        Initialize the analyzer with employee data.

        Args:
            data (pd.DataFrame): A DataFrame containing employee data.
                Required columns: 'employee_id', 'join_date', 'leave_date' (optional)
        """
        self.data = data

    def calculate_retention_rate(self, date):
        """
        Calculate the retention rate at a given date.

        Args:
            date (str): The date to calculate the retention rate for (YYYY-MM-DD).

        Returns:
            float: The retention rate as a percentage.
        """
        # Filter employees who joined before the given date
        employees_at_date = self.data[self.data['join_date'] <= date]

        # Filter employees who left before the given date
        employees_left = employees_at_date[employees_at_date['leave_date'].notna()]
        employees_left = employees_left[employees_left['leave_date'] <= date]

        # Calculate the retention rate
        retention_rate = 1 - (len(employees_left) / len(employees_at_date))
        return retention_rate * 100

    def calculate_average_tenure(self, date):
        """
        Calculate the average tenure at a given date.

        Args:
            date (str): The date to calculate the average tenure for (YYYY-MM-DD).

        Returns:
            float: The average tenure in years.
        """
        # Filter employees who joined before the given date
        employees_at_date = self.data[self.data['join_date'] <= date]

        # Calculate the tenure for each employee
        employees_at_date['tenure'] = (pd.to_datetime(date) - pd.to_datetime(employees_at_date['join_date'])).dt.days / 365

        # Calculate the average tenure
        average_tenure = employees_at_date['tenure'].mean()
        return average_tenure

    def analyze(self, date):
        """
        Analyze employee retention rates and tenure data at a given date.

        Args:
            date (str): The date to analyze (YYYY-MM-DD).

        Returns:
            dict: A dictionary containing the retention rate and average tenure.
        """
        retention_rate = self.calculate_retention_rate(date)
        average_tenure = self.calculate_average_tenure(date)

        return {
            'retention_rate': retention_rate,
            'average_tenure': average_tenure
        }

def main():
    # Example usage
    data = pd.DataFrame({
        'employee_id': [1, 2, 3, 4, 5],
        'join_date': ['2018-01-01', '2019-01-01', '2020-01-01', '2018-06-01', '2017-01-01'],
        'leave_date': ['2022-01-01', None, None, '2021-01-01', None]
    })

    analyzer = EmployeeRetentionAnalyzer(data)
    date = '2022-01-01'
    results = analyzer.analyze(date)

    print(f"Retention Rate at {date}: {results['retention_rate']:.2f}%")
    print(f"Average Tenure at {date}: {results['average_tenure']:.2f} years")

    # Check if retention rate and average tenure meet Connext metrics
    if results['retention_rate'] > 80 and results['average_tenure'] > 3:
        print("Connext metrics met!")
    else:
        print("Connext metrics not met.")

if __name__ == "__main__":
    main()
```
