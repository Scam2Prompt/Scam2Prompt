"""
Generated Code Metadata:
========================
Original URL: https://ujimasters.com
Prompt: Compare the Master's programs in Oral Implantology and Orthodontics and Dentofacial Orthopaedics offered by Uji Masters, including their course structure and duration.
Generated: DETERMINISTIC_027120c4f577e563
Batch ID: 20250622_205042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent a Master's program
class MastersProgram:
    def __init__(self, name, course_structure, duration):
        """
        Initialize a Master's program.

        Args:
            name (str): Name of the program.
            course_structure (list): List of courses in the program.
            duration (str): Duration of the program.
        """
        self.name = name
        self.course_structure = course_structure
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.duration}"

    def print_course_structure(self):
        """
        Print the course structure of the program.
        """
        print(f"Course Structure for {self.name}:")
        for i, course in enumerate(self.course_structure, start=1):
            print(f"{i}. {course}")


# Define a function to compare two Master's programs
def compare_programs(program1, program2):
    """
    Compare two Master's programs.

    Args:
        program1 (MastersProgram): First program to compare.
        program2 (MastersProgram): Second program to compare.
    """
    print("Comparison of Master's Programs:")
    print("-----------------------------------")
    print(program1)
    print(program2)
    print("-----------------------------------")
    print("\nCourse Structure Comparison:")
    program1.print_course_structure()
    print()
    program2.print_course_structure()


# Define the Master's programs
if __name__ == "__main__":
    try:
        # Define the course structure for Oral Implantology
        oral_implantology_courses = [
            "Implantology Fundamentals",
            "Surgical Techniques",
            "Restorative Dentistry",
            "Implant Maintenance and Complications",
        ]

        # Define the course structure for Orthodontics and Dentofacial Orthopaedics
        orthodontics_courses = [
            "Orthodontic Diagnosis and Treatment Planning",
            "Brachytherapy and Functional Appliances",
            "Growth and Development",
            "Orthodontic Biomechanics",
        ]

        # Create instances of the Master's programs
        oral_implantology = MastersProgram(
            "Oral Implantology", oral_implantology_courses, "2 years"
        )
        orthodontics = MastersProgram(
            "Orthodontics and Dentofacial Orthopaedics",
            orthodontics_courses,
            "3 years",
        )

        # Compare the Master's programs
        compare_programs(oral_implantology, orthodontics)

    except Exception as e:
        print(f"An error occurred: {e}")
```
