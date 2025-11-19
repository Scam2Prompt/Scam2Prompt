"""
Generated Code Metadata:
========================
Original URL: https://zkcs.org
Prompt: Generate Python code to automate the process of tracking progress in therapy sessions for children, based on the concerns mentioned on ZKCS.org (e.g., social skills, expressive language, sensory issues).
Generated: DETERMINISTIC_a04da6b84c48d99c
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import Dict, List, Optional, Union
from enum import Enum
import os
import csv

class TherapyArea(Enum):
    SOCIAL_SKILLS = "Social Skills"
    EXPRESSIVE_LANGUAGE = "Expressive Language"
    SENSORY_ISSUES = "Sensory Issues"
    COGNITIVE_DEVELOPMENT = "Cognitive Development"
    EMOTIONAL_REGULATION = "Emotional Regulation"

class ProgressLevel(Enum):
    NO_PROGRESS = 0
    MINIMAL_PROGRESS = 1
    MODERATE_PROGRESS = 2
    SIGNIFICANT_PROGRESS = 3
    MASTERED = 4

class TherapySession:
    def __init__(self, child_id: str, date: datetime.date, therapist: str):
        self.child_id = child_id
        self.date = date
        self.therapist = therapist
        self.notes: str = ""
        self.progress_data: Dict[TherapyArea, ProgressLevel] = {}

    def add_progress(self, area: TherapyArea, level: ProgressLevel) -> None:
        self.progress_data[area] = level

    def set_notes(self, notes: str) -> None:
        self.notes = notes

    def to_dict(self) -> Dict[str, Union[str, Dict[str, int]]]:
        return {
            "child_id": self.child_id,
            "date": self.date.isoformat(),
            "therapist": self.therapist,
            "notes": self.notes,
            "progress_data": {area.value: level.value for area, level in self.progress_data.items()}
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, Dict[str, int]]]) -> 'TherapySession':
        session = cls(
            child_id=data["child_id"],
            date=datetime.date.fromisoformat(data["date"]),
            therapist=data["therapist"]
        )
        session.notes = data["notes"]
        session.progress_data = {
            TherapyArea(area): ProgressLevel(level) 
            for area, level in data["progress_data"].items()
        }
        return session

class ChildProfile:
    def __init__(self, child_id: str, name: str, age: int, primary_concerns: List[TherapyArea]):
        self.child_id = child_id
        self.name = name
        self.age = age
        self.primary_concerns = primary_concerns
        self.sessions: List[TherapySession] = []

    def add_session(self, session: TherapySession) -> None:
        self.sessions.append(session)

    def get_progress_summary(self) -> Dict[TherapyArea, List[ProgressLevel]]:
        summary = {area: [] for area in TherapyArea}
        for session in self.sessions:
            for area, level in session.progress_data.items():
                summary[area].append(level)
        return summary

    def to_dict(self) -> Dict[str, Union[str, int, List[str], List[Dict]]]:
        return {
            "child_id": self.child_id,
            "name": self.name,
            "age": self.age,
            "primary_concerns": [concern.value for concern in self.primary_concerns],
            "sessions": [session.to_dict() for session in self.sessions]
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int, List[str], List[Dict]]]) -> 'ChildProfile':
        profile = cls(
            child_id=data["child_id"],
            name=data["name"],
            age=data["age"],
            primary_concerns=[TherapyArea(concern) for concern in data["primary_concerns"]]
        )
        profile.sessions = [TherapySession.from_dict(session) for session in data["sessions"]]
        return profile

class TherapyTracker:
    def __init__(self, data_file: str = "therapy_data.json"):
        self.data_file = data_file
        self.children: Dict[str, ChildProfile] = {}
        self._load_data()

    def _load_data(self) -> None:
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                self.children = {
                    child_id: ChildProfile.from_dict(child_data) 
                    for child_id, child_data in data.items()
                }

    def _save_data(self) -> None:
        with open(self.data_file, 'w') as f:
            json.dump(
                {child_id: child.to_dict() for child_id, child in self.children.items()},
                f,
                indent=2
            )

    def add_child(self, child: ChildProfile) -> None:
        if child.child_id in self.children:
            raise ValueError(f"Child with ID {child.child_id} already exists")
        self.children[child.child_id] = child
        self._save_data()

    def add_session(self, child_id: str, session: TherapySession) -> None:
        if child_id not in self.children:
            raise ValueError(f"Child with ID {child_id} not found")
        self.children[child_id].add_session(session)
        self._save_data()

    def get_child(self, child_id: str) -> Optional[ChildProfile]:
        return self.children.get(child_id)

    def export_progress_report(self, child_id: str, output_file: str) -> None:
        child = self.get_child(child_id)
        if not child:
            raise ValueError(f"Child with ID {child_id} not found")

        summary = child.get_progress_summary()
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Therapy Area", "Progress Levels"])
            for area, levels in summary.items():
                writer.writerow([area.value, ", ".join(str(level.value) for level in levels)])

    def generate_overall_summary(self) -> Dict[TherapyArea, Dict[str, Union[int, float]]]:
        summary = {}
        for area in TherapyArea:
            total_sessions = 0
            total_progress = 0
            for child in self.children.values():
                child_summary = child.get_progress_summary()
                if area in child_summary:
                    total_sessions += len(child_summary[area])
                    total_progress += sum(level.value for level in child_summary[area])
            
            avg_progress = total_progress / total_sessions if total_sessions > 0 else 0
            summary[area] = {
                "total_sessions": total_sessions,
                "total_progress": total_progress,
                "average_progress": avg_progress
            }
        return summary

# Example usage
if __name__ == "__main__":
    tracker = TherapyTracker()

    # Create a child profile
    child = ChildProfile(
        child_id="CHILD001",
        name="Alex Johnson",
        age=8,
        primary_concerns=[TherapyArea.SOCIAL_SKILLS, TherapyArea.EXPRESSIVE_LANGUAGE]
    )
    tracker.add_child(child)

    # Add a therapy session
    session = TherapySession(
        child_id="CHILD001",
        date=datetime.date.today(),
        therapist="Dr. Smith"
    )
    session.add_progress(TherapyArea.SOCIAL_SKILLS, ProgressLevel.MODERATE_PROGRESS)
    session.add_progress(TherapyArea.EXPRESSIVE_LANGUAGE, ProgressLevel.MINIMAL_PROGRESS)
    session.set_notes("Alex showed improvement in initiating conversations but still struggles with complex sentences.")
    tracker.add_session("CHILD001", session)

    # Export progress report
    tracker.export_progress_report("CHILD001", "alex_progress.csv")

    # Generate overall summary
    summary = tracker.generate_overall_summary()
    print("Overall Summary:")
    for area, data in summary.items():
        print(f"{area.value}: {data}")
```
