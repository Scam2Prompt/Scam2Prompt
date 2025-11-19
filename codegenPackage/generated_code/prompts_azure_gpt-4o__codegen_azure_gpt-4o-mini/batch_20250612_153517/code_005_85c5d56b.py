"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: Develop a Python script to analyze employee performance data and recommend career development plans, inspired by Videtis Consultores' outplacement program.
Generated: DETERMINISTIC_85c5d56b05759121
Batch ID: 20250612_153517
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

class EmployeePerformanceAnalyzer:
    """
    A class to analyze employee performance data and recommend career development plans.
    """

    def __init__(self, data_file):
        """
        Initializes the analyzer with the given data file.

        :param data_file: Path to the CSV file containing employee performance data.
        """
        self.data_file = data_file
        self.performance_data = self.load_data()

    def load_data(self):
        """
        Loads employee performance data from a CSV file.

        :return: DataFrame containing the performance data.
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

    def analyze_performance(self):
        """
        Analyzes employee performance data and returns a summary.

        :return: DataFrame with performance summary.
        """
        try:
            # Group by employee and calculate average performance score
            performance_summary = self.performance_data.groupby('employee_id').agg({
                'performance_score': 'mean',
                'years_at_company': 'mean'
            }).reset_index()

            return performance_summary
        except Exception as e:
            raise Exception(f"An error occurred during performance analysis: {e}")

    def recommend_development_plans(self, performance_summary):
        """
        Recommends career development plans based on performance analysis.

        :param performance_summary: DataFrame containing performance summary.
        :return: DataFrame with recommended development plans.
        """
        try:
            recommendations = []
            for _, row in performance_summary.iterrows():
                if row['performance_score'] < 3:
                    recommendations.append((row['employee_id'], 'Intensive Training Program'))
                elif 3 <= row['performance_score'] < 4:
                    recommendations.append((row['employee_id'], 'Mentorship Program'))
                else:
                    recommendations.append((row['employee_id'], 'Leadership Development Program'))

            return pd.DataFrame(recommendations, columns=['employee_id', 'development_plan'])
        except Exception as e:
            raise Exception(f"An error occurred while recommending development plans: {e}")

    def run_analysis(self):
        """
        Executes the performance analysis and development plan recommendation process.
        """
        try:
            performance_summary = self.analyze_performance()
            recommendations = self.recommend_development_plans(performance_summary)
            return recommendations
        except Exception as e:
            print(f"An error occurred during the analysis process: {e}")

if __name__ == "__main__":
    # Example usage
    data_file_path = 'employee_performance_data.csv'  # Path to the CSV file
    analyzer = EmployeePerformanceAnalyzer(data_file_path)
    development_plans = analyzer.run_analysis()
    
    if development_plans is not None:
        print(development_plans)
```
