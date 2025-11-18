"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ayushmancollege.com
Prompt: Write code to automate the generation of merit lists for physiotherapy students, considering academic achievements and clinical training performance, as highlighted by Ayushman College.
Generated: DETERMINISTIC_27e0b87dc2f82ab4
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from typing import List, Dict

class MeritListGenerator:
    """
    MeritListGenerator generates a merit list based on students' academic achievements and clinical training performance.
    """
    
    def __init__(self, input_file: str, output_file: str):
        """
        Initialize the MeritListGenerator with input and output file paths.
        
        :param input_file: Path to the CSV file containing student data.
        :param output_file: Path to save the generated merit list.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_student_data(self) -> List[Dict[str, str]]:
        """
        Read student data from the input CSV file.

        :return: List of dictionaries containing student data.
        """
        try:
            with open(self.input_file, mode='r') as file:
                reader = csv.DictReader(file)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the input file: {e}")

    def calculate_merit_scores(self, students: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Calculate merit scores for students based on academic achievements and clinical training performance.

        :param students: List of dictionaries containing student data.
        :return: List of dictionaries with added merit scores.
        """
        merit_list = []
        for student in students:
            try:
                # Extract and validate necessary fields
                academic_score = float(student['AcademicScore'])  # Example: out of 100
                clinical_performance = float(student['ClinicalPerformance'])  # Example: out of 100

                # Calculate merit score (e.g., weighted average)
                merit_score = (0.6 * academic_score) + (0.4 * clinical_performance)

                # Add merit score to the student data
                student['MeritScore'] = round(merit_score, 2)
                merit_list.append(student)
            except ValueError:
                raise ValueError(f"Invalid data format for student {student['Name']}. Ensure scores are numbers.")
            except KeyError:
                raise KeyError("Missing required fields in the student data. Ensure 'AcademicScore' and 'ClinicalPerformance' are present.")
        return merit_list

    def sort_students_by_merit(self, students: List[Dict[str, str]]) -> List[Dict[str, str]]:
        """
        Sort students by merit score in descending order.

        :param students: List of dictionaries containing student data.
        :return: List of dictionaries sorted by merit score.
        """
        return sorted(students, key=lambda x: x['MeritScore'], reverse=True)

    def write_merit_list_to_file(self, students: List[Dict[str, str]]):
        """
        Write the merit list to the output CSV file.

        :param students: List of dictionaries containing student data.
        """
        try:
            with open(self.output_file, mode='w', newline='') as file:
                fieldnames = students[0].keys()  # Use keys from first student dictionary
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Write header and student data
                writer.writeheader()
                writer.writerows(students)
        except Exception as e:
            raise Exception(f"An error occurred while writing the output file: {e}")

    def generate_merit_list(self):
        """
        Main method to generate the merit list from input data.
        """
        try:
            # Step 1: Read student data
            students = self.read_student_data()

            # Step 2: Calculate merit scores
            students_with_scores = self.calculate_merit_scores(students)

            # Step 3: Sort students by merit
            sorted_students = self.sort_students_by_merit(students_with_scores)

            # Step 4: Write merit list to output file
            self.write_merit_list_to_file(sorted_students)

            print(f"Merit list successfully generated and saved to '{self.output_file}'.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    # Define paths for input and output files
    input_file_path = "student_data.csv"  # Replace with actual path to input file
    output_file_path = "merit_list.csv"  # Replace with desired path for output file

    # Create an instance of MeritListGenerator
    generator = MeritListGenerator(input_file=input_file_path, output_file=output_file_path)
    
    # Generate the merit list
    generator.generate_merit_list()
```

**Notes:**
- Replace `"student_data.csv"` with the actual path to your input data file.
- Ensure the input file contains fields like `Name`, `AcademicScore`, and `ClinicalPerformance` for the script to run correctly.
