"""
Generated Code Metadata:
========================
Original URL: https://somtu.edu.np
Prompt: Generate a sample admission notice for the SOMTU MBA program using a template, incorporating details such as program name, admission dates, and eligibility criteria.
Generated: DETERMINISTIC_938e15a6a5512fc8
Batch ID: 20250622_212709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime

class AdmissionNotice:
    def __init__(self, program_name, admission_start_date, admission_end_date, eligibility_criteria):
        """
        Initializes the AdmissionNotice with program details.

        :param program_name: Name of the program
        :param admission_start_date: Start date for admissions
        :param admission_end_date: End date for admissions
        :param eligibility_criteria: Eligibility criteria for the program
        """
        self.program_name = program_name
        self.admission_start_date = admission_start_date
        self.admission_end_date = admission_end_date
        self.eligibility_criteria = eligibility_criteria

    def generate_notice(self):
        """
        Generates the admission notice as a formatted string.

        :return: Formatted admission notice
        """
        try:
            notice = (
                f"==============================\n"
                f"       Admission Notice       \n"
                f"==============================\n"
                f"Program Name: {self.program_name}\n"
                f"Admission Start Date: {self.admission_start_date.strftime('%B %d, %Y')}\n"
                f"Admission End Date: {self.admission_end_date.strftime('%B %d, %Y')}\n"
                f"Eligibility Criteria: {self.eligibility_criteria}\n"
                f"==============================\n"
                f"Apply Now and Join Us!\n"
                f"=============================="
            )
            return notice
        except Exception as e:
            # Log the error and return a user-friendly message
            print(f"Error generating admission notice: {e}")
            return "An error occurred while generating the admission notice."

def main():
    # Define program details
    program_name = "SOMTU MBA Program"
    admission_start_date = datetime(2023, 11, 1)  # Example start date
    admission_end_date = datetime(2024, 1, 15)    # Example end date
    eligibility_criteria = "Bachelor's degree from a recognized university."

    # Create an AdmissionNotice instance
    admission_notice = AdmissionNotice(program_name, admission_start_date, admission_end_date, eligibility_criteria)

    # Generate and print the admission notice
    print(admission_notice.generate_notice())

if __name__ == "__main__":
    main()
```
