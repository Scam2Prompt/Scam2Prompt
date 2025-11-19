"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Write Python code to generate a timetable for MBBS students based on the "Master Time Table for MBBS" provided by MIMSR Medical College, including clinical postings and integrated teaching modules.
Generated: DETERMINISTIC_fc9049c778015950
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import time, datetime, timedelta
from typing import List, Dict, Optional, Union

class Subject:
    """Represents a subject in the timetable."""
    def __init__(self, name: str, code: str, is_clinical: bool = False):
        self.name = name
        self.code = code
        self.is_clinical = is_clinical

class TimeSlot:
    """Represents a time slot in the timetable."""
    def __init__(self, start_time: time, end_time: time):
        self.start_time = start_time
        self.end_time = end_time

    def duration(self) -> timedelta:
        """Calculate duration of the time slot."""
        start = datetime.combine(datetime.today(), self.start_time)
        end = datetime.combine(datetime.today(), self.end_time)
        return end - start

class TimetableEntry:
    """Represents an entry in the timetable."""
    def __init__(self, day: str, time_slot: TimeSlot, subject: Subject, faculty: str, venue: str):
        self.day = day
        self.time_slot = time_slot
        self.subject = subject
        self.faculty = faculty
        self.venue = venue

class MBBSBatch:
    """Represents an MBBS batch with students."""
    def __init__(self, batch_name: str, year: int, student_count: int):
        self.batch_name = batch_name
        self.year = year
        self.student_count = student_count

class TimetableGenerator:
    """Generates timetable for MBBS students."""
    
    DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    def __init__(self):
        self.subjects = []
        self.time_slots = []
        self.batches = []
        self.timetable = {day: [] for day in self.DAYS}
        
    def load_config(self, config_file: str) -> bool:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                
            # Load subjects
            for subj in config.get("subjects", []):
                self.subjects.append(
                    Subject(
                        name=subj["name"],
                        code=subj["code"],
                        is_clinical=subj.get("is_clinical", False)
                    )
                )
                
            # Load time slots
            for slot in config.get("time_slots", []):
                self.time_slots.append(
                    TimeSlot(
                        start_time=time.fromisoformat(slot["start"]),
                        end_time=time.fromisoformat(slot["end"])
                    )
                )
                
            # Load batches
            for batch in config.get("batches", []):
                self.batches.append(
                    MBBSBatch(
                        batch_name=batch["name"],
                        year=batch["year"],
                        student_count=batch["student_count"]
                    )
                )
                
            return True
            
        except Exception as e:
            print(f"Error loading config: {e}")
            return False
    
    def generate_timetable(self) -> Dict[str, List[TimetableEntry]]:
        """Generate timetable based on loaded configuration."""
        if not self.subjects or not self.time_slots or not self.batches:
            raise ValueError("Configuration not properly loaded")
            
        # Sample timetable generation logic
        # This would be replaced with actual business rules from MIMSR Medical College
        
        # Basic structure: Morning and afternoon sessions
        morning_slots = [slot for slot in self.time_slots if slot.start_time < time(12, 0)]
        afternoon_slots = [slot for slot in self.time_slots if slot.start_time >= time(12, 0)]
        
        clinical_subjects = [subj for subj in self.subjects if subj.is_clinical]
        theory_subjects = [subj for subj in self.subjects if not subj.is_clinical]
        
        for day in self.DAYS:
            # Morning sessions - Theory
            for i, slot in enumerate(morning_slots):
                subject = theory_subjects[i % len(theory_subjects)]
                self.timetable[day].append(
                    TimetableEntry(
                        day=day,
                        time_slot=slot,
                        subject=subject,
                        faculty=f"Dr. {subject.name.split()[0]}",
                        venue="Lecture Hall 1"
                    )
                )
            
            # Afternoon sessions - Clinical postings
            if clinical_subjects and day != "Saturday":  # No clinical on Saturday
                for i, slot in enumerate(afternoon_slots):
                    subject = clinical_subjects[i % len(clinical_subjects)]
                    self.timetable[day].append(
                        TimetableEntry(
                            day=day,
                            time_slot=slot,
                            subject=subject,
                            faculty=f"Prof. {subject.name.split()[0]}",
                            venue=f"{subject.name} Ward"
                        )
                    )
            
            # Integrated teaching on Friday afternoon
            if day == "Friday" and afternoon_slots:
                self.timetable[day].append(
                    TimetableEntry(
                        day=day,
                        time_slot=afternoon_slots[0],
                        subject=Subject(name="Integrated Teaching", code="IT01", is_clinical=False),
                        faculty="Multi-disciplinary Team",
                        venue="Seminar Hall"
                    )
                )
        
        return self.timetable
    
    def export_timetable(self, output_format: str = "json", filename: str = "timetable") -> bool:
        """Export timetable to specified format."""
        if not self.timetable:
            raise ValueError("Timetable not generated")
            
        try:
            if output_format == "json":
                with open(f"{filename}.json", 'w') as f:
                    export_data = {
                        day: [
                            {
                                "day": entry.day,
                                "start_time": entry.time_slot.start_time.isoformat(),
                                "end_time": entry.time_slot.end_time.isoformat(),
                                "subject": entry.subject.name,
                                "subject_code": entry.subject.code,
                                "faculty": entry.faculty,
                                "venue": entry.venue,
                                "is_clinical": entry.subject.is_clinical
                            }
                            for entry in entries
                        ]
                        for day, entries in self.timetable.items()
                    }
                    json.dump(export_data, f, indent=2)
                    
            elif output_format == "csv":
                import csv
                with open(f"{filename}.csv", 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(["Day", "Start Time", "End Time", "Subject", "Code", "Faculty", "Venue", "Clinical"])
                    for day, entries in self.timetable.items():
                        for entry in entries:
                            writer.writerow([
                                entry.day,
                                entry.time_slot.start_time.isoformat(),
                                entry.time_slot.end_time.isoformat(),
                                entry.subject.name,
                                entry.subject.code,
                                entry.faculty,
                                entry.venue,
                                "Yes" if entry.subject.is_clinical else "No"
                            ])
            else:
                raise ValueError("Unsupported output format")
                
            return True
            
        except Exception as e:
            print(f"Error exporting timetable: {e}")
            return False

# Example usage
if __name__ == "__main__":
    generator = TimetableGenerator()
    
    # Load configuration (would typically be from a config file)
    config = {
        "subjects": [
            {"name": "Anatomy", "code": "ANA101", "is_clinical": False},
            {"name": "Physiology", "code": "PHY101", "is_clinical": False},
            {"name": "Biochemistry", "code": "BCH101", "is_clinical": False},
            {"name": "Medicine", "code": "MED201", "is_clinical": True},
            {"name": "Surgery", "code": "SUR201", "is_clinical": True},
            {"name": "Pediatrics", "code": "PED201", "is_clinical": True}
        ],
        "time_slots": [
            {"start": "08:00", "end": "09:00"},
            {"start": "09:00", "end": "10:00"},
            {"start": "10:30", "end": "11:30"},
            {"start": "11:30", "end": "12:30"},
            {"start": "14:00", "end": "15:00"},
            {"start": "15:00", "end": "16:00"}
        ],
        "batches": [
            {"name": "Batch A", "year": 1, "student_count": 150},
            {"name": "Batch B", "year": 2, "student_count": 150}
        ]
    }
    
    # Save config to temporary file for loading
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(config, f)
        config_file = f.name
    
    try:
        if generator.load_config(config_file):
            timetable = generator.generate_t
