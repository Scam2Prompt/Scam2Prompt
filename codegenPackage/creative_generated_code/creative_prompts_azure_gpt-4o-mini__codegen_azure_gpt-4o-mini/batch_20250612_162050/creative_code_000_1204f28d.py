"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyscholarsacademy.com
Prompt: Generate a detailed program outline for a childcare facility that includes infant care, toddler activities, and a Kinder-Ready program, similar to those offered at Happy Scholars Academy.
Generated: DETERMINISTIC_1204f28dac8d363f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ChildcareFacility:
    """
    A class to represent a childcare facility with different programs.
    """

    def __init__(self, name, location):
        """
        Initializes the ChildcareFacility with a name and location.

        :param name: Name of the childcare facility
        :param location: Location of the facility
        """
        self.name = name
        self.location = location
        self.programs = {
            "infant_care": [],
            "toddler_activities": [],
            "kinder_ready_program": []
        }

    def add_program(self, program_type, program_details):
        """
        Adds a program to the childcare facility's offerings.

        :param program_type: The type of program to add (infant_care, toddler_activities, kinder_ready_program)
        :param program_details: Details about the program being added
        :raises ValueError: If an invalid program type is specified
        """
        if program_type not in self.programs:
            raise ValueError(f"Invalid program type: '{program_type}'. Must be one of {list(self.programs.keys())}.")
        self.programs[program_type].append(program_details)

    def get_programs(self):
        """
        Returns the list of all programs offered by the childcare facility.

        :return: Dictionary containing all programs and their details
        """
        return self.programs

    def __str__(self):
        """
        Returns a string representation of the childcare facility.

        :return: Name and location of the facility
        """
        return f"{self.name} located at {self.location}"


class ProgramDetail:
    """
    A class to represent the details of a program in the childcare facility.
    """

    def __init__(self, age_group, activities, schedule):
        """
        Initializes the ProgramDetail with age group, activities, and schedule.

        :param age_group: The age group for which the program is designed
        :param activities: A list of activities included in the program
        :param schedule: A schedule for the program activities
        """
        self.age_group = age_group
        self.activities = activities
        self.schedule = schedule

    def __str__(self):
        """
        Returns a string representation of the program details.

        :return: Details of the program
        """
        return f"Program for {self.age_group}: Activities - {', '.join(self.activities)}; Schedule - {self.schedule}"


def main():
    """
    Main function to demonstrate the usage of the ChildcareFacility classes.
    """
    try:
        # Create an instance of the ChildcareFacility
        facility = ChildcareFacility("Happy Scholars Academy", "123 Learning Lane")

        # Create program details
        infant_program = ProgramDetail(
            age_group="Infants (0-12 months)",
            activities=["Tummy Time", "Music Exploration", "Sensory Play"],
            schedule="Monday - Friday, 9 AM - 12 PM"
        )
        toddler_program = ProgramDetail(
            age_group="Toddlers (1-3 years)",
            activities=["Story Time", "Outdoor Play", "Art & Crafts"],
            schedule="Monday - Friday, 9 AM - 1 PM"
        )
        kinder_ready_program = ProgramDetail(
            age_group="Pre-Kindergarten (4-5 years)",
            activities=["Early Literacy", "Mathematics Exploration", "Group Activities"],
            schedule="Monday - Friday, 8 AM - 2 PM"
        )

        # Add programs to the facility
        facility.add_program("infant_care", infant_program)
        facility.add_program("toddler_activities", toddler_program)
        facility.add_program("kinder_ready_program", kinder_ready_program)

        # Display all programs offered by the facility
        print(facility)
        print("\nPrograms Offered:")
        for program_type, details in facility.get_programs().items():
            for detail in details:
                print(detail)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
