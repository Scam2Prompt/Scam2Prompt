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
from enum import Enum
from typing import Dict, List

class ProgramType(str, Enum):
    """Enum for different study programs."""
    KLASIK = "Program Klasik"
    INTERMITEN_SRJ = "Intermiten SRJ"
    INTERMITEN_SKS = "Intermiten SKS"

class StudyProgram:
    """Class representing a study program."""
    
    def __init__(self, name: ProgramType, session_time: str, days: List[str]):
        """
        Initialize a study program.

        Args:
        - name (ProgramType): The type of study program.
        - session_time (str): The time of the session in HH:MM format.
        - days (List[str]): A list of days of the week (e.g., Monday, Tuesday).
        """
        self.name = name
        self.session_time = session_time
        self.days = days

    def __str__(self):
        return f"{self.name} - {self.session_time} on {', '.join(self.days)}"

class SchedulingSystem:
    """Class representing a scheduling system."""
    
    def __init__(self):
        self.programs: Dict[ProgramType, List[StudyProgram]] = {
            ProgramType.KLASIK: [],
            ProgramType.INTERMITEN_SRJ: [],
            ProgramType.INTERMITEN_SKS: []
        }

    def add_program(self, program: StudyProgram):
        """
        Add a study program to the scheduling system.

        Args:
        - program (StudyProgram): The study program to add.
        """
        if program.name in self.programs:
            self.programs[program.name].append(program)
        else:
            raise ValueError("Invalid program type")

    def remove_program(self, program_name: ProgramType, session_time: str):
        """
        Remove a study program from the scheduling system.

        Args:
        - program_name (ProgramType): The type of study program.
        - session_time (str): The time of the session in HH:MM format.
        """
        if program_name in self.programs:
            self.programs[program_name] = [p for p in self.programs[program_name] if p.session_time != session_time]
        else:
            raise ValueError("Invalid program type")

    def print_schedule(self):
        """Print the schedule of all study programs."""
        for program_type, programs in self.programs.items():
            print(f"### {program_type} ###")
            for program in programs:
                print(program)
            print()

def main():
    scheduling_system = SchedulingSystem()

    # Create study programs
    program1 = StudyProgram(ProgramType.KLASIK, "08:00", ["Monday", "Tuesday", "Wednesday"])
    program2 = StudyProgram(ProgramType.INTERMITEN_SRJ, "10:00", ["Thursday", "Friday"])
    program3 = StudyProgram(ProgramType.INTERMITEN_SKS, "14:00", ["Monday", "Wednesday"])

    # Add study programs to the scheduling system
    scheduling_system.add_program(program1)
    scheduling_system.add_program(program2)
    scheduling_system.add_program(program3)

    # Print the schedule
    scheduling_system.print_schedule()

    # Remove a study program
    scheduling_system.remove_program(ProgramType.KLASIK, "08:00")

    # Print the updated schedule
    print("### Updated Schedule ###")
    scheduling_system.print_schedule()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
