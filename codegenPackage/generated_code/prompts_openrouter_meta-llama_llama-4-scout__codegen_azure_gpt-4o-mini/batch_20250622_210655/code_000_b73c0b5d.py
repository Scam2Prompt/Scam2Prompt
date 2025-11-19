"""
Generated Code Metadata:
========================
Original URL: https://www.getaconsulenze.it
Prompt: "Generate a Python script to manage certification programs for a training institute like Geta Consulenze, including tracking course completion and certification expiry dates."
Generated: DETERMINISTIC_b73c0b5d97ad2b26
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class CertificationProgram:
    """Class to manage certification programs for a training institute."""

    def __init__(self, program_name):
        """Initialize the certification program with a name and an empty list of participants."""
        self.program_name = program_name
        self.participants = []

    def add_participant(self, name, completion_date, expiry_duration_years):
        """Add a participant to the certification program.

        Args:
            name (str): The name of the participant.
            completion_date (str): The date of course completion in 'YYYY-MM-DD' format.
            expiry_duration_years (int): The duration in years before the certification expires.
        """
        try:
            completion_date = datetime.datetime.strptime(completion_date, '%Y-%m-%d').date()
            expiry_date = completion_date + datetime.timedelta(days=expiry_duration_years * 365)
            participant = {
                'name': name,
                'completion_date': completion_date,
                'expiry_date': expiry_date
            }
            self.participants.append(participant)
            print(f"Participant {name} added successfully.")
        except ValueError as e:
            print(f"Error adding participant: {e}")

    def check_expiry(self):
        """Check and return a list of participants whose certifications are expired."""
        expired_participants = []
        today = datetime.date.today()
        for participant in self.participants:
            if participant['expiry_date'] < today:
                expired_participants.append(participant)
        return expired_participants

    def save_to_file(self, filename):
        """Save the certification program data to a JSON file.

        Args:
            filename (str): The name of the file to save the data.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.participants, file, default=str)
            print(f"Data saved to {filename}.")
        except IOError as e:
            print(f"Error saving data to file: {e}")

    def load_from_file(self, filename):
        """Load certification program data from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.
        """
        if not os.path.exists(filename):
            print(f"File {filename} does not exist.")
            return
        
        try:
            with open(filename, 'r') as file:
                self.participants = json.load(file)
            print(f"Data loaded from {filename}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from file: {e}")

def main():
    """Main function to demonstrate the CertificationProgram class."""
    program = CertificationProgram("Python Programming Certification")

    # Example usage
    program.add_participant("Alice Smith", "2023-01-15", 2)
    program.add_participant("Bob Johnson", "2021-05-20", 1)

    # Check for expired certifications
    expired = program.check_expiry()
    if expired:
        print("Expired Certifications:")
        for participant in expired:
            print(f"{participant['name']} - Expired on {participant['expiry_date']}")
    else:
        print("No expired certifications.")

    # Save to file
    program.save_to_file("certification_data.json")

    # Load from file
    program.load_from_file("certification_data.json")

if __name__ == "__main__":
    main()
```
