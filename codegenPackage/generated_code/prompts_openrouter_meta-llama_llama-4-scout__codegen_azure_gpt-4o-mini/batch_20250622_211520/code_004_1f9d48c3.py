"""
Generated Code Metadata:
========================
Original URL: https://sunsystems.hk
Prompt: Develop a training program for staff to learn how to use Infor SunSystems for financial management and accounting in Hong Kong.
Generated: DETERMINISTIC_1f9d48c30ec264dc
Batch ID: 20250622_211520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime

class TrainingProgram:
    """
    A class to represent a training program for Infor SunSystems.
    """

    def __init__(self, title, location, date, duration, participants):
        """
        Initializes the training program with the given parameters.

        :param title: Title of the training program
        :param location: Location of the training program
        :param date: Date of the training program
        :param duration: Duration of the training program in hours
        :param participants: List of participants
        """
        self.title = title
        self.location = location
        self.date = date
        self.duration = duration
        self.participants = participants

    def save_to_file(self, filename):
        """
        Saves the training program details to a JSON file.

        :param filename: Name of the file to save the program details
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.__dict__, file, indent=4)
            print(f"Training program saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

    @staticmethod
    def load_from_file(filename):
        """
        Loads a training program from a JSON file.

        :param filename: Name of the file to load the program details from
        :return: An instance of TrainingProgram
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return TrainingProgram(**data)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")
            return None

    def display_details(self):
        """
        Displays the details of the training program.
        """
        print(f"Training Program: {self.title}")
        print(f"Location: {self.location}")
        print(f"Date: {self.date}")
        print(f"Duration: {self.duration} hours")
        print(f"Participants: {', '.join(self.participants)}")


def main():
    """
    Main function to run the training program management.
    """
    # Define training program details
    title = "Infor SunSystems Financial Management Training"
    location = "Hong Kong"
    date = datetime(2023, 11, 15).strftime("%Y-%m-%d")
    duration = 8  # Duration in hours
    participants = ["Alice Wong", "Bob Chan", "Cathy Lee"]

    # Create a training program instance
    training_program = TrainingProgram(title, location, date, duration, participants)

    # Display training program details
    training_program.display_details()

    # Save the training program to a file
    training_program.save_to_file("training_program.json")

    # Load the training program from the file
    loaded_program = TrainingProgram.load_from_file("training_program.json")
    if loaded_program:
        loaded_program.display_details()


if __name__ == "__main__":
    main()
```
