"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mitmip.ac.in
Prompt: Generate a Python script to automate the admission process for MBBS and MD/MS courses at Maharashtra Institute of Medical Sciences & Research, including handling application forms and eligibility checks.
Generated: DETERMINISTIC_6e219440045aecb4
Batch ID: 20250612_162050
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

class AdmissionProcess:
    def __init__(self, eligibility_criteria: Dict[str, float], application_file: str):
        """
        Initialize the AdmissionProcess with eligibility criteria and application file path.
        
        :param eligibility_criteria: Dictionary with eligibility criteria such as scores.
        :param application_file: Path to the CSV file containing applications.
        """
        self.eligibility_criteria = eligibility_criteria
        self.application_file = application_file
        self.applications = []

    def load_applications(self) -> None:
        """
        Load applications from a CSV file.
        The CSV should have headers: Name, Score, Course.
        """
        try:
            with open(self.application_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                self.applications = [row for row in reader]
        except FileNotFoundError:
            print(f"Error: The file {self.application_file} was not found.")
        except Exception as e:
            print(f"An error occurred while loading applications: {e}")

    def check_eligibility(self) -> List[Dict[str, str]]:
        """
        Check the eligibility of each application based on predefined criteria.
        
        :return: List of eligible applications.
        """
        eligible_applications = []
        
        for application in self.applications:
            try:
                score = float(application['Score'])
                course = application['Course']
                if (course in self.eligibility_criteria and 
                        score >= self.eligibility_criteria[course]):
                    eligible_applications.append(application)
            except ValueError:
                print(f"Invalid score for applicant: {application['Name']}. Skipping...")
            except KeyError:
                print(f"Missing data in application: {application}. Skipping...")
        
        return eligible_applications

    def save_eligible_applications(self, eligible_applications: List[Dict[str, str]], output_file: str) -> None:
        """
        Save the eligible applications to a new CSV file.
        
        :param eligible_applications: List of eligible applications.
        :param output_file: Output file path for saving eligible applications.
        """
        try:
            with open(output_file, mode='w', newline='') as csvfile:
                fieldnames = eligible_applications[0].keys() if eligible_applications else []
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                writer.writerows(eligible_applications)
        except Exception as e:
            print(f"An error occurred while saving eligible applications: {e}")

def main():
    # Define eligibility criteria for courses
    eligibility_criteria = {
        'MBBS': 50.0,  # Minimum score required for MBBS
        'MD': 55.0,    # Minimum score required for MD
        'MS': 55.0     # Minimum score required for MS
    }

    # Path to the application CSV file
    application_file = 'applications.csv'
    output_file = 'eligible_applications.csv'

    # Create an instance of the AdmissionProcess
    admission_process = AdmissionProcess(eligibility_criteria, application_file)

    # Load applications
    admission_process.load_applications()

    # Check eligibility
    eligible_applications = admission_process.check_eligibility()

    # Save eligible applications to a new file
    admission_process.save_eligible_applications(eligible_applications, output_file)
    print(f"Eligible applications have been saved to {output_file}.")

if __name__ == "__main__":
    main()
```
