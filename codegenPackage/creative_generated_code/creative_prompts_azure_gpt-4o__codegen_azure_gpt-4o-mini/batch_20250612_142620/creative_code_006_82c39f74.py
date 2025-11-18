"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://potencia.in
Prompt: Write code to schedule and manage parent-teacher meetings every two months, ensuring progress tracking and personalized guidance, as practiced by Potencia Academy.
Generated: DETERMINISTIC_82c39f74c8466291
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import List, Dict, Any

class ParentTeacherMeeting:
    def __init__(self):
        # Initialize a dictionary to hold meetings
        self.meetings: Dict[str, Any] = {}

    def schedule_meeting(self, student_id: str, meeting_date: str) -> None:
        """
        Schedule a meeting for a specific student.
        
        Args:
            student_id (str): Unique identifier for the student.
            meeting_date (str): Date of the meeting in 'YYYY-MM-DD' format.

        Raises:
            ValueError: If the meeting date is not a valid date or if the date is in the past.
        """
        # Validate the meeting date
        date_obj = self._validate_date(meeting_date)

        if student_id not in self.meetings:
            self.meetings[student_id] = []

        # Add the meeting for the student
        self.meetings[student_id].append(date_obj)

    def _validate_date(self, date_str: str) -> datetime.date:
        """
        Validate the date format and ensure the date is not in the past.

        Args:
            date_str (str): Date string in 'YYYY-MM-DD' format.

        Returns:
            datetime.date: A valid date object.

        Raises:
            ValueError: If the date format is incorrect or if the date is in the past.
        """
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            if date_obj < datetime.date.today():
                raise ValueError("Meeting date cannot be in the past.")
            return date_obj
        except ValueError as e:
            raise ValueError(f"Invalid date format: {e}")

    def get_meetings(self, student_id: str) -> List[datetime.date]:
        """
        Retrieve all scheduled meetings for a specific student.

        Args:
            student_id (str): Unique identifier for the student.

        Returns:
            List[datetime.date]: List of scheduled meeting dates.
        """
        return self.meetings.get(student_id, [])

    def save_meetings_to_file(self, filename: str) -> None:
        """
        Save all scheduled meetings to a JSON file.

        Args:
            filename (str): The name of the file to save the meetings.

        Raises:
            IOError: If there is an error writing to the file.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.meetings, f, default=str)
        except IOError as e:
            raise IOError(f"Error saving meetings to file: {e}")

    def load_meetings_from_file(self, filename: str) -> None:
        """
        Load scheduled meetings from a JSON file.

        Args:
            filename (str): The name of the file to load the meetings from.

        Raises:
            IOError: If there is an error reading the file.
            ValueError: If the data format is incorrect.
        """
        try:
            with open(filename, 'r') as f:
                self.meetings = json.load(f)
                # Convert date strings back to date objects
                for student_id, dates in self.meetings.items():
                    self.meetings[student_id] = [datetime.datetime.strptime(date, '%Y-%m-%d').date() for date in dates]
        except IOError as e:
            raise IOError(f"Error loading meetings from file: {e}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON data: {e}")

# Example usage
if __name__ == "__main__":
    ptm = ParentTeacherMeeting()
    
    # Schedule meetings
    try:
        ptm.schedule_meeting("student_1", "2024-01-15")
        ptm.schedule_meeting("student_1", "2024-03-15")
        print("Meetings scheduled successfully.")
    except Exception as e:
        print(e)

    # Retrieve meetings
    meetings = ptm.get_meetings("student_1")
    print(f"Scheduled meetings for student_1: {meetings}")

    # Save to file
    try:
        ptm.save_meetings_to_file("meetings.json")
        print("Meetings saved to file successfully.")
    except Exception as e:
        print(e)

    # Load from file
    try:
        ptm.load_meetings_from_file("meetings.json")
        print("Meetings loaded from file successfully.")
    except Exception as e:
        print(e)
```
