"""
Generated Code Metadata:
========================
Original URL: https://mitmip.ac.in
Prompt: Generate a Python script to automate the admission process for MBBS and MD/MS courses at Maharashtra Institute of Medical Sciences & Research, including handling application forms and eligibility checks.
Generated: DETERMINISTIC_6e219440045aecb4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AdmissionProcess:
    def __init__(self, eligibility_criteria):
        """
        Initialize the AdmissionProcess with eligibility criteria.

        :param eligibility_criteria: A dictionary containing eligibility criteria for MBBS and MD/MS courses.
        """
        self.eligibility_criteria = eligibility_criteria
        self.applications = []

    def load_applications(self, file_path):
        """
        Load applications from a JSON file.

        :param file_path: Path to the JSON file containing application data.
        :raises FileNotFoundError: If the file does not exist.
        :raises json.JSONDecodeError: If the file is not a valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                self.applications = json.load(file)
                logging.info("Applications loaded successfully.")
        except FileNotFoundError:
            logging.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logging.error("Error decoding JSON from the file.")
            raise

    def check_eligibility(self, application):
        """
        Check if the given application meets the eligibility criteria.

        :param application: A dictionary representing a single application.
        :return: True if eligible, False otherwise.
        """
        for key, value in self.eligibility_criteria.items():
            if application.get(key) < value:
                logging.warning(f"Application {application['name']} is not eligible due to {key}.")
                return False
        logging.info(f"Application {application['name']} is eligible.")
        return True

    def process_applications(self):
        """
        Process all applications and determine eligibility.
        """
        eligible_applicants = []
        for application in self.applications:
            if self.check_eligibility(application):
                eligible_applicants.append(application)
        
        logging.info(f"Total eligible applicants: {len(eligible_applicants)}")
        return eligible_applicants

    def save_eligible_applicants(self, eligible_applicants, output_file):
        """
        Save the list of eligible applicants to a JSON file.

        :param eligible_applicants: List of eligible applicants.
        :param output_file: Path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(eligible_applicants, file, indent=4)
                logging.info(f"Eligible applicants saved to {output_file}.")
        except IOError as e:
            logging.error(f"Error saving eligible applicants: {e}")
            raise

def main():
    # Define eligibility criteria for MBBS and MD/MS courses
    eligibility_criteria = {
        'age': 17,  # Minimum age
        'marks': 50  # Minimum percentage in qualifying exam
    }

    # Create an instance of the AdmissionProcess
    admission_process = AdmissionProcess(eligibility_criteria)

    # Load applications from a JSON file
    try:
        admission_process.load_applications('applications.json')
    except (FileNotFoundError, json.JSONDecodeError):
        return

    # Process applications to find eligible candidates
    eligible_applicants = admission_process.process_applications()

    # Save eligible applicants to a new JSON file
    admission_process.save_eligible_applicants(eligible_applicants, 'eligible_applicants.json')

if __name__ == "__main__":
    main()
```

**Note**: Ensure that the `applications.json` file exists in the same directory as this script and contains valid JSON data structured appropriately for the eligibility checks.
