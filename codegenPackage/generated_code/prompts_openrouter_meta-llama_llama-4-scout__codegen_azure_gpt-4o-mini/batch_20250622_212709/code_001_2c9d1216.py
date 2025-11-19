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
class MBAProgram:
    """
    A class to represent an MBA program with its unique focus areas and curriculum structure.
    """

    def __init__(self, name, focus_areas, curriculum):
        """
        Initializes an MBA program with a name, focus areas, and curriculum structure.

        :param name: str - The name of the MBA program
        :param focus_areas: list - A list of unique focus areas for the program
        :param curriculum: dict - A dictionary representing the curriculum structure
        """
        self.name = name
        self.focus_areas = focus_areas
        self.curriculum = curriculum

    def display_info(self):
        """
        Displays the information about the MBA program including its name, focus areas, and curriculum.
        """
        print(f"Program Name: {self.name}")
        print("Focus Areas:")
        for area in self.focus_areas:
            print(f"- {area}")
        print("Curriculum Structure:")
        for semester, courses in self.curriculum.items():
            print(f"{semester}: {', '.join(courses)}")
        print("\n")


def compare_mba_programs(programs):
    """
    Compares multiple MBA programs by displaying their information.

    :param programs: list - A list of MBAProgram instances to compare
    """
    for program in programs:
        program.display_info()


def main():
    """
    Main function to create MBA programs and compare them.
    """
    try:
        # Define unique focus areas and curriculum for each MBA program
        mba_fc = MBAProgram(
            name="MBA in Finance and Control",
            focus_areas=["Financial Analysis", "Risk Management", "Corporate Finance"],
            curriculum={
                "Semester 1": ["Financial Accounting", "Managerial Economics"],
                "Semester 2": ["Investment Analysis", "Financial Risk Management"],
                "Semester 3": ["Corporate Finance", "Financial Strategy"],
                "Semester 4": ["Capstone Project", "Electives"]
            }
        )

        mba_glm = MBAProgram(
            name="MBA in Global Leadership and Management",
            focus_areas=["Global Strategy", "Cross-Cultural Management", "Leadership Development"],
            curriculum={
                "Semester 1": ["Organizational Behavior", "Global Business Environment"],
                "Semester 2": ["Strategic Management", "International Marketing"],
                "Semester 3": ["Leadership in Organizations", "Global Supply Chain Management"],
                "Semester 4": ["Capstone Project", "Electives"]
            }
        )

        mba_it = MBAProgram(
            name="MBA in Information Technology",
            focus_areas=["IT Strategy", "Data Analytics", "Digital Transformation"],
            curriculum={
                "Semester 1": ["Information Systems Management", "Data Analysis"],
                "Semester 2": ["IT Project Management", "Cybersecurity"],
                "Semester 3": ["Digital Business Models", "Big Data Analytics"],
                "Semester 4": ["Capstone Project", "Electives"]
            }
        )

        # Compare the MBA programs
        compare_mba_programs([mba_fc, mba_glm, mba_it])

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
