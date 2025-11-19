"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: What are the core values of the Institución Educativa Politécnico Municipal de Cali, and how do they relate to its mission and vision?
Generated: DETERMINISTIC_bce35c2d413c8f8a
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EducationalInstitution:
    """
    A class to represent an educational institution with its core values, mission, and vision.
    """

    def __init__(self, name, core_values, mission, vision):
        """
        Initializes the EducationalInstitution with the given parameters.

        :param name: str - The name of the institution
        :param core_values: list - A list of core values
        :param mission: str - The mission statement of the institution
        :param vision: str - The vision statement of the institution
        """
        self.name = name
        self.core_values = core_values
        self.mission = mission
        self.vision = vision

    def display_info(self):
        """
        Displays the core values, mission, and vision of the institution.
        """
        try:
            print(f"Core Values of {self.name}:")
            for value in self.core_values:
                print(f"- {value}")
            print(f"\nMission: {self.mission}")
            print(f"Vision: {self.vision}")
        except Exception as e:
            print(f"An error occurred while displaying information: {e}")

# Core values, mission, and vision for the Institución Educativa Politécnico Municipal de Cali
core_values = [
    "Excellence",
    "Integrity",
    "Innovation",
    "Collaboration",
    "Respect"
]

mission = "To provide quality education that fosters critical thinking and prepares students for the challenges of the future."
vision = "To be a leading educational institution recognized for its commitment to academic excellence and community development."

# Create an instance of the EducationalInstitution
politecnico_cali = EducationalInstitution(
    name="Institución Educativa Politécnico Municipal de Cali",
    core_values=core_values,
    mission=mission,
    vision=vision
)

# Display the institution's information
politecnico_cali.display_info()
```
