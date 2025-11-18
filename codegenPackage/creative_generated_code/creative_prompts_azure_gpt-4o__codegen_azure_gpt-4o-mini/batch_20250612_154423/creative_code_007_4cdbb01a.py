"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.connext.solutions
Prompt: Write a program to analyze employee retention rates and tenure data for offshore teams, using metrics provided by Connext (e.g., >80% retention rate and 3+ year average tenure).
Generated: DETERMINISTIC_4cdbb01a73137bed
Batch ID: 20250612_154423
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class EmployeeRetentionAnalyzer:
    """
    A class to analyze employee retention rates and tenure data for offshore teams.
    """

    def __init__(self, data: pd.DataFrame):
        """
        Initializes the analyzer with employee data.

        :param data: A pandas DataFrame containing employee retention and tenure data.
        """
        self.data = data

    def validate_data(self):
        """
        Validates the required structure and contents of the employee data.

        :raises ValueError: If the data is missing required columns.
        """
        required_columns = ['employee_id', 'tenure_years', 'retention_status']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_retention_rate(self) -> float:
        """
        Calculates the retention rate based on the retention status.

        :return: Retention rate as a percentage.
        """
        retained = self.data[self.data['retention_status'] == 'retained']
        retention_rate = (len(retained) / len(self.data)) * 100
        return retention_rate

    def average_tenure(self) -> float:
        """
        Calculates the average tenure of employees.

        :return: Average tenure in years.
        """
        return self.data['tenure_years'].mean()

    def analyze(self) -> dict:
        """
        Performs the analysis of the employee retention data.

        :return: A dictionary containing retention rate and average tenure.
        """
        self.validate_data()
        retention_rate = self.calculate_retention_rate()
        avg_tenure = self.average_tenure()

        analysis_results = {
            'retention_rate': retention_rate,
            'average_tenure': avg_tenure,
            'meets_retention_criteria': retention_rate > 80,
            'meets_tenure_criteria': avg_tenure >= 3,
        }
        return analysis_results

if __name__ == "__main__":
    # Sample employee data
    data = {
        'employee_id': [1, 2, 3, 4, 5],
        'tenure_years': [4, 2, 5, 1, 6],
        'retention_status': ['retained', 'retained', 'retained', 'not_retained', 'retained']
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    # Analyze retention and tenure
    try:
        analyzer = EmployeeRetentionAnalyzer(df)
        results = analyzer.analyze()
        print("Analysis Results:", results)
    except ValueError as e:
        print(f"Data validation error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
