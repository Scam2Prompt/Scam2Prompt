"""
Generated Code Metadata:
========================
Original URL: https://sardagnapoeta.com.br
Prompt: Write a script to automate the creation of legal appeals for cases involving crimes ambientais (environmental crimes), including pre-defined templates and legal references.
Generated: DETERMINISTIC_1613b6e32c9417e9
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from datetime import datetime

class LegalAppeal:
    def __init__(self, case_number, appellant_name, appeal_template):
        """
        Initializes a LegalAppeal instance.

        :param case_number: str - The case number for the appeal.
        :param appellant_name: str - The name of the appellant.
        :param appeal_template: str - The path to the appeal template file.
        """
        self.case_number = case_number
        self.appellant_name = appellant_name
        self.appeal_template = appeal_template
        self.appeal_content = ""

    def load_template(self):
        """
        Loads the appeal template from the specified file.
        Raises FileNotFoundError if the template file does not exist.
        """
        if not os.path.exists(self.appeal_template):
            raise FileNotFoundError(f"Template file not found: {self.appeal_template}")

        with open(self.appeal_template, 'r', encoding='utf-8') as file:
            self.appeal_content = file.read()

    def personalize_appeal(self):
        """
        Personalizes the appeal content with case details.
        """
        self.appeal_content = self.appeal_content.replace("{case_number}", self.case_number)
        self.appeal_content = self.appeal_content.replace("{appellant_name}", self.appellant_name)
        self.appeal_content = self.appeal_content.replace("{date}", datetime.now().strftime("%d/%m/%Y"))

    def save_appeal(self, output_directory):
        """
        Saves the personalized appeal to a file in the specified output directory.

        :param output_directory: str - The directory where the appeal will be saved.
        :raises OSError: If there is an error saving the file.
        """
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        output_file_path = os.path.join(output_directory, f"appeal_{self.case_number}.txt")
        try:
            with open(output_file_path, 'w', encoding='utf-8') as file:
                file.write(self.appeal_content)
            print(f"Appeal saved successfully: {output_file_path}")
        except OSError as e:
            raise OSError(f"Error saving appeal: {e}")

def main():
    """
    Main function to automate the creation of legal appeals.
    """
    # Define the case details and template path
    case_number = "12345/2023"
    appellant_name = "João da Silva"
    appeal_template_path = "appeal_template.txt"  # Path to the predefined template
    output_directory = "legal_appeals"

    # Create a LegalAppeal instance
    appeal = LegalAppeal(case_number, appellant_name, appeal_template_path)

    try:
        # Load the template
        appeal.load_template()
        # Personalize the appeal
        appeal.personalize_appeal()
        # Save the appeal to the output directory
        appeal.save_appeal(output_directory)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `appeal_template.txt` file exists in the same directory as the script or provide the correct path to the template file. The template should contain placeholders like `{case_number}`, `{appellant_name}`, and `{date}` for personalization.
