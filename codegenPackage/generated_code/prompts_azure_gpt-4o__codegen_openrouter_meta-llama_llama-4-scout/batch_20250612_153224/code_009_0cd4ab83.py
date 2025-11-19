"""
Generated Code Metadata:
========================
Original URL: https://byamed.net
Prompt: Write code to implement a virtual meeting scheduler for brainstorming sessions, inspired by ByAmed.net's "Grab Coffee" consultation process.
Generated: DETERMINISTIC_0cd4ab838cb34ba1
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class MeetingScheduler:
    def __init__(self):
        """
        Initialize the meeting scheduler.
        """
        self.meetings = {}

    def schedule_meeting(self, attendee: str, duration: int = 30) -> str:
        """
        Schedule a meeting with an attendee.

        Args:
        - attendee (str): The name of the attendee.
        - duration (int): The duration of the meeting in minutes. Defaults to 30.

        Returns:
        - meeting_id (str): A unique identifier for the scheduled meeting.
        """
        meeting_id = f"meeting-{len(self.meetings) + 1}"
        start_time = datetime.now() + timedelta(minutes=10)  # start 10 minutes from now
        end_time = start_time + timedelta(minutes=duration)

        self.meetings[meeting_id] = {
            "attendee": attendee,
            "start_time": start_time,
            "end_time": end_time,
        }

        return meeting_id

    def reschedule_meeting(self, meeting_id: str, new_start_time: datetime) -> bool:
        """
        Reschedule a meeting.

        Args:
        - meeting_id (str): The unique identifier of the meeting to reschedule.
        - new_start_time (datetime): The new start time for the meeting.

        Returns:
        - bool: True if the meeting was rescheduled successfully, False otherwise.
        """
        if meeting_id not in self.meetings:
            return False

        duration = (self.meetings[meeting_id]["end_time"] - self.meetings[meeting_id]["start_time"]).total_seconds() / 60
        self.meetings[meeting_id]["start_time"] = new_start_time
        self.meetings[meeting_id]["end_time"] = new_start_time + timedelta(minutes=duration)

        return True

    def cancel_meeting(self, meeting_id: str) -> bool:
        """
        Cancel a meeting.

        Args:
        - meeting_id (str): The unique identifier of the meeting to cancel.

        Returns:
        - bool: True if the meeting was canceled successfully, False otherwise.
        """
        if meeting_id not in self.meetings:
            return False

        del self.meetings[meeting_id]
        return True

    def get_meeting_details(self, meeting_id: str) -> Dict:
        """
        Get the details of a meeting.

        Args:
        - meeting_id (str): The unique identifier of the meeting.

        Returns:
        - meeting_details (Dict): A dictionary containing the meeting details.
        """
        return self.meetings.get(meeting_id, {})

    def list_meetings(self) -> List[Dict]:
        """
        List all scheduled meetings.

        Returns:
        - meetings (List[Dict]): A list of dictionaries containing the meeting details.
        """
        return list(self.meetings.values())


def main():
    scheduler = MeetingScheduler()

    # Schedule a meeting
    meeting_id = scheduler.schedule_meeting("John Doe")
    print(f"Meeting ID: {meeting_id}")

    # Get meeting details
    meeting_details = scheduler.get_meeting_details(meeting_id)
    print("Meeting Details:")
    for key, value in meeting_details.items():
        print(f"{key.capitalize().replace('_', ' ')}: {value}")

    # Reschedule the meeting
    new_start_time = datetime.now() + timedelta(minutes=30)
    rescheduled = scheduler.reschedule_meeting(meeting_id, new_start_time)
    print(f"Rescheduled: {rescheduled}")

    # List all meetings
    meetings = scheduler.list_meetings()
    print("\nScheduled Meetings:")
    for i, meeting in enumerate(meetings):
        print(f"Meeting {i+1}:")
        for key, value in meeting.items():
            print(f"{key.capitalize().replace('_', ' ')}: {value}")
        print()

    # Cancel the meeting
    canceled = scheduler.cancel_meeting(meeting_id)
    print(f"Meeting {meeting_id} canceled: {canceled}")


if __name__ == "__main__":
    main()
```
