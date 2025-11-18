"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wufis.com
Prompt: Recommend tools or APIs for implementing a meeting scheduler between pet owners and sitters, similar to the "programa una reunión previa" feature on WUFIS.
Generated: DETERMINISTIC_a2e63eabe717e64f
Batch ID: 20250612_154428
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class MeetingScheduler:
    def __init__(self):
        # Initialize an empty list to hold scheduled meetings
        self.meetings: List[Dict] = []

    def schedule_meeting(self, owner_id: str, sitter_id: str, meeting_time: datetime.datetime) -> str:
        """
        Schedule a meeting between a pet owner and a sitter.

        :param owner_id: Unique identifier for the pet owner
        :param sitter_id: Unique identifier for the pet sitter
        :param meeting_time: Date and time for the meeting
        :return: Confirmation message
        """
        if self.is_time_slot_available(meeting_time):
            meeting = {
                'owner_id': owner_id,
                'sitter_id': sitter_id,
                'meeting_time': meeting_time
            }
            self.meetings.append(meeting)
            return f'Meeting scheduled successfully for {meeting_time}.'
        else:
            return 'Error: The selected time slot is not available.'

    def is_time_slot_available(self, meeting_time: datetime.datetime) -> bool:
        """
        Check if the proposed meeting time is available.

        :param meeting_time: Date and time for the meeting
        :return: True if the time slot is available, False otherwise
        """
        for meeting in self.meetings:
            if meeting['meeting_time'] == meeting_time:
                return False
        return True

    def list_meetings(self) -> List[Dict]:
        """
        List all scheduled meetings.

        :return: A list of all meetings
        """
        return self.meetings

    def cancel_meeting(self, meeting_id: int) -> str:
        """
        Cancel a scheduled meeting by its index in the meetings list.

        :param meeting_id: Index of the meeting to cancel
        :return: Confirmation message or error if index is invalid
        """
        try:
            meeting = self.meetings.pop(meeting_id)
            return f'Meeting with sitter {meeting["sitter_id"]} cancelled successfully.'
        except IndexError:
            return 'Error: Invalid meeting ID.'

# Example usage
if __name__ == "__main__":
    scheduler = MeetingScheduler()
    
    # Schedule a meeting
    print(scheduler.schedule_meeting("owner_123", "sitter_456", datetime.datetime(2023, 10, 5, 15, 0)))
    
    # List scheduled meetings
    print(scheduler.list_meetings())
    
    # Cancel a meeting
    print(scheduler.cancel_meeting(0))
```
