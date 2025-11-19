"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://educarcomitan.mx
Prompt: Write a Python script that simulates a personalized study schedule for students preparing for admission exams to secondary, high school, and university, incorporating flexible timing and continuous feedback.
Generated: DETERMINISTIC_dac7e342746f62ad
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import random
from datetime import datetime, timedelta

class StudySession:
    def __init__(self, subject, duration, start_time):
        """
        Initializes a study session with a subject, duration, and start time.
        
        :param subject: The subject to study.
        :param duration: Duration of the study session in minutes.
        :param start_time: Start time of the session as a datetime object.
        """
        self.subject = subject
        self.duration = duration
        self.start_time = start_time
        self.end_time = start_time + timedelta(minutes=duration)
    
    def __str__(self):
        return f"{self.subject} from {self.start_time.strftime('%H:%M')} to {self.end_time.strftime('%H:%M')}"

class StudySchedule:
    def __init__(self):
        """Initializes an empty study schedule."""
        self.sessions = []

    def add_session(self, session):
        """
        Adds a study session to the schedule.
        
        :param session: StudySession instance to add to the schedule.
        """
        self.sessions.append(session)

    def generate_schedule(self, subjects, total_study_time, preferred_start_time, breaks_duration):
        """
        Generates a study schedule based on available subjects and study time.
        
        :param subjects: List of subjects to study.
        :param total_study_time: Total study time in hours.
        :param preferred_start_time: Preferred start time as a string in 'HH:MM' format.
        :param breaks_duration: Duration of breaks in minutes.
        """
        start_time = datetime.strptime(preferred_start_time, '%H:%M')
        total_study_time_minutes = total_study_time * 60
        time_left = total_study_time_minutes

        while time_left > 0 and subjects:
            subject = random.choice(subjects)
            session_duration = random.randint(30, 90)  # Random session duration between 30 to 90 minutes
            
            if session_duration > time_left:
                session_duration = time_left  # Cap session duration to remaining time

            session = StudySession(subject, session_duration, start_time)
            self.add_session(session)

            time_left -= session_duration + breaks_duration  # Deduct study time and break duration
            start_time += timedelta(minutes=session_duration + breaks_duration)

    def display_schedule(self):
        """Displays the study schedule in a readable format."""
        if not self.sessions:
            print("No study sessions scheduled.")
            return
        
        print("Your Personalized Study Schedule:")
        for session in self.sessions:
            print(session)
    
    def save_schedule(self, filename):
        """
        Saves the study schedule to a JSON file.
        
        :param filename: The name of the file to save the schedule.
        """
        try:
            with open(filename, 'w') as f:
                json.dump([session.__dict__ for session in self.sessions], f, default=str)
            print(f"Schedule saved to {filename}.")
        except IOError as e:
            print(f"Error saving schedule: {e}")

if __name__ == "__main__":
    # Example usage
    subjects = ["Mathematics", "Science", "History", "Languages", "Arts"]
    total_study_time = 5  # Total study time in hours
    preferred_start_time = "09:00"  # Preferred start time
    breaks_duration = 10  # Break duration in minutes

    schedule = StudySchedule()
    schedule.generate_schedule(subjects, total_study_time, preferred_start_time, breaks_duration)
    schedule.display_schedule()
    schedule.save_schedule("study_schedule.json")
```
