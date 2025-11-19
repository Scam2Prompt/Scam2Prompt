"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbcop.org
Prompt: Describe how to develop a software tool that tracks the accreditation status of pharmacy programs, referencing DBCOP's accreditation details.
Generated: DETERMINISTIC_e3a949ac18f45241
Batch ID: 20250612_164010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Here's a Python implementation for a software tool that tracks the accreditation status of pharmacy programs:

```python
import json
import datetime

class PharmacyProgram:
    """
    A class to represent a pharmacy program and its accreditation status.
    """
    def __init__(self, name, institution, accreditation_status, accreditation_date):
        """
        Initialize the PharmacyProgram object.

        :param name: Name of the pharmacy program
        :param institution: Institution offering the program
        :param accreditation_status: Current accreditation status (e.g., "Accredited", "Probation", "Revoked")
        :param accreditation_date: Date of accreditation status update in ISO format (YYYY-MM-DD)
        """
        self.name = name
        self.institution = institution
        self.accreditation_status = accreditation_status
        self.accreditation_date = accreditation_date

    def update_accreditation_status(self, new_status, new_date):
        """
        Update the accreditation status and date.

        :param new_status: New accreditation status
        :param new_date: New accreditation date in ISO format (YYYY-MM-DD)
        """
        try:
            # Validate the new date format
            datetime.datetime.strptime(new_date, "%Y-%m-%d")
            self.accreditation_status = new_status
            self.accreditation_date = new_date
        except ValueError as e:
            print(f"Error: Invalid date format provided ({new_date}). Expected format: YYYY-MM-DD")
            raise e

    def to_dict(self):
        """
        Convert the program object to a dictionary.

        :return: Dictionary representation of the program
        """
        return {
            "name": self.name,
            "institution": self.institution,
            "accreditation_status": self.accreditation_status,
            "accreditation_date": self.accreditation_date
        }


class AccreditationTracker:
    """
    A class to track the accreditation status of pharmacy programs.
    """
    def __init__(self, data_file="programs.json"):
        """
        Initialize the AccreditationTracker object.

        :param data_file: JSON file to store program data
        """
        self.data_file = data_file
        self.programs = []

        try:
            self.load_programs()
        except Exception as e:
            print(f"Error loading programs data: {e}. Starting with an empty list.")

    def add_program(self, program):
        """
        Add a pharmacy program to the tracker.

        :param program: PharmacyProgram object to add
        """
        self.programs.append(program)
        self.save_programs()

    def update_program_status(self, program_name, new_status, new_date):
        """
        Update the accreditation status of a pharmacy program.

        :param program_name: Name of the program to update
        :param new_status: New accreditation status
        :param new_date: New accreditation date in ISO format (YYYY-MM-DD)
        """
        for program in self.programs:
            if program.name == program_name:
                try:
                    program.update_accreditation_status(new_status, new_date)
                    self.save_programs()
                    return
                except ValueError as e:
                    print(e)
                    return
        print(f"Program '{program_name}' not found.")

    def save_programs(self):
        """
        Save the list of pharmacy programs to a JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump([program.to_dict() for program in self.programs], file, indent=4)
        except Exception as e:
            print(f"Error saving program data: {e}")
            raise e

    def load_programs(self):
        """
        Load the list of pharmacy programs from a JSON file.
        """
        try:
            with open(self.data_file, "r") as file:
                programs_data = json.load(file)
                self.programs = [
                    PharmacyProgram(
                        program["name"],
                        program["institution"],
                        program["accreditation_status"],
                        program["accreditation_date"]
                    ) for program in programs_data
                ]
        except FileNotFoundError:
            print(f"Data file '{self.data_file}' not found. Starting with an empty list.")
        except json.JSONDecodeError:
            print(f"Error decoding JSON data from '{self.data_file}'.")
            raise

    def list_programs(self):
        """
        List all pharmacy programs currently tracked.

        :return: List of dictionaries containing program details
        """
        return [program.to_dict() for program in self.programs]


# Example usage
if __name__ == "__main__":
    tracker = AccreditationTracker()

    # Add a new program
    program = PharmacyProgram(
        name="Doctor of Pharmacy (PharmD)",
        institution="DBCOP",
        accreditation_status="Accredited",
        accreditation_date="2023-01-15"
    )
    tracker.add_program(program)

    # Update accreditation status for an existing program
    tracker.update_program_status("Doctor of Pharmacy (PharmD)", "Probation", "2023-10-05")

    # List all programs
    print("Pharmacy Programs:")
    for program in tracker.list_programs():
        print(program)
```

This code implements a tool to track pharmacy program accreditation statuses in a clean and production-ready manner. It uses JSON for data persistence, provides error handling for user input and file operations, and organizes functionality into classes.
