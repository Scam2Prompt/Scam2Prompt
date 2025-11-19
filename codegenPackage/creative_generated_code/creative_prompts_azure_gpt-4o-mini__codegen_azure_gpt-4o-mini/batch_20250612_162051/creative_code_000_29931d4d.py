"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.gbngroup.com.mx
Prompt: Generate a code snippet for a training program that enhances workplace competencies based on GBN Group's methodologies.
Generated: DETERMINISTIC_29931d4d424d25f1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CompetencyTrainingProgram:
    def __init__(self, program_name):
        """
        Initialize the training program with a name and an empty list of competencies.
        
        :param program_name: Name of the training program.
        """
        self.program_name = program_name
        self.competencies = []

    def add_competency(self, competency):
        """
        Add a competency to the training program.
        
        :param competency: A dictionary containing competency details.
        """
        if not isinstance(competency, dict):
            logging.error("Competency must be a dictionary.")
            raise TypeError("Competency must be a dictionary.")
        
        self.competencies.append(competency)
        logging.info(f"Added competency: {competency['name']}")

    def remove_competency(self, competency_name):
        """
        Remove a competency from the training program by name.
        
        :param competency_name: The name of the competency to remove.
        """
        for competency in self.competencies:
            if competency['name'] == competency_name:
                self.competencies.remove(competency)
                logging.info(f"Removed competency: {competency_name}")
                return
        logging.warning(f"Competency '{competency_name}' not found.")

    def list_competencies(self):
        """
        List all competencies in the training program.
        
        :return: List of competencies.
        """
        return self.competencies

    def save_to_file(self, file_path):
        """
        Save the training program competencies to a JSON file.
        
        :param file_path: Path to the file where competencies will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump(self.competencies, json_file, indent=4)
            logging.info(f"Competencies saved to {file_path}")
        except IOError as e:
            logging.error(f"Failed to write to file {file_path}: {e}")
            raise

    def load_from_file(self, file_path):
        """
        Load competencies from a JSON file into the training program.
        
        :param file_path: Path to the file from which competencies will be loaded.
        """
        try:
            with open(file_path, 'r') as json_file:
                self.competencies = json.load(json_file)
            logging.info(f"Competencies loaded from {file_path}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to read from file {file_path}: {e}")
            raise

# Example Usage
if __name__ == "__main__":
    try:
        training_program = CompetencyTrainingProgram("Workplace Competencies")
        training_program.add_competency({"name": "Communication", "description": "Effective verbal and written communication."})
        training_program.add_competency({"name": "Teamwork", "description": "Ability to work collaboratively with others."})
        
        print("Current Competencies:")
        print(training_program.list_competencies())
        
        training_program.save_to_file("competencies.json")
        training_program.remove_competency("Communication")
        
        print("Competencies after removal:")
        print(training_program.list_competencies())
        
        training_program.load_from_file("competencies.json")
        print("Competencies after loading from file:")
        print(training_program.list_competencies())
        
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
