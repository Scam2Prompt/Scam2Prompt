"""
Generated Code Metadata:
========================
Original URL: https://vertical1.org
Prompt: Compare and contrast general contracting and project management services in the construction industry, as provided by Vertical Horizons Construction Group.
Generated: DETERMINISTIC_9240e641e6e73846
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_services.py

class ConstructionService:
    """Base class for construction services."""

    def __init__(self, name, description):
        """
        Initialize a construction service.

        Args:
            name (str): Name of the service.
            description (str): Description of the service.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class GeneralContractingService(ConstructionService):
    """General contracting service."""

    def __init__(self, name, description, scope_of_work):
        """
        Initialize a general contracting service.

        Args:
            name (str): Name of the service.
            description (str): Description of the service.
            scope_of_work (str): Scope of work for the service.
        """
        super().__init__(name, description)
        self.scope_of_work = scope_of_work

    def __str__(self):
        return super().__str__() + f"\nScope of Work: {self.scope_of_work}"


class ProjectManagementService(ConstructionService):
    """Project management service."""

    def __init__(self, name, description, project_phases):
        """
        Initialize a project management service.

        Args:
            name (str): Name of the service.
            description (str): Description of the service.
            project_phases (list): List of project phases.
        """
        super().__init__(name, description)
        self.project_phases = project_phases

    def __str__(self):
        phases_str = "\n".join([f"- {phase}" for phase in self.project_phases])
        return super().__str__() + f"\nProject Phases:\n{phases_str}"


class VerticalHorizonsConstructionGroup:
    """Vertical Horizons Construction Group."""

    def __init__(self):
        self.services = []

    def add_service(self, service):
        """
        Add a construction service.

        Args:
            service (ConstructionService): Service to add.
        """
        self.services.append(service)

    def compare_services(self):
        """
        Compare and contrast construction services.

        Returns:
            str: Comparison of services.
        """
        comparison = ""
        for i, service in enumerate(self.services):
            comparison += f"Service {i+1}: {service}\n\n"
        return comparison


def main():
    try:
        # Create services
        general_contracting = GeneralContractingService(
            "General Contracting",
            "General contracting services for construction projects.",
            "Design, build, and manage construction projects."
        )
        project_management = ProjectManagementService(
            "Project Management",
            "Project management services for construction projects.",
            ["Initiation", "Planning", "Execution", "Monitoring and Control", "Closure"]
        )

        # Create Vertical Horizons Construction Group
        vhcg = VerticalHorizonsConstructionGroup()
        vhcg.add_service(general_contracting)
        vhcg.add_service(project_management)

        # Compare services
        comparison = vhcg.compare_services()
        print(comparison)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
