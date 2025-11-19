"""
Generated Code Metadata:
========================
Original URL: https://batikenttofas.com
Prompt: Write a Python script to manage the fitness class schedule for Batıkent Tofaş Spor Klübü, including classes like Yoga & Pilates, Group Fitness, and Express Dance.
Generated: DETERMINISTIC_2f4712b8d80c908e
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fitness_class_scheduler.py

from datetime import datetime, timedelta
from enum import Enum

class FitnessClassType(Enum):
    """Enum for fitness class types."""
    YOGA_PILATES = "Yoga & Pilates"
    GROUP_FITNESS = "Group Fitness"
    EXPRESS_DANCE = "Express Dance"

class FitnessClass:
    """Represents a fitness class."""
    def __init__(self, class_type, start_time, end_time, instructor):
        """
        Initializes a FitnessClass object.

        Args:
            class_type (FitnessClassType): Type of fitness class.
            start_time (datetime): Start time of the class.
            end_time (datetime): End time of the class.
            instructor (str): Instructor's name.
        """
        self.class_type = class_type
        self.start_time = start_time
        self.end_time = end_time
        self.instructor = instructor

    def __str__(self):
        return f"{self.class_type.value} - {self.start_time.strftime('%Y-%m-%d %H:%M')} - {self.end_time.strftime('%Y-%m-%d %H:%M')} - {self.instructor}"

class FitnessClassScheduler:
    """Manages the fitness class schedule."""
    def __init__(self):
        self.schedule = []

    def add_class(self, fitness_class):
        """
        Adds a fitness class to the schedule.

        Args:
            fitness_class (FitnessClass): Fitness class to add.

        Raises:
            ValueError: If the class time conflicts with an existing class.
        """
        for existing_class in self.schedule:
            if (fitness_class.start_time < existing_class.end_time and 
                fitness_class.end_time > existing_class.start_time):
                raise ValueError("Class time conflicts with an existing class.")
        self.schedule.append(fitness_class)
        self.schedule.sort(key=lambda x: x.start_time)

    def remove_class(self, class_type, start_time):
        """
        Removes a fitness class from the schedule.

        Args:
            class_type (FitnessClassType): Type of fitness class.
            start_time (datetime): Start time of the class.

        Raises:
            ValueError: If the class is not found in the schedule.
        """
        for fitness_class in self.schedule:
            if fitness_class.class_type == class_type and fitness_class.start_time == start_time:
                self.schedule.remove(fitness_class)
                return
        raise ValueError("Class not found in the schedule.")

    def print_schedule(self):
        """Prints the fitness class schedule."""
        for fitness_class in self.schedule:
            print(fitness_class)

def main():
    scheduler = FitnessClassScheduler()

    try:
        # Add classes
        scheduler.add_class(FitnessClass(FitnessClassType.YOGA_PILATES, 
                                         datetime(2024, 9, 16, 9, 0), 
                                         datetime(2024, 9, 16, 10, 0), 
                                         "Instructor1"))
        scheduler.add_class(FitnessClass(FitnessClassType.GROUP_FITNESS, 
                                         datetime(2024, 9, 16, 10, 0), 
                                         datetime(2024, 9, 16, 11, 0), 
                                         "Instructor2"))
        scheduler.add_class(FitnessClass(FitnessClassType.EXPRESS_DANCE, 
                                         datetime(2024, 9, 16, 11, 0), 
                                         datetime(2024, 9, 16, 12, 0), 
                                         "Instructor3"))

        # Print schedule
        print("Fitness Class Schedule:")
        scheduler.print_schedule()

        # Remove a class
        scheduler.remove_class(FitnessClassType.GROUP_FITNESS, datetime(2024, 9, 16, 10, 0))

        # Print updated schedule
        print("\nUpdated Fitness Class Schedule:")
        scheduler.print_schedule()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
