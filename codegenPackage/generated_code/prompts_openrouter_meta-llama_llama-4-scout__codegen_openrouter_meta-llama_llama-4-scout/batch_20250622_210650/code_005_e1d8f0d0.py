"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: What is the mission and vision statement of Deepti Convent Higher Secondary School, and how can it be implemented in a school management software?
Generated: DETERMINISTIC_e1d8f0d0eb86ac4c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school.py

class School:
    def __init__(self, name, mission_statement, vision_statement):
        """
        Initialize a School object.

        Args:
            name (str): The name of the school.
            mission_statement (str): The mission statement of the school.
            vision_statement (str): The vision statement of the school.
        """
        self.name = name
        self.mission_statement = mission_statement
        self.vision_statement = vision_statement

    def get_mission_statement(self):
        """Return the mission statement of the school."""
        return self.mission_statement

    def get_vision_statement(self):
        """Return the vision statement of the school."""
        return self.vision_statement


class SchoolManagementSoftware:
    def __init__(self):
        """Initialize a SchoolManagementSoftware object."""
        self.schools = {}

    def add_school(self, school):
        """
        Add a school to the school management software.

        Args:
            school (School): The school to add.

        Raises:
            ValueError: If a school with the same name already exists.
        """
        if school.name in self.schools:
            raise ValueError("A school with the same name already exists.")
        self.schools[school.name] = school

    def get_school(self, name):
        """
        Get a school from the school management software.

        Args:
            name (str): The name of the school.

        Returns:
            School: The school with the given name, or None if not found.
        """
        return self.schools.get(name)

    def display_school_info(self, name):
        """
        Display the mission and vision statement of a school.

        Args:
            name (str): The name of the school.

        Raises:
            ValueError: If the school is not found.
        """
        school = self.get_school(name)
        if school is None:
            raise ValueError("School not found.")
        print(f"Mission Statement of {school.name}: {school.get_mission_statement()}")
        print(f"Vision Statement of {school.name}: {school.get_vision_statement()}")


def main():
    # Create a school management software
    software = SchoolManagementSoftware()

    # Create Deepti Convent Higher Secondary School
    deepti_convent = School(
        "Deepti Convent Higher Secondary School",
        "To provide a nurturing environment that fosters academic excellence, creativity, and character development.",
        "To empower students to become responsible citizens, critical thinkers, and lifelong learners."
    )

    # Add the school to the software
    software.add_school(deepti_convent)

    # Display the mission and vision statement of Deepti Convent Higher Secondary School
    software.display_school_info("Deepti Convent Higher Secondary School")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
