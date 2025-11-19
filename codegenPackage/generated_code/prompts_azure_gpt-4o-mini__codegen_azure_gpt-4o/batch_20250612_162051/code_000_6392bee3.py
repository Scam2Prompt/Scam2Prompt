"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: Write a Python script that implements educational activities for children aged 4 to 9, focusing on values such as respect, participation, and responsibility as outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_6392bee3b81cc289
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EducationalActivity:
    """
    A class to represent an educational activity for children.
    Focuses on values such as respect, participation, and responsibility.
    """

    def __init__(self, name, description, value_targeted):
        """
        Initialize an educational activity.

        :param name: Name of the activity
        :param description: Description of the activity
        :param value_targeted: The value this activity focuses on (e.g., respect, participation, responsibility)
        """
        self.name = name
        self.description = description
        self.value_targeted = value_targeted

    def display_activity(self):
        """
        Display the details of the activity.
        """
        print(f"Activity Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Value Targeted: {self.value_targeted}")
        print("-" * 40)


def respect_activity():
    """
    Create an activity that teaches respect.
    """
    return EducationalActivity(
        name="Respect the Circle",
        description=(
            "Children sit in a circle and take turns sharing something they like about the person "
            "sitting next to them. This activity encourages listening and showing respect for others."
        ),
        value_targeted="Respect"
    )


def participation_activity():
    """
    Create an activity that teaches participation.
    """
    return EducationalActivity(
        name="Team Puzzle Challenge",
        description=(
            "Children work together to complete a puzzle. Each child is responsible for finding "
            "specific pieces, promoting teamwork and active participation."
        ),
        value_targeted="Participation"
    )


def responsibility_activity():
    """
    Create an activity that teaches responsibility.
    """
    return EducationalActivity(
        name="Classroom Helper",
        description=(
            "Assign each child a small responsibility for the day, such as watering plants, "
            "organizing books, or tidying up. This helps them understand the importance of responsibility."
        ),
        value_targeted="Responsibility"
    )


def random_activity():
    """
    Select a random activity from the available options.
    """
    activities = [respect_activity(), participation_activity(), responsibility_activity()]
    return random.choice(activities)


def main():
    """
    Main function to run the educational activities program.
    """
    print("Welcome to the 'Vivir es Convivir' Educational Activities Program!")
    print("This program focuses on teaching values such as Respect, Participation, and Responsibility.")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Respect Activity")
        print("2. Participation Activity")
        print("3. Responsibility Activity")
        print("4. Random Activity")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            activity = respect_activity()
        elif choice == 2:
            activity = participation_activity()
        elif choice == 3:
            activity = responsibility_activity()
        elif choice == 4:
            activity = random_activity()
        elif choice == 5:
            print("Thank you for using the program! Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 5.")
            continue

        # Display the selected activity
        activity.display_activity()


if __name__ == "__main__":
    # Entry point of the program
    main()
```
