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
    def __init__(self, name, location, description):
        """
        Initialize an EducationalInstitution object.

        Args:
            name (str): The name of the institution.
            location (str): The location of the institution.
            description (str): A brief description of the institution.
        """
        self.name = name
        self.location = location
        self.description = description
        self.programs = []

    def add_program(self, program):
        """
        Add an educational program to the institution.

        Args:
            program (str): The name of the program.
        """
        self.programs.append(program)

    def __str__(self):
        """
        Return a string representation of the institution.

        Returns:
            str: A string containing the institution's name, location, description, and programs.
        """
        institution_info = f"{self.name} - {self.location}\n{self.description}\n"
        programs_info = "Programs:\n" + "\n".join(f"- {program}" for program in self.programs)
        return institution_info + programs_info


class BilingualInstitution(EducationalInstitution):
    def __init__(self, name, location, description, languages):
        """
        Initialize a BilingualInstitution object.

        Args:
            name (str): The name of the institution.
            location (str): The location of the institution.
            description (str): A brief description of the institution.
            languages (list): A list of languages spoken at the institution.
        """
        super().__init__(name, location, description)
        self.languages = languages

    def __str__(self):
        """
        Return a string representation of the bilingual institution.

        Returns:
            str: A string containing the institution's name, location, description, languages, and programs.
        """
        institution_info = f"{self.name} - {self.location}\n{self.description}\nLanguages: {', '.join(self.languages)}\n"
        programs_info = "Programs:\n" + "\n".join(f"- {program}" for program in self.programs)
        return institution_info + programs_info


def main():
    try:
        # Create a bilingual institution
        institution = BilingualInstitution(
            name="Unidad Educativa Cristiana",
            location="Quito, Ecuador",
            description="A bilingual educational institution offering programs from initial education to high school, incorporating Christian values.",
            languages=["Spanish", "English"]
        )

        # Add programs
        institution.add_program("Initial Education")
        institution.add_program("Elementary Education")
        institution.add_program("Middle School")
        institution.add_program("High School")

        # Print institution information
        print(institution)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
