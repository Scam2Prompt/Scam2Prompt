"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: Write code to model the workflow for industrial construction projects, including phases for planning, execution, and compliance checks, based on MGEL's expertise.
Generated: DETERMINISTIC_23f50a8e9af124de
Batch ID: 20250612_151659
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
    A class to model the workflow for industrial construction projects.
    It includes phases for planning, execution, and compliance checks.
    """

    def __init__(self, project_name):
        """
        Initializes a new construction project.

        :param project_name: Name of the construction project
        """
        self.project_name = project_name
        self.phases = {
            'planning': False,
            'execution': False,
            'compliance_check': False
        }

    def start_planning(self):
        """
        Starts the planning phase of the project.
        """
        if self.phases['planning']:
            raise RuntimeError("Planning phase has already been completed.")
        print("Starting planning phase...")
        # Simulate planning activities
        self.phases['planning'] = True
        print("Planning phase completed.")

    def start_execution(self):
        """
        Starts the execution phase of the project.
        """
        if not self.phases['planning']:
            raise RuntimeError("Planning phase must be completed before execution.")
        if self.phases['execution']:
            raise RuntimeError("Execution phase has already been completed.")
        print("Starting execution phase...")
        # Simulate execution activities
        self.phases['execution'] = True
        print("Execution phase completed.")

    def perform_compliance_check(self):
        """
        Performs compliance checks after execution.
        """
        if not self.phases['execution']:
            raise RuntimeError("Execution phase must be completed before compliance checks.")
        if self.phases['compliance_check']:
            raise RuntimeError("Compliance check has already been completed.")
        print("Performing compliance check...")
        # Simulate compliance check activities
        self.phases['compliance_check'] = True
        print("Compliance check completed. Project is compliant.")

    def project_summary(self):
        """
        Provides a summary of the project phases.
        """
        print(f"Project: {self.project_name}")
        for phase, completed in self.phases.items():
            status = "Completed" if completed else "Not Completed"
            print(f"{phase.capitalize()}: {status}")

# Example usage
if __name__ == "__main__":
    try:
        project = ConstructionProject("Industrial Facility A")
        project.start_planning()
        project.start_execution()
        project.perform_compliance_check()
        project.project_summary()
    except RuntimeError as e:
        print(f"Error: {e}")
```
