"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Outline a training program for corporate teams focusing on data analysis skills, based on PDMA's corporate training offerings.
Generated: DETERMINISTIC_9ff7713df65d74b6
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from datetime import datetime, timedelta

class TrainingProgram:
    """
    A class representing a training program for corporate teams focusing on data analysis skills.
    """

    def __init__(self, program_name, duration, start_date):
        """
        Initializes a TrainingProgram object.

        Args:
            program_name (str): The name of the training program.
            duration (int): The duration of the training program in days.
            start_date (str): The start date of the training program in 'YYYY-MM-DD' format.
        """
        self.program_name = program_name
        self.duration = duration
        self.start_date = datetime.strptime(start_date, '%Y-%m-%d')
        self.end_date = self.start_date + timedelta(days=duration)

    def get_program_details(self):
        """
        Returns a dictionary containing the program details.

        Returns:
            dict: A dictionary containing the program name, start date, end date, and duration.
        """
        return {
            'Program Name': self.program_name,
            'Start Date': self.start_date.strftime('%Y-%m-%d'),
            'End Date': self.end_date.strftime('%Y-%m-%d'),
            'Duration': self.duration
        }

class PDMA_TrainingProgram(TrainingProgram):
    """
    A subclass of TrainingProgram representing PDMA's corporate training offerings.
    """

    def __init__(self, program_name, duration, start_date, pdma_program_id):
        """
        Initializes a PDMA_TrainingProgram object.

        Args:
            program_name (str): The name of the training program.
            duration (int): The duration of the training program in days.
            start_date (str): The start date of the training program in 'YYYY-MM-DD' format.
            pdma_program_id (str): The PDMA program ID.
        """
        super().__init__(program_name, duration, start_date)
        self.pdma_program_id = pdma_program_id

    def get_program_details(self):
        """
        Returns a dictionary containing the program details, including the PDMA program ID.

        Returns:
            dict: A dictionary containing the program name, start date, end date, duration, and PDMA program ID.
        """
        program_details = super().get_program_details()
        program_details['PDMA Program ID'] = self.pdma_program_id
        return program_details

def create_training_programs():
    """
    Creates a list of TrainingProgram objects representing PDMA's corporate training offerings.

    Returns:
        list: A list of TrainingProgram objects.
    """
    training_programs = [
        PDMA_TrainingProgram('Data Analysis Fundamentals', 3, '2024-09-01', 'PDMA-001'),
        PDMA_TrainingProgram('Data Visualization with Python', 5, '2024-09-15', 'PDMA-002'),
        PDMA_TrainingProgram('Machine Learning with R', 7, '2024-10-01', 'PDMA-003')
    ]
    return training_programs

def main():
    try:
        training_programs = create_training_programs()
        for program in training_programs:
            print(program.get_program_details())
            print('------------------------')
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
