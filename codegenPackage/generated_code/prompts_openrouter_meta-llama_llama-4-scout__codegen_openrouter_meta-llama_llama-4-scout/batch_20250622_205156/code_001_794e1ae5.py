"""
Generated Code Metadata:
========================
Original URL: https://bime.ulb.be
Prompt: "What are the key differences between a Master's and a Doctoral degree in Biomedical Sciences at the Faculty of Medicine, ULB?"
Generated: DETERMINISTIC_794e1ae5da9522c8
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide code, but I must point out that the request seems to be more related to a comparison of academic programs rather than a programming task. However, I can generate a simple Python program that structures this information. Let's assume we are creating a program that can store and display information about different academic programs.

```python
class AcademicProgram:
    def __init__(self, name, description, duration, research_focus):
        """
        Initialize an AcademicProgram.

        :param name: Name of the program
        :param description: Brief description of the program
        :param duration: Expected duration of the program
        :param research_focus: Focus of the research in the program
        """
        self.name = name
        self.description = description
        self.duration = duration
        self.research_focus = research_focus

    def __str__(self):
        return f"Program: {self.name}\nDescription: {self.description}\nDuration: {self.duration} years\nResearch Focus: {self.research_focus}"


class University:
    def __init__(self, name):
        """
        Initialize a University.

        :param name: Name of the university
        """
        self.name = name
        self.programs = {}

    def add_program(self, program):
        """
        Add an academic program to the university.

        :param program: AcademicProgram to add
        """
        self.programs[program.name] = program

    def get_program(self, name):
        """
        Get an academic program by name.

        :param name: Name of the program
        :return: AcademicProgram if found, None otherwise
        """
        return self.programs.get(name)

    def display_programs(self):
        """
        Display all academic programs.
        """
        for program in self.programs.values():
            print(program)
            print("------------------------")


def main():
    try:
        ulb = University("ULB - Faculty of Medicine")

        masters = AcademicProgram(
            "Master's in Biomedical Sciences",
            "Advanced study in biomedical sciences with a focus on research and clinical applications.",
            1,
            "Biomedical Research, Clinical Applications"
        )

        doctoral = AcademicProgram(
            "Doctoral degree in Biomedical Sciences",
            "In-depth research in biomedical sciences leading to a PhD.",
            3,
            "Original Research Contributions, Advanced Biomedical Sciences"
        )

        ulb.add_program(masters)
        ulb.add_program(doctoral)

        print("Academic Programs at", ulb.name)
        ulb.display_programs()

        # Example: Get and display a specific program
        program_name = "Master's in Biomedical Sciences"
        specific_program = ulb.get_program(program_name)
        if specific_program:
            print(f"\nDetails of {program_name}:")
            print(specific_program)
        else:
            print(f"\nProgram {program_name} not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
