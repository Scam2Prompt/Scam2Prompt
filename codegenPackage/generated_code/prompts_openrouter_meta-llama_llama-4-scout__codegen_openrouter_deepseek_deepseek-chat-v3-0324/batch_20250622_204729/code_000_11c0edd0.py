"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Generate a description of a bilingual educational institution in Quito, Ecuador that offers programs from initial education to high school, incorporating Christian values."
Generated: DETERMINISTIC_11c0edd0d90a73a0
Batch ID: 20250622_204729
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
    A class representing a bilingual educational institution in Quito, Ecuador.
    Offers programs from initial education to high school with Christian values.
    """

    def __init__(self, name: str, location: str = "Quito, Ecuador"):
        """
        Initialize the educational institution.

        Args:
            name (str): Name of the institution
            location (str, optional): Location of the institution. Defaults to "Quito, Ecuador".
        """
        self.name = name
        self.location = location
        self.programs = {
            'initial_education': True,
            'primary': True,
            'secondary': True,
            'high_school': True
        }
        self.values = ['Christian', 'Bilingual', 'Academic Excellence']
        self.languages = ['Spanish', 'English']

    def get_description(self) -> str:
        """
        Generate a comprehensive description of the institution.

        Returns:
            str: Formatted description of the institution
        """
        program_levels = ", ".join([k.replace('_', ' ').title() for k, v in self.programs.items() if v])
        core_values = ", ".join(self.values)
        languages = " and ".join(self.languages)

        description = (
            f"{self.name} is a bilingual educational institution located in {self.location}. "
            f"We offer comprehensive programs from {program_levels}, providing a complete "
            f"educational journey for our students. Our institution is founded on {core_values} "
            f"values, integrating faith-based principles throughout our curriculum. "
            f"With instruction in both {languages}, we prepare students for global opportunities "
            f"while maintaining strong roots in our local community and Christian traditions."
        )

        return description


# Example usage
if __name__ == "__main__":
    school = EducationalInstitution(name="Colegio Cristiano Bilingüe")
    print(school.get_description())
```
