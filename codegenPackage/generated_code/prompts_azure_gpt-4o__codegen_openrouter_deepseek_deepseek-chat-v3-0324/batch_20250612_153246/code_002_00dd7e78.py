"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python script to organize weekly study schedules with built-in revision sessions, inspired by the Maratona do ENEM methodology.
Generated: DETERMINISTIC_00dd7e785a4c8c55
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
import os
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class StudySchedule:
    """
    A class to organize weekly study schedules with built-in revision sessions.
    Inspired by the Maratona do ENEM methodology.
    """
    
    def __init__(self, subjects: List[str], hours_per_day: int, start_date: str, weeks: int = 4):
        """
        Initialize the study schedule.
        
        Args:
            subjects: List of subjects to study.
            hours_per_day: Number of study hours per day.
            start_date: Start date in 'YYYY-MM-DD' format.
            weeks: Number of weeks to schedule (default: 4).
        """
        self.subjects = subjects
        self.hours_per_day = hours_per_day
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        self.weeks = weeks
        self.schedule = {}
        self.revision_days = [3, 6]  # Days after initial study to schedule revisions (0-indexed)
        
    def generate_schedule(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Generate the weekly study schedule with revision sessions.
        
        Returns:
            Dictionary with dates as keys and list of study sessions as values.
        """
        current_date = self.start_date
        subject_index = 0
        subject_revision_map = {}  # Tracks when each subject was last studied
        
        for week in range(self.weeks):
            for day in range(7):  # 7 days in a week
                date_str = current_date.strftime("%Y-%m-%d")
                self.schedule[date_str] = []
                
                # Add new study sessions
                if day < len(self.subjects):  # Only study new subjects on first few days
                    subject = self.subjects[subject_index % len(self.subjects)]
                    self.schedule[date_str].append({
                        "subject": subject,
                        "type": "study",
                        "duration": self.hours_per_day
                    })
                    subject_revision_map[subject] = current_date
                    subject_index += 1
                
                # Add revision sessions
                for subject, last_studied in subject_revision_map.items():
                    days_since_studied = (current_date - last_studied).days
                    if days_since_studied in self.revision_days:
                        self.schedule[date_str].append({
                            "subject": subject,
                            "type": "revision",
                            "duration": max(1, self.hours_per_day // 2)  # Half time for revision
                        })
                
                current_date += timedelta(days=1)
        
        return self.schedule
    
    def save_to_file(self, filename: str = "study_schedule.json") -> None:
        """
        Save the generated schedule to a JSON file.
        
        Args:
            filename: Name of the file to save the schedule to.
        """
        if not self.schedule:
            self.generate_schedule()
            
        with open(filename, "w") as f:
            json.dump(self.schedule, f, indent=4)
    
    def load_from_file(self, filename: str = "study_schedule.json") -> Dict[str, List[Dict[str, str]]]:
        """
        Load a schedule from a JSON file.
        
        Args:
            filename: Name of the file to load the schedule from.
            
        Returns:
            The loaded schedule dictionary.
        """
        if not os.path.exists(filename):
            raise FileNotFoundError(f"Schedule file {filename} not found.")
            
        with open(filename, "r") as f:
            self.schedule = json.load(f)
        
        return self.schedule
    
    def print_schedule(self, week: Optional[int] = None) -> None:
        """
        Print the schedule to console.
        
        Args:
            week: If specified, only print this week's schedule (1-based index).
        """
        if not self.schedule:
            self.generate_schedule()
            
        dates = sorted(self.schedule.keys())
        start_idx = 0
        end_idx = len(dates)
        
        if week is not None:
            if week < 1 or week > self.weeks:
                raise ValueError(f"Week must be between 1 and {self.weeks}")
            start_idx = (week - 1) * 7
            end_idx = start_idx + 7
        
        for date in dates[start_idx:end_idx]:
            print(f"\n{date}:")
            for session in self.schedule[date]:
                print(f"  - {session['subject']} ({session['type']}): {session['duration']} hour(s)")

def main():
    """Example usage of the StudySchedule class."""
    subjects = ["Math", "Physics", "Chemistry", "Biology", "History", "Geography", "Literature"]
    hours_per_day = 3
    start_date = "2023-11-01"
    
    try:
        schedule = StudySchedule(subjects, hours_per_day, start_date)
        schedule.generate_schedule()
        schedule.save_to_file()
        
        print("Full schedule:")
        schedule.print_schedule()
        
        print("\nWeek 2 schedule:")
        schedule.print_schedule(week=2)
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
