"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Compare the MBA in Finance and Control (MBA FC), MBA in Global Leadership and Management (MBA GLM), and MBA in Information Technology (MBA IT) programs at SOMTU, highlighting their unique focus areas and curriculum structures.
Generated: DETERMINISTIC_2c9d1216093fb0f2
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class to represent an MBA program
class MBAProgram:
    def __init__(self, name, focus_area, curriculum):
        """
        Initialize an MBA program.

        Args:
            name (str): Name of the program.
            focus_area (str): Unique focus area of the program.
            curriculum (list): List of courses in the program.
        """
        self.name = name
        self.focus_area = focus_area
        self.curriculum = curriculum

    def __str__(self):
        return f"{self.name}: {self.focus_area}"

    def display_curriculum(self):
        """
        Display the curriculum of the program.
        """
        print(f"Curriculum for {self.name}:")
        for course in self.curriculum:
            print(f"- {course}")


# Define a class to compare MBA programs
class MBAProgramComparator:
    def __init__(self):
        """
        Initialize a comparator for MBA programs.
        """
        self.programs = []

    def add_program(self, program):
        """
        Add an MBA program to the comparator.

        Args:
            program (MBAProgram): Program to add.
        """
        self.programs.append(program)

    def compare_programs(self):
        """
        Compare the MBA programs and highlight their unique focus areas and curriculum structures.
        """
        print("MBA Program Comparison:")
        for program in self.programs:
            print(program)
            program.display_curriculum()
            print()


# Define the MBA programs at SOMTU
def create_mba_programs():
    """
    Create the MBA programs at SOMTU.

    Returns:
        list: List of MBA programs.
    """
    mba_fc = MBAProgram(
        "MBA in Finance and Control (MBA FC)",
        "Financial management, control, and strategy",
        [
            "Financial Accounting",
            "Financial Management",
            "Investment Analysis",
            "Corporate Finance",
            "Risk Management",
        ],
    )

    mba_glm = MBAProgram(
        "MBA in Global Leadership and Management (MBA GLM)",
        "Global leadership, management, and organizational behavior",
        [
            "Global Leadership",
            "Organizational Behavior",
            "Strategic Management",
            "International Business",
            "Cross-Cultural Management",
        ],
    )

    mba_it = MBAProgram(
        "MBA in Information Technology (MBA IT)",
        "Information technology, data analytics, and digital transformation",
        [
            "Data Structures and Algorithms",
            "Database Management",
            "Data Analytics and Visualization",
            "Digital Transformation",
            "IT Project Management",
        ],
    )

    return [mba_fc, mba_glm, mba_it]


# Main function
def main():
    try:
        comparator = MBAProgramComparator()
        programs = create_mba_programs()

        for program in programs:
            comparator.add_program(program)

        comparator.compare_programs()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
