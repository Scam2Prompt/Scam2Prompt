"""
Generated Code Metadata:
========================
Original URL: https://potencia.in
Prompt: Write code to schedule and manage parent-teacher meetings every two months, ensuring progress tracking and personalized guidance, as practiced by Potencia Academy.
Generated: DETERMINISTIC_82c39f74c8466291
Batch ID: 20250612_142620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional
from enum import Enum
import json
import os

class MeetingStatus(Enum):
    SCHEDULED = "Scheduled"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"
    RESCHEDULED = "Rescheduled"

class Meeting:
    def __init__(self, meeting_id: str, parent_name: str, teacher_name: str, 
                 student_name: str, scheduled_time: datetime.datetime, 
                 status: MeetingStatus = MeetingStatus.SCHEDULED):
        self.meeting_id = meeting_id
        self.parent_name = parent_name
        self.teacher_name = teacher_name
        self.student_name = student_name
        self.scheduled_time = scheduled_time
        self.status = status
        self.notes: str = ""
        self.follow_up_actions: List[str] = []
        self.progress_updates: Dict[str, str] = {}

    def to_dict(self) -> Dict:
        return {
            "meeting_id": self.meeting_id,
            "parent_name": self.parent_name,
            "teacher_name": self.teacher_name,
            "student_name": self.student_name,
            "scheduled_time": self.scheduled_time.isoformat(),
            "status": self.status.value,
            "notes": self.notes,
            "follow_up_actions": self.follow_up_actions,
            "progress_updates": self.progress_updates
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Meeting':
        meeting = cls(
            meeting_id=data["meeting_id"],
            parent_name=data["parent_name"],
            teacher_name=data["teacher_name"],
            student_name=data["student_name"],
            scheduled_time=datetime.datetime.fromisoformat(data["scheduled_time"]),
            status=MeetingStatus(data["status"])
        )
        meeting.notes = data.get("notes", "")
        meeting.follow_up_actions = data.get("follow_up_actions", [])
        meeting.progress_updates = data.get("progress_updates", {})
        return meeting

class MeetingScheduler:
    def __init__(self, storage_file: str = "meetings.json"):
        self.storage_file = storage_file
        self.meetings: Dict[str, Meeting] = {}
        self._load_meetings()

    def _load_meetings(self) -> None:
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, "r") as f:
                    data = json.load(f)
                    self.meetings = {
                        meeting_id: Meeting.from_dict(meeting_data)
                        for meeting_id, meeting_data in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading meetings: {e}")
                self.meetings = {}

    def _save_meetings(self) -> None:
        try:
            with open(self.storage_file, "w") as f:
                json.dump(
                    {mid: m.to_dict() for mid, m in self.meetings.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            print(f"Error saving meetings: {e}")

    def schedule_meeting(self, parent_name: str, teacher_name: str, 
                        student_name: str, initial_date: datetime.datetime) -> Meeting:
        meeting_id = f"mtg-{datetime.datetime.now().timestamp()}"
        next_meeting_date = initial_date
        
        # Schedule every two months
        if datetime.datetime.now() > initial_date:
            months_to_add = ((datetime.datetime.now().year - initial_date.year) * 12 + 
                            datetime.datetime.now().month - initial_date.month)
            months_to_add = (months_to_add // 2 + 1) * 2
            next_meeting_date = initial_date + datetime.timedelta(days=30*months_to_add)
        
        meeting = Meeting(
            meeting_id=meeting_id,
            parent_name=parent_name,
            teacher_name=teacher_name,
            student_name=student_name,
            scheduled_time=next_meeting_date
        )
        
        self.meetings[meeting_id] = meeting
        self._save_meetings()
        return meeting

    def get_upcoming_meetings(self, days_ahead: int = 30) -> List[Meeting]:
        now = datetime.datetime.now()
        end_date = now + datetime.timedelta(days=days_ahead)
        return [
            meeting for meeting in self.meetings.values()
            if meeting.status == MeetingStatus.SCHEDULED and
            now <= meeting.scheduled_time <= end_date
        ]

    def update_meeting_status(self, meeting_id: str, status: MeetingStatus) -> Optional[Meeting]:
        if meeting_id not in self.meetings:
            return None
        
        meeting = self.meetings[meeting_id]
        meeting.status = status
        self._save_meetings()
        return meeting

    def add_meeting_notes(self, meeting_id: str, notes: str) -> Optional[Meeting]:
        if meeting_id not in self.meetings:
            return None
        
        meeting = self.meetings[meeting_id]
        meeting.notes = notes
        self._save_meetings()
        return meeting

    def add_follow_up_action(self, meeting_id: str, action: str) -> Optional[Meeting]:
        if meeting_id not in self.meetings:
            return None
        
        meeting = self.meetings[meeting_id]
        meeting.follow_up_actions.append(action)
        self._save_meetings()
        return meeting

    def add_progress_update(self, meeting_id: str, area: str, update: str) -> Optional[Meeting]:
        if meeting_id not in self.meetings:
            return None
        
        meeting = self.meetings[meeting_id]
        meeting.progress_updates[area] = update
        self._save_meetings()
        return meeting

    def reschedule_meeting(self, meeting_id: str, new_date: datetime.datetime) -> Optional[Meeting]:
        if meeting_id not in self.meetings:
            return None
        
        meeting = self.meetings[meeting_id]
        meeting.scheduled_time = new_date
        meeting.status = MeetingStatus.RESCHEDULED
        self._save_meetings()
        return meeting

    def get_student_meetings(self, student_name: str) -> List[Meeting]:
        return [
            meeting for meeting in self.meetings.values()
            if meeting.student_name == student_name
        ]

    def get_teacher_meetings(self, teacher_name: str) -> List[Meeting]:
        return [
            meeting for meeting in self.meetings.values()
            if meeting.teacher_name == teacher_name
        ]

    def get_parent_meetings(self, parent_name: str) -> List[Meeting]:
        return [
            meeting for meeting in self.meetings.values()
            if meeting.parent_name == parent_name
        ]

# Example usage
if __name__ == "__main__":
    scheduler = MeetingScheduler()
    
    # Schedule initial meeting
    initial_date = datetime.datetime.now() + datetime.timedelta(days=7)
    meeting = scheduler.schedule_meeting(
        parent_name="John Doe",
        teacher_name="Jane Smith",
        student_name="Alice Doe",
        initial_date=initial_date
    )
    
    # Add notes and follow-ups
    scheduler.add_meeting_notes(meeting.meeting_id, "Alice is doing well in math but needs help with reading.")
    scheduler.add_follow_up_action(meeting.meeting_id, "Provide extra reading materials")
    scheduler.add_progress_update(meeting.meeting_id, "Reading", "Improved from level 2 to level 3")
    
    # Get upcoming meetings
    upcoming = scheduler.get_upcoming_meetings()
    print(f"Upcoming meetings: {len(upcoming)}")
```
