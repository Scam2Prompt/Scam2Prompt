"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Implement a scheduling system in Python for managing different study programs (e.g., Program Klasik, Intermiten SRJ, Intermiten SKS) offered by Atria, with customizable session times and days.
Generated: DETERMINISTIC_2a968b2a3084cd55
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
import json

class StudyProgram:
    """Class representing a study program with customizable session times and days."""
    
    def __init__(self, name, session_days, session_time):
        """
        Initialize a StudyProgram instance.

        Args:
            name (str): The name of the study program.
            session_days (list): List of days the program is scheduled (e.g., ['Monday', 'Wednesday']).
            session_time (str): The time of day the sessions occur (e.g., '14:00').
        """
        self.name = name
        self.session_days = session_days
        self.session_time = self._parse_time(session_time)
        self.sessions = self._generate_sessions()

    def _parse_time(self, session_time):
        """Parse the session time string into a datetime object."""
        try:
            return datetime.strptime(session_time, '%H:%M').time()
        except ValueError as e:
            raise ValueError(f"Invalid time format: {session_time}. Expected format: 'HH:MM'.") from e

    def _generate_sessions(self):
        """Generate a list of upcoming session dates based on the current date."""
        today = datetime.now()
        sessions = []
        for day in self.session_days:
            next_session_date = self._get_next_session_date(today, day)
            sessions.append(datetime.combine(next_session_date, self.session_time))
        return sessions

    def _get_next_session_date(self, today, day_name):
        """Get the next date for a given day of the week."""
        days_ahead = (getattr(datetime, day_name.upper()) - today.weekday() + 7) % 7
        if days_ahead == 0 and today.time() >= self.session_time:
            days_ahead = 7  # Move to next week if today is the session day and time has passed
        return today + timedelta(days=days_ahead)

    def to_dict(self):
        """Convert the study program to a dictionary for easy serialization."""
        return {
            'name': self.name,
            'session_days': self.session_days,
            'session_time': str(self.session_time),
            'sessions': [session.strftime('%Y-%m-%d %H:%M') for session in self.sessions]
        }

class Scheduler:
    """Class to manage multiple study programs."""
    
    def __init__(self):
        """Initialize the Scheduler with an empty list of study programs."""
        self.programs = []

    def add_program(self, program):
        """Add a new study program to the scheduler.

        Args:
            program (StudyProgram): The study program to add.
        """
        if not isinstance(program, StudyProgram):
            raise TypeError("Expected a StudyProgram instance.")
        self.programs.append(program)

    def save_to_file(self, filename):
        """Save the current programs to a JSON file.

        Args:
            filename (str): The name of the file to save the programs to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump([program.to_dict() for program in self.programs], file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        """Load study programs from a JSON file.

        Args:
            filename (str): The name of the file to load the programs from.
        """
        try:
            with open(filename, 'r') as file:
                programs_data = json.load(file)
                for program_data in programs_data:
                    program = StudyProgram(
                        name=program_data['name'],
                        session_days=program_data['session_days'],
                        session_time=program_data['session_time']
                    )
                    self.add_program(program)
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    scheduler = Scheduler()
    
    # Create study programs
    program_klasik = StudyProgram("Program Klasik", ["Monday", "Wednesday"], "14:00")
    program_intermiten_sjr = StudyProgram("Intermiten SRJ", ["Tuesday", "Thursday"], "16:00")
    program_intermiten_sks = StudyProgram("Intermiten SKS", ["Friday"], "10:00")
    
    # Add programs to the scheduler
    scheduler.add_program(program_klasik)
    scheduler.add_program(program_intermiten_sjr)
    scheduler.add_program(program_intermiten_sks)
    
    # Save programs to a file
    scheduler.save_to_file("study_programs.json")
    
    # Load programs from a file
    new_scheduler = Scheduler()
    new_scheduler.load_from_file("study_programs.json")
    
    # Print loaded programs
    for program in new_scheduler.programs:
        print(program.to_dict())
```
