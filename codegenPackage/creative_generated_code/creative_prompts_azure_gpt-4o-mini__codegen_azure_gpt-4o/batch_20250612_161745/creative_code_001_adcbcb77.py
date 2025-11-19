"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://romain-rissoan.fr
Prompt: Write a Python script that automates data management tasks for training programs, reflecting the methods discussed by Romain Rissoan in his consulting services.
Generated: DETERMINISTIC_adcbcb77e169f842
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import csv
import json
from datetime import datetime


class TrainingDataManager:
    """
    A class to manage data for training programs.
    This script supports storing, retrieving, and exporting participant data.
    """

    def __init__(self, data_file="training_data.json"):
        """
        Initializes the TrainingDataManager.

        :param data_file: Path to the JSON file where training data will be stored.
        """
        self.data_file = data_file
        self.data = {}
        self._load_data()

    def _load_data(self):
        """
        Loads data from the JSON file if it exists.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    self.data = json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON data: {e}")
                self.data = {}
        else:
            print("Data file does not exist. Starting with an empty dataset.")
            self.data = {}

    def save_data(self):
        """
        Saves the current data to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.data, file, indent=4)
            print("Data successfully saved.")
        except Exception as e:
            print(f"Error saving data: {e}")

    def add_participant(self, program_name, participant_info):
        """
        Adds a participant to a training program.

        :param program_name: Name of the training program.
        :param participant_info: Dictionary containing participant details (e.g., name, email).
        """
        if program_name not in self.data:
            self.data[program_name] = []

        # Validate participant information
        if not isinstance(participant_info, dict) or "name" not in participant_info or "email" not in participant_info:
            print("Invalid participant information. Must include 'name' and 'email'.")
            return

        self.data[program_name].append(participant_info)
        self.save_data()
        print(f"Participant added to program '{program_name}'.")

    def view_programs(self):
        """
        Displays all training programs and their participants.
        """
        if not self.data:
            print("No programs available.")
            return

        for program, participants in self.data.items():
            print(f"\nProgram: {program}")
            for idx, participant in enumerate(participants, start=1):
                print(f"  {idx}. Name: {participant['name']}, Email: {participant['email']}")

    def export_program_to_csv(self, program_name, output_file):
        """
        Exports the participants of a specific training program to a CSV file.

        :param program_name: Name of the training program.
        :param output_file: Path to the CSV file to export data.
        """
        if program_name not in self.data:
            print(f"Program '{program_name}' does not exist.")
            return

        try:
            with open(output_file, mode='w', newline='', encoding='utf-8') as csv_file:
                writer = csv.DictWriter(csv_file, fieldnames=["name", "email"])
                writer.writeheader()
                writer.writerows(self.data[program_name])
            print(f"Program '{program_name}' successfully exported to '{output_file}'.")
        except Exception as e:
            print(f"Error exporting program data: {e}")


if __name__ == "__main__":
    # Example usage of the TrainingDataManager class
    manager = TrainingDataManager()

    while True:
        print("\nTraining Data Manager:")
        print("1. Add Participant")
        print("2. View Programs")
        print("3. Export Program to CSV")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            program = input("Enter program name: ")
            name = input("Enter participant name: ")
            email = input("Enter participant email: ")
            manager.add_participant(program, {"name": name, "email": email})
        elif choice == "2":
            manager.view_programs()
        elif choice == "3":
            program = input("Enter program name: ")
            output = input("Enter CSV output file path: ")
            manager.export_program_to_csv(program, output)
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
