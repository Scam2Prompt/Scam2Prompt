"""
Generated Code Metadata:
========================
Original URL: https://romain-rissoan.fr
Prompt: Write a Python script that automates data management tasks for training programs, reflecting the methods discussed by Romain Rissoan in his consulting services.
Generated: DETERMINISTIC_adcbcb77e169f842
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# training_program_manager.py

import pandas as pd
import numpy as np
from datetime import datetime

class TrainingProgramManager:
    """
    Manages data for training programs.

    Attributes:
        data (pd.DataFrame): Training program data.
    """

    def __init__(self, data=None):
        """
        Initializes the TrainingProgramManager.

        Args:
            data (pd.DataFrame, optional): Initial training program data. Defaults to None.
        """
        if data is None:
            self.data = pd.DataFrame(columns=['Program ID', 'Name', 'Start Date', 'End Date', 'Status'])
        else:
            self.data = data

    def add_program(self, program_id, name, start_date, end_date, status='Scheduled'):
        """
        Adds a new training program.

        Args:
            program_id (int): Unique program ID.
            name (str): Program name.
            start_date (str): Program start date (YYYY-MM-DD).
            end_date (str): Program end date (YYYY-MM-DD).
            status (str, optional): Program status. Defaults to 'Scheduled'.

        Raises:
            ValueError: If program ID already exists.
        """
        if program_id in self.data['Program ID'].values:
            raise ValueError("Program ID already exists")

        new_program = pd.DataFrame({
            'Program ID': [program_id],
            'Name': [name],
            'Start Date': [start_date],
            'End Date': [end_date],
            'Status': [status]
        })

        self.data = pd.concat([self.data, new_program], ignore_index=True)

    def update_program(self, program_id, **kwargs):
        """
        Updates an existing training program.

        Args:
            program_id (int): Unique program ID.
            **kwargs: Program attributes to update.

        Raises:
            ValueError: If program ID does not exist.
        """
        if program_id not in self.data['Program ID'].values:
            raise ValueError("Program ID does not exist")

        self.data.loc[self.data['Program ID'] == program_id, kwargs.keys()] = list(kwargs.values())

    def delete_program(self, program_id):
        """
        Deletes a training program.

        Args:
            program_id (int): Unique program ID.

        Raises:
            ValueError: If program ID does not exist.
        """
        if program_id not in self.data['Program ID'].values:
            raise ValueError("Program ID does not exist")

        self.data = self.data[self.data['Program ID'] != program_id]

    def get_program(self, program_id):
        """
        Retrieves a training program.

        Args:
            program_id (int): Unique program ID.

        Returns:
            pd.Series: Training program data.

        Raises:
            ValueError: If program ID does not exist.
        """
        if program_id not in self.data['Program ID'].values:
            raise ValueError("Program ID does not exist")

        return self.data.loc[self.data['Program ID'] == program_id].iloc[0]

    def list_programs(self):
        """
        Lists all training programs.

        Returns:
            pd.DataFrame: Training program data.
        """
        return self.data

def main():
    # Example usage
    manager = TrainingProgramManager()

    try:
        manager.add_program(1, 'Python Training', '2024-09-01', '2024-09-30')
        manager.add_program(2, 'Data Science Training', '2024-10-01', '2024-10-31')

        print("All Programs:")
        print(manager.list_programs())

        manager.update_program(1, Status='In Progress')
        print("\nUpdated Program:")
        print(manager.get_program(1))

        manager.delete_program(2)
        print("\nPrograms after deletion:")
        print(manager.list_programs())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
