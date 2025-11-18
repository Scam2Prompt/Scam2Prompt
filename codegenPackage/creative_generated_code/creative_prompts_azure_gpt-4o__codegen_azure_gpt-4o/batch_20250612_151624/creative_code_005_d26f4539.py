"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://glowconsultants.org
Prompt: Develop a proposal for a program design that includes baseline, midline, and endline evaluations, incorporating GLOW Consultants' expertise in monitoring and evaluation.
Generated: DETERMINISTIC_d26f453919291c61
Batch ID: 20250612_151624
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program for managing baseline, midline, and endline evaluations
with GLOW Consultants' monitoring and evaluation expertise.
This program is designed to handle effective tracking and reporting
for project evaluation phases.

Author: [Your Name]
Date: [Today's Date]
"""

import csv
import datetime

class EvaluationManager:
    """
    A class to manage baseline, midline, and endline evaluations.
    """

    def __init__(self, project_name: str):
        """
        Initialize the EvaluationManager with project details.

        Args:
        project_name (str): Name of the project.
        """
        self.project_name = project_name
        self.evaluations = {"Baseline": [], "Midline": [], "Endline": []}

    def add_evaluation(self, phase: str, evaluator: str, date: str, notes: str):
        """
        Add an evaluation record.

        Args:
        phase (str): The phase of evaluation (Baseline, Midline, Endline).
        evaluator (str): Name of the evaluator.
        date (str): Date of evaluation in YYYY-MM-DD format.
        notes (str): Additional notes or observations.

        Raises:
        ValueError: If the phase is invalid.
        """
        if phase not in self.evaluations:
            raise ValueError("Invalid phase. Choose from Baseline, Midline, or Endline.")
        
        # Validate date format
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        evaluation_record = {
            "Evaluator": evaluator,
            "Date": date,
            "Notes": notes
        }

        self.evaluations[phase].append(evaluation_record)

    def get_evaluations(self, phase: str):
        """
        Retrieve evaluations for a specific phase.

        Args:
        phase (str): The phase of evaluation (Baseline, Midline, Endline).

        Returns:
        list: List of evaluations for the specified phase.

        Raises:
        ValueError: If the phase is invalid.
        """
        if phase not in self.evaluations:
            raise ValueError("Invalid phase. Choose from Baseline, Midline, or Endline.")
        
        return self.evaluations[phase]

    def export_to_csv(self, filename: str):
        """
        Export all evaluations to a CSV file.

        Args:
        filename (str): Name of the CSV file to save the data.

        Raises:
        IOError: If an error occurs during file writing.
        """
        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Phase", "Evaluator", "Date", "Notes"])

                for phase, records in self.evaluations.items():
                    for record in records:
                        writer.writerow([phase, record["Evaluator"], record["Date"], record["Notes"]])
        except IOError as e:
            raise IOError(f"Error writing to file: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the program with a project name
        manager = EvaluationManager(project_name="Community Development Project")

        # Add evaluation records
        manager.add_evaluation(phase="Baseline", evaluator="Alice Johnson", date="2023-01-15", notes="Initial survey completed.")
        manager.add_evaluation(phase="Midline", evaluator="Bob Smith", date="2023-06-20", notes="Midline evaluation underway.")
        manager.add_evaluation(phase="Endline", evaluator="Charlie Brown", date="2023-12-01", notes="Final results collected.")

        # Retrieve evaluations for a specific phase
        print("Baseline Evaluations:", manager.get_evaluations(phase="Baseline"))

        # Export all evaluations to a CSV file
        manager.export_to_csv(filename="evaluation_report.csv")
        print("Evaluations exported successfully to evaluation_report.csv")

    except Exception as e:
        print(f"An error occurred: {e}")
```
