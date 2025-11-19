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
import pandas as pd
import os
from datetime import datetime

class TrainingProgramManager:
    """
    A class to manage training program data, including loading,
    processing, and saving data efficiently.
    """

    def __init__(self, data_file: str):
        """
        Initializes the TrainingProgramManager with the given data file.

        Args:
            data_file (str): The path to the CSV file containing training program data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self) -> pd.DataFrame:
        """
        Loads training program data from a CSV file.

        Returns:
            pd.DataFrame: A DataFrame containing the training program data.
        """
        try:
            if not os.path.exists(self.data_file):
                raise FileNotFoundError(f"The file {self.data_file} does not exist.")
            data = pd.read_csv(self.data_file)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred while loading data: {e}")
            return pd.DataFrame()  # Return empty DataFrame on failure

    def save_data(self):
        """
        Saves the current DataFrame back to the CSV file.
        """
        try:
            self.data.to_csv(self.data_file, index=False)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

    def add_training_program(self, program_name: str, date: str, duration: int):
        """
        Adds a new training program to the data.

        Args:
            program_name (str): The name of the training program.
            date (str): The date of the training program in YYYY-MM-DD format.
            duration (int): The duration of the training program in hours.
        """
        try:
            new_program = {
                'Program Name': program_name,
                'Date': datetime.strptime(date, "%Y-%m-%d"),
                'Duration (hours)': duration
            }
            self.data = self.data.append(new_program, ignore_index=True)
            print(f"Added new training program: {new_program}")
        except Exception as e:
            print(f"An error occurred while adding the training program: {e}")

    def get_upcoming_programs(self):
        """
        Retrieves upcoming training programs based on the current date.

        Returns:
            pd.DataFrame: A DataFrame containing upcoming training programs.
        """
        try:
            today = datetime.now()
            upcoming = self.data[self.data['Date'] > today]
            print("Retrieved upcoming training programs.")
            return upcoming
        except Exception as e:
            print(f"An error occurred while retrieving upcoming programs: {e}")
            return pd.DataFrame()  # Return empty DataFrame on failure

    def update_program_duration(self, program_name: str, new_duration: int):
        """
        Updates the duration of an existing training program.

        Args:
            program_name (str): The name of the training program to update.
            new_duration (int): The new duration for the training program in hours.
        """
        try:
            self.data.loc[self.data['Program Name'] == program_name, 'Duration (hours)'] = new_duration
            print(f"Updated duration for {program_name} to {new_duration} hours.")
        except Exception as e:
            print(f"An error occurred while updating program duration: {e}")

if __name__ == "__main__":
    # Example of how to use the TrainingProgramManager
    manager = TrainingProgramManager('training_programs.csv')
    manager.add_training_program('Python Fundamentals', '2023-12-01', 4)
    manager.update_program_duration('Python Fundamentals', 5)
    upcoming_programs = manager.get_upcoming_programs()
    print(upcoming_programs)
    manager.save_data()
```
