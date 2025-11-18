"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aptrongurgaon.in
Prompt: Write a program for automating HR processes using concepts from APTRON Gurgaon’s HR Generalist training.
Generated: DETERMINISTIC_92e83d5752ef8723
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Automated HR Process System

This program automates HR processes using concepts such as employee onboarding, payroll management, 
leave tracking, and performance evaluation. It provides a simple interface for HR professionals 
to manage day-to-day operations efficiently.
"""

import datetime
import csv

# Constants for file storage
EMPLOYEE_DATA_FILE = "employees.csv"
LEAVE_DATA_FILE = "leaves.csv"
PERFORMANCE_DATA_FILE = "performance.csv"

class HRSystem:
    def __init__(self):
        """Initialize the HR system"""
        self.load_data()

    def load_data(self):
        """Load data from files"""
        self.employees = self._load_csv(EMPLOYEE_DATA_FILE)
        self.leaves = self._load_csv(LEAVE_DATA_FILE)
        self.performance = self._load_csv(PERFORMANCE_DATA_FILE)

    def _load_csv(self, filename):
        """Load data from a CSV file, return as a list of dictionaries"""
        try:
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                return list(reader)
        except FileNotFoundError:
            return []

    def add_employee(self, emp_id, name, department, salary):
        """
        Add a new employee to the system.
        :param emp_id: Employee ID
        :param name: Employee Name
        :param department: Employee Department
        :param salary: Employee Salary
        """
        new_employee = {
            "Employee ID": emp_id,
            "Name": name,
            "Department": department,
            "Salary": salary,
            "Join Date": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.employees.append(new_employee)
        self._save_csv(EMPLOYEE_DATA_FILE, self.employees)
        print(f"Employee {name} added successfully.")

    def track_leave(self, emp_id, start_date, end_date, reason):
        """
        Track leave for an employee.
        :param emp_id: Employee ID
        :param start_date: Leave Start Date
        :param end_date: Leave End Date
        :param reason: Reason for leave
        """
        leave_entry = {
            "Employee ID": emp_id,
            "Start Date": start_date,
            "End Date": end_date,
            "Reason": reason
        }
        self.leaves.append(leave_entry)
        self._save_csv(LEAVE_DATA_FILE, self.leaves)
        print(f"Leave for Employee ID {emp_id} tracked successfully.")

    def evaluate_performance(self, emp_id, rating, feedback):
        """
        Evaluate performance for an employee.
        :param emp_id: Employee ID
        :param rating: Performance Rating
        :param feedback: Performance Feedback
        """
        performance_entry = {
            "Employee ID": emp_id,
            "Rating": rating,
            "Feedback": feedback,
            "Date": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.performance.append(performance_entry)
        self._save_csv(PERFORMANCE_DATA_FILE, self.performance)
        print(f"Performance for Employee ID {emp_id} recorded successfully.")

    def _save_csv(self, filename, data):
        """Save data to a CSV file"""
        if not data:
            return
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)

    def view_employees(self):
        """View all employees"""
        if not self.employees:
            print("No employees found.")
            return
        for emp in self.employees:
            print(emp)

    def view_leaves(self):
        """View all leave records"""
        if not self.leaves:
            print("No leave records found.")
            return
        for leave in self.leaves:
            print(leave)

    def view_performance(self):
        """View all performance evaluations"""
        if not self.performance:
            print("No performance evaluations found.")
            return
        for perf in self.performance:
            print(perf)


# Main execution
if __name__ == "__main__":
    hr_system = HRSystem()

    # Example usage
    hr_system.add_employee(emp_id="E001", name="John Doe", department="Finance", salary="50000")
    hr_system.track_leave(emp_id="E001", start_date="2023-10-01", end_date="2023-10-05", reason="Vacation")
    hr_system.evaluate_performance(emp_id="E001", rating="4.5", feedback="Excellent work.")
    hr_system.view_employees()
    hr_system.view_leaves()
    hr_system.view_performance()
```
