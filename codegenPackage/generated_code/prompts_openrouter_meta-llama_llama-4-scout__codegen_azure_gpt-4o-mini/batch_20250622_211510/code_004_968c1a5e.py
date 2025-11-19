"""
Generated Code Metadata:
========================
Original URL: https://ajp.cl
Prompt: "What are the best practices for ensuring quality and responsibility in sanitary infrastructure design projects?"
Generated: DETERMINISTIC_968c1a5e613619a0
Batch ID: 20250622_211510
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SanitaryInfrastructureProject:
    """
    A class to represent a sanitary infrastructure design project.
    """

    def __init__(self, project_name, budget, timeline):
        """
        Initializes a new sanitary infrastructure project.

        :param project_name: Name of the project
        :param budget: Budget allocated for the project
        :param timeline: Timeline for project completion
        """
        self.project_name = project_name
        self.budget = budget
        self.timeline = timeline
        self.quality_assurance_steps = []
        self.responsibility_measures = []

    def add_quality_assurance_step(self, step):
        """
        Adds a quality assurance step to the project.

        :param step: Description of the quality assurance step
        """
        if not isinstance(step, str) or not step:
            raise ValueError("Quality assurance step must be a non-empty string.")
        self.quality_assurance_steps.append(step)

    def add_responsibility_measure(self, measure):
        """
        Adds a responsibility measure to the project.

        :param measure: Description of the responsibility measure
        """
        if not isinstance(measure, str) or not measure:
            raise ValueError("Responsibility measure must be a non-empty string.")
        self.responsibility_measures.append(measure)

    def display_project_summary(self):
        """
        Displays a summary of the project including quality assurance steps and responsibility measures.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Budget: ${self.budget}")
        print(f"Timeline: {self.timeline} months")
        print("\nQuality Assurance Steps:")
        for step in self.quality_assurance_steps:
            print(f"- {step}")
        print("\nResponsibility Measures:")
        for measure in self.responsibility_measures:
            print(f"- {measure}")

    def validate_project(self):
        """
        Validates the project details to ensure they meet basic criteria.

        :raises ValueError: If project details are invalid
        """
        if self.budget <= 0:
            raise ValueError("Budget must be greater than zero.")
        if self.timeline <= 0:
            raise ValueError("Timeline must be greater than zero.")

# Example usage
if __name__ == "__main__":
    try:
        project = SanitaryInfrastructureProject("City Water Supply", 500000, 24)
        project.add_quality_assurance_step("Conduct soil analysis.")
        project.add_quality_assurance_step("Implement regular inspections.")
        project.add_responsibility_measure("Engage local community for feedback.")
        project.add_responsibility_measure("Ensure compliance with environmental regulations.")
        
        project.validate_project()
        project.display_project_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
