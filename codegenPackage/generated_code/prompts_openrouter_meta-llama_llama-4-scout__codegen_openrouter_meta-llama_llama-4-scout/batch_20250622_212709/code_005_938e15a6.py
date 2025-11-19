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
    def __init__(self, program_name, admission_dates, eligibility_criteria):
        """
        Initialize the AdmissionNotice class.

        Args:
            program_name (str): The name of the program.
            admission_dates (dict): A dictionary containing admission dates.
            eligibility_criteria (str): The eligibility criteria for the program.
        """
        self.program_name = program_name
        self.admission_dates = admission_dates
        self.eligibility_criteria = eligibility_criteria

    def generate_notice(self):
        """
        Generate a sample admission notice.

        Returns:
            str: A sample admission notice.
        """
        notice_template = """
ADMISSION NOTICE

We are pleased to announce that applications are now open for the {program_name} program at SOMTU.

**Program Details**

* Program Name: {program_name}
* Admission Dates:
    + Application Start Date: {application_start_date}
    + Application End Date: {application_end_date}
    + Class Start Date: {class_start_date}
* Eligibility Criteria: {eligibility_criteria}

**How to Apply**

To apply, please submit your application through our website.

**Contact Us**

For more information, please contact us at [insert contact email/phone number].

Sincerely,
[Your Name]
        """
        formatted_notice = notice_template.format(
            program_name=self.program_name,
            application_start_date=self.admission_dates['application_start_date'].strftime('%B %d, %Y'),
            application_end_date=self.admission_dates['application_end_date'].strftime('%B %d, %Y'),
            class_start_date=self.admission_dates['class_start_date'].strftime('%B %d, %Y'),
            eligibility_criteria=self.eligibility_criteria
        )
        return formatted_notice


def main():
    try:
        program_name = "MBA"
        admission_dates = {
            'application_start_date': datetime(2024, 9, 1),
            'application_end_date': datetime(2024, 12, 31),
            'class_start_date': datetime(2025, 1, 15)
        }
        eligibility_criteria = "Bachelor's degree from an accredited institution and a minimum of 2 years of work experience."

        notice = AdmissionNotice(program_name, admission_dates, eligibility_criteria)
        print(notice.generate_notice())
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
