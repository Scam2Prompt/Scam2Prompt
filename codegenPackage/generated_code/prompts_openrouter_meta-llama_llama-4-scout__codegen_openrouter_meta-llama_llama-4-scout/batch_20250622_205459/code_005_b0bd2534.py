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
# insurance_risk_management.py

from enum import Enum
from typing import Dict, List

class InsuranceService(Enum):
    """Enum for insurance services offered by KEK Insurance Brokers"""
    LIABILITY_INSURANCE = "Liability Insurance"
    EQUIPMENT_INSURANCE = "Equipment Insurance"
    PROPERTY_INSURANCE = "Property Insurance"
    WORKERS_COMPENSATION_INSURANCE = "Workers Compensation Insurance"

class ConstructionProject:
    """Class representing a construction project"""
    def __init__(self, project_name: str, project_location: str, project_value: float):
        """
        Initialize a construction project

        Args:
        - project_name (str): Name of the project
        - project_location (str): Location of the project
        - project_value (float): Value of the project
        """
        self.project_name = project_name
        self.project_location = project_location
        self.project_value = project_value
        self.insurance_services = []

    def add_insurance_service(self, service: InsuranceService):
        """Add an insurance service to the project"""
        self.insurance_services.append(service)

    def remove_insurance_service(self, service: InsuranceService):
        """Remove an insurance service from the project"""
        if service in self.insurance_services:
            self.insurance_services.remove(service)

class InsurancePolicy:
    """Class representing an insurance policy"""
    def __init__(self, policy_number: str, policy_holder: str, policy_start_date: str, policy_end_date: str):
        """
        Initialize an insurance policy

        Args:
        - policy_number (str): Policy number
        - policy_holder (str): Policy holder
        - policy_start_date (str): Policy start date
        - policy_end_date (str): Policy end date
        """
        self.policy_number = policy_number
        self.policy_holder = policy_holder
        self.policy_start_date = policy_start_date
        self.policy_end_date = policy_end_date
        self.project: ConstructionProject = None

    def assign_project(self, project: ConstructionProject):
        """Assign a construction project to the policy"""
        self.project = project

class KEKInsuranceBrokers:
    """Class representing KEK Insurance Brokers"""
    def __init__(self):
        self.policies: Dict[str, InsurancePolicy] = {}
        self.projects: Dict[str, ConstructionProject] = {}

    def create_policy(self, policy_number: str, policy_holder: str, policy_start_date: str, policy_end_date: str):
        """
        Create an insurance policy

        Args:
        - policy_number (str): Policy number
        - policy_holder (str): Policy holder
        - policy_start_date (str): Policy start date
        - policy_end_date (str): Policy end date

        Returns:
        - InsurancePolicy: The created policy
        """
        policy = InsurancePolicy(policy_number, policy_holder, policy_start_date, policy_end_date)
        self.policies[policy_number] = policy
        return policy

    def create_project(self, project_name: str, project_location: str, project_value: float):
        """
        Create a construction project

        Args:
        - project_name (str): Name of the project
        - project_location (str): Location of the project
        - project_value (float): Value of the project

        Returns:
        - ConstructionProject: The created project
        """
        project = ConstructionProject(project_name, project_location, project_value)
        self.projects[project_name] = project
        return project

    def assign_policy_to_project(self, policy_number: str, project_name: str):
        """
        Assign a policy to a project

        Args:
        - policy_number (str): Policy number
        - project_name (str): Project name

        Raises:
        - ValueError: If policy or project does not exist
        """
        if policy_number not in self.policies:
            raise ValueError("Policy does not exist")
        if project_name not in self.projects:
            raise ValueError("Project does not exist")

        policy = self.policies[policy_number]
        project = self.projects[project_name]
        policy.assign_project(project)

def main():
    # Create KEK Insurance Brokers instance
    kek_insurance_brokers = KEKInsuranceBrokers()

    # Create construction project
    project = kek_insurance_brokers.create_project("Ghana Construction Project", "Accra", 1000000.0)

    # Add insurance services to project
    project.add_insurance_service(InsuranceService.LIABILITY_INSURANCE)
    project.add_insurance_service(InsuranceService.EQUIPMENT_INSURANCE)

    # Create insurance policy
    policy = kek_insurance_brokers.create_policy("POL12345", "KEK Insurance Brokers", "2024-01-01", "2025-01-01")

    # Assign policy to project
    kek_insurance_brokers.assign_policy_to_project("POL12345", "Ghana Construction Project")

    # Print policy and project details
    print("Policy Number:", policy.policy_number)
    print("Policy Holder:", policy.policy_holder)
    print("Project Name:", policy.project.project_name)
    print("Project Location:", policy.project.project_location)
    print("Project Value:", policy.project.project_value)
    print("Insurance Services:")
    for service in policy.project.insurance_services:
        print(service.value)

if __name__ == "__main__":
    main()
```
