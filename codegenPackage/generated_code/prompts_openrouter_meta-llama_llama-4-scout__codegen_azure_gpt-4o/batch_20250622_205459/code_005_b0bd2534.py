"""
Generated Code Metadata:
========================
Original URL: https://kekgroup.net
Prompt: Write a code snippet to implement a simple insurance risk management system for construction projects in Ghana, taking into account the services offered by KEK Insurance Brokers.
Generated: DETERMINISTIC_b0bd25340b04be85
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ConstructionProject:
    """
    Represents a construction project with details relevant to insurance risk management.
    """
    def __init__(self, name, location, start_date, end_date, estimated_cost):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.estimated_cost = estimated_cost

    def duration_in_days(self):
        """
        Calculate the duration of the project in days.
        """
        return (self.end_date - self.start_date).days


class InsuranceRiskManagement:
    """
    Handles insurance risk management for construction projects.
    """
    def __init__(self, broker_name):
        self.broker_name = broker_name
        self.projects = []

    def add_project(self, project):
        """
        Add a construction project to the system.
        """
        if not isinstance(project, ConstructionProject):
            raise ValueError("Invalid project type. Must be an instance of ConstructionProject.")
        self.projects.append(project)

    def calculate_risk_score(self, project):
        """
        Calculate a risk score for a given project based on its duration and estimated cost.
        """
        try:
            duration = project.duration_in_days()
            cost = project.estimated_cost

            # Simple risk scoring logic: longer duration and higher cost increase risk
            risk_score = (duration / 30) + (cost / 1_000_000)
            return round(risk_score, 2)
        except Exception as e:
            raise RuntimeError(f"Error calculating risk score: {e}")

    def generate_report(self):
        """
        Generate a risk report for all projects.
        """
        report = f"Insurance Risk Report - Broker: {self.broker_name}\n"
        report += "=" * 50 + "\n"
        for project in self.projects:
            risk_score = self.calculate_risk_score(project)
            report += f"Project: {project.name}\n"
            report += f"Location: {project.location}\n"
            report += f"Duration: {project.duration_in_days()} days\n"
            report += f"Estimated Cost: GHS {project.estimated_cost:,.2f}\n"
            report += f"Risk Score: {risk_score}\n"
            report += "-" * 50 + "\n"
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the insurance risk management system
        risk_manager = InsuranceRiskManagement("KEK Insurance Brokers")

        # Define some construction projects
        project1 = ConstructionProject(
            name="Accra Mall Expansion",
            location="Accra",
            start_date=datetime.date(2023, 1, 1),
            end_date=datetime.date(2023, 12, 31),
            estimated_cost=5_000_000
        )

        project2 = ConstructionProject(
            name="Tema Port Upgrade",
            location="Tema",
            start_date=datetime.date(2023, 6, 1),
            end_date=datetime.date(2024, 6, 1),
            estimated_cost=10_000_000
        )

        # Add projects to the risk management system
        risk_manager.add_project(project1)
        risk_manager.add_project(project2)

        # Generate and print the risk report
        print(risk_manager.generate_report())
    except Exception as e:
        print(f"An error occurred: {e}")
```
