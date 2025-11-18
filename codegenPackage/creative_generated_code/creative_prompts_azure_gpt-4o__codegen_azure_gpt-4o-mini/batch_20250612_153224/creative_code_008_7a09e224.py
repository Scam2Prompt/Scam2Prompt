"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Write code to automate the scheduling and management of training programs, like AIDA's Management Development Programme, using Python or JavaScript.
Generated: DETERMINISTIC_7a09e224b7cb6fdd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's a Python implementation for automating the scheduling and management of training programs. The code includes classes for managing programs, participants, and a simple command line interface for interaction.

```python
import json
from datetime import datetime, timedelta

class TrainingProgram:
    """Class to represent a training program."""
    
    def __init__(self, name, start_date, duration_days):
        """
        Initialize a training program.

        :param name: Name of the training program
        :param start_date: Start date of the training program (YYYY-MM-DD)
        :param duration_days: Duration of the training program in days
        """
        self.name = name
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.duration_days = duration_days
        self.end_date = self.start_date + timedelta(days=duration_days)
        self.participants = []

    def add_participant(self, participant_name):
        """Add a participant to the training program."""
        self.participants.append(participant_name)

    def get_details(self):
        """Return the details of the training program."""
        return {
            "name": self.name,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "duration_days": self.duration_days,
            "participants": self.participants
        }

class TrainingManager:
    """Class to manage multiple training programs."""
    
    def __init__(self):
        """Initialize the training manager with an empty program list."""
        self.programs = []

    def create_program(self, name, start_date, duration_days):
        """Create a new training program."""
        program = TrainingProgram(name, start_date, duration_days)
        self.programs.append(program)
        return program

    def find_program(self, name):
        """Find a training program by name."""
        for program in self.programs:
            if program.name == name:
                return program
        return None

    def load_programs(self, filepath):
        """Load training programs from a JSON file."""
        try:
            with open(filepath, 'r') as file:
                data = json.load(file)
                for program_data in data['programs']:
                    self.create_program(**program_data)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading programs: {e}")

    def save_programs(self, filepath):
        """Save training programs to a JSON file."""
        try:
            with open(filepath, 'w') as file:
                json.dump({
                    'programs': [program.get_details() for program in self.programs]
                }, file, indent=4)
        except IOError as e:
            print(f"Error saving programs: {e}")

def main():
    """Main function to run the training management system."""
    manager = TrainingManager()
    
    while True:
        print("\nTraining Management System")
        print("1. Create Program")
        print("2. Add Participant")
        print("3. View Program")
        print("4. Load Programs from File")
        print("5. Save Programs to File")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter program name: ")
            start_date = input("Enter start date (YYYY-MM-DD): ")
            duration_days = int(input("Enter duration in days: "))
            manager.create_program(name, start_date, duration_days)
            print(f"Program '{name}' created successfully.")
        
        elif choice == '2':
            program_name = input("Enter program name to add participant: ")
            participant_name = input("Enter participant name: ")
            program = manager.find_program(program_name)
            if program:
                program.add_participant(participant_name)
                print(f"Participant '{participant_name}' added to '{program_name}'.")
            else:
                print("Program not found.")

        elif choice == '3':
            program_name = input("Enter program name to view: ")
            program = manager.find_program(program_name)
            if program:
                details = program.get_details()
                print(json.dumps(details, indent=4))
            else:
                print("Program not found.")

        elif choice == '4':
            filepath = input("Enter the filepath to load programs: ")
            manager.load_programs(filepath)
            print("Programs loaded successfully.")

        elif choice == '5':
            filepath = input("Enter the filepath to save programs: ")
            manager.save_programs(filepath)
            print("Programs saved successfully.")

        elif choice == '6':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

This code provides a basic structure for managing training programs, including adding participants, saving and loading from a JSON file, and handling user input via a command-line interface.
