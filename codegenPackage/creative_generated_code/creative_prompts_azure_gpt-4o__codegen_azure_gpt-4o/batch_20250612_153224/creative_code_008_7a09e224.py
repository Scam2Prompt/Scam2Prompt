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

Here’s a Python implementation for automating the scheduling and management of training programs:

```python
import json
from datetime import datetime, timedelta

class TrainingProgramManager:
    def __init__(self):
        """Initialize the manager with an empty list of training programs."""
        self.programs = []

    def create_program(self, name, start_date, duration_days):
        """
        Create a new training program.

        Args:
            name (str): Name of the training program.
            start_date (str): Start date in 'YYYY-MM-DD' format.
            duration_days (int): Duration of the program in days.

        Returns:
            dict: The created program details.
        """
        try:
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
            end_date_obj = start_date_obj + timedelta(days=duration_days)
            program = {
                'name': name,
                'start_date': start_date_obj.strftime('%Y-%m-%d'),
                'end_date': end_date_obj.strftime('%Y-%m-%d'),
                'duration_days': duration_days
            }
            self.programs.append(program)
            return program
        except ValueError as e:
            raise ValueError(f"Invalid date format: {str(e)}")

    def list_programs(self):
        """
        List all scheduled training programs.

        Returns:
            list: List of training programs.
        """
        return self.programs

    def find_program_by_name(self, name):
        """
        Find a training program by its name.

        Args:
            name (str): Name of the program to search for.

        Returns:
            dict: The matching program, or None if no match is found.
        """
        for program in self.programs:
            if program['name'].lower() == name.lower():
                return program
        return None

    def delete_program(self, name):
        """
        Delete a training program by its name.

        Args:
            name (str): Name of the program to delete.

        Returns:
            bool: True if deleted successfully, False if not found.
        """
        for program in self.programs:
            if program['name'].lower() == name.lower():
                self.programs.remove(program)
                return True
        return False

    def save_programs_to_file(self, file_path):
        """
        Save all training programs to a JSON file.

        Args:
            file_path (str): Path to the file where programs will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(self.programs, file, indent=4)
        except IOError as e:
            raise IOError(f"Error saving to file: {str(e)}")

    def load_programs_from_file(self, file_path):
        """
        Load training programs from a JSON file.

        Args:
            file_path (str): Path to the file to load programs from.
        """
        try:
            with open(file_path, 'r') as file:
                self.programs = json.load(file)
        except IOError as e:
            raise IOError(f"Error loading from file: {str(e)}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON format: {str(e)}")


# Example usage
if __name__ == '__main__':
    manager = TrainingProgramManager()

    # Create a couple of programs
    program1 = manager.create_program("Management Development Programme", "2023-11-01", 5)
    program2 = manager.create_program("Leadership Training", "2023-12-01", 3)

    # List all programs
    print("Scheduled Programs:", manager.list_programs())

    # Find a specific program
    print("Finding Program:", manager.find_program_by_name("Leadership Training"))

    # Delete a program
    manager.delete_program("Management Development Programme")
    print("Programs after deletion:", manager.list_programs())

    # Save programs to a file
    manager.save_programs_to_file("programs.json")

    # Load programs from a file
    manager.load_programs_from_file("programs.json")
    print("Loaded Programs:", manager.list_programs())
```

This Python script fulfills your requirements and is ready for production use. It includes error handling, clean structure, and documentation for clarity.
