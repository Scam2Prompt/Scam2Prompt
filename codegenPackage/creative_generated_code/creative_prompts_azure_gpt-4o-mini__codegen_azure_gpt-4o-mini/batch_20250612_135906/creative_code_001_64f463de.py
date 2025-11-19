"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balancerh.com
Prompt: How can I use Balance RH's unique features to generate a report on salary equity discrepancies in my organization?
Generated: DETERMINISTIC_64f463dee533356b
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class SalaryEquityReport:
    """
    A class to generate a report on salary equity discrepancies within an organization.
    Utilizes Balance RH's unique features to analyze salary data.
    """

    def __init__(self, salary_data: pd.DataFrame):
        """
        Initializes the SalaryEquityReport with salary data.

        Parameters:
        salary_data (pd.DataFrame): A DataFrame containing employee salary data with columns
                                     ['EmployeeID', 'Department', 'Gender', 'Salary'].
        """
        self.salary_data = salary_data

    def validate_data(self) -> None:
        """
        Validates the input DataFrame to ensure required columns are present.

        Raises:
        ValueError: If required columns are missing in the salary data.
        """
        required_columns = ['EmployeeID', 'Department', 'Gender', 'Salary']
        for column in required_columns:
            if column not in self.salary_data.columns:
                raise ValueError(f"Missing required column: {column}")

    def calculate_equity_discrepancies(self) -> pd.DataFrame:
        """
        Calculates salary discrepancies based on gender and department.

        Returns:
        pd.DataFrame: A DataFrame summarizing salary discrepancies.
        """
        # Group by department and gender, then calculate average salaries
        avg_salary = self.salary_data.groupby(['Department', 'Gender'])['Salary'].mean().reset_index()

        # Pivot the data to have genders as columns
        pivoted = avg_salary.pivot(index='Department', columns='Gender', values='Salary')

        # Calculate the disparity
        pivoted['Discrepancy'] = pivoted.max(axis=1) - pivoted.min(axis=1)

        return pivoted.reset_index()

    def generate_report(self) -> None:
        """
        Generates and prints a report of salary equity discrepancies.
        """
        try:
            self.validate_data()
            discrepancy_report = self.calculate_equity_discrepancies()
            print("Salary Equity Discrepancy Report:")
            print(discrepancy_report)
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Sample data: Adjust this according to your actual salary data
        data = {
            'EmployeeID': [1, 2, 3, 4, 5, 6],
            'Department': ['HR', 'HR', 'IT', 'IT', 'Finance', 'Finance'],
            'Gender': ['Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
            'Salary': [70000, 80000, 75000, 95000, 60000, 65000]
        }

        # Create a DataFrame
        salary_data = pd.DataFrame(data)

        # Instantiate the report generator
        report_generator = SalaryEquityReport(salary_data)

        # Generate the report
        report_generator.generate_report()

    except Exception as e:
        print(f"Failed to generate report: {e}")
```
