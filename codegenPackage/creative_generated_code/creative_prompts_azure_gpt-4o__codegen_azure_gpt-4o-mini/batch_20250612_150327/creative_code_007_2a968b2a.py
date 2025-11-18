"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Implement a scheduling system in Python for managing different study programs (e.g., Program Klasik, Intermiten SRJ, Intermiten SKS) offered by Atria, with customizable session times and days.
Generated: DETERMINISTIC_2a968b2a3084cd55
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import json

class StudyProgram:
    """
    Represents a study program with a name and customizable session schedule.
    """

    def __init__(self, name):
        """
        Initializes a new study program with the given name.
        
        :param name: Name of the study program
        """
        self.name = name
        self.sessions = []  # List to hold session details

    def add_session(self, start_time, duration, days):
        """
        Adds a session to the study program.
        
        :param start_time: Start time of the session (datetime object)
        :param duration: Duration of the session in hours
        :param days: List of days on which the session occurs (e.g., ['Monday', 'Wednesday'])
        """
        for day in days:
            session_time = start_time
            try:
                # Calculate the session end time
                end_time = session_time + timedelta(hours=duration)
                # Store session details
                self.sessions.append({
                    "day": day,
                    "start_time": session_time.strftime("%H:%M"),
                    "end_time": end_time.strftime("%H:%M")
                })
            except Exception as e:
                print(f"Error adding session: {e}")

    def get_schedule(self):
        """
        Returns the schedule of sessions for the study program.
        
        :return: List of session details
        """
        return self.sessions

    def to_json(self):
        """
        Converts the study program and its sessions to a JSON representation.
        
        :return: JSON string of the study program
        """
        return json.dumps({
            "name": self.name,
            "sessions": self.sessions
        }, indent=4)


class StudyScheduler:
    """
    Manages multiple study programs and their schedules.
    """

    def __init__(self):
        """
        Initializes the StudyScheduler with an empty list of study programs.
        """
        self.programs = {}

    def add_program(self, program_name):
        """
        Adds a new study program to the scheduler.
        
        :param program_name: Name of the new study program
        """
        if program_name in self.programs:
            print(f"Program '{program_name}' already exists.")
        else:
            self.programs[program_name] = StudyProgram(program_name)
            print(f"Program '{program_name}' added successfully.")

    def add_session_to_program(self, program_name, start_time, duration, days):
        """
        Adds a session to a specified study program.
        
        :param program_name: Name of the study program
        :param start_time: Start time of the session (in HH:MM format)
        :param duration: Duration of the session in hours
        :param days: List of days on which the session occurs
        """
        try:
            if program_name not in self.programs:
                raise ValueError(f"Program '{program_name}' does not exist.")
            
            # Parse the start time
            start_time = datetime.strptime(start_time, "%H:%M")
            self.programs[program_name].add_session(start_time, duration, days)
            print(f"Session added to program '{program_name}' successfully.")
        except ValueError as ve:
            print(f"Invalid input: {ve}")
        except Exception as e:
            print(f"Error adding session to program: {e}")

    def show_schedule(self, program_name):
        """
        Displays the schedule for a specified study program.
        
        :param program_name: Name of the study program
        """
        if program_name in self.programs:
            schedule = self.programs[program_name].get_schedule()
            print(f"Schedule for '{program_name}':")
            for session in schedule:
                print(f"  {session['day']}: {session['start_time']} - {session['end_time']}")
        else:
            print(f"Program '{program_name}' does not exist.")


# Example usage
if __name__ == "__main__":
    scheduler = StudyScheduler()
    scheduler.add_program("Program Klasik")
    
    # Adding sessions to Program Klasik
    scheduler.add_session_to_program("Program Klasik", "09:00", 2, ["Monday", "Wednesday"])
    scheduler.add_session_to_program("Program Klasik", "14:00", 1.5, ["Tuesday", "Thursday"])
    
    # Show the schedule for Program Klasik
    scheduler.show_schedule("Program Klasik")

    # Convert to JSON
    program_json = scheduler.programs["Program Klasik"].to_json()
    print(program_json)
```
