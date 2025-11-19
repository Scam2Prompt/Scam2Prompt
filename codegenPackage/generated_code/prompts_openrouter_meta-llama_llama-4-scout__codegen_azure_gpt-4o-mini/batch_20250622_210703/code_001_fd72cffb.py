"""
Generated Code Metadata:
========================
Original URL: https://enafo.cl
Prompt: "Describe the academic programs offered by ENAFO, including monitorías and módulos, and their focus on folklore and traditional culture."
Generated: DETERMINISTIC_fd72cffbbd4dab03
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class AcademicProgram:
    """
    A class to represent an academic program offered by ENAFO.
    """

    def __init__(self, name, description, focus_areas):
        """
        Initializes an instance of AcademicProgram.

        :param name: str - The name of the academic program.
        :param description: str - A brief description of the program.
        :param focus_areas: list - A list of focus areas within the program.
        """
        self.name = name
        self.description = description
        self.focus_areas = focus_areas

    def __str__(self):
        """
        Returns a string representation of the academic program.
        """
        return f"{self.name}: {self.description} (Focus Areas: {', '.join(self.focus_areas)})"


class ENAFO:
    """
    A class to represent the ENAFO institution and its academic programs.
    """

    def __init__(self):
        """
        Initializes an instance of ENAFO with an empty list of programs.
        """
        self.programs = []

    def add_program(self, program):
        """
        Adds a new academic program to the ENAFO institution.

        :param program: AcademicProgram - The program to be added.
        :raises ValueError: If the program is not an instance of AcademicProgram.
        """
        if not isinstance(program, AcademicProgram):
            raise ValueError("The program must be an instance of AcademicProgram.")
        self.programs.append(program)

    def list_programs(self):
        """
        Lists all academic programs offered by ENAFO.

        :return: list - A list of string representations of the programs.
        """
        return [str(program) for program in self.programs]


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of ENAFO
        enafo = ENAFO()

        # Define academic programs
        folklore_program = AcademicProgram(
            name="Folklore Studies",
            description="A program focused on the study of folklore and traditional culture.",
            focus_areas=["Oral Traditions", "Festivals", "Traditional Music"]
        )

        monitorias_program = AcademicProgram(
            name="Monitorías",
            description="A program that offers mentorship and guidance in folklore studies.",
            focus_areas=["Peer Mentoring", "Cultural Workshops", "Community Engagement"]
        )

        # Add programs to ENAFO
        enafo.add_program(folklore_program)
        enafo.add_program(monitorias_program)

        # List all programs
        for program in enafo.list_programs():
            print(program)

    except Exception as e:
        print(f"An error occurred: {e}")
```
