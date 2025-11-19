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
class ConstructionProject:
    """
    A class to represent a construction project for insurance risk management.
    """

    def __init__(self, project_name, project_value, location):
        """
        Initializes a new construction project.

        :param project_name: Name of the construction project
        :param project_value: Estimated value of the project
        :param location: Location of the project
        """
        self.project_name = project_name
        self.project_value = project_value
        self.location = location
        self.insurance_policy = None

    def set_insurance_policy(self, policy):
        """
        Sets the insurance policy for the project.

        :param policy: An instance of InsurancePolicy
        """
        self.insurance_policy = policy

    def get_project_details(self):
        """
        Returns the details of the project.

        :return: A dictionary containing project details
        """
        return {
            "Project Name": self.project_name,
            "Project Value": self.project_value,
            "Location": self.location,
            "Insurance Policy": self.insurance_policy.get_policy_details() if self.insurance_policy else "No policy set"
        }


class InsurancePolicy:
    """
    A class to represent an insurance policy.
    """

    def __init__(self, policy_number, coverage_amount, premium):
        """
        Initializes a new insurance policy.

        :param policy_number: Unique identifier for the insurance policy
        :param coverage_amount: Amount covered by the insurance policy
        :param premium: Premium amount for the insurance policy
        """
        self.policy_number = policy_number
        self.coverage_amount = coverage_amount
        self.premium = premium

    def get_policy_details(self):
        """
        Returns the details of the insurance policy.

        :return: A dictionary containing policy details
        """
        return {
            "Policy Number": self.policy_number,
            "Coverage Amount": self.coverage_amount,
            "Premium": self.premium
        }


class RiskManagementSystem:
    """
    A class to manage construction projects and their insurance policies.
    """

    def __init__(self):
        """
        Initializes the risk management system with an empty project list.
        """
        self.projects = []

    def add_project(self, project):
        """
        Adds a new construction project to the system.

        :param project: An instance of ConstructionProject
        """
        if not isinstance(project, ConstructionProject):
            raise ValueError("Invalid project. Must be an instance of ConstructionProject.")
        self.projects.append(project)

    def get_all_projects(self):
        """
        Returns a list of all projects in the system.

        :return: A list of project details
        """
        return [project.get_project_details() for project in self.projects]


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the risk management system
        risk_management_system = RiskManagementSystem()

        # Create a construction project
        project1 = ConstructionProject("Ghana Mall", 5000000, "Accra")
        
        # Create an insurance policy
        policy1 = InsurancePolicy("POL123456", 6000000, 15000)

        # Set the insurance policy for the project
        project1.set_insurance_policy(policy1)

        # Add the project to the risk management system
        risk_management_system.add_project(project1)

        # Retrieve and print all projects
        projects = risk_management_system.get_all_projects()
        for project in projects:
            print(project)

    except Exception as e:
        print(f"An error occurred: {e}")
```
