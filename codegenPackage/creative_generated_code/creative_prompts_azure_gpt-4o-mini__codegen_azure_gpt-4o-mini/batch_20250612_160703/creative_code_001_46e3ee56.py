"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starke-orte.land
Prompt: What are some best practices for municipal representatives to transform unused buildings into vibrant community spaces, according to the Starke Orte Netzwerk?
Generated: DETERMINISTIC_46e3ee56ac5b4b45
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CommunitySpaceTransformer:
    """
    A class to represent the transformation of unused buildings into community spaces.
    It uses best practices according to the Starke Orte Netzwerk.
    """

    def __init__(self, building_name, location):
        """
        Initializes the CommunitySpaceTransformer with a building name and location.

        :param building_name: str - The name of the unused building
        :param location: str - The location of the building
        """
        self.building_name = building_name
        self.location = location
        self.transformation_steps = []

    def add_transformation_step(self, step):
        """
        Adds a transformation step to the project.

        :param step: str - A description of the step to be added
        """
        if not isinstance(step, str) or not step:
            raise ValueError("Step must be a non-empty string.")
        self.transformation_steps.append(step)

    def transform(self):
        """
        Executes the transformation process and returns the planned steps.

        :return: list - A list of transformation steps
        """
        if not self.transformation_steps:
            raise RuntimeError("No transformation steps specified.")
        
        # Execute the transformation
        print(f"Transforming '{self.building_name}' located at {self.location}...")
        for step in self.transformation_steps:
            print(f"- {step}")
        
        return self.transformation_steps

    def report(self):
        """
        Generates a report of the transformation plan.

        :return: dict - A report with building details and transformation steps
        """
        return {
            "building_name": self.building_name,
            "location": self.location,
            "transformation_steps": self.transformation_steps
        }


# Example Usage
if __name__ == "__main__":
    try:
        # Create instance of CommunitySpaceTransformer
        transformer = CommunitySpaceTransformer("Old Library", "123 Main St")

        # Add transformation steps
        transformer.add_transformation_step("Conduct community needs assessment")
        transformer.add_transformation_step("Involve local artists and businesses")
        transformer.add_transformation_step("Create multifunctional spaces")
        transformer.add_transformation_step("Establish a maintenance plan")

        # Perform the transformation
        transformer.transform()

        # Generate report
        report = transformer.report()
        print("Transformation Report:", report)

    except Exception as e:
        print(f"An error occurred: {e}")
```
