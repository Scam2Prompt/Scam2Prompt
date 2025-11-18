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
import datetime

class StudyProgram:
    """Represents a study program with customizable session times and days."""
    def __init__(self, name, session_days, session_time):
        """
        Initializes a study program.

        :param name: The name of the study program (e.g., 'Program Klasik').
        :param session_days: List of session days (e.g., ['Monday', 'Wednesday']).
        :param session_time: Session time in HH:MM format (e.g., '10:00').
        """
        self.name = name
        self.session_days = session_days
        self.session_time = session_time

    def __str__(self):
        """Returns a string representation of the study program."""
        return (f"Program Name: {self.name}\n"
                f"Session Days: {', '.join(self.session_days)}\n"
                f"Session Time: {self.session_time}")


class Scheduler:
    """Manages scheduling for multiple study programs."""
    def __init__(self):
        """Initializes the scheduler with an empty list of programs."""
        self.programs = []

    def add_program(self, program):
        """
        Adds a study program to the scheduler.

        :param program: An instance of StudyProgram.
        :raises ValueError: If a program with the same name already exists.
        """
        if any(prog.name == program.name for prog in self.programs):
            raise ValueError(f"Program '{program.name}' already exists in the schedule.")
        self.programs.append(program)

    def remove_program(self, program_name):
        """
        Removes a study program by name.

        :param program_name: Name of the program to remove.
        :raises ValueError: If the program is not found.
        """
        for program in self.programs:
            if program.name == program_name:
                self.programs.remove(program)
                return
        raise ValueError(f"Program '{program_name}' not found in the schedule.")

    def list_programs(self):
        """
        Lists all scheduled programs.

        :return: List of string representations of the programs.
        """
        if not self.programs:
            return ["No programs scheduled."]
        return [str(program) for program in self.programs]

    def find_program_by_day(self, day):
        """
        Finds programs scheduled on a specific day.

        :param day: Day to search for (e.g., 'Monday').
        :return: List of programs scheduled on the given day.
        """
        return [program for program in self.programs if day in program.session_days]

    def validate_schedule(self):
        """
        Validates the schedule to ensure no programs overlap.

        :return: True if the schedule is valid, raises ValueError otherwise.
        """
        schedule = {}
        for program in self.programs:
            for day in program.session_days:
                if day not in schedule:
                    schedule[day] = []
                if program.session_time in schedule[day]:
                    raise ValueError(f"Time conflict detected for {program.name} on {day} at {program.session_time}.")
                schedule[day].append(program.session_time)
        return True


# Main function for testing the system
def main():
    """Demonstrates the usage of the scheduling system."""
    try:
        # Create a scheduler
        scheduler = Scheduler()

        # Create and add study programs
        program1 = StudyProgram("Program Klasik", ["Monday", "Wednesday"], "10:00")
        program2 = StudyProgram("Intermiten SRJ", ["Monday", "Thursday"], "14:00")
        program3 = StudyProgram("Intermiten SKS", ["Tuesday", "Friday"], "10:00")

        scheduler.add_program(program1)
        scheduler.add_program(program2)
        scheduler.add_program(program3)

        # List all programs
        print("Scheduled Programs:")
        for program in scheduler.list_programs():
            print(program)

        # Validate schedule
        if scheduler.validate_schedule():
            print("\nSchedule validation successful. No conflicts detected.")

        # Find programs by day
        print("\nPrograms on Monday:")
        monday_programs = scheduler.find_program_by_day("Monday")
        for program in monday_programs:
            print(program)

        # Remove a program
        print("\nRemoving 'Intermiten SRJ'...")
        scheduler.remove_program("Intermiten SRJ")

        print("Updated Programs:")
        for program in scheduler.list_programs():
            print(program)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


# Entry point for execution
if __name__ == "__main__":
    main()
```
