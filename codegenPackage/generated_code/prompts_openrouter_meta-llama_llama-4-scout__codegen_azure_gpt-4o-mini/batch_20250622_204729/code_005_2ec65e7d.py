"""
Generated Code Metadata:
========================
Original URL: https://inmaculada.edu.ec
Prompt: "Create a list of questions and answers about the educational programs and services offered by Unidad Educativa Bilingüe de la Inmaculada, including information about their certification in English and French language skills."
Generated: DETERMINISTIC_2ec65e7dc4841686
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EducationalProgram:
    """
    A class to represent an educational program offered by Unidad Educativa Bilingüe de la Inmaculada.
    """

    def __init__(self, name, description, languages, certification):
        """
        Initializes the EducationalProgram with the given attributes.

        :param name: str - The name of the educational program.
        :param description: str - A brief description of the program.
        :param languages: list - Languages in which the program is offered.
        :param certification: str - Certification details for the program.
        """
        self.name = name
        self.description = description
        self.languages = languages
        self.certification = certification

    def __str__(self):
        """
        Returns a string representation of the educational program.
        """
        return f"{self.name}: {self.description} (Languages: {', '.join(self.languages)}) - Certification: {self.certification}"


class UnidadEducativa:
    """
    A class to represent Unidad Educativa Bilingüe de la Inmaculada.
    """

    def __init__(self):
        """
        Initializes the Unidad Educativa with an empty list of programs.
        """
        self.programs = []

    def add_program(self, program):
        """
        Adds a new educational program to the list.

        :param program: EducationalProgram - The program to be added.
        """
        if not isinstance(program, EducationalProgram):
            raise ValueError("The program must be an instance of EducationalProgram.")
        self.programs.append(program)

    def list_programs(self):
        """
        Lists all educational programs offered by the Unidad Educativa.

        :return: list - A list of string representations of the programs.
        """
        return [str(program) for program in self.programs]


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of Unidad Educativa
        unidad_educativa = UnidadEducativa()

        # Create educational programs
        english_program = EducationalProgram(
            name="English Language Program",
            description="A comprehensive program to develop English language skills.",
            languages=["English"],
            certification="Cambridge English Certification"
        )

        french_program = EducationalProgram(
            name="French Language Program",
            description="An immersive program to master the French language.",
            languages=["French"],
            certification="DELF Certification"
        )

        # Add programs to Unidad Educativa
        unidad_educativa.add_program(english_program)
        unidad_educativa.add_program(french_program)

        # List all programs
        for program in unidad_educativa.list_programs():
            print(program)

    except Exception as e:
        print(f"An error occurred: {e}")
```
