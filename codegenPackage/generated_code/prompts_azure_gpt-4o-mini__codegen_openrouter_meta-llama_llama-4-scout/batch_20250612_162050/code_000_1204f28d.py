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
# childcare_facility.py

class ChildcareFacility:
    def __init__(self, name):
        """
        Initialize a childcare facility with a given name.

        Args:
            name (str): The name of the childcare facility.
        """
        self.name = name
        self.infants = []
        self.toddlers = []
        self.kinder_ready_students = []

    def add_infant(self, name, age):
        """
        Add an infant to the childcare facility.

        Args:
            name (str): The name of the infant.
            age (int): The age of the infant in months.

        Raises:
            ValueError: If the age is not a positive integer.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.infants.append({"name": name, "age": age})

    def add_toddler(self, name, age):
        """
        Add a toddler to the childcare facility.

        Args:
            name (str): The name of the toddler.
            age (int): The age of the toddler in years.

        Raises:
            ValueError: If the age is not a positive integer.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.toddlers.append({"name": name, "age": age})

    def add_kinder_ready_student(self, name, age):
        """
        Add a student to the Kinder-Ready program.

        Args:
            name (str): The name of the student.
            age (int): The age of the student in years.

        Raises:
            ValueError: If the age is not a positive integer.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        self.kinder_ready_students.append({"name": name, "age": age})

    def display_infant_care(self):
        """
        Display the list of infants in care.
        """
        print("Infant Care:")
        for infant in self.infants:
            print(f"Name: {infant['name']}, Age: {infant['age']} months")

    def display_toddler_activities(self):
        """
        Display the list of toddlers and their activities.
        """
        print("\nToddler Activities:")
        for toddler in self.toddlers:
            print(f"Name: {toddler['name']}, Age: {toddler['age']} years")
            # Sample activities
            print("  - Playtime: Blocks, Toys, and Music")
            print("  - Snack Time: Fresh Fruits and Yogurt")
            print("  - Nap Time: Quiet Rest")

    def display_kinder_ready_program(self):
        """
        Display the list of students in the Kinder-Ready program.
        """
        print("\nKinder-Ready Program:")
        for student in self.kinder_ready_students:
            print(f"Name: {student['name']}, Age: {student['age']} years")
            # Sample program activities
            print("  - Alphabet and Number Recognition")
            print("  - Shape and Color Identification")
            print("  - Social Skills and Emotional Intelligence")


def main():
    try:
        facility = ChildcareFacility("Happy Scholars Academy")

        # Add infants
        facility.add_infant("John Doe", 6)
        facility.add_infant("Jane Doe", 9)

        # Add toddlers
        facility.add_toddler("Emily Chen", 2)
        facility.add_toddler("Michael Brown", 3)

        # Add Kinder-Ready students
        facility.add_kinder_ready_student("Sophia Lee", 5)
        facility.add_kinder_ready_student("Oliver Kim", 5)

        # Display programs
        facility.display_infant_care()
        facility.display_toddler_activities()
        facility.display_kinder_ready_program()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
