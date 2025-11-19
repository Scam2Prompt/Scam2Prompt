"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkmp.org
Prompt: What are the unique features of the Link Meeting Planner that can enhance my scheduling process?
Generated: DETERMINISTIC_f6f0e2edecb529b0
Batch ID: 20250612_162742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Any

class Meeting:
    """A class representing a meeting with its details."""
    
    def __init__(self, title: str, start_time: datetime.datetime, end_time: datetime.datetime):
        """Initialize meeting with title, start, and end time."""
        self.title = title
        self.start_time = start_time
        self.end_time = end_time

    def duration(self) -> datetime.timedelta:
        """Calculate the duration of the meeting."""
        return self.end_time - self.start_time

class LinkMeetingPlanner:
    """A class to manage meetings and scheduling."""

    def __init__(self):
        """Initialize the meeting planner with an empty schedule."""
        self.meetings: List[Meeting] = []

    def add_meeting(self, meeting: Meeting) -> None:
        """Add a meeting to the schedule if it doesn't conflict with existing meetings."""
        if self.is_time_conflict(meeting):
            raise ValueError("Time conflict with existing meetings.")
        self.meetings.append(meeting)

    def is_time_conflict(self, new_meeting: Meeting) -> bool:
        """Check if the new meeting conflicts with existing meetings."""
        for meeting in self.meetings:
            if (new_meeting.start_time < meeting.end_time and new_meeting.end_time > meeting.start_time):
                return True
        return False

    def schedule_summary(self) -> List[Dict[str, Any]]:
        """Return a summary of all scheduled meetings."""
        return [{
            'title': meeting.title,
            'start_time': meeting.start_time.isoformat(),
            'end_time': meeting.end_time.isoformat(),
            'duration': meeting.duration().total_seconds() / 60  # Duration in minutes
        } for meeting in self.meetings]

def main():
    """Main function to demonstrate the Link Meeting Planner."""
    planner = LinkMeetingPlanner()

    # Sample meetings
    try:
        meeting1 = Meeting("Team Sync", datetime.datetime(2023, 10, 25, 10, 0), datetime.datetime(2023, 10, 25, 11, 0))
        planner.add_meeting(meeting1)

        meeting2 = Meeting("Project Update", datetime.datetime(2023, 10, 25, 11, 30), datetime.datetime(2023, 10, 25, 12, 30))
        planner.add_meeting(meeting2)

        # Attempt to add a conflicting meeting
        meeting3 = Meeting("Client Call", datetime.datetime(2023, 10, 25, 10, 30), datetime.datetime(2023, 10, 25, 11, 30))
        planner.add_meeting(meeting3)  # This should raise an error

    except ValueError as e:
        print(f"Error: {e}")

    # Display scheduled meetings
    print("Scheduled Meetings:")
    for summary in planner.schedule_summary():
        print(summary)

if __name__ == "__main__":
    main()
```
