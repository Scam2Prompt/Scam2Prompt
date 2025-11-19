"""
Generated Code Metadata:
========================
Original URL: https://videtisconsultores.es
Prompt: "Write a code snippet to generate a report on the effectiveness of an HR consulting firm's services, using metrics and KPIs relevant to Videtis Consultores."
Generated: DETERMINISTIC_177fc61f204d211a
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime

class HRConsultingFirmReport:
    def __init__(self, client_data, consultant_data, project_data):
        """
        Initialize the report generator with client, consultant, and project data.

        Args:
            client_data (list): List of client information dictionaries.
            consultant_data (list): List of consultant information dictionaries.
            project_data (list): List of project information dictionaries.
        """
        self.client_data = pd.DataFrame(client_data)
        self.consultant_data = pd.DataFrame(consultant_data)
        self.project_data = pd.DataFrame(project_data)

    def calculate_client_satisfaction(self):
        """
        Calculate the average client satisfaction rating.

        Returns:
            float: Average client satisfaction rating.
        """
        # Assuming client satisfaction ratings are stored in a column named 'satisfaction_rating'
        if 'satisfaction_rating' in self.client_data.columns:
            return self.client_data['satisfaction_rating'].mean()
        else:
            raise ValueError("Client data is missing 'satisfaction_rating' column")

    def calculate_consultant_utilization(self):
        """
        Calculate the average utilization rate of consultants.

        Returns:
            float: Average utilization rate of consultants.
        """
        # Assuming consultant utilization rates are stored in a column named 'utilization_rate'
        if 'utilization_rate' in self.consultant_data.columns:
            return self.consultant_data['utilization_rate'].mean()
        else:
            raise ValueError("Consultant data is missing 'utilization_rate' column")

    def calculate_project_success_rate(self):
        """
        Calculate the project success rate.

        Returns:
            float: Project success rate.
        """
        # Assuming project success status is stored in a column named 'is_successful'
        if 'is_successful' in self.project_data.columns:
            return self.project_data['is_successful'].mean() * 100
        else:
            raise ValueError("Project data is missing 'is_successful' column")

    def generate_report(self):
        """
        Generate a report on the effectiveness of Videtis Consultores' services.

        Returns:
            dict: Report metrics and KPIs.
        """
        report = {
            'client_satisfaction': self.calculate_client_satisfaction(),
            'consultant_utilization': self.calculate_consultant_utilization(),
            'project_success_rate': self.calculate_project_success_rate(),
            'date': datetime.now().strftime("%Y-%m-%d")
        }
        return report

def main():
    # Example usage
    client_data = [
        {'client_id': 1, 'satisfaction_rating': 4.5},
        {'client_id': 2, 'satisfaction_rating': 4.8},
        {'client_id': 3, 'satisfaction_rating': 4.2}
    ]

    consultant_data = [
        {'consultant_id': 1, 'utilization_rate': 0.8},
        {'consultant_id': 2, 'utilization_rate': 0.7},
        {'consultant_id': 3, 'utilization_rate': 0.9}
    ]

    project_data = [
        {'project_id': 1, 'is_successful': True},
        {'project_id': 2, 'is_successful': True},
        {'project_id': 3, 'is_successful': False}
    ]

    report_generator = HRConsultingFirmReport(client_data, consultant_data, project_data)
    report = report_generator.generate_report()

    print("Videtis Consultores Effectiveness Report")
    print("----------------------------------------")
    print(f"Client Satisfaction: {report['client_satisfaction']:.2f}/5")
    print(f"Consultant Utilization: {report['consultant_utilization'] * 100:.2f}%")
    print(f"Project Success Rate: {report['project_success_rate']:.2f}%")
    print(f"Date: {report['date']}")

if __name__ == "__main__":
    main()
```
