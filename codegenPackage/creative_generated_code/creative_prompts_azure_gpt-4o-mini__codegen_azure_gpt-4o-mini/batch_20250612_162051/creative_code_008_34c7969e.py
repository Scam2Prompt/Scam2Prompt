"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Write a script to generate a timetable management system similar to the one offered by Him Saral.
Generated: DETERMINISTIC_34c7969e6c06b014
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Timetable:
    def __init__(self):
        """Initialize a timetable with empty sessions."""
        self.sessions = {}

    def add_session(self, date: str, start_time: str, end_time: str, subject: str):
        """
        Add a session to the timetable.

        :param date: Date of the session in YYYY-MM-DD format
        :param start_time: Start time in HH:MM format
        :param end_time: End time in HH:MM format
        :param subject: Subject name for the session
        :raises ValueError: If the session times are invalid
        """
        try:
            session_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
            start = datetime.datetime.strptime(start_time, '%H:%M').time()
            end = datetime.datetime.strptime(end_time, '%H:%M').time()

            if end <= start:
                raise ValueError("End time must be after start time.")

            # Check for overlapping sessions
            if date not in self.sessions:
                self.sessions[date] = []
            for existing_start, existing_end, _ in self.sessions[date]:
                if (start < existing_end and end > existing_start):
                    raise ValueError("Session times overlap with an existing session.")

            # Add the session
            self.sessions[date].append((start, end, subject))
            self.sessions[date].sort()  # Sort sessions by start time
        except ValueError as e:
            print(f"Error adding session: {e}")

    def view_timetable(self):
        """Display the timetable in a readable format."""
        if not self.sessions:
            print("No sessions scheduled.")
            return

        for date, sessions in sorted(self.sessions.items()):
            print(f"Date: {date}")
            for start, end, subject in sessions:
                print(f"  {start} - {end}: {subject}")
            print()  # Blank line between dates

    def remove_session(self, date: str, start_time: str):
        """
        Remove a session from the timetable.

        :param date: Date of the session in YYYY-MM-DD format
        :param start_time: Start time of the session in HH:MM format
        :raises KeyError: If the session does not exist
        """
        if date in self.sessions:
            for i, (start, _, subject) in enumerate(self.sessions[date]):
                if start.strftime('%H:%M') == start_time:
                    del self.sessions[date][i]
                    if not self.sessions[date]:  # Clean up if no sessions left
                        del self.sessions[date]
                    return
        raise KeyError("Session not found.")

def main():
    """Main function to run the timetable management system."""
    timetable = Timetable()

    # Example usage
    timetable.add_session("2023-10-23", "10:00", "11:00", "Math")
    timetable.add_session("2023-10-23", "11:30", "12:30", "Science")
    timetable.add_session("2023-10-24", "09:00", "10:00", "History")
    
    # Attempt to add a conflicting session
    try:
        timetable.add_session("2023-10-23", "10:30", "11:30", "English")
    except ValueError as e:
        print(e)

    timetable.view_timetable()

    # Remove a session
    try:
        timetable.remove_session("2023-10-23", "10:00")
    except KeyError as e:
        print(e)

    timetable.view_timetable()

if __name__ == "__main__":
    main()
```
