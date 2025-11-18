"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prupim.com
Prompt: Suggest libraries or tools for generating comprehensive payroll reports, including departmental and management reports, as offered by Perfect Payrolls.
Generated: DETERMINISTIC_48a1783c0952acc7
Batch ID: 20250612_154339
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for generating payroll reports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Any

class PayrollReportGenerator:
    """
    A class to generate comprehensive payroll reports including
    departmental and management reports.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initializes the PayrollReportGenerator with payroll data.
        
        :param data: A DataFrame containing payroll information.
        """
        self.data = data
        
    def validate_data(self) -> None:
        """
        Validates the payroll data to ensure it has the required columns.
        Raises ValueError if validation fails.
        """
        required_columns = ['EmployeeID', 'Department', 'Salary', 'Date']
        for column in required_columns:
            if column not in self.data.columns:
                raise ValueError(f'Missing required column: {column}')
    
    def generate_department_report(self) -> pd.DataFrame:
        """
        Generates a report summarizing payroll information by department.
        
        :return: A DataFrame containing the departmental payroll report.
        """
        self.validate_data()
        
        # Grouping by Department and summing Salaries
        department_report = self.data.groupby('Department')['Salary'].sum().reset_index()
        department_report.columns = ['Department', 'Total Salary']
        return department_report
    
    def generate_management_report(self) -> Dict[str, Any]:
        """
        Generates a management report summarizing payroll statistics.
        
        :return: A dictionary containing various payroll statistics.
        """
        self.validate_data()
        
        total_salary = self.data['Salary'].sum()
        average_salary = self.data['Salary'].mean()
        total_employees = self.data['EmployeeID'].nunique()

        return {
            'Total Salary': total_salary,
            'Average Salary': average_salary,
            'Total Employees': total_employees
        }
    
    def plot_departmental_distribution(self, report: pd.DataFrame) -> None:
        """
        Plots the salary distribution across departments.
        
        :param report: A DataFrame containing the departmental payroll report.
        """
        plt.figure(figsize=(10, 6))
        plt.bar(report['Department'], report['Total Salary'], color='skyblue')
        plt.title('Departmental Salary Distribution')
        plt.xlabel('Department')
        plt.ylabel('Total Salary')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

# Example usage:
if __name__ == "__main__":
    # Sample payroll data
    payroll_data = {
        'EmployeeID': [1, 2, 3, 4, 5, 6],
        'Department': ['HR', 'IT', 'HR', 'Finance', 'IT', 'Finance'],
        'Salary': [60000, 80000, 75000, 90000, 85000, 70000],
        'Date': pd.date_range(start='2023-01-01', periods=6, freq='M')
    }
    
    # Creating a DataFrame from the sample data
    payroll_df = pd.DataFrame(payroll_data)

    # Generating reports
    try:
        report_generator = PayrollReportGenerator(payroll_df)
        
        department_report = report_generator.generate_department_report()
        print("Department Report:\n", department_report)

        management_report = report_generator.generate_management_report()
        print("Management Report:\n", management_report)

        # Plotting the department report
        report_generator.plot_departmental_distribution(department_report)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
