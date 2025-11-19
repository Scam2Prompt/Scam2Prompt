"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Develop a comprehensive plan for a deck and fence staining project in Mornington Peninsula, including surface preparation, stain selection, and application techniques, as offered by Painters Mornington Peninsula.
Generated: DETERMINISTIC_5a1bbb0ad37d2a80
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DeckAndFenceStainingProject:
    """
    A class to represent a deck and fence staining project.
    """

    def __init__(self, location):
        """
        Initializes the project with a specified location.

        :param location: str - The location of the project (e.g., Mornington Peninsula).
        """
        self.location = location
        self.surface_preparation_steps = []
        self.stain_selection = None
        self.application_techniques = []

    def add_surface_preparation_step(self, step):
        """
        Adds a surface preparation step to the project.

        :param step: str - Description of the surface preparation step.
        """
        self.surface_preparation_steps.append(step)

    def select_stain(self, stain_type):
        """
        Selects the type of stain for the project.

        :param stain_type: str - The type of stain to be used (e.g., oil-based, water-based).
        """
        valid_stains = ['oil-based', 'water-based', 'semi-transparent', 'solid']
        if stain_type not in valid_stains:
            raise ValueError(f"Invalid stain type. Choose from: {valid_stains}")
        self.stain_selection = stain_type

    def add_application_technique(self, technique):
        """
        Adds an application technique to the project.

        :param technique: str - Description of the application technique.
        """
        self.application_techniques.append(technique)

    def generate_project_plan(self):
        """
        Generates a comprehensive project plan.

        :return: dict - A dictionary containing the project plan details.
        """
        if not self.surface_preparation_steps:
            raise ValueError("No surface preparation steps added.")
        if not self.stain_selection:
            raise ValueError("No stain selected.")
        if not self.application_techniques:
            raise ValueError("No application techniques added.")

        project_plan = {
            'Location': self.location,
            'Surface Preparation Steps': self.surface_preparation_steps,
            'Stain Selection': self.stain_selection,
            'Application Techniques': self.application_techniques
        }
        return project_plan


# Example usage
if __name__ == "__main__":
    try:
        project = DeckAndFenceStainingProject("Mornington Peninsula")
        
        # Adding surface preparation steps
        project.add_surface_preparation_step("Clean the surface with a pressure washer.")
        project.add_surface_preparation_step("Sand the surface to remove old stain and smooth rough areas.")
        project.add_surface_preparation_step("Allow the surface to dry completely.")

        # Selecting stain
        project.select_stain("oil-based")

        # Adding application techniques
        project.add_application_technique("Apply stain using a brush for better control.")
        project.add_application_technique("Use a roller for larger areas to speed up the process.")
        project.add_application_technique("Back-brush to ensure even coverage.")

        # Generating the project plan
        plan = project.generate_project_plan()
        print(plan)

    except ValueError as e:
        print(f"Error: {e}")
```
