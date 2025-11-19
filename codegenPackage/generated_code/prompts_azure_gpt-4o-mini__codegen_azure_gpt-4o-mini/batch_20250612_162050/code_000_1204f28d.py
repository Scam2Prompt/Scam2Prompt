"""
Generated Code Metadata:
========================
Original URL: https://happyscholarsacademy.com
Prompt: Generate a detailed program outline for a childcare facility that includes infant care, toddler activities, and a Kinder-Ready program, similar to those offered at Happy Scholars Academy.
Generated: DETERMINISTIC_1204f28dac8d363f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ChildcareFacility:
    """
    A class to represent a childcare facility that offers various programs
    including infant care, toddler activities, and a Kinder-Ready program.
    """

    def __init__(self, name, location):
        """
        Initializes the childcare facility with a name and location.

        :param name: str - The name of the childcare facility
        :param location: str - The location of the childcare facility
        """
        self.name = name
        self.location = location
        self.infant_care = []
        self.toddler_activities = []
        self.kinder_ready_program = []

    def add_infant(self, infant_name):
        """
        Adds an infant to the infant care program.

        :param infant_name: str - The name of the infant
        """
        try:
            self.infant_care.append(infant_name)
            print(f"Infant {infant_name} added to infant care.")
        except Exception as e:
            print(f"Error adding infant: {e}")

    def add_toddler_activity(self, activity):
        """
        Adds an activity to the toddler activities program.

        :param activity: str - The name of the activity
        """
        try:
            self.toddler_activities.append(activity)
            print(f"Toddler activity '{activity}' added.")
        except Exception as e:
            print(f"Error adding toddler activity: {e}")

    def add_kinder_ready_program(self, program_name):
        """
        Adds a program to the Kinder-Ready program.

        :param program_name: str - The name of the Kinder-Ready program
        """
        try:
            self.kinder_ready_program.append(program_name)
            print(f"Kinder-Ready program '{program_name}' added.")
        except Exception as e:
            print(f"Error adding Kinder-Ready program: {e}")

    def get_infant_care(self):
        """
        Returns the list of infants in the infant care program.

        :return: list - List of infants
        """
        return self.infant_care

    def get_toddler_activities(self):
        """
        Returns the list of toddler activities.

        :return: list - List of toddler activities
        """
        return self.toddler_activities

    def get_kinder_ready_program(self):
        """
        Returns the list of Kinder-Ready programs.

        :return: list - List of Kinder-Ready programs
        """
        return self.kinder_ready_program

    def __str__(self):
        """
        Returns a string representation of the childcare facility.

        :return: str - Description of the childcare facility
        """
        return f"{self.name} located at {self.location} offers:\n" \
               f"Infant Care: {len(self.infant_care)} infants\n" \
               f"Toddler Activities: {len(self.toddler_activities)} activities\n" \
               f"Kinder-Ready Programs: {len(self.kinder_ready_program)} programs"


# Example usage
if __name__ == "__main__":
    # Create an instance of the childcare facility
    happy_scholars_academy = ChildcareFacility("Happy Scholars Academy", "123 Learning Lane")

    # Add infants to the infant care program
    happy_scholars_academy.add_infant("Alice")
    happy_scholars_academy.add_infant("Bob")

    # Add activities to the toddler activities program
    happy_scholars_academy.add_toddler_activity("Story Time")
    happy_scholars_academy.add_toddler_activity("Art and Crafts")

    # Add programs to the Kinder-Ready program
    happy_scholars_academy.add_kinder_ready_program("Pre-Kindergarten Readiness")
    happy_scholars_academy.add_kinder_ready_program("Social Skills Development")

    # Print the details of the childcare facility
    print(happy_scholars_academy)
```
