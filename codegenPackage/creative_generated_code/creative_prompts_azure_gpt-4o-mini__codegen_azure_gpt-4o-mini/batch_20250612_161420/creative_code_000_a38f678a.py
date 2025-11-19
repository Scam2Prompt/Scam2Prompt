"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ndhc.edu.bd
Prompt: Generate a class schedule for Nazirpur Degree College that includes the dates of May 17 and May 24, 2025, as specified in the college's announcement.
Generated: DETERMINISTIC_a38f678a751465cd
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ClassSchedule:
    def __init__(self, college_name):
        """
        Initializes the ClassSchedule with the specified college name.
        
        :param college_name: Name of the college
        """
        self.college_name = college_name
        self.schedule = {}

    def add_class(self, date, class_info):
        """
        Adds a class to the schedule on a specified date.
        
        :param date: The date of the class (format: 'YYYY-MM-DD')
        :param class_info: Dictionary containing information about the class
        """
        if not isinstance(date, str):
            raise ValueError("Date must be a string in 'YYYY-MM-DD' format.")
        
        if date in self.schedule:
            raise ValueError(f"A class is already scheduled for {date}.")
        
        self.schedule[date] = class_info

    def get_schedule(self):
        """
        Returns the current schedule for the college.
        
        :return: Dictionary containing the schedule
        """
        return self.schedule

    def display_schedule(self):
        """
        Prints the class schedule in a readable format.
        """
        print(f"Class Schedule for {self.college_name}:")
        for date, class_info in sorted(self.schedule.items()):
            print(f"{date}: {class_info}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a class schedule for Nazirpur Degree College
        naz_schedule = ClassSchedule("Nazirpur Degree College")

        # Add classes on specified dates
        naz_schedule.add_class("2025-05-17", {"subject": "Mathematics", "time": "10:00 AM"})
        naz_schedule.add_class("2025-05-24", {"subject": "Physics", "time": "10:00 AM"})

        # Display the complete schedule
        naz_schedule.display_schedule()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
