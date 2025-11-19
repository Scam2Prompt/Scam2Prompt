"""
Generated Code Metadata:
========================
Original URL: https://csl-seqirus.co.uk
Prompt: Generate a script to manage career development data for employees in a biotech company, incorporating diversity, equity, and inclusion metrics as outlined by CSL Seqirus UK.
Generated: DETERMINISTIC_29e546d73a193280
Batch ID: 20250612_154653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# career_development_manager.py

import pandas as pd
from datetime import datetime

class CareerDevelopmentManager:
    """
    Manages career development data for employees in a biotech company,
    incorporating diversity, equity, and inclusion metrics.
    """

    def __init__(self, data_file):
        """
        Initializes the CareerDevelopmentManager with employee data.

        Args:
            data_file (str): Path to the employee data CSV file.
        """
        self.data_file = data_file
        self.employees = self.load_employees()

    def load_employees(self):
        """
        Loads employee data from the CSV file.

        Returns:
            pd.DataFrame: Employee data.
        """
        try:
            return pd.read_csv(self.data_file)
        except FileNotFoundError:
            print(f"Error: File '{self.data_file}' not found.")
            return pd.DataFrame()

    def save_employees(self):
        """
        Saves employee data to the CSV file.
        """
        self.employees.to_csv(self.data_file, index=False)

    def add_employee(self, employee_data):
        """
        Adds a new employee to the database.

        Args:
            employee_data (dict): Employee data, including:
                - name (str)
                - job_title (str)
                - department (str)
                - diversity_group (str)
                - equity_status (str)
                - inclusion_score (float)
        """
        new_employee = pd.DataFrame([employee_data])
        self.employees = pd.concat([self.employees, new_employee], ignore_index=True)
        self.save_employees()

    def update_employee(self, employee_id, employee_data):
        """
        Updates an existing employee's data.

        Args:
            employee_id (int): Employee ID.
            employee_data (dict): Updated employee data.
        """
        if employee_id < len(self.employees):
            self.employees.loc[employee_id, employee_data.keys()] = employee_data.values()
            self.save_employees()
        else:
            print(f"Error: Employee with ID {employee_id} not found.")

    def calculate_diversity_metric(self):
        """
        Calculates the diversity metric based on employee data.

        Returns:
            float: Diversity metric score.
        """
        diversity_groups = self.employees['diversity_group'].unique()
        diversity_metric = len(diversity_groups) / len(self.employees)
        return diversity_metric

    def calculate_equity_metric(self):
        """
        Calculates the equity metric based on employee data.

        Returns:
            float: Equity metric score.
        """
        equity_statuses = self.employees['equity_status'].unique()
        equity_metric = len([status for status in equity_statuses if status == 'active']) / len(self.employees)
        return equity_metric

    def calculate_inclusion_metric(self):
        """
        Calculates the inclusion metric based on employee data.

        Returns:
            float: Inclusion metric score.
        """
        inclusion_scores = self.employees['inclusion_score']
        inclusion_metric = inclusion_scores.mean()
        return inclusion_metric

    def generate_report(self):
        """
        Generates a report on diversity, equity, and inclusion metrics.
        """
        diversity_metric = self.calculate_diversity_metric()
        equity_metric = self.calculate_equity_metric()
        inclusion_metric = self.calculate_inclusion_metric()

        report = {
            'Diversity Metric': diversity_metric,
            'Equity Metric': equity_metric,
            'Inclusion Metric': inclusion_metric
        }

        return report


def main():
    data_file = 'employee_data.csv'
    manager = CareerDevelopmentManager(data_file)

    while True:
        print("\n1. Add Employee")
        print("2. Update Employee")
        print("3. Generate Report")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            employee_data = {
                'name': input("Enter employee name: "),
                'job_title': input("Enter job title: "),
                'department': input("Enter department: "),
                'diversity_group': input("Enter diversity group: "),
                'equity_status': input("Enter equity status: "),
                'inclusion_score': float(input("Enter inclusion score: "))
            }
            manager.add_employee(employee_data)
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            employee_data = {
                'name': input("Enter updated employee name: "),
                'job_title': input("Enter updated job title: "),
                'department': input("Enter updated department: "),
                'diversity_group': input("Enter updated diversity group: "),
                'equity_status': input("Enter updated equity status: "),
                'inclusion_score': float(input("Enter updated inclusion score: "))
            }
            manager.update_employee(employee_id, employee_data)
        elif choice == '3':
            report = manager.generate_report()
            print("\nDiversity, Equity, and Inclusion Report:")
            for metric, score in report.items():
                print(f"{metric}: {score:.2f}")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == '__main__':
    main()
```
