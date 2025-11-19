"""
Generated Code Metadata:
========================
Original URL: https://nzothofetcollege.co.za
Prompt: What are the differences between the Occupational Certificate: Electrician and the National N Diploma: Electrical Engineering programs at Nzotho FET College?
Generated: DETERMINISTIC_bbc48f05c7a31fba
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ElectricalProgram:
    """
    A class to represent an electrical program at Nzotho FET College.
    """

    def __init__(self, name, duration, focus_area, certification):
        """
        Initializes the ElectricalProgram with the given attributes.

        :param name: str - The name of the program
        :param duration: str - The duration of the program
        :param focus_area: str - The main focus area of the program
        :param certification: str - The type of certification awarded
        """
        self.name = name
        self.duration = duration
        self.focus_area = focus_area
        self.certification = certification

    def display_info(self):
        """
        Displays the information about the electrical program.
        """
        print(f"Program Name: {self.name}")
        print(f"Duration: {self.duration}")
        print(f"Focus Area: {self.focus_area}")
        print(f"Certification: {self.certification}")


def compare_programs(program1, program2):
    """
    Compares two electrical programs and prints their differences.

    :param program1: ElectricalProgram - The first program to compare
    :param program2: ElectricalProgram - The second program to compare
    """
    print("Comparing Programs:")
    print("-------------------")
    print(f"1. {program1.name} vs {program2.name}")
    print(f"   Duration: {program1.duration} vs {program2.duration}")
    print(f"   Focus Area: {program1.focus_area} vs {program2.focus_area}")
    print(f"   Certification: {program1.certification} vs {program2.certification}")


def main():
    """
    Main function to create program instances and compare them.
    """
    try:
        # Create instances of the programs
        electrician_program = ElectricalProgram(
            name="Occupational Certificate: Electrician",
            duration="3 years",
            focus_area="Practical electrical work and safety",
            certification="Occupational Certificate"
        )

        diploma_program = ElectricalProgram(
            name="National N Diploma: Electrical Engineering",
            duration="2 years",
            focus_area="Theoretical and practical electrical engineering principles",
            certification="National N Diploma"
        )

        # Display program information
        electrician_program.display_info()
        print()
        diploma_program.display_info()
        print()

        # Compare the two programs
        compare_programs(electrician_program, diploma_program)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
