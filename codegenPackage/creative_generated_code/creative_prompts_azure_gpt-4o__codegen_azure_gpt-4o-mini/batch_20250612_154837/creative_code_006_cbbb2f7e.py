"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mujeresautistas.com
Prompt: Write a script to calculate the total number of hours spent in various dance classes per week, based on a schedule like the one offered at Sakura Dance Studio.
Generated: DETERMINISTIC_cbbb2f7eb7f54de3
Batch ID: 20250612_154837
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DanceClass:
    """
    A class to represent a dance class with its name and duration in hours.
    """

    def __init__(self, name: str, duration: float):
        """
        Initialize the DanceClass with a name and a duration.

        :param name: The name of the dance class.
        :param duration: The duration of the class in hours.
        """
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.duration} hours"


class DanceSchedule:
    """
    A class to manage a weekly dance schedule, allowing for the calculation
    of total hours spent in dance classes.
    """

    def __init__(self):
        """
        Initialize the DanceSchedule with an empty list of classes.
        """
        self.classes = []

    def add_class(self, dance_class: DanceClass):
        """
        Add a DanceClass to the schedule.

        :param dance_class: An instance of DanceClass to add to the schedule.
        """
        if not isinstance(dance_class, DanceClass):
            raise TypeError("Expected an instance of DanceClass.")
        self.classes.append(dance_class)

    def total_hours(self) -> float:
        """
        Calculate the total number of hours spent in dance classes per week.

        :return: Total hours in float.
        """
        total = sum(dance_class.duration for dance_class in self.classes)
        return total


def main():
    """
    Main function to demonstrate the usage of DanceClass and DanceSchedule.
    """
    schedule = DanceSchedule()

    # Sample data for classes
    try:
        schedule.add_class(DanceClass("Ballet", 1.5))
        schedule.add_class(DanceClass("Hip Hop", 2.0))
        schedule.add_class(DanceClass("Jazz", 1.5))
        schedule.add_class(DanceClass("Contemporary", 2.0))

        total = schedule.total_hours()
        print(f"Total hours spent in dance classes per week: {total:.2f} hours")

    except TypeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
