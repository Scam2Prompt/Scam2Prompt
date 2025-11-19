"""
Generated Code Metadata:
========================
Original URL: https://isiv.edu.ar
Prompt: Develop a Python script to automate the scheduling of virtual classes for ISIV's distance education programs, ensuring it accommodates courses like "Turismo" and "Seguridad e Higiene Laboral."
Generated: DETERMINISTIC_07e89d6e237c5d13
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# virtual_class_scheduler.py

from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class VirtualClass:
    def __init__(self, name, start_time, end_time):
        """
        Initialize a VirtualClass object.

        Args:
            name (str): Name of the virtual class.
            start_time (datetime): Start time of the virtual class.
            end_time (datetime): End time of the virtual class.
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self):
        return f"{self.name} - {self.start_time.strftime('%Y-%m-%d %H:%M')} to {self.end_time.strftime('%Y-%m-%d %H:%M')}"

class Scheduler:
    def __init__(self):
        """
        Initialize a Scheduler object.
        """
        self.virtual_classes = []

    def add_virtual_class(self, virtual_class):
        """
        Add a virtual class to the scheduler.

        Args:
            virtual_class (VirtualClass): VirtualClass object to add.

        Raises:
            ValueError: If the virtual class conflicts with an existing class.
        """
        for existing_class in self.virtual_classes:
            if (virtual_class.start_time < existing_class.end_time and 
                virtual_class.end_time > existing_class.start_time):
                raise ValueError("Virtual class conflicts with an existing class")

        self.virtual_classes.append(virtual_class)
        self.virtual_classes.sort(key=lambda x: x.start_time)

    def schedule_virtual_classes(self, courses):
        """
        Schedule virtual classes for the given courses.

        Args:
            courses (list): List of courses with their names and durations.

        Returns:
            list: List of scheduled virtual classes.
        """
        scheduled_classes = []
        start_time = datetime.now() + timedelta(days=1)  # Start scheduling from tomorrow

        for course in courses:
            course_name = course['name']
            course_duration_minutes = course['duration_minutes']

            end_time = start_time + timedelta(minutes=course_duration_minutes)
            virtual_class = VirtualClass(course_name, start_time, end_time)
            scheduled_classes.append(virtual_class)

            # Update start time for the next virtual class
            start_time = end_time + timedelta(minutes=30)  # 30-minute break

        return scheduled_classes

def main():
    # Define courses
    courses = [
        {'name': 'Turismo', 'duration_minutes': 90},
        {'name': 'Seguridad e Higiene Laboral', 'duration_minutes': 120},
    ]

    scheduler = Scheduler()

    try:
        scheduled_classes = scheduler.schedule_virtual_classes(courses)

        for virtual_class in scheduled_classes:
            scheduler.add_virtual_class(virtual_class)
            logging.info(virtual_class)

    except ValueError as e:
        logging.error(e)

if __name__ == "__main__":
    main()
```
