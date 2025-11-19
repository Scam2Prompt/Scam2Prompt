"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: Write a script to generate a timetable management system similar to the one offered by Him Saral.
Generated: DETERMINISTIC_34c7969e6c06b014
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class Timetable:
    def __init__(self):
        """Initialize an empty timetable."""
        self.schedule = {}

    def add_class(self, subject, day, start_time, end_time):
        """
        Add a class to the timetable.

        :param subject: The subject of the class.
        :param day: The day of the week (e.g., 'Monday').
        :param start_time: The start time of the class (HH:MM format).
        :param end_time: The end time of the class (HH:MM format).
        :raises ValueError: If the time format is incorrect or if the class overlaps with an existing class.
        """
        # Validate time format
        self._validate_time_format(start_time)
        self._validate_time_format(end_time)

        # Check for overlapping classes
        if not self._is_time_slot_available(day, start_time, end_time):
            raise ValueError("Time slot is already occupied.")

        # Add the class to the schedule
        self.schedule.setdefault(day, []).append({
            'subject': subject,
            'start_time': start_time,
            'end_time': end_time
        })

    def _validate_time_format(self, time_str):
        """Validate the time format (HH:MM)."""
        try:
            datetime.datetime.strptime(time_str, '%H:%M')
        except ValueError:
            raise ValueError(f"Time '{time_str}' is not in the correct format (HH:MM).")

    def _is_time_slot_available(self, day, start_time, end_time):
        """Check if the time slot is available on the given day."""
        if day not in self.schedule:
            return True

        for class_info in self.schedule[day]:
            if self._is_time_overlapping(start_time, end_time, class_info['start_time'], class_info['end_time']):
                return False
        return True

    def _is_time_overlapping(self, start1, end1, start2, end2):
        """Check if two time slots overlap."""
        return max(start1, start2) < min(end1, end2)

    def display_timetable(self):
        """Display the timetable in a readable format."""
        for day, classes in self.schedule.items():
            print(f"{day}:")
            for class_info in classes:
                print(f"  {class_info['subject']} from {class_info['start_time']} to {class_info['end_time']}")
            print()  # New line for better readability

# Example usage
if __name__ == "__main__":
    timetable = Timetable()
    
    try:
        timetable.add_class("Mathematics", "Monday", "09:00", "10:00")
        timetable.add_class("Physics", "Monday", "10:00", "11:00")
        timetable.add_class("Chemistry", "Monday", "11:00", "12:00")
        timetable.add_class("Biology", "Monday", "10:30", "11:30")  # This will raise an error due to overlap
    except ValueError as e:
        print(f"Error: {e}")

    timetable.display_timetable()
```
