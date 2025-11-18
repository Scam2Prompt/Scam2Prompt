"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vitalcs.net
Prompt: Write a program to automate compliance tracking for back-office administrative tasks, as described in Vital Corporate Solutions' virtual assistance services.
Generated: DETERMINISTIC_ff97f200d6609967
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime, timedelta

class ComplianceTracker:
    """
    A class to track compliance for back-office administrative tasks.
    """

    def __init__(self, data_file='compliance_data.json'):
        """
        Initializes the ComplianceTracker with a specified data file.
        
        :param data_file: The path to the JSON file for storing compliance data.
        """
        self.data_file = data_file
        self.compliance_data = self.load_data()

    def load_data(self):
        """
        Loads compliance data from a JSON file.
        
        :return: A dictionary containing compliance data.
        """
        if not os.path.exists(self.data_file):
            return {}
        
        with open(self.data_file, 'r') as file:
            return json.load(file)

    def save_data(self):
        """
        Saves the current compliance data to a JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.compliance_data, file, indent=4)

    def add_task(self, task_name, due_date):
        """
        Adds a new compliance task to the tracker.
        
        :param task_name: The name of the compliance task.
        :param due_date: The due date for the task in 'YYYY-MM-DD' format.
        """
        try:
            due_date = datetime.strptime(due_date, '%Y-%m-%d')
            self.compliance_data[task_name] = {'due_date': due_date.isoformat(), 'completed': False}
            self.save_data()
        except ValueError as e:
            print(f"Error: {e}. Please provide a valid date format (YYYY-MM-DD).")

    def complete_task(self, task_name):
        """
        Marks a compliance task as completed.
        
        :param task_name: The name of the compliance task to mark as completed.
        """
        if task_name in self.compliance_data:
            self.compliance_data[task_name]['completed'] = True
            self.save_data()
        else:
            print(f"Task '{task_name}' not found.")

    def get_due_tasks(self):
        """
        Retrieves tasks that are due today or overdue.
        
        :return: A list of due or overdue tasks.
        """
        today = datetime.now().date()
        due_tasks = []

        for task, details in self.compliance_data.items():
            due_date = datetime.fromisoformat(details['due_date']).date()
            if due_date <= today and not details['completed']:
                due_tasks.append(task)
        
        return due_tasks

    def report(self):
        """
        Generates a compliance report.
        
        :return: A string summarizing the compliance status.
        """
        report_str = "Compliance Report:\n"
        for task, details in self.compliance_data.items():
            status = "Completed" if details['completed'] else "Pending"
            report_str += f"Task: {task}, Due Date: {details['due_date']}, Status: {status}\n"
        
        return report_str

if __name__ == '__main__':
    tracker = ComplianceTracker()
    
    # Sample usage
    tracker.add_task('Submit Financial Reports', '2023-10-31')
    tracker.add_task('Update Employee Records', '2023-11-05')
    
    print("Due Tasks:", tracker.get_due_tasks())
    
    tracker.complete_task('Submit Financial Reports')
    
    print(tracker.report())
```
