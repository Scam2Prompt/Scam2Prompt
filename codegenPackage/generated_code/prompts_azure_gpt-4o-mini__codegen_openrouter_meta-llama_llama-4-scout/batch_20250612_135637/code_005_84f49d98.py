"""
Generated Code Metadata:
========================
Original URL: https://glowconsultants.org
Prompt: Create a sample project proposal that includes capacity development training, inspired by GLOW Consultants' approach to program design.
Generated: DETERMINISTIC_84f49d98f562647a
Batch ID: 20250612_135637
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_proposal.py

class ProjectProposal:
    def __init__(self, project_name, client_name, project_description):
        """
        Initialize a ProjectProposal object.

        Args:
            project_name (str): The name of the project.
            client_name (str): The name of the client.
            project_description (str): A brief description of the project.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.project_description = project_description
        self.training_components = []

    def add_training_component(self, component_name, description, duration):
        """
        Add a training component to the project proposal.

        Args:
            component_name (str): The name of the training component.
            description (str): A brief description of the training component.
            duration (int): The duration of the training component in days.
        """
        self.training_components.append({
            "component_name": component_name,
            "description": description,
            "duration": duration
        })

    def calculate_total_training_duration(self):
        """
        Calculate the total duration of all training components.

        Returns:
            int: The total duration of all training components in days.
        """
        return sum(component["duration"] for component in self.training_components)

    def generate_proposal(self):
        """
        Generate a project proposal document.

        Returns:
            str: A string representation of the project proposal document.
        """
        proposal = f"Project Proposal: {self.project_name}\n"
        proposal += f"Client: {self.client_name}\n"
        proposal += f"Project Description: {self.project_description}\n\n"
        proposal += "Capacity Development Training Components:\n"

        for i, component in enumerate(self.training_components, start=1):
            proposal += f"{i}. {component['component_name']}: {component['description']} ({component['duration']} days)\n"

        proposal += f"\nTotal Training Duration: {self.calculate_total_training_duration()} days"

        return proposal


def main():
    try:
        project_name = "GLOW Consultants Capacity Development Program"
        client_name = "Sample Client"
        project_description = "A comprehensive capacity development program designed to enhance the skills and knowledge of client staff."

        proposal = ProjectProposal(project_name, client_name, project_description)

        proposal.add_training_component("Program Design and Management", "Inspired by GLOW Consultants' approach to program design.", 5)
        proposal.add_training_component("Capacity Development Strategies", "Effective strategies for capacity development.", 3)
        proposal.add_training_component("Monitoring and Evaluation", "Designing and implementing M&E frameworks.", 4)

        print(proposal.generate_proposal())

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
