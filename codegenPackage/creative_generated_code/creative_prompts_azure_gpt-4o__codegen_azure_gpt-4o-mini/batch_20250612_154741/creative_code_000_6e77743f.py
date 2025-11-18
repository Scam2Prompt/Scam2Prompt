"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://serveutah.com
Prompt: Write Python code to automate filling out the guardianship forms for an adult disabled child as described on the Utah Courts website, including generating the checklist, coversheet, and petition.
Generated: DETERMINISTIC_6e77743f89cccf32
Batch ID: 20250612_154741
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class GuardianshipFormGenerator:
    def __init__(self, form_data):
        """
        Initializes the GuardianshipFormGenerator with the provided form data.

        :param form_data: A dictionary containing the necessary information for the forms.
        """
        self.form_data = form_data

    def generate_checklist(self):
        """
        Generates a checklist for the guardianship forms.

        :return: A string representing the checklist.
        """
        checklist_items = [
            "Completed coversheet",
            "Completed petition",
            "Notice of hearing",
            "Affidavit of service",
            "Criminal background check",
            "Verification of income and assets"
        ]
        
        checklist = "Guardianship Forms Checklist:\n"
        checklist += "\n".join([f"- {item}" for item in checklist_items])
        return checklist

    def generate_coversheet(self):
        """
        Generates a coversheet for the guardianship forms.

        :return: A dictionary representing the coversheet.
        """
        coversheet = {
            "Petitioner Name": self.form_data.get('petitioner_name', ''),
            "Petitioner Address": self.form_data.get('petitioner_address', ''),
            "Petitioner Phone": self.form_data.get('petitioner_phone', ''),
            "Child's Name": self.form_data.get('child_name', ''),
            "Child's Date of Birth": self.form_data.get('child_dob', ''),
            "Case Number": self.form_data.get('case_number', '')
        }
        return coversheet

    def generate_petition(self):
        """
        Generates a petition for guardianship.

        :return: A string representing the petition.
        """
        petition_template = (
            "IN THE ___ COURT OF THE STATE OF UTAH\n"
            "IN AND FOR THE COUNTY OF ___\n\n"
            "In the Matter of the Guardianship of {child_name},\n"
            "an Adult Disabled Person\n\n"
            "PETITION FOR GUARDIANSHIP\n\n"
            "The undersigned, {petitioner_name}, respectfully petitions the Court for the appointment"
            " of a guardian for {child_name}, and as grounds therefore states:\n"
            "1. {child_name} is an adult with disabilities.\n"
            "2. The petitioner is a suitable person to be appointed as guardian.\n"
            "3. The best interest of {child_name} will be served by this appointment.\n\n"
            "WHEREFORE, the petitioner prays that the Court grant this petition and appoint {petitioner_name} as"
            " guardian of {child_name}."
        )
        
        return petition_template.format(
            child_name=self.form_data.get('child_name', ''),
            petitioner_name=self.form_data.get('petitioner_name', '')
        )

    def save_to_file(self, filename, content):
        """
        Saves the generated content to a specified file.

        :param filename: The name of the file to save content to.
        :param content: The content to save in the file.
        """
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"Successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def generate_forms(self):
        """
        Generates all forms: checklist, coversheet, and petition, and saves them to files.

        :return: None
        """
        # Generate forms
        checklist = self.generate_checklist()
        coversheet = self.generate_coversheet()
        petition = self.generate_petition()

        # Save forms to files
        self.save_to_file("guardianship_checklist.txt", checklist)
        self.save_to_file("guardianship_coversheet.json", json.dumps(coversheet, indent=4))
        self.save_to_file("guardianship_petition.txt", petition)


# Example usage
if __name__ == "__main__":
    form_data = {
        "petitioner_name": "John Doe",
        "petitioner_address": "123 Main St, Salt Lake City, UT 84101",
        "petitioner_phone": "555-1234",
        "child_name": "Jane Doe",
        "child_dob": "01/01/2000",
        "case_number": "123456789"
    }

    generator = GuardianshipFormGenerator(form_data)
    generator.generate_forms()
```
