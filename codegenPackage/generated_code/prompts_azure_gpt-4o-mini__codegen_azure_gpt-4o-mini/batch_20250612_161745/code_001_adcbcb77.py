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
import pandas as pd
import os
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrainingProgramManager:
    def __init__(self, data_file):
        """
        Initializes the TrainingProgramManager with the specified data file.

        :param data_file: Path to the CSV file containing training program data.
        """
        self.data_file = data_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads training program data from a CSV file.

        :return: DataFrame containing the training program data.
        """
        try:
            data = pd.read_csv(self.data_file)
            logging.info("Data loaded successfully from %s", self.data_file)
            return data
        except FileNotFoundError:
            logging.error("File not found: %s", self.data_file)
            raise
        except pd.errors.EmptyDataError:
            logging.error("No data: %s is empty", self.data_file)
            raise
        except Exception as e:
            logging.error("An error occurred while loading data: %s", e)
            raise

    def save_data(self):
        """
        Saves the current state of the training program data back to the CSV file.
        """
        try:
            self.data.to_csv(self.data_file, index=False)
            logging.info("Data saved successfully to %s", self.data_file)
        except Exception as e:
            logging.error("An error occurred while saving data: %s", e)
            raise

    def add_training_program(self, program_details):
        """
        Adds a new training program to the data.

        :param program_details: Dictionary containing details of the training program.
        """
        try:
            self.data = self.data.append(program_details, ignore_index=True)
            logging.info("Added new training program: %s", program_details)
        except Exception as e:
            logging.error("An error occurred while adding a training program: %s", e)
            raise

    def update_training_program(self, program_id, updated_details):
        """
        Updates an existing training program based on its ID.

        :param program_id: ID of the training program to update.
        :param updated_details: Dictionary containing updated details of the training program.
        """
        try:
            self.data.loc[self.data['ID'] == program_id, updated_details.keys()] = updated_details.values()
            logging.info("Updated training program ID %d with details: %s", program_id, updated_details)
        except Exception as e:
            logging.error("An error occurred while updating the training program: %s", e)
            raise

    def delete_training_program(self, program_id):
        """
        Deletes a training program based on its ID.

        :param program_id: ID of the training program to delete.
        """
        try:
            self.data = self.data[self.data['ID'] != program_id]
            logging.info("Deleted training program ID %d", program_id)
        except Exception as e:
            logging.error("An error occurred while deleting the training program: %s", e)
            raise

    def get_training_programs(self):
        """
        Returns the current list of training programs.

        :return: DataFrame containing the training programs.
        """
        return self.data

if __name__ == "__main__":
    # Example usage of the TrainingProgramManager
    data_file_path = 'training_programs.csv'

    # Check if the data file exists, if not create an empty one
    if not os.path.exists(data_file_path):
        pd.DataFrame(columns=['ID', 'Name', 'Duration', 'Cost']).to_csv(data_file_path, index=False)

    manager = TrainingProgramManager(data_file_path)

    # Example of adding a new training program
    new_program = {'ID': 1, 'Name': 'Python Programming', 'Duration': '4 weeks', 'Cost': 500}
    manager.add_training_program(new_program)

    # Example of updating a training program
    updated_program = {'Name': 'Advanced Python Programming', 'Duration': '6 weeks', 'Cost': 700}
    manager.update_training_program(1, updated_program)

    # Example of deleting a training program
    manager.delete_training_program(1)

    # Save changes to the data file
    manager.save_data()
```
