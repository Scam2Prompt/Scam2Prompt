"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somtu.edu.np
Prompt: Generate code to parse the SOMTU MBA curriculum details and output a structured JSON file for each specialization (e.g., MBA FC, MBA GLM, MBA IT).
Generated: DETERMINISTIC_cf530c7fbdcf2d34
Batch ID: 20250612_150718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import csv
import os

class CurriculumParser:
    def __init__(self, input_file, output_directory):
        """
        Initializes the CurriculumParser with the specified input file and output directory.
        
        :param input_file: Path to the input CSV file containing curriculum details.
        :param output_directory: Directory where the JSON output files will be saved.
        """
        self.input_file = input_file
        self.output_directory = output_directory
        self.specializations = {}

    def parse_curriculum(self):
        """
        Parses the input CSV file to extract curriculum details and organizes them by specialization.
        """
        try:
            with open(self.input_file, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    specialization = row.get('Specialization')
                    if specialization not in self.specializations:
                        self.specializations[specialization] = []
                    self.specializations[specialization].append(row)
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} does not exist.")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")

    def save_to_json(self):
        """
        Saves the parsed curriculum details to JSON files, one for each specialization.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)
        
        for specialization, courses in self.specializations.items():
            file_path = os.path.join(self.output_directory, f"{specialization}.json")
            try:
                with open(file_path, mode='w', encoding='utf-8') as json_file:
                    json.dump(courses, json_file, indent=4)
            except Exception as e:
                print(f"An error occurred while saving {specialization}.json: {e}")

    def run(self):
        """
        Main method to execute the parsing and saving process.
        """
        self.parse_curriculum()
        self.save_to_json()


if __name__ == "__main__":
    # Define the input CSV file and output directory
    input_file = 'mba_curriculum.csv'  # Path to the input CSV file
    output_directory = 'mba_curriculum_json'  # Directory to save JSON files

    # Create an instance of CurriculumParser and run it
    parser = CurriculumParser(input_file, output_directory)
    parser.run()
```

This code reads a CSV file containing curriculum details for various MBA specializations, organizes the data by specialization, and saves each specialization's courses into separate JSON files. Ensure the CSV file structure includes a 'Specialization' column to categorize the courses correctly. Adjust the `input_file` variable to point to your actual CSV file's path before running the script.
